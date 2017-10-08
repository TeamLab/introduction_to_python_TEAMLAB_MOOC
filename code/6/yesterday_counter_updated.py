f = open("yesterday.txt", "r")
yesterday_lyric = ""
while 1:
	line = f.readline()
	if not line:
		break
	yesterday_lyric = yesterday_lyric + line.strip() + "\n"
f.close()
small_n_of_yesterday = yesterday_lyric.count("Yesterday")
titled_n_of_yesterday = yesterday_lyric.count("yesterday")

print ("Number of a Word 'Yesterday'" , small_n_of_yesterday)
print ("Number of a Word 'yesterday'" , titled_n_of_yesterday)
