#booleans

print(10 > 9)
True

print(10 == 9)
False

print(10 < 9)
False

print(bool("abc"))
True

print(bool("abc"))
True

print(bool(0))
False

#operators

print(10*5) #ex1

print(10/2) #ex2

fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!") #ex3

if 5 != 10:
  print("5 and 10 is not equal") #ex4

if 5 == 10 or 4 == 4:
  print("At least one of the statements is true") #ex5

#list

fruits = ["apple", "banana", "cherry"] #1
print(fruits[1])


fruits = ["apple", "banana", "cherry"] #2
fruits[0]="kiwi" #замена эпл на киви


fruits = ["apple", "banana", "cherry"] #3
fruits.append("orange") #конец списка

fruits = ["apple", "banana", "cherry"] #4
fruits.insert(1,"lemon")

fruits = ["apple", "banana", "cherry"] #5
fruits.remove("banana")


fruits = ["apple", "banana", "cherry"] #6
print(fruits[-1]) #последний элемент


fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"] #7
print(fruits[2:5])


fruits = ["apple", "banana", "cherry"] #8
print(len(fruits)) #длина

#tuples

fruits = ("apple", "banana", "cherry") #1
print(fruits[0])

fruits = ("apple", "banana", "cherry") #2
print(len(fruits))

fruits = ("apple", "banana", "cherry") #3
print(fruits[-1])


fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#Sets
fruits = {"apple", "banana", "cherry"} #1
if "apple" in fruits:
     print("Yes, apple is a fruit!")



fruits = {"apple", "banana", "cherry"} #2
fruits.add("orange")



fruits = {"apple", "banana", "cherry"} #3
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)



fruits = {"apple", "banana", "cherry"} #4
fruits.remove("banana") 



fruits = {"apple", "banana", "cherry"} #5
fruits.discard("banana")

#dictionaries

car =	{   #1
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))



car =	{ #2
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

car =	{ #3
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] ="red"


car =	{ #4
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model") #удаление модел


car =	{ #5
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear() #удаление всего

#if else

a = 50 #1
b = 10
if a > b:print("Hello World")



a = 50 #2
b = 10
if a != b:print("Hello World")


a = 50 #3
b = 10
if a == b:
   print("Yes")
else:
   print("No")



a = 50 #4
b = 10
if a == b:print("1")
elif a > b:
   print("2")
else:
   print("3")


if a == b and b == a: #5
   print("Hello")


if a == b or b == a: #6
   print("Hello")


if 5 > 2:  #7
    print("YES")

a = 2 #8
b = 5
print("YES") if a == b else print("NO")

a = 2 #9
b = 50
c = 2
if a == c or b == c:

  print("YES")

  #while loops

  i = 1 #1
while i < 6:
 print(i) 
 i += 1

 i = 1 #2
while i < 6:
  if i == 3:
    break
i += 1

i = 0  #3
while i < 6:
  i += 1
  if i == 3:
    continue
print(i)

i = 1 #4
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

  #for loops

  fruits = ["apple", "banana", "cherry"] #1
for x  in fruits:
    print(x)


fruits = ["apple", "banana", "cherry"] #2
for x in fruits:
  if x == "banana":
    continue
print(x)

for x in range(6): #3
   print(x)


fruits = ["apple", "banana", "cherry"] #4
for x in fruits:
  if x == "banana":
    break
print(x)

