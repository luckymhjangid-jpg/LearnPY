with open("read1.txt" ,"r") as listt:
    listt =  listt.readlines()

print("Total lines",len(listt))
print("2nd line", listt[1])
print("4th line" ,listt[3])


