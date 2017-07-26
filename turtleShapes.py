import turtle

numPts = 5 ## Num of sides/pointes to polygon

turtle.shape("turtle")
triangle.setpos(-50, 50)
turtle.circle(50)

for i in range(numPts):
    ## Smart
    ## Change to the right angle in pentagon
    turtle.left(360 / numPts)

    ## 100 = length of the side
    turtle.forward(100)

turtle.mainloop()
