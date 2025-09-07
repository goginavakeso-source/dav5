#10
import itertools
import random
import string

digits = string.digits

password = ''.join(str(random.randint(1, 6)) for _ in range(4))

#ყველა შესაძლო პაროლი
yvela = [''.join(p) for p in itertools.product(digits, repeat=4)]

for paroli in yvela:
    print(paroli)
    if paroli == password:
        print(f"{paroli} სწორია")
        break