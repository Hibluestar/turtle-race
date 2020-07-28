#!/usr/bin/env python
# coding: utf-8

# In[17]:


import turtle
turtle0=turtle.Turtle()
turtle1=turtle.Turtle()
turtle2=turtle.Turtle()
turtle3=turtle.Turtle()
turtlelist=[turtle0,turtle1,turtle2,turtle3]
colorlist=['red','blue','orange','black']
for i in range(4):#define the turtles and their starting positions
    turtlelist[i].shape('turtle')
    turtlelist[i].color(colorlist[i])
    turtlelist[i].penup()
    turtlelist[i].goto(-200, (i-1.5)*100)
    turtlelist[i].pendown()
turtle4=turtle.Turtle()#draw the finish line
turtle4.color('black')
turtle4.penup()
turtle4.goto(200,-300)
turtle4.pendown()
turtle4.left(90)
turtle4.forward(600)
import random#define random speeds for all turtles
speed0=random.randint(1,8)
speed1=random.randint(1,8)
speed2=random.randint(1,8)
speed3=random.randint(1,8)
speedlist=[speed0,speed1,speed2,speed3]
for n in range (500):
    for i in range (4):
        if (n+1)*(speedlist[i])<=400:
            turtlelist[i].forward(speedlist[i])
            if (n+1)*(speedlist[i])>=400:
                print(colorlist[i])


# In[16]:


for i in range(4):
    turtlelist[i].reset()
turtle4.reset()


# In[ ]:




