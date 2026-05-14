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
print(student)
print(student["subjects_Marks"])
print(student["subjects_Marks"]["python"])