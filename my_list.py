#Create an empty list called my_list
my_list=[]

#Append the following elements to my_list:10,20,30,40
my_list.extend([10,20,30,40])

#Insret the value 15 at the second postion in the list
my_list.insert(1,15)

#Extend my_list with another list:[50,60,70]
my_list.extend([50,60,70])

#Remove the last element from my_list
my_list.pop()

#Sort my_list in ascending order
my_list.sort()

#Find and print the index of thr value 30 in my_list
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)

#Print the final list
print("Final List:", my_list)