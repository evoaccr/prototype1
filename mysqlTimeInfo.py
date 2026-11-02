import requests
from bs4 import BeautifulSoup

def getTime(*args):
    req = requests.get("https://www.timeanddate.com/time/zone/turkey/istanbul")

    soup = BeautifulSoup(req.content,"html.parser")

    prettyT = soup.find('span', id='ct').text.strip()
    prettyD = soup.find('span', class_='fs-date').text.strip()

    t = prettyT
    d = prettyD

    '''t = "10:24:24"
    d = "2 Eylül 2024 Cumartesi"'''

    f = ""

    d = d.split(" ")
    t = t.split(":")
    f += d[2][2:]
    if d[1] == "Ocak":
        f += "01"
    elif d[1] == "Şubat":
        f += "02"
    elif d[1] == "Mart":
        f += "03"
    elif d[1] == "Nisan":
        f += "04"
    elif d[1] == "Mayıs":
        f += "05"
    elif d[1] == "Haziran":
        f += "06"
    elif d[1] == "Temmuz":
        f += "07"
    elif d[1] == "Ağustos":
        f += "08"
    elif d[1] == "Eylül":
        f += "09"
    elif d[1] == "Ekim":
        f += "10"
    elif d[1] == "Kasım":
        f += "11"
    elif d[1] == "Aralık":
        f += "12"
    if len(d[0]) == 1:
        f += "0" + d[0]
    else:
        f += d[0]
    f += t[0]
    f += t[1]
    if args == ():
        return f
    elif args == ("sec",):
        return f + t[2]
    else:
        return [prettyT,prettyD]

if __name__ == '__main__':
    print(getTime("sec"))