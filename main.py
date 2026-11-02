from customtkinter import * 
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
import CTkMessagebox as msg
from mysqlTimeInfo import getTime
from ctk_xyframe import CTkXYFrame
from operator import itemgetter
from time import sleep
from textwrap import wrap
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import * 
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebEngineWidgets import *


set_appearance_mode("light")
window = CTk()
window.geometry("800x400")
window.title("Ajarise")
screen = "1920x1080"    #DEGIŞTIRILECEK BİR YER
startTime = getTime()

class IndividualIlacInfo():
    def __init__(self,info,master):
        info = list(info)
        for i in range(0,len(info)):
            if info[i] == None:
                info[i] = "0"
        self.info = info
        self.mainFrame = CTkFrame(master,height=50,width=50)
        self.mainFrame.pack(pady=10)
        CTkLabel(self.mainFrame,text="Ilac Adı: " + self.info[1]).pack()
        CTkLabel(self.mainFrame,text="Karekod: " + self.info[0]).pack()
        CTkLabel(self.mainFrame,text="Alınan Tarih: " + self.info[3]).pack()
        CTkLabel(self.mainFrame,text="Alınan Yer: " + self.info[6]).pack()
        if self.info[4] != "0" or self.info[5] != "0":
            self.sold = ["Satılmış",1]
        else:
            self.sold = ["Satılmamış",0]
        CTkLabel(self.mainFrame,text="Satılma Durumu: " + self.sold[0]).pack()
        if self.sold[1]:
            CTkLabel(self.mainFrame,text="Satma Tarih: " + self.info[4]).pack()
            CTkLabel(self.mainFrame,text="Satılan Hasta: " + self.info[5]).pack()
    
class StockIlacInfo():
    def __init__(self,name):
        self.name = name[0]
        self.topLevel = CTkToplevel(window)
        self.topLevel.bind("<FocusOut>",self.destroy)
        self.topLevel.geometry("200x200")
        self.topLevel.title(self.name)
        CTkLabel(self.topLevel,text="İlaç Adı : " + self.name).pack(anchor="w",padx=5,pady=2)
        CTkLabel(self.topLevel,text="Stokta Bulunan miktar : " + str(name[1]) + "\n Satılmış Filtresine Dikkat!!").pack(anchor="w",padx=5,pady=2)
        CTkLabel(self.topLevel,text="Barkod : " + str(name[2])).pack(anchor="w",padx=5,pady=2)
        self.expandButton = CTkButton(self.topLevel,text="Bireysel İncele",command=self.expand)
        self.expandButton.pack(anchor="w",padx=5,pady=2)
       
    def destroy(self,event):
        self.topLevel.destroy()

    def expand(self):
        self.topLevel.geometry("200x250")
        self.ScrFrame = CTkScrollableFrame(self.topLevel,height=500,fg_color="transparent")
        self.ScrFrame.pack(anchor="w")
        cursor.execute("SELECT * FROM "+db+".stok WHERE ad = '"+ self.name+"';")
        self.fetched = cursor.fetchall()
        for item in self.fetched:
            self.expandButton.destroy()
            IndividualIlacInfo(item,self.ScrFrame)

class GiveMessageBox():
    def __init__(self,info,master,side,name,func):
        self.info = info
        self.master = master
        self.func = func
        self.side = side
        self.name = name
        cursor.execute("SELECT * FROM "+db+".takas WHERE karekod = '"+self.info[1][6:].split()[0]+"'")
        self.x = cursor.fetchone()
        cursor.execute("SELECT * FROM "+db+".stok WHERE karekod = '"+self.info[1][6:].split()[0]+"'")
        self.y = cursor.fetchone()
        if self.y == None:
            cursor.execute("SELECT * FROM "+self.name+".stok WHERE karekod = '"+self.info[1][6:].split()[0]+"'")
            self.y = cursor.fetchone()
        if self.x != None and self.y[4] == "pendingTra":
            self.sold = True
        else:
            self.sold = False
    
        self.frame = CTkFrame(self.master,fg_color="gold")
        if side == "left":
            self.frame.pack(anchor="w",pady=5)
        elif side == "right":
            self.frame.pack(anchor="e",pady=5)
        self.label = CTkLabel(self.frame,text="İlaç Verme İsteği",font=('TkDefaultFont',18))
        self.label.pack()
        self.label2 = CTkLabel(self.frame,text="Verilen İlaçlar (Karekod) : \n" + self.info[1][6:],font=('TkDefaultFont',12))
        self.label2.pack()
        if not self.sold:
            if self.side == "right":
                self.button = CTkButton(self.frame,text="Geri Al",command=self.revert,fg_color="transparent",text_color="black")
            elif self.side == "left":
                self.button = CTkButton(self.frame,text="Al",command=self.accept,fg_color="transparent",text_color="black")
            self.button.pack()
        else:
            self.label3 = CTkLabel(self.frame,text="İşlem Yapıldı")
            self.label3.pack()

    def revert(self):
        cursor.execute("DELETE FROM `"+db+"`.`messages` WHERE (`messageTime` = '"+self.info[0]+"');")
        self.frame.destroy()

    def accept(self):
        msg.CTkMessagebox(window,title="Bildiri",message="İşlem yapılmıştır, iptal etmek, durumuna bakmak ve ilaç geldiği zaman veri tabanına işlemek için lütfen 'Takas' menüsüne bakınız")
        for item in self.info[1][6:].split(":"):
            cursor.execute("SELECT * FROM "+self.name+".stok WHERE karekod = '"+item+"'")
            ilacName = cursor.fetchone()[1]
            cursor.execute("INSERT INTO `"+db+"`.`takas` (`karekod`, `ad`, `toT`, `fromT`,`verTarih`) VALUES ('"+item+"', '"+ilacName+"', '"+db+"','"+self.name+"','"+getTime("sec")+"');")
            cursor.execute("INSERT INTO `"+self.name+"`.`takas` (`karekod`, `ad`, `toT`, `fromT`,`verTarih`) VALUES ('"+item+"', '"+ilacName+"', '"+db+"','"+self.name+"','"+getTime("sec")+"');")
            cursor.execute("UPDATE `"+self.name+"`.`stok` SET `satmaTarih` = 'pendingTra',`satmaHasta` = '"+db+"' WHERE (`karekod` = '"+item+"');")
        self.func()    

class WantMessageBox():
    def __init__(self,info,master,side,name):
        self.info = info
        self.master = master
        self.side = side
        self.name = name
        #cursor.execute("S")   #SAĞLIK BAKANLIĞI DB'SİNDEN AD BİLGİSİNİ ALIP SELF.İLACLAR'A VERECEK
        self.ilaclar = "temp"
        #SATILIP SATILMADIĞINA KARAR VER
        self.frame = CTkFrame(self.master,fg_color="green")
        if side == "left":
            self.frame.pack(anchor="w",pady=5)
        elif side == "right":
            self.frame.pack(anchor="e",pady=5)
        self.label = CTkLabel(self.frame,text="İlaç Alma İsteği",font=('TkDefaultFont',18))
        self.label.pack()
        self.label2 = CTkLabel(self.frame,text="İstenen İlaç ve miktarı : \n" + self.ilaclar + " " + self.info[1],font=('TkDefaultFont',12))
        self.label2.pack()
        #SATILIP SATILMADIĞINA GÖRE BURAYA BUTTON YAP

class Messengers():
    def __init__(self,info,master,reset):
        self.time = info[0][4:6] + "/" + info[0][2:4] + "/" + info[0][:2] + " " + info[0][6:8] + ":" + info[0][8:10]
        self.name = info[3]
        self.msg = reset
        self.master = master
        self.Button = CTkButton(self.master,text=self.name.capitalize() + "\n Son Gelen Mesaj: " + self.time + "\n" + "Konuşmayı Aç",command=self.open)
        self.Button.pack(fill="both")

    def open(self):
        for item in self.master.winfo_children():
            item.destroy()
        self.returnButton = CTkButton(self.master,text="Geri Dön",command=self.reset)
        self.returnButton.pack(fill="both",pady=5)
        self.Entry = CTkEntry(self.master,placeholder_text="Yaz . . .   (Enter ile gönderin) ")
        self.Entry.pack(fill="both",pady=5)
        self.Entry.bind("<Return>",self.onEnter)
        self.Button = CTkButton(self.master,text="Özel Gönderi (ilaç,kardeş vb.)",command=self.spec)
        self.Button.pack(fill="both",pady=5)
        cursor.execute("SELECT * FROM "+db+".messages WHERE toM = '"+self.name+"';")
        sent = cursor.fetchall()
        cursor.execute("SELECT * FROM "+self.name+".messages WHERE toM = '"+db+"';")
        recieved = cursor.fetchall()
        messages = sorted(sent + recieved,key=itemgetter(0))
        for i in range(0,len(messages)):
            if messages[i][0] == self.name:
                messages.pop(i)
                break
        for item in messages:
            if item[1][:1] == "#":
                if item[1][1:].split("/")[0] == "give":
                    if item in recieved:
                        GiveMessageBox(item,self.master,"left",self.name,self.msg)
                    elif item in sent:
                        GiveMessageBox(item,self.master,"right",self.name,self.msg)
            else:
                if item in recieved:
                    CTkLabel(self.master,text=item[1],fg_color="lime green",corner_radius=8).pack(anchor="w",pady=2)
                elif item in sent:
                    CTkLabel(self.master,text=item[1],fg_color="SteelBlue1",corner_radius=8).pack(anchor="e",pady=2) 
    
    def reset(self):
        self.returnButton.destroy()
        self.msg()

    def onEnter(self,event):
        if not self.Entry.get() == "":
            text = self.Entry.get()
            CTkLabel(self.master,text=text,fg_color="SteelBlue1",corner_radius=8).pack(anchor="e",pady=2) 
            self.Entry.delete(0,END)
            sleep(1)                                     #THREADING ILE 1 SANIYE BEKLETME MEKANIZMASI YAP
            cursor.execute("INSERT INTO `"+db+"`.`messages` (`messageTime`, `content`, `toM`, `fromM`) VALUES ('"+getTime("sec")+"', '"+text+"', '"+self.name+"', '"+db+"');")

    def spec(self):
        self.topLevel = CTkToplevel(self.master)
        self.topLevel.attributes("-topmost",1)
        self.topLevel.geometry("600x300")
        self.topLevel.title("Özel Mesaj")
        self.topFrame = CTkFrame(self.topLevel,height=28,fg_color="#ffffff")
        self.topFrame.pack(anchor="n",fill="both")
        self.b1 = CTkButton(self.topFrame,fg_color="transparent",text="İlaç Ver",text_color="black",command=self.giveIlac)
        self.b1.grid(row=1,column=1)
        self.b2 = CTkButton(self.topFrame,fg_color="transparent",text="İlaç İste",text_color="black",command=self.takeIlac)
        self.b2.grid(row=1,column=2)
        self.b3 = CTkButton(self.topFrame,fg_color="transparent",text="Kardeşlik Teklifi",text_color="black")
        self.b3.grid(row=1,column=3)
        self.guide = CTkLabel(self.topLevel,text="Lütfen Yukarıdan Bir Tür seçiniz.")
        self.guide.pack()

    def giveIlac(self):
        self.guide.destroy()
        self.giveFrame = CTkFrame(self.topLevel,height=28,fg_color="transparent")
        self.giveFrame.pack(fill="both")
        self.giveEntry = CTkEntry(self.giveFrame,placeholder_text="Karekod")
        self.giveEntry.pack(side="left")
        self.giveButton = CTkButton(self.giveFrame,text="+",width=28,command=self.giveAdd).pack(side="left")
        self.giveFinalButton = CTkButton(self.giveFrame,text="Gönder",width=70,command=self.giveFinal).pack(side="left")
        self.giveTree = ttk.Treeview(self.topLevel,columns=["barkod","ad","fiyat"],show="headings")
        self.giveTree.pack()
        self.inTree = []
        for item in ["barkod","ad","fiyat"]:
            self.giveTree.heading(item,text=item.capitalize())
 
    def giveAdd(self):
        cursor.execute("SELECT * FROM "+db+".stok WHERE karekod = '"+self.giveEntry.get()+"'")
        check = cursor.fetchall()
        if check == []:
            msg.CTkMessagebox(window,title="Hata",message="Aratılan Karekodlu ilaç bulunamadı")
            return
        fetched = check[0]
        if not fetched[4] == None or not fetched[5] == None:
            msg.CTkMessagebox(window,title="Hata",message="Aratılan Karekodlu ilaç, veri tabanınızda Satılmış olarak gözüküyor.")
            return 
        if fetched in self.inTree:
            msg.CTkMessagebox(window,title="Hata",message="Zaten listeye eklenmiş.")
            return
        self.inTree.append(fetched)
        self.giveTree.insert("",END,values=[fetched[0],fetched[1],"10"])

    def giveFinal(self):
        self.topLevel.destroy()
        self.giveKarekods = "#give/"
        for item in self.inTree:
            self.giveKarekods += item[0] + ":"
        self.giveKarekods = self.giveKarekods[:-1]
        time = getTime("sec")
        cursor.execute("INSERT INTO `"+db+"`.`messages` (`messageTime`, `content`, `toM`, `fromM`) VALUES ('"+time+"', '"+self.giveKarekods+"', '"+self.name+"', '"+db+"');")
        GiveMessageBox([time,self.giveKarekods,self.name,db],self.master,"right",self.name,self.msg)

    def takeIlac(self):
        self.guide.destroy()
        self.barkodEntry = CTkEntry(self.topLevel,placeholder_text="Barkod")
        self.barkodEntry.pack(side="left")
        self.countEntry = CTkEntry(self.topLevel,placeholder_text="Miktar")
        self.countEntry.pack(side="left")
        self.enterButton = CTkButton(self.topLevel,text="+",width=28,command=self.takeAdd)
        self.enterButton.pack(side="left")

    def takeAdd(self):
        WantMessageBox([self.barkodEntry.get(),self.countEntry.get()],self.master,"right",self.name)
        self.topLevel.destroy()

class Browser():
    def __init__(self):

        self.window = QWidget()
        self.window.setWindowTitle("Medule Browser")
        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        #self.urlBar = QTextEdit()
        #self.urlBar.setMaximumHeight(30)
        #self.goButton = QPushButton("Go")
        #self.goButton.setMinimumHeight(30)
        #self.goButton.clicked.connect(lambda: self.navigate(self.urlBar.toPlainText()))
        self.backButton = QPushButton("<-")
        self.backButton.setMinimumHeight(30)
        self.forwardButton = QPushButton("->")
        self.forwardButton.setMinimumHeight(30)
        #self.horizontal.addWidget(self.urlBar)
        #self.horizontal.addWidget(self.goButton)
        self.horizontal.addWidget(self.backButton)
        self.horizontal.addWidget(self.forwardButton)
        
        self.browser = QWebEngineView()
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)
        self.browser.setUrl(QUrl("https://medeczane.sgk.gov.tr/eczane/login.jsp"))
        self.backButton.clicked.connect(self.browser.back)
        self.forwardButton.clicked.connect(self.browser.forward)

        self.window.setLayout(self.layout)
        self.window.show()

    '''def navigate(self,url):
        if not url.startswith("https://"):
            #https://www.google.com/search?q=else+if+in
            newUrl = url.split(" ")
            url = "https://google.com/search?q="
            for item in newUrl:
                url += item + "+"
        self.browser.setUrl(QUrl(url))'''

def loginScreen():
    def login(*args):
        def save():
            tempTopLevel.destroy()
            with open(r"./x.txt","w") as file:
                file.write(mainUsername.get() + "," + password.get())
        global connection

        if read != []:
            if mainUsername.get() == "":
                loginUser = read[0]
            else:
                loginUser = mainUsername.get()
            if password.get() == "":
                loginPass = read[1]
            else:
                loginPass = password.get()
        else:
            loginUser = mainUsername.get()
            loginPass = password.get()

        connection = mysql.connector.connect(
            host="ajarise.cylexjzubmxb.eu-north-1.rds.amazonaws.com",
            port=3306,
            user=loginUser,
            password=loginPass
        )
        try:
            if connection.is_connected():
                connection.autocommit = True
                global cursor
                cursor = connection.cursor()
                print("Connection Connected")
                with open(r"./x.txt","r") as file:
                    lines = file.readlines()
                    if lines == []:
                        tempTopLevel = CTkToplevel(window)
                        tempTopLevel.attributes('-topmost',True)
                        tempTopLevel.title("Bildiri")
                        t = CTkLabel(tempTopLevel,text="Bir sonraki girişiniz için şifre ve kullanıcı adınızı kaydetmek ister misiniz?")
                        t.pack(pady=10,padx=5)
                        t = CTkButton(tempTopLevel,text="Evet",command=save)
                        t.pack(pady=5)
                        t = CTkButton(tempTopLevel,text="Hayır",command=lambda:tempTopLevel.destroy())
                        t.pack(pady=5)
                global db
                db = loginUser
                mainScreen()

        except:
            print("Couldn't Connect")
            return
        

    ajariseLogo = CTkLabel(window,text="Ajarise ",font=('TkDefaultFont',60)).pack()
    loginframe = CTkFrame(window)
    loginframe.pack(pady=10,fill="both")
    mainUsername = CTkEntry(loginframe,placeholder_text="Ana kullanıcı adı : ")
    username = CTkEntry(loginframe,placeholder_text="Kişisel kullanıcı adı : ")
    password = CTkEntry(loginframe,placeholder_text="Şifre : ")
    mainUsername.pack(pady=5)
    username.pack(pady=5)
    password.pack(pady=5)
    enterButton = CTkButton(window,text="Giriş Yap",command=login)
    enterButton.pack()
    with open(r"./x.txt","r") as file:
        read = file.readlines()[0].split(",")
        if read != []:
            read[0] = read[0]
            mainUsername.configure(placeholder_text=read[0])
            password.configure(placeholder_text=read[1])
            
def topMenu():
    topMenu = CTkFrame(window,fg_color="#ffffff",bg_color="#ffffff",height=28)
    topMenu.pack(fill="both")
    b1 = CTkButton(topMenu,width=200,text="Stok",fg_color="transparent",text_color="black",command=stockScreen)
    b1.grid(row=1,column=1)
    b2 = CTkButton(topMenu,width=200,text="Perakenade",fg_color="transparent",text_color="black",command=perakenade)
    b2.grid(row=1,column=2)
    b3 = CTkButton(topMenu,width=200,text="Hastalar",fg_color="transparent",text_color="black")
    b3.grid(row=1,column=3)
    b4 = CTkButton(topMenu,width=200,text="İlaçlar",fg_color="transparent",text_color="black")
    b4.grid(row=1,column=4)
    b5 = CTkButton(topMenu,width=200,text="Takas",fg_color="transparent",text_color="black",command=takasScreen)
    b5.grid(row=1,column=5)
    b5 = CTkButton(topMenu,width=200,text="Eczane Ayarları",fg_color="transparent",text_color="black",command=settings)
    b5.grid(row=1,column=6)
    b6 = CTkButton(topMenu,width=200,text="Broswer",fg_color="transparent",text_color="black",command=browser)
    b6.grid(row=1,column=7)
    b7 = CTkButton(topMenu,width=200,text="Muhasebe",fg_color="transparent",text_color="black",command=muhasebe)
    b7.grid(row=1,column=7)

def mainScreen():
    for item in window.winfo_children():
        item.destroy()
    window.geometry(screen)
    topMenu()

def stockScreen():
    for item in window.winfo_children():
        item.destroy()
    topMenu()


    def filterTree():
        filters = []
        if nameFilter.get() != "":
            filters.append("name")
        if barkodFilter.get() != "":
            filters.append("barkod")
        if soldCheckbox.state() == ('focus', 'selected') or soldCheckbox.state() == ('selected',):
            filters.append("satilmis")
        
        if "satilmis" in filters:
            cursor.execute("SELECT * FROM "+db+".stok;")
            fetched = cursor.fetchall()
            final = {}
            for item in fetched:
                if not item[1] + "," + item[2] in final:
                    final.update({item[1] + "," + item[2]:1})
                else:
                    final[item[1] + "," + item[2]] = final[item[1] + "," + item[2]] + 1
            final = list(final.items())
            last = []
            for item in final:
                x = item[0].split(",")
                x.insert(1,item[1])
                last.append(x)
        else:
            last = old

        returner = []    
        for item in last    :
            check = ""
            if "name" in filters:
                if item[0].startswith(nameFilter.get()):
                    check += "1"
                else:
                    check += "0"
            if "barkod" in filters:
                if item[2].startswith(barkodFilter.get()):
                    check += "1"
                else:
                    check += "0"
            if not "0" in check:
                returner.append(item)


        for item in mainTree.get_children():
            mainTree.delete(item)

        for item in returner:
            mainTree.insert("",END,values=item)
        filters = []

    def onDouble(event):
        if mainTree.identify_region(event.x,event.y) not in ("cell"):
            return

        StockIlacInfo(mainTree.item(mainTree.identify_row(event.y))["values"])
        

    frame1 = CTkFrame(window,height=300)
    frame1.pack(fill="both")
    frame2 = CTkFrame(window,height=700)
    frame2.pack(fill='both')
    nameFilter = CTkEntry(frame1,placeholder_text="Ad")
    nameFilter.pack(side='left',anchor="n",padx=2)
    barkodFilter = CTkEntry(frame1,placeholder_text="Barkod")
    barkodFilter.pack(side="left",anchor="n",padx=2)
    soldCheckbox = ttk.Checkbutton(frame1,text="Satılmışları Ekle")
    soldCheckbox.pack(side="left",padx=2)
    searchButton = CTkButton(frame1,text="+",width=28,command=filterTree)
    searchButton.pack(side='left',anchor="n",padx=2)
    contents =["ad","miktar","barkod","tür"]
    mainTree = ttk.Treeview(frame2,columns=contents,show="headings")
    for item in contents:
        mainTree.heading(item,text=item.capitalize())
    cursor.execute("SELECT * FROM "+db+".stok;")
    fetched = cursor.fetchall()
    final = {}
    for item in fetched:
        if item[5] == None or item[4] == None:
            if not item[1] + "," + item[2] in final:
                final.update({item[1] + "," + item[2]:1})
            else:
                final[item[1] + "," + item[2]] = final[item[1] + "," + item[2]] + 1
    final = list(final.items())
    last = []
    for item in final:
        x = item[0].split(",")
        x.insert(1,item[1])
        last.append(x)
    old = last.copy()
    for item in last:
        mainTree.insert("",END,values=item)

    mainTree.pack()
    mainTree.bind("<Double-1>",onDouble)

def perakenade():
    for item in window.winfo_children():
        item.destroy()
    topMenu()
    def sellAction():
        
        cursor.execute("SELECT * FROM "+db+".stok WHERE karekod = '"+KarekodEntry.get()+"'")
        fetched = cursor.fetchall()
        if fetched == []:
            msg.CTkMessagebox(window,title="Hata",message="Arattığınız ilaç sistemde bulunmadı, mümkün neden: İlaç Bu eczaneye aktarılmadı veya karekod yanlış girildi.")
            return 
        if fetched[0][4] != None or fetched[0][5] != None:
            msg.CTkMessagebox(window,title="Hata",message="Aratılan ilaç sisteminizde satılmış gözüküyor.")   #REÇETE KONTROL VE TAKAS HATASI EKLE         
            return  
        alreadyInTree = []
        for item in mainTree.get_children():
            alreadyInTree.append(mainTree.item(item)["values"][1])
        if int(KarekodEntry.get()) in alreadyInTree:
            msg.CTkMessagebox(window,title="Hata",message="Girdiğiniz Karekod zaten listede")
            return  
        inserting = [fetched[0][1],fetched[0][0],fetched[0][2],10]#BURAYI DOLDUR
        mainTree.insert("",END,values=inserting)
        
        total = 0
        for item in mainTree.get_children():
            total += int(mainTree.item(item)["values"][3])
        totalLabel.configure(text="Toplam : " + str(total))
    
    def onDouble(event):
        mainTree.delete(mainTree.identify_row(event.y))

    def recentlySold():
        for item in leftFrame.winfo_children():
            item.destroy()
        sideTree = ttk.Treeview(leftFrame,columns=["ad","karekod","barkod","satisTarih","satmaIlac","fiyat"],show="headings")
        for item in ["ad","karekod","barkod","satisTarih","satmaIlac","fiyat"]:
            sideTree.heading(item,text=item.capitalize())
        cursor.execute("SELECT * FROM "+db+".stok;")
        fetched = cursor.fetchall()
        x = 0
        for i in range(0,len(fetched)):
            if fetched[x][4] == None:
                fetched.pop(x)
            elif fetched[x][4][:6] == getTime()[:6]:
                x += 1
            else:
                fetched.pop(x)
        inserting = []
        for item in fetched:
            inserting.append([item[1],item[0],item[2],item[4],item[5],"10"])
        for item in inserting:
             sideTree.insert("",END,values=item) 
        sideTree.pack()

    def sell():
        hasta = HastaEntry.get()
        if hasta == "":
            msg.CTkMessagebox(window,title="Hata",message="Hasta adı boştur, birdaha 'Sat' butonuna basarak anonim/misafir olarak satış yapabilirsiniz.")
            HastaEntry.insert(0,"Anonim")
            return
        if mainTree.get_children() == []:
            msg.CTkMessagebox(window,title="Hata",message="Lütfen listeye İlaç ekleyiniz.")
            return
        for item in mainTree.get_children():
            sellItem = mainTree.item(item)["values"][1]
            cursor.execute("UPDATE `"+db+"`.`stok` SET `satmaHasta` = '"+hasta+"' WHERE (`karekod` = '"+str(sellItem)+"');")
            cursor.execute("UPDATE `"+db+"`.`stok` SET `satmaTarih` = '"+getTime()+"' WHERE (`karekod` = '"+str(sellItem)+"');")
            mainTree.delete(item)
        totalLabel.configure(text="Toplam : ")
        recentlySold()

    topFrame = CTkFrame(window,height=100)
    topFrame.pack(fill="both")
    
    leftFrame = CTkXYFrame  (window,width=400)
    leftFrame.pack(side="left",padx=5,pady=5,anchor="n")
    midFrame = CTkFrame(window,width=800)
    midFrame.pack(fill="both",padx=5,pady=5)
    
    KarekodEntry = CTkEntry(topFrame,placeholder_text="Karekod")
    KarekodEntry.pack(side="left")
    HastaEntry = CTkEntry(topFrame,placeholder_text="Hasta")
    HastaEntry.pack(side="left")
    SearchButton = CTkButton(topFrame,text="+",width=28,command=sellAction)
    SearchButton.pack(side="left")
    mainTree = ttk.Treeview(midFrame,columns=["ad","karekod","barkod","fiyat"],show="headings")
    totalLabel = CTkLabel(midFrame,text="Toplam : ")
    totalLabel.pack()
    for item in ["ad","karekod","barkod","fiyat"]:
        mainTree.heading(item,text=item.capitalize())
    mainTree.pack()
    mainTree.bind("<Double-1>",onDouble)
    sellButton = CTkButton(midFrame,text="Satış",command=sell)
    sellButton.pack()
    recentlySold()

def takasScreen():
    for item in window.winfo_children():
        item.destroy()
    topMenu()
    
    def onDoubleLeft(event):
        def ret():
            msg.CTkMessagebox(leftTopLevel,title="Dikkat",message="Eğer ilaç yoldayken bunu yaparsanız geri alınan eczaneye gönderilmesi veya takas işleminin yeniden yapılması gerekebilir. Lütfen bu seçimi yapmadan önce gelecek eczane ile iletişime geçiniz. Eminseniz yeniden tuşa bakarak iptal edebilirsiniz.")
            button.configure(command=conf,text="Emin Misiniz?")
        def conf():
            cursor.execute("INSERT INTO `"+db+"`.`messages` (`messageTime`, `content`, `toM`, `fromM`) VALUES ('"+getTime("sec")+"', '"+db+" eczanesi "+values[0]+" barkodlu ilacın takasını reddetmiştir. -Sistem', '"+values[2]+"', '"+db+"');")
            cursor.execute("DELETE FROM "+db+".takas WHERE karekod = '"+values[0]+"'")
            cursor.execute("DELETE FROM "+values[2]+".takas WHERE karekod = '"+values[0]+"'")
            refresh()
        if leftTree.identify_region(event.x,event.y) not in ("cell"):
            return
        values = leftTree.item(leftTree.identify_row(event.y),"values")
        leftTopLevel = CTkToplevel(window)
        leftTopLevel.title(values[1])
        leftTopLevel.geometry("400x400")
        for item in values:
            if not item == None:
                CTkLabel(leftTopLevel,text=item).pack()
        button = CTkButton(leftTopLevel,text="Gelmesini Reddet",command=ret)
        button.pack()
    leftFrame = CTkFrame(window,width=int(screen[:4])/2)
    leftFrame.pack(side="left",padx=2,pady=2,anchor="n")
    rightFrame = CTkFrame(window,width=int(screen[:4])/2)
    rightFrame.pack(side="right",padx=2,pady=2,anchor="n")
    gelenLabel = CTkLabel(leftFrame,text="Gelecek İlaçlar",font=("TkDeafultFont",25))
    gelenLabel.pack(anchor="n")
    gidenLabel = CTkLabel(rightFrame,text="Gidecek İlaçlar",font=("TkDeafultFont",25))
    gidenLabel.pack(anchor="n")

    leftTree = ttk.Treeview(leftFrame,columns=["karekod","ad","eczane","tarih"],show="headings")
    leftTree.pack()
    for item in ["karekod","ad","eczane","tarih"]:
        leftTree.heading(item,text=item)
    rightTree = ttk.Treeview(rightFrame,columns=["karekod","ad","eczane","tarih","tamamlandı"],show="headings")
    rightTree.pack()
    for item in ["karekod","ad","eczane","tarih","tamamlandı"]:
        rightTree.heading(item,text=item)

    def refresh():
        for item in leftTree.get_children():
            leftTree.delete(item)
        for item in rightTree.get_children():
            rightTree.delete(item)
        cursor.execute("SELECT * FROM "+db+".takas;")
        fetched = cursor.fetchall()
        x = 0
        for i in range(0,len(fetched)):
            if fetched[x][5] != None:
                fetched.pop(x)
            else:
                x += 1
        
        ifList = []
        elseList = []
        for item in fetched:
            if item[2] == db:
                ifList.append(item)
            elif item[3] == db:
                elseList.append(item)
        for item in ifList:
            leftTree.insert("",END,values=[item[0],item[1],item[3],item[4]])
        for item in elseList:
            rightTree.insert("",END,values=[item[0],item[1],item[2],item[4],"Hayır"])
        leftTree.bind("<Double-1>",onDoubleLeft)

    def giveEnter():
        karekod = cameEntry.get()
        cameEntry.delete(0,END)
        cursor.execute("SELECT * FROM "+db+".takas WHERE karekod = '"+karekod+"';")
        fethced = cursor.fetchone()
        if fethced == None:
            msg.CTkMessagebox(window,title="Hata",message="Aratılan Karekod takas veri tabanınızda bulunamadı.")
            return
        if fethced[2] != db:
            msg.CTkMessagebox(window,title="Hata",message="Aratılan Karekodlu ilaç veri tabanınızda bulundu fakat gönderildiği eczane siz değilsiniz.Mümkün hatalar: Sizden gidecek bir ilaç olabilir.")    
            return
        
        cursor.execute("SELECT * FROM "+db+".takas WHERE karekod = '"+karekod+"#'; ")
        newfetched = cursor.fetchone()
        if not newfetched == ():
            cursor.execute("DELETE FROM "+db+".takas WHERE karekod = '"+karekod+"#';")
        cursor.execute("UPDATE "+db+".`takas` SET `alTarih` = '"+getTime("sec")+"' WHERE (`karekod` = '"+karekod+"');")
        cursor.execute("UPDATE "+db+".takas SET karekod = '"+karekod + "#' "+" WHERE karekod = '"+karekod+"'")

        cursor.execute("SELECT * FROM "+fethced[3]+".takas WHERE karekod ='"+karekod+"#';")
        newfetched = cursor.fetchone()
        if not newfetched == ():
            cursor.execute("DELETE FROM "+fethced[3]+".takas WHERE karekod = '"+karekod+"#'")
        cursor.execute("UPDATE "+fethced[3]+".takas SET karekod = '"+karekod+"#' WHERE karekod='"+karekod+"'")
        cursor.execute("UPDATE "+fethced[3]+".`takas` SET `alTarih` = '"+getTime("sec")+"' WHERE (`karekod` = '"+karekod+"');")

        cursor.execute("SELECT * FROM "+fethced[3]+".stok  WHERE (`karekod` = '"+karekod+"');")
        fetchone = cursor.fetchone()
        cursor.execute("DELETE FROM `"+fethced[3]+"`.`stok` WHERE (`karekod` = '"+karekod+"');")
        cursor.execute("INSERT INTO `"+db+"`.`stok` (`karekod`, `ad`, `barkod`, `almaTarih`, `satmaTarih`, `satmaHasta`, `almaYer`) VALUES ('"+karekod+"', '"+fetchone[1]+"', '"+fetchone[2]+"', '"+getTime()+"', NULL, NULL, '"+fethced[3]+"');")
        refresh()

    #leftFrame
    cameEntry = CTkEntry(leftFrame,placeholder_text="Karekkod")
    cameEntry.pack()
    enterButton = CTkButton(leftFrame,text="+",width=28,command=giveEnter)
    enterButton.pack()
    refresh()

def settings():
    for item in window.winfo_children():
        item.destroy()
    topMenu()
    
    def msgOpen():
        for item in leftframe.winfo_children():
            item.destroy()
        cursor.execute("SELECT * FROM "+db+".messages WHERE toM = 'x';")
        fetched = cursor.fetchall()
        allMessages = []
        for item in fetched:
            if not item[0] == "sistem":
                cursor.execute("SELECT * FROM "+item[0]+".messages WHERE not toM = 'x';")
                allMessages.append(cursor.fetchall())   
        firstSort = []
        for item in allMessages:
            firstSort.append(sorted(item,key=itemgetter(0))[-1])
        for item in sorted(firstSort,key=itemgetter(0),reverse=True):
            Messengers(item,leftframe,msgOpen)
    leftframe = CTkScrollableFrame(window,width=300)
    leftframe.pack(side="left",fill="both",anchor="n")
    msgOpen()

def muhasebe():
    for item in window.winfo_children():
        item.destroy()
    topMenu()
    topFrame = CTkFrame(window)
    topFrame.pack(anchor="n")
    menuFrame = CTkFrame(topFrame,height=int(screen[:4]))
    menuFrame.pack(side="left",anchor="nw")
    secondFrame = CTkFrame(topFrame,height=1)
    secondFrame.pack(side="left",anchor="n")
    def home():
        button1 = CTkButton(menuFrame,text="Gelirler",fg_color="transparent",text_color="black",command=gelirler)
        button1.grid(row=2,column=1,ipady=5)
        button2 = CTkButton(menuFrame,text="Raporlar",fg_color="transparent",text_color="black",command=raporlar)
        button2.grid(row=3,column=1,ipady=5)
        button3 = CTkButton(menuFrame,text="Giderler",fg_color="transparent",text_color="black",command=giderler)
        button3.grid(row=4,column=1,ipady=5)
    def gelirler():
        for item in secondFrame.winfo_children():
            item.destroy()
        button1 = CTkButton(secondFrame,text="Perakenade Satış",fg_color="transparent",text_color="black",command=perkenadeSatis)
        button1.grid(row=1,column=1,ipady=5)
        button2 = CTkButton(secondFrame,text="SGK Satış",fg_color="transparent",text_color="black")
        button2.grid(row=2,column=1,ipady=5)
    def raporlar():
        for item in secondFrame.winfo_children():
            item.destroy()
        button1 = CTkButton(secondFrame,text="Toplam Satış",fg_color="transparent",text_color="black")
        button1.grid(row=1,column=1,ipady=5)
        button2 = CTkButton(secondFrame,text="Aylık Satış",fg_color="transparent",text_color="black")
        button2.grid(row=2,column=1,ipady=5)
        button3 = CTkButton(secondFrame,text="Yıllık Satış",fg_color="transparent",text_color="black")
        button3.grid(row=3,column=1,ipady=5)
    def giderler():
        for item in secondFrame.winfo_children():
            item.destroy()
        button1 = CTkButton(secondFrame,text="Personel",fg_color="transparent",text_color="black")
        button1.grid(row=1,column=1,ipady=5)
        button2 = CTkButton(secondFrame,text="Eczacı",fg_color="transparent",text_color="black")
        button2.grid(row=2,column=1,ipady=5)
        button3 = CTkButton(secondFrame,text="Eczane",fg_color="transparent",text_color="black")
        button3.grid(row=3,column=1,ipady=5)
    def perkenadeSatis():
        configureTree(["karekod","barkod","ad","fiyat","tarih","hasta"],)
    home()

    def configureTree(headings,value):
        mainTree = ttk.Treeview(window,show="headings",columns=headings)
        for item in headings:
            mainTree.heading(item,text=item.capitalize())

def browser():
    app = QApplication([])
    Qwindow = Browser()
    app.exec()

loginScreen()

window.mainloop()
try:
    connection.close()
except:
    print("Closed without connection")
else:
    print("Closed Connection")

#MESAJLAR YENİ ESKİ SIRASI
#UZUN MESAJLARI SIĞDIRMA
#GİDECEK İLAÇLAR TAMAMLANDI CHECKBOX : cursor exeecute if karekod + "#" falan
#WANT MESSAGE BOX