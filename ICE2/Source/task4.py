#list of words and return the longest one
inp =True
list1=[]
count1=[]
max = 0
while(inp):
    word=input('enter a word')
    if(word.__eq__('No')):
        break
    list1.append(word)
    count1.append(word.__len__())
result1=[]
for x in list1:
  result1.append((str(x).__len__(),x))
result1.sort()
print(result1)
print(result1.__getitem__(result1.__len__()-1))