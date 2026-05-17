"""dict={
    "name":"satyarth",
    "subjects" : ["python", "java", "c++"],
    "topics" : ["list", "tuple", "dictionary"],
    "list" : [1, 2, 3, 4, 5],
    "is_adlt" : True,
    "age": 23,
    "marks": 90.5
}
print(dict)
print(type(dict))   
print(dict["name"])
print(dict["subjects"])     
print(dict["topics"])
print(dict["list"])
dict["list"].reverse()

print(dict["list"])
dict["age"] = 24
print(dict["age"])
dict["gender"] = "Female"
print(dict)

null_dictt = {}
print(null_dictt)   
null_dictt["name"] = "satyarth"
null_dictt["age"] = 23
print(null_dictt)"""

student = {
    "name" : "Sushil",
    "age" : 23,
    "subjects_Marks":{
        "python": 90,
        "java": 85,
        "c++": 80
    }
    }
"""print(student)
print(student["subjects_Marks"])
print(student["subjects_Marks"]["python"])

print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))
print(list(student["subjects_Marks"].keys()))   
print(list(student["subjects_Marks"].values()))
print(list(student["subjects_Marks"].items()))
print(len(student) )
print(len(student["subjects_Marks"]))
print(student.get("name   "))
print(student.get("name", "Not Found"))"""
"""print(student["name"])
print(student.get("name"))"""


"""student.update({"name": "Satyarth"})
print(student.update({"Roll_Number": 24}))
print(student)



#store follwing wrod meaing in dictionary and print them
dictt = {
    "cat" : "A small animal",
    "table" : ["A piece of furniture", "List of facts& figures"]
}
print(dictt)"""

#wap to enter marks of 3 subjects from the user and store them in a dictionary and print the dictionary and start wirh an
#  empty dictionary
marks ={}
marks["physics"] = input("enter phy marks : ")
marks["chemistry"] = input("enter chem marks : ")
marks["maths"] = input("enter maths marks : ")
print(marks)
