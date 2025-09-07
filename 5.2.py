#2
# 1 რადგან არის სამშაბათის ინდექსი, ამიტომ გამოვაკელი 1-ს დღევანდელი დღის ინდექსი. ასევე ბოლოს ნაშთით 7ზე აღარ გავყავი, რადგან
#როგორც მივხვდი, მაგ. დღეს რომ ორშაბათი იყოს, ხვალინდელ სამშაბათს დაითვლიდა მაგ შემტხვევაში
from datetime import datetime, timedelta
today = datetime.today()
day_ow = today.weekday()
days_remaining = (1 - today.weekday() + 7)
next_t = today + timedelta(days_remaining)
print(next_t)