info = {
    "name" : "apna college",
    "subjects" : ["python", "java", "C++", "javascript"],
    "topics" : ("data structures", "dict" , "set"),
    "age": 23,
    "is_adult": True,
    12.99 : 23.54,


}

print (type(info))
print(info["topics"])


student = {
    "name" : "Mayuri Gupta",
    "college" : "apna college",
    "subjects" : {
        "physics" : 90,
        "chemistry" : 46,
        "maths" : 30,

    }
}

#nested dictionary 
print(student["subjects"]["physics"])
print(len(list(student.keys())))
print(student.values())
pairs = list(student.items())
print(pairs[0])
print(student.get("name2")) #noerror
# print(student["name2"]) error

new_dict = {"city" : "delhi"}
student.update(new_dict)

print(student)

#set
collection = {1, 2, 3, 4}

print(collection)
print(type(collection))

collection = {} #empty dictionary
print(type(collection))
collection = set() #empty set
print(type(collection))

#practice questions 1- store following word meaning in a dictionary
word_meaning = {
    "table": ("a piece of furniture", "list of facts and figires"),
    "cat": "a small animal"
}

print(word_meaning)

#you are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.

subjects = {
    "python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "C",

}

print(len(subjects))

#WAP to enter marks of 3 subjects from the user and store them in a dictionary . Start with an empty dictionary and add one by one .Use subject name as key and marks as value.
marks = {}

x = int(input("enter physics: "))
marks.update({"physics" : x})

y = int(input("enter chemistry: "))
marks.update({"chemistry": y})

z = int(input("enter maths: "))
marks.update({"maths": z})

print(marks)

#figure out a way to store 9 and 9.0 as seperate value in the set .(you can take help of bulit in data types)
value = {9, "9.0"}
print(value)
