import feedparser
import random #Random module is imported

d = feedparser.parse('http://hvg.hu/rss/vilag')
#for post in d.entries:
    #print(post.title + "\n")

number =0
for i in d.entries:
    number = number + 1
    #if number == 1 or number == 3 or number == 4 or number == 13 or number ==  18:
    print (number,".",i.title)

print("------------------------------------")
def returnTitle(titleNumber):
    d = feedparser.parse('http://hvg.hu/rss/vilag')
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
deck = int(input("Enter text!")) #Entered text is split into separate words
myTitle = returnTitle(deck)

#print("Original title:", deck, " is: ", myTitle)
#print (returnTitle(13))
splitTitle = myTitle.split()
random.shuffle(splitTitle) #Separeted words are shuffled
print("Mixed words: ",", ".join(splitTitle))
