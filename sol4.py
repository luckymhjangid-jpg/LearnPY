inputt = input("Enter any sentence:")
with open("input.txt" , "w+") as file1:
    file1.write(inputt)
    file1.seek(0)
    dataa=file1.read()

words = dataa.split()
biggest=""
for w in words:
    if len(w) > len(biggest):
        biggest=w
print(biggest)
