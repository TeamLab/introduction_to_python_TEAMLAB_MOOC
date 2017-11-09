def asterisk_test(a, b, *args):
    return a+b+sum(args)


print(asterisk_test(1, 2, 3, 4, 5))
<<<<<<< HEAD


def asterisk_test_2(*args):
    x, y, z = args
    return x, y, z


print(asterisk_test_2(3, 4, 5))
=======
>>>>>>> c312bb0449ce721bb60ecc38f420ea75a6d6f9cd
