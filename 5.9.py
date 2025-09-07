#9
from datetime import datetime, date
usr = input("შეიყვანე დაბადების თარიღი(YYYY-MM-DD): ")
tarigi = datetime.strptime(usr, "%Y-%m-%d").date()
today = date.today()
bday = date(today.year, tarigi.month, tarigi.day) #დბ წელს
if today >= bday:
    nextbday = date(today.year + 1, tarigi.month, tarigi.day)
    remaining = nextbday - today
    print(f"დარჩა {remaining.days} დღე")
elif today < bday:
    nextbday = date(today.year, tarigi.month, tarigi.day)
    remaining = nextbday - today
    print(f"დარჩა {remaining.days} დღე")