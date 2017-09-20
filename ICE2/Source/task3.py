#list of numbers
inp = True
list1=[]
while(inp):
  x =input('Enter the element to list')
  if(x.__eq__("No")):
      break
  list1.append(x)
list2 =[list1[0],list1[list1.__len__()-1]]
print(list1)
print(list2)