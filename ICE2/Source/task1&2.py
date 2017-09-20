#character frequency in a string
str = input('Enter a string')
x=[]
for i in str:
    if(not x.__contains__(i)):
       x.append(i)
       print(i,str.count(i))
#calculate number of digits and letters
digit = 0
alpha=0
for i in str:
   if(i.isdigit()):
     digit= digit+1
   else:
      alpha = alpha+1
print('No of digits',digit)
print('No of characters',alpha)