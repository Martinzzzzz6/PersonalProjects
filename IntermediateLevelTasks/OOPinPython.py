from turtle import Turtle, Screen
from prettytable import PrettyTable
#
# pen4o = Turtle()
# my_screen = Screen()
# pen4o.shape("turtle")
# pen4o.color("DarkGreen")
# pen4o.forward(100)
# pen4o.left(90.3)
# pen4o.forward(100)
# pen4o.left(90.4)
# pen4o.forward(100)
# pen4o.left(90)
# pen4o.forward(100)
#
# my_screen.exitonclick()
#
# print(my_screen.canvheight)

table = PrettyTable()

table.add_column("Tasks", ["OOP", "Queries", "More OOP", "Data Structures and Algorithms"])
table.add_column("TODO", ["Study", "Learn", "Projects", "-"])

table.align = "c"

print(table)