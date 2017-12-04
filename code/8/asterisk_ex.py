def asterisk_test(a, *vars):
    print(a, vars)
    print(type(vars))


asterisk_test(1,2,3,4,5,6)

asterisk_test(1, *(2,3,4,5,6))

a, b, c = ([1, 2], [3, 4], [5, 6])
print(a, b, c)

data = ([1, 2], [3, 4], [5, 6])
print(*data)


for data in zip(*([1, 2], [3, 4], [5, 6])):
    print(data)

def asterisk_test(a, b, c, *vars):
    print(a, b, c)

data = {"a":1 , "b":2, "c":3}
asterisk_test(**data)
