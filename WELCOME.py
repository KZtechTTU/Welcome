import turtle

def draw_text(pen, text, position, font, text_color, outline_color, outline_thickness):
    # Draw outline
    pen.penup()
    pen.goto(position)
    pen.pendown()
    pen.color(outline_color)
    for offset_x in range(-outline_thickness, outline_thickness + 1, outline_thickness):
        for offset_y in range(-outline_thickness, outline_thickness + 1, outline_thickness):
            pen.penup()
            pen.goto(position[0] + offset_x, position[1] + offset_y)
            pen.pendown()
            pen.write(text, align="center", font=font)

    # Draw main text
    pen.penup()
    pen.goto(position)
    pen.pendown()
    pen.color(text_color)
    pen.write(text, align="center", font=font)

def display_welcome():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)

    pen = turtle.Turtle()
    pen.hideturtle()

    # Draw "Welcome" - Bigger and Centered
    draw_text(pen, "Welcome", (0, 150), ("Arial", 60, "bold"), "white", "blue", 5)

    # Draw "KZ" - Positioned beside "Tech" with spacing
    draw_text(pen, "KZ", (-100, 50), ("Arial", 80, "bold"), "white", "blue", 8)

    # Draw "Tech" beside "KZ"
    draw_text(pen, "Tech", (100, 50), ("Arial", 80, "italic"), "white", "blue", 6)

    screen.mainloop()

if __name__ == "__main__":
    display_welcome()