# n = 5 

# while n>= 0 :
#     print(n, end=" ")
#     n-=1

# Binary Search in python 

nums = [0,3,9,15,32,95,103]

key = int(input("Enter the number to be searched : "))
s = 0
e = len(nums) - 1

found = False
while(s<=e):
    mid = s + (e-s)//2
    if nums[mid]== key :
        print("Element found at index ", mid)
        found = True
        break
    elif nums[mid] > key :
        e = mid-1
    elif nums[mid] < key:
        s = mid + 1

if not found:
    print("Element not Found")   
 
