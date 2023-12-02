# # import turtle # is a GUI libary for beginner devloper
# from turtle import Turtle, Screen
# import another_module
# print(another_module.another_varible)

# # timmy = turtle.Turtle()

# timmy = Turtle()  # call the class
# print(timmy)
# timmy.shape("turtle")  # to change the graphic element
# timmy.color("coral")
# timmy.forward(90)
# myscreen = Screen()
# timmy.circle(90)
# timmy.right(90)
# timmy.circle(90)
# timmy.left(180)
# timmy.circle(90)
# timmy.back(90)
# timmy.circle(90)
# timmy.right(90)
# timmy.circle(90) 
# myscreen.exitonclick()  # with out this function can the window not work
from prettytable import PrettyTable
table = PrettyTable()  # tabel lib
# is take a str and list to  creat a column
# table.add_column("number", [1, 2, 3, 4, 5])
# table.add_column("new Number", [1, 2, 3, 4, 5])
table.field_names = ["name", "type", "id"]
table.add_rows(
    [
        ["Fennekin", "Fire", "#0004"],
        ["Pidgeotto", "Flying", "#0018"],
        ["Beedrill", ["bug", "Poison"], "#0028"]
    ]
)
table.align = "l"

print(table)
