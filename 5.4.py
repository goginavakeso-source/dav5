#4
from datetime import datetime
today = datetime.today()
newy = datetime(today.year + 1, 1, 1)
remaining = (newy - today).days // 7
print(f"ახალ წლამდე დარჩა {remaining} კვირა")