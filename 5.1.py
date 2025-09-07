#1
import itertools

word = "ABCD"
perms = [''.join(l) for l in itertools.permutations(word)]
print(perms)
print(f"ვარიაციების რაოდენობა: {len(perms)}")