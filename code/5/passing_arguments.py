def print_somthing(my_name, your_name):
    print("Hello {0}, My name is {1}".format(your_name, my_name))

print_somthing("Sungchul", "TEAMLAB")
print_somthing(your_name="TEAMLAB", my_name="Sungchul")

def print_somthing_2(my_name, your_name="TEAMLAB"):
    print("Hello {0}, My name is {1}".format(your_name, my_name))

print_somthing_2("Sungchul", "TEAMLAB")
print_somthing_2("Sungchul")
