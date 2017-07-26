import turtle

## Draw a triangle
'''
turtle.goto(50, 50)
turtle.goto(50, 0)
turtle.goto(0, 0)
'''
x = 0
count = 0

while x < 300:
    y = x**2/300
    turtle.goto(x, y)

    x  = x + 100
    count = count + 1

print(count)
    
turtle.mainloop()
