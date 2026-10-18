
freq={}
with open("sample.txt", "r") as file1:
    readfile1 = file1.readlines()
    

with open("textfile.txt", "w") as file2:
    count =1
    for line in readfile1:
        if(count % 2 == 0):
            file2.write(line)
        count +=1
        
    
with open("textfile.txt", "r") as file2:
    readfile2 = file2.read()
    print(readfile2)
    




  

    
    










