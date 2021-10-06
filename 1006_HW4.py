import turtle 

seurat = turtle.Turtle()
seurat.speed(0)
turtle.bgcolor("black")
seurat.pencolor("white")
circle_distance = 30
width = 10
height = 10
radius = 30

for y in range(height):
    for i in range(width):
        seurat.pendown()
        seurat.circle(radius)
        seurat.penup()
        seurat.forward(circle_distance)


  
    seurat.backward(circle_distance * width)
    seurat.right(90)
    seurat.forward(circle_distance)
    seurat.left(90)

turtle.done()
