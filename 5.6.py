#6
import itertools
var = "XYZ"
#perm1-ში ჯოინი სტრინგად გადასაქცევად დამჭირდა
perm1 = [''.join(i) for i in itertools.permutations(var, 1)]
perm2 = [''.join(i) for i in itertools.permutations(var, 2)]
perm3 = [''.join(i) for i in itertools.permutations(var, 3)]
perm = list(itertools.chain(perm1, perm2, perm3))
print(perm)