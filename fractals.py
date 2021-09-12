from turtle import *
speed(0)
'''def tree(size,levels,angle):
    if levels==0:
        return
    forward(size)
    right(angle)
    tree(size*0.8,levels-1,angle)
    left(angle*2)
    tree(size*0.8,levels-1,angle)
    right(angle)
    backward(size)
left(90)
tree(50,12,25)'''
def snowflake_side(length,levels):
    if levels==0:
        forward(length)
        return
    length/=3.0
    snowflake_side(length,levels-1)
    left(60)
    snowflake_side(length,levels-1)
    right(120)
    snowflake_side(length,levels-1)
    left(60)
    snowflake_side(length,levels-1)
def create_snowflake(sides,length):
    for _ in range(sides):
        snowflake_side(length,sides)
        right(360/sides)
create_snowflake(5,200)
mainloop()