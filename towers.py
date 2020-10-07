#!/usr/bin/env python
# coding: utf-8

# # Towers of Hanoi

# In[5]:


def hanoi(n: int, a: int, b:int, c: int):
   """
   https://www.mathsisfun.com/games/towerofhanoi.html
   :param n: number of disks
   :param a: from
   :param b: temporary
   :param c: destination
   :return: None
   """

   if n == 1:
       print("Move from", a, 'to', c)
   else:

       # move n-1 disks from a to b using c as a temp
       hanoi(n-1, a, c, b)
       print("Move from", a, 'to', c)

       # move n-1 disks from b to c using a as a temp
       hanoi(n-1, b, a, c)

if __name__ == "__main__":
   hanoi(3, 1, 2, 3)


# In[ ]:




