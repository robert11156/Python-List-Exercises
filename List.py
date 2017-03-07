#1
Integer, float, string, booleam- True or False  
#2
my_list = [5, 2, 6, 8, 101]
print(my_list[1]) -2
print(my_list[4]) -101
print(my_list[5]) -Error, there is no 5th value 

#3
my_list=[5, 2, 6, 8, 101]
for my_item in my_list:
    print(my_item)
 
This would print your whole entire list which is 5,2,6,8 and 101

#4
my_list1 = [5, 2, 6, 8, 101]
my_list2 = (5, 2, 6, 8, 101)
my_list1[3] = 10
print(my_list1)
my_list2[2] = 10
print(my_list2)

This would print [5, 2, 6, 10, 101]

#5
my_list = [3 * 5]
print(my_list)
my_list = [3] * 5
print(my_list)

[3 * 5] This would print [15] becasue it's saying 3*5. While [3] *5 would print [3,3,3,3,3] because the bracket is around the 3.

#6
my_list = [5]
for i in range(5):
    my_list.append(i)
print(my_list)

This would print [5, 0, 1, 2, 3, 4]

#7
print(len("Hi"))
print(len("Hi there."))
print(len("Hi") + len("there."))
print(len("2"))
print(len(2))

This would print 2,9,8,1 

#8
print("Simpson" + "College")
print("Simpson" + "College"[1])
print( ("Simpson" + "College")[1] )

This would print 
SimpsonCollege
Simpsono
i

#9 
word = "Simpson"
for letter in word:
    print(letter)
 This would print
 S
 i
 m
 p
 s
 o
 n
 
 #10
 word = "Simpson"
for i in range(3):
    word += "College"
print(word)

This would print SimpsonCollegeCollegeCollege

#11
word = "Hi" * 3
print(word)

This would print Hi 3 times  = HiHiHi

#12
my_text = "The quick brown fox jumped over the lazy dogs."
print("The 3rd spot is: " + my_text[3])
print("The -1 spot is: " + my_text[-1])
