# author: <name here>
# date: <date here>

# -------------------- Section 4 -------------------- #

# Input | ASCII Art


# Objectives:
#   1. Diamond
#       a. Define a function that accept the parameters listed below.
#           Name   | Type(s)         | Description
#           symbol | Integer / Float | The symbol used to create the diamond.
#
#           The function should print the chevron seen in the output below using the symbol.
#       b. Prompt input from the user in the form of a single character, save it to a variable.
#       c. Call the function you defined to create the diamond, sending the character as an argument.
#
#       HINT: Start with a smaller diamond! Then make it bigger once you figure out the pattern.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> $
#
#           $
#          $$$
#         $$$$$
#        $$$$$$$
#       $$$$$$$$$
#      $$$$$$$$$$$
#     $$$$$$$$$$$$$
#      $$$$$$$$$$$
#       $$$$$$$$$
#        $$$$$$$
#         $$$$$
#          $$$
#           $
#
# ---- WRITE CODE BELOW ---- #
diamond = input('enter a symbol, it\'s worth it i promise: ')
print(' '*11 + diamond*1 + ' '*11)
print(' '*10 + diamond*3 + ' '*10)
print(' '*9 + diamond*5 + ' '*9)
print(' '*8 + diamond*7 + ' '*8)
print(' '*7 + diamond*9 + ' '*7)
print(' '*6 + diamond*11 + ' '*6)
print(' '*5 + diamond*13 + ' '*5)
print(' '*6 + diamond*11 + ' '*11)
print(' '*7 + diamond*9 + ' '*10)
print(' '*8 + diamond*7 + ' '*9)
print(' '*9 + diamond*5 + ' '*8)
print(' '*10 + diamond*3 + ' '*7)
print(' '*11 + diamond*1 + ' '*6)

#   2. Framed Diamond
#       a. Define a function that accept the parameters listed below.
#           Name   | Type(s)         | Description
#           symbol1 | Integer / Float | The symbol used to create the diamond.
#           symbol2 | Integer / Float | The symbol used to create the frame.
#
#           The function should print the chevron seen in the output below using the symbol.
#       b. Prompt input from the user in the form of a single character, save it to a variable.
#       c. Prompt input from the user in the form of a single character again, and save it to a second variable.
#       d. Call the function you defined to create the framed diamond, sending the characters as arguments.
#
#       HINT: Start with a smaller diamond! Then make it bigger once you figure out the pattern.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> &
#   >> ~
#
#     ~~~~~~$~~~~~~
#     ~~~~~$$$~~~~~
#     ~~~~$$$$$~~~~
#     ~~~$$$$$$$~~~
#     ~~$$$$$$$$$~~
#     ~$$$$$$$$$$$~
#     $$$$$$$$$$$$$
#     ~$$$$$$$$$$$~
#     ~~$$$$$$$$$~~
#     ~~~$$$$$$$~~~
#     ~~~~$$$$$~~~~
#     ~~~~~$$$~~~~~
#     ~~~~~~$~~~~~~
#
# ---- WRITE CODE BELOW ---- #
symbol1 = input('please enter a random symbol: ')
symbol2 = input('please enter ANOTHER random symbol: ')

print(symbol2*6 + symbol1*1 + symbol2*6)
print(symbol2*5 + symbol1*3 + symbol2*5)
print(symbol2*4 + symbol1*5 + symbol2*4)
print(symbol2*3 + symbol1*7 + symbol2*3)
print(symbol2*2 + symbol1*9 + symbol2*2)
print(symbol2*1 + symbol1*11 + symbol2*1)
print(symbol1*13)
print(symbol2*1 + symbol1*11 + symbol2*1)
print(symbol2*2 + symbol1*9 + symbol2*2)
print(symbol2*3 + symbol1*7 + symbol2*3)
print(symbol2*4 + symbol1*5 + symbol2*4)
print(symbol2*5 + symbol1*3 + symbol2*5)
print(symbol2*6 + symbol1*1 + symbol2 *6)
print('i don\'t mean to brag but i think this is amazing, don\'t you? lol ')