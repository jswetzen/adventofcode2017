import sys
l = sys.stdin.readline().strip()

print(sum((int(a) for a,b in zip(l,l[1:]+l) if a is b)))
print(sum((int(a) for a,b in zip(l,l[len(l)//2:]+l) if a is b)))
