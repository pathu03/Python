class partherror(Exception):
    pass
x=9
assert x==6,"partherror"

if x==6:
    raise partherror("no chale")

print(x)