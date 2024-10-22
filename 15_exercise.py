# Print Square Sequence using yield
#     Create Generator method such that every time it will returns a next square number
#
# for exmaple : 1 4 9 16 ..

def n_s():
    i = 1
    while True:
        yield i * i
        i += 1

for n in n_s():
    if n>25:
        break
    print(n)