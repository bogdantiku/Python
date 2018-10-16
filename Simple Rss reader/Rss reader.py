import feedparser
import random #Random module is imported

d = feedparser.parse('http://hvg.hu/rss/tudomany')
#for post in d.entries:
    #print(post.title + "\n")

number =0
for i in d.entries:
    number = number + 1
    #if number == 1 or number == 3 or number == 4 or number == 13 or number ==  18:
    print (number,".",i.title)

print("------------------------------------")
def returnTitle(titleNumber):
    d = feedparser.parse('http://hvg.hu/rss/tudomany')
    #for post in d.entries:
        #print(post.title + "\n")

    number = 0
    for i in d.entries:
        number = number + 1
        if number == titleNumber:
            print(number, ".", i.title)
            return i.title


#print(returnTitle())

#deck = 13
while 1 == 1: #The script will ask for input over and over
 deck = int(input("Enter text!")) #Entered text is split into separate words
 if deck == 0: #Exit by typing zero
     break

 myTitle = returnTitle(deck)


#print("Original title:", deck, " is: ", myTitle)
#print (returnTitle(13))
 splitTitle = myTitle.split()
 random.shuffle(splitTitle) #Separeted words are shuffled
 print("Mixed words: ",", ".join(splitTitle))
