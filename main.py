#AYMEN DEV 
#نجمة بوكلي
import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(10)
col = ["red","red","red","red"]
c = 0
for i in range (50):
    t.forward(i*15)
    t.right(144)
    t.color(col[c])
    if c == 3:
        c = 0
    else:
        c+=1

turtle.mainloop()
