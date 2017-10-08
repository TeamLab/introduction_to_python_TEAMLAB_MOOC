def f():
    global s
    s = "I love London!"
    print(s)

s = "I love Paris!"
f()
print(s)