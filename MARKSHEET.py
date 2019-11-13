#!/usr/bin/env python
# coding: utf-8

# In[1]:


NAME=input("ENTER YOUR NAME:")
MARKS=int(input("Enter your HSC marks="))
TotalMarks=int(input("Enter your total HSC marks="))
x=float(((MARKS/TotalMarks)*100))
percent=x
print(percent)
if percent>=80:
    print("You have got A-1 Grade in HSC Exam")
elif percent < 80 and percent>=70:
   
    print(NAME+" You have got A Grade in HSC Exam")
elif percent < 70 and percent>=60:
    print(NAME+" You have got B Grade in HSC Exam")  
elif percent < 60 and percent>=50:
    print(NAME+" You have got C Grade in HSC Exam")  
elif percent < 50 and percent>=0:
    print(NAME+"  *** You are Fail***") 


# In[ ]:




