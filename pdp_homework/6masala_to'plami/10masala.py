n = int(input("n ni kiriting: "))

k = 1
while 3 ** k < n:
    k += 1

print("3k < n tengsizlik o'rnli eng katta k:", k)
