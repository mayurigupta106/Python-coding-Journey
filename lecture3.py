marks1 = 924.34
marks2 = 34.53
marks3 = 43.35
marks4 = 245.53
marks5 = 24.52

marks = [924.34, 34.53, 43.35, 245.53, 24.52]
print(marks)
print(type(marks))
print(len(marks))

student = ["sachin" , 83.4, "maths"]
print(student[1])
student[1] = "megha"
print(student[1])

list = [2,4, 1]
list.append(10)
print(list)
list.sort()
print(list)
list.reverse()
print(list)
list.insert(2,8)
print(list)
list.remove(4)
print(list)
list.pop(2)
print(list)
list.clear()
print(list)


# tuples
tup = (2, 4, 2, 3)
print(type(tup))
print(tup.index(4))
print(tup.count(2))



# WAP to ask the user to enter names of their 3 facourite movies and store them in a list.
movie1 =input("enter your first fav movie: ")
movie2 =input("enter your second fav movie: ")
movie3 =input("enter your third fav movie: ")

movies = [movie1, movie2, movie3]
print(movies)

# WAP to check if a list contains a palindrome of elements.
list = [1, 3, 3, 1]
copy_list1 = list.copy()
copy_list1.reverse()
if (list == copy_list1):
    print("palindrome")
else:
    print("not palindrome")

# WAP to count the number of students with the "A" grade in the following tuple.
tup = ["C", "D", "A", "A", "B", "B", "A"]
print(tup.count("A"))
grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print(grade)
