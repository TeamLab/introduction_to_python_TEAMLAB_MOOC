f = open("yesterday.txt", "r")
yesterday_lyric = ""
while 1:
	line = f.readline()
	# print(line)
	if not line:
		break
	yesterday_lyric = yesterday_lyric + line.strip() + "\n"
	# print (yesterday_lyric)
f.close()
n_of_yesterday = yesterday_lyric.upper().count("yesterday")
print ("Number of a Word 'Yesterday'" , n_of_yesterday)
