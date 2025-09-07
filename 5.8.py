#8
import random
from datetime import timedelta, datetime

start = datetime.now()
player1 = start + timedelta(seconds=random.randint(5,20))
player2 = start + timedelta(seconds=random.randint(5,20))
time1 = (player1 - start).total_seconds()
time2 = (player2 - start).total_seconds()
if time1 > time2:
    print(f"გამარჯვებული: პირველი მოთამაშე. დრო: {time1} წამი")
elif time1 < time2:
    print(f"გამარჯვებული: პირველი მოთამაშე. დრო: {time2} წამი")
else:
    print(f"ფრე. დრო: {time1}")