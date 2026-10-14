students={
    101:{"Name" , "Aditi" , "Scores" : [10,20,25]},
    102:{"Name" , "Rahul" , "Scores" : [10,40,38]},
    103:{"Name" , "Saurabh","Scores" :[25,20,25]},
    104:{"Name" , "Vinay" , "Scores" : [26,47,25]},
}
for sid, details in students.items():
    avg = sum(details["Score"]) / len(details["Scores"])
    details["Average"]=avg
    details["Passed"]  = avg >=30
    
