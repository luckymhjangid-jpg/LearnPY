numbers =[10,34,21,56,77,49]
result=[]
for i in range(len(numbers)):
    if(numbers[i] % 2 == 0):
        result.append(numbers[i])

print(result)

s ="abdgierng"
total_vowels = 0
clean_s = s.lower()
vowel_list = ["a", "e","i","o","u"]
for vowel  in vowel_list:
    occurence = clean_s.count(vowel)
    total_vowels = total_vowels + occurence
print(total_vowels)




