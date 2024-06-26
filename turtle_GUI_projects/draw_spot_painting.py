import turtle as t
import random
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('spot_painting.jpg', 15)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
    
# print(rgb_colors)

color_list = [(42, 2, 176), (81, 252, 177), (235, 232, 253), (224, 151, 110), (154, 3, 85), (5, 210, 101), (4, 138, 60), (244, 42, 125), (109, 108, 245), (251, 252, 56), (184, 184, 250), (210, 106, 6)]

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)


for dot_count in range(1, 100 + 1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)






screen = t.Screen()
screen.exitonclick()