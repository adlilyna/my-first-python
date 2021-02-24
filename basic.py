# Get the player's name with input and store it in the name variable

# Greet the player using string concatenation

# Print out some steps for player to choose from, for example:
# Next steps: 1) Look around 2) Chop down tree 3) Jump

# Use an if statement to decide the next steps to print. For example, if they picked 1:
# You've spotted a suit of armor! 1) Put it on 2) Ignore it

# Do this inside a loop until the user is done with the game

name = input('Enter your name: ')
print ('Hello and welcome, ' + name)

print ('You need to choose steps!')
print ('1) Look around')
print ('2) Chop down tree')
print ('3) Jump')
choose_steps = int(input('Choose your steps: '))

if choose_steps == 1:
    print ('You have spotted a house!')
    print ('What are you gonna do now?')
    house = int(input('1) Go into the house 2) Ignore // '))
    if house == 1:
        print ('Lets go!')
    else:
        print ('Okay what are you gonna do now?')
else:
    print ('Okay, lets chop down the tree!')

