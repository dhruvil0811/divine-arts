def mygen():
    yield 'A'
    yield 'B'
    yield 'C'

g = mygen()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(nect(g)) 

