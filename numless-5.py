#!/usr/bin/env python
# coding: utf-8

# In[7]:


MARKS=int(input("Enter your HSC marks="))
TotalMarks=int(input("Enter your total HSC marks="))
x=float(((MARKS/TotalMarks)*100))
percent=x
print(percent)
if percent>=80:
    print("You have got A-1 Grade in HSC Exam")
elif percent < 80 and percent>=70:
   
    print("You have got A Grade in HSC Exam")
elif percent < 70 and percent>=60:
    print("You have got B Grade in HSC Exam")  
elif percent < 60 and percent>=50:
    print("You have got C Grade in HSC Exam")  
elif percent < 50 and percent>=0:
    print("***Fail***") 


# In[15]:


NUM=int(input("Enter the number="))
x=int(NUM/2)*2
if x==NUM:
    print("the number is even")
else:
    print("the number is odd")
    


# In[33]:


arr=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x=(arr<5)
print("The  largest number in array is:",x)


# In[27]:


arr = [10, 324, 45, 90, 9808] 
def largest(arr,n): 
    for i in range(1, n): 
        if arr[i] > max: 
            max = arr[i] 
    return max

n = len(arr) 
Ans = largest(arr,n) 
print ("Largest in given array is",Ans)


# In[36]:


array=[1, 4, 5, 7, 3, 6, 9, 3, 6]
copy = list(array)
array = [1, 4, 5, 7, 3, 6, 9, 3, 6]
k=5
for k in array:
    if k > x:
            copy.append(k)


# In[49]:


arr=[1,2,3,4,5,6,7]
 a=len(arr)


# In[70]:


arr=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
sorted(x for x in arr if x < 5)


# In[ ]:





# In[ ]:




