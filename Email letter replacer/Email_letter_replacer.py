import re
#s = input("Enter email: ")#Enter desired email
s="Some.Name@gmail.com"
s=re.split(r"[\@'.]+",s) #split by dot and @
s2=(s[0][:1].replace(s[0][:1], "%",1)+s[0][1:]+"."+s[1][:1].replace(s[1][:1], "%",1)+s[1][1:]+"@"+s[2][:1].replace(s[2][:1], "%",1)+s[2][1:]+"."+s[3][:1].replace(s[3][:1], "%",1)+s[3][1:])
print(s2)
