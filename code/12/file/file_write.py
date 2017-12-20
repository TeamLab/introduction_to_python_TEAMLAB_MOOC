f = open("count_log.txt", 'w', encoding="utf8")
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

with open("count_log.txt", 'a', encoding="utf8") as f:
    for i in range(100, 111):
        data = "%d번째 줄입니다.\n" % i
        f.write(data)
