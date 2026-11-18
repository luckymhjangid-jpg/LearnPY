with open("sample.txt" ,"r") as file:
    
    file.seek(0)
    ct = file.readline()
    ws = ct.split()
print(ct)

print(ct)
print("Total words",len(ws))