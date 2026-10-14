 #lsit of odd numeber table
for i in range(1,11):
    if(i % 2 !=0):
       for j in range(1,11):
           print(i*j,end=" ")
           print(" ")


#create a hetrogenous list of number and name, split the list from highest number
#accept the number and check if the number is palindrome
#print the sum of digits
#print the following pattern
listt = [1,"raj",2,"soham",5,3,4,"rohan"]
i=0
max=0
while(i <len(listt)):
    if(type(list[i])==int):
        max = max(listt)
    
    
        


     
    






n=123
temp=n
val=n
palin=0
res=100
while((n !=0)):
    temp=n % 10
    palin = palin  + temp*res
    res=res//10
    n= n //10
print(palin)
j=4
for i in range(5):
    print(' '*j,'* ' * i,)
   
    j=j-1

t=20
sum=0
for i in range(t+1):
    sum=sum+i
print(sum)



