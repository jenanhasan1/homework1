import json
name = input("YOUR NAME IS : ")
i = 0
jen = 0
with open('data.json') as jsonfile:
    data = json.load(jsonfile)
    for j in data:
        print(j)
        ANS = input()
        if ANS == data[j]:
            i += 1
        jen += 1

resultFile = open("JEN.txt", "w")
resultFile.write("your name is: "+name+"\n")
resultFile.write("and your a result is: " + str(i)+"/" + str(jen))
