string_ex = "123abc"
for value in string_ex:
    try:
        print(int(value))
    except NameError as err:
        print(err)
