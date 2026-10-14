with open("read1.txt" , "r") as read1:
   fileread = read1.read()


count =0
for i in fileread:
    if('a' == i or 'A' == i):
      count +=1
    if('e' == i or 'E' == i):
          count +=1
    if('i' == i or 'I' == i):
          count +=1
    if('o' == i or 'O' == i):
          count +=1
    if('u' == i or 'U' == i):
          count +=1

print(count)
    


    
   