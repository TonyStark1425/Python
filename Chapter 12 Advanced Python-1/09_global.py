a = 89
def fun():
    global a
    a = 7
    print(a)

fun()
print(a)