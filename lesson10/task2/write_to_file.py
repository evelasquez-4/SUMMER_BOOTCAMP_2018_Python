file = open("output.txt","a")

for i in range(0,100,5):
	file.write(str(i)+" \n")

file.close()