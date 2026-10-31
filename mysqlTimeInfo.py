"""Local demo clock; preserves the original getTime() return formats."""
from datetime import datetime, timezone, timedelta


def getTime(*args):
    now = datetime.now(timezone(timedelta(hours=3)))
    if args == ():
        return now.strftime("%y%m%d%H%M")
    if args == ("sec",):
        return now.strftime("%y%m%d%H%M%S")
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    return [now.strftime("%H:%M:%S"),
            f"{now.day} {months[now.month - 1]} {now.year}"]


if __name__ == "__main__":
    print(getTime("sec"))
