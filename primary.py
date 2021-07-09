# author: <Lyric Marner>
# date: <July 8, 2021>

# -------------------- Section 1 -------------------- #

# Input | Saving String Responses to Variables

# Objectives:
#   1. Name in Reverse
#       a. Prompts input from the user in the form of a first name and last name.
#           Save these values to variables first_name and last_name.
#       b. Print the first and last names in reverse order.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> first name... elia
#   >> last name... deppe
#   deppe, elia
#
# ---- WRITE CODE BELOW ---- #
first_name = input('what\'s your first name? ')
last_name = input('and what\'s your last name? ')

print(last_name,',',first_name)
print()
#   2. Pyramid
#       a. Prompt input from the user in the form of a single character. Save to a variable named symbol.
#       b. Using the symbol, create a pyramid like you see in the example output. (Think, how can you make
#           duplicates of text symbol?)
#
# ----- EXAMPLE OUTPUT ----- #
#   >> $
#
#   $
#   $$
#   $$$
#   $$
#   $
#
# ---- WRITE CODE BELOW ---- #
symbol = input('enter a symbol! (&, @, etc...) ')
print(symbol * 1)
print(symbol * 2)
print(symbol * 3)
print(symbol * 2)
print(symbol * 1)
print()
#   3. Parallelogram
#       a. Prompt input from the user in the form of a single character. Save to a variable named symbol.
#       b. Using the symbol, create a pyramid like you see in the example output. (Think, how can you make
#           duplicates of text symbol?)
#
# ----- EXAMPLE OUTPUT ----- #
#   >> @
#
#   @
#   @@
#   @@@
#   @@@@
#    @@@
#     @@
#      @
#
# ---- WRITE CODE BELOW ---- #
symbol_2 = input('enter another symbol! or the same one, whatever works for you. ')
print(symbol_2 * 1)
print(symbol_2 * 2)
print(symbol_2 * 3)
print(symbol_2 * 4)
print(' '*1 + symbol_2 * 3)
print(' '*2 + symbol_2 * 2)
print(' '*3 + symbol_2 * 1)
print('i made a parallelogram, cool right?')
print()
# -------------------- Section 2 -------------------- #

# Casting | Getting Integers and Floats from the User

# Objectives:
#   1. Comparison
#       a. Prompt the user to enter a number, and save it to a variable named num1. DO NOT CAST IT.
#       b. Prompt the user to enter a number, and save it to a variable named num2. CAST IT TO AN INTEGER.
#       c. Prompt the user to enter a number, and save it to a variable named num3. CAST IT TO A FLOAT.
#       d. Print out each variable multiplied by 10.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> num1... 45
#   >> num2... -132.45
#   >> num3... 2132.24
#
#   num1 (str)   | 45454545454545454545
#   num2 (int)   | -1320
#   num3 (float) | 21322.4
#
# ---- WRITE CODE BELOW ---- #
num1 = input('enter a number! ')
num2 = int(input('enter another number! '))
num3 = float(input('enter one last number! '))

print(num1 *10)
print(num2 *10)
print(num3 *10)
print()
# Objectives:
#   2. Diameter of a Circle
#       a. Prompt input from the user to enter a radius. Save this value to a
#           variable named num as an integer or float.
#       b. Compute the diameter, and print it to the user.
#           diameter = radius * 2
#
# ----- EXAMPLE OUTPUT ----- #
#   >> radius... 12.3
#
#   diameter = 24.6
#
# ---- WRITE CODE BELOW ---- #
num = float(input('you probably thought this was over but...enter another number as the radius for a circle: '))
print('diameter= ',num*2 )
print()
# Objectives:
#   3. Area of a Circle
#       a. Define a function named area_circle(). Accept the parameters listed below.
#           Name   | Type(s)         | Description
#           radius | Integer / Float | The radius of the circle.
#
#           The function should compute the area of a circle, and print it to the terminal.
#               area = 3.14 * radius ** 2
#       b. Prompt input from the user to enter a radius. Save this value to a
#           variable named num as an integer or float.
#       c. Compute the radius by calling the function area_circle(), sending num as a parameter.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> radius... 44.2
#
#   area of the circle: 6134.4296
#
# ---- WRITE CODE BELOW ---- #
num_radius = float(input('please enter a whole number as the radius for a DIFFERENT circle: '))

area_circle = 3.14 * num_radius ** 2

print('using the radius you gave, the area of this new circle is', area_circle)
print()
# -------------------- Section 4 -------------------- #
#
# Create a conversation with a faux (fake) AI, using input and print().
# See the example in examples.py
fav_song = input('let\'s get to know each other, what\'s your favorite song? ')
print(fav_song,'? i haven\'t heard that one. ')
sport = input('do you like to watch any sports? you know like baseball, football, that type of stuff. ')
print('wow, everyone else i\'ve asked that said the same thing. ')
food = input('ok um...what\'s your favorite food? ')
print('oh...i mean if that\'s what you\'re into great but is that really your favorite? actually, ignore that question.')
pet_peeve = input('anyways, what\'s a pet peeve of yours? like something you absolutely hate? ')
print('LITERALLY. SAME. i also can\'t stand when people don\'t clean up after themselves!')
dog_cat = input('ok now here\'s the most important question out of all of these, are you a dog person or a cat person? ')
print('hm. i want you to reflect on that answer ok?')
print('well i have to go now, my battery\'s running low, but hopefully we can do this again sometime. nice to meet you!')