guest = []
guest.append("Alice")
guest.append("jhon")
guest.append(1)
guest.insert(0,"Charlie")
party_group = ["simon" , "andrew"]
guest.extend(party_group)

data = guest.sort()
print(data)
