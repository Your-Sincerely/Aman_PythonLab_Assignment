# taking an empty list
List1 = []  

# comparing list
List2 = [1, 2, 3, 4, 5, 6]  

 # length of list
n = int(input("Enter number of elements : ")) 

# taking input in list1
for i in range(0, n):  
    item = int(input("Enter Item in list :"))
    # adding items in list1
    List1.append(item)  

for k in List2:  # for items in list2
    if k in List1:  # if the items are in list1
        ans = "Equal"
    else:
        ans = "Not Equal"

print(ans)
