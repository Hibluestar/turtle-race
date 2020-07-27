#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
turtle0=turtle.Turtle()
turtle1=turtle.Turtle()
turtle2=turtle.Turtle()
turtle3=turtle.Turtle()
turtlelist=[turtle0,turtle1,turtle2,turtle3]
colorlist=['red','blue','orange','black']
for i in range(4):
    turtlelist[i].shape('turtle')
    turtlelist[i].color(colorlist[i])
    turtlelist[i].penup()
    turtlelist[i].goto(-200, (i-1.5)*100)
    turtlelist[i].pendown()
import random
speed0=random.randint(1,8)
speed1=random.randint(1,8)
speed2=random.randint(1,8)
speed3=random.randint(1,8)
speedlist=[speed0,speed1,speed2,speed3]
for n in range (50):
    for i in range (4):
        turtlelist[i].forward(speedlist[i])


# In[2]:


for i in range(4):
    turtlelist[i].reset()


# In[5]:


turtle.hideturtle()


# In[4]:


for i in range (4):
    print(turtlelist[i].position())


# In[ ]:




