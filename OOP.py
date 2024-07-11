from turtle import Turtle , Screen
from prettytable import PrettyTable

# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color("red","green")
# timmy.forward(100)
#
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon Names",["Pikachu","Raichu","Charmander"])
table.add_column("Type",["Electric","Electric","Fire"])
table.align="l"
print(table)