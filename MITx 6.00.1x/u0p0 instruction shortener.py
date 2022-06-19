'''
Problem: copying Python instructions for these assignments doesn't fit into
the general 80 character limit.

Solution: more Python!

TO DO:
    ✔ Go back a few words and break on a space to keep words whole
    - Reset count on normal new line breaks

Idea for v2: interact with clipboard or other .py files
'''
##############################################################

# I'm thinking it's easiest to have the big string field here
instructions = '''

Note: In programming there are many ways to solve a problem. For your code to check correctly here, though, you must write your recursive function such that you make a recursive call directly to the function isIn. Thank you for understanding.



'''


##############################################################
debug = False
# max length of string before break. 
max_len = 78
# I wonder if I even need enumerate if this tracker is used
new_line_tracker, last_space = 0, 0

if debug:
    print(instructions)
    print(len(instructions), 'characters total\n')
    
# use enumerate method to keep track of where we are
for position, letter in enumerate(instructions):
    if debug:
        print(position, letter, end=", ") # where are we, really?
    # take note if the character is a space
    if letter == ' ':
        last_space = position
        if debug:
            print('last_space =', last_space)
            print('str:', instructions, '\n')
    # reset counter if there's a new line anyways
    # will code this later
    
    # this determines when we've hit the line length
    if (position + new_line_tracker) % max_len == 0 and position != 0:
        # this puts in a new line at the last space
        instructions = instructions[:last_space] + str('\n') + \
            instructions[last_space+1:]
        # it's very ironic that this goes over 80 characters
        if debug:
            print('insert triggered:', instructions, '\n')
        
        new_line_tracker = position - last_space
        if debug:
            print('new line tracker =', new_line_tracker)

# print the results to copy from the console
if debug:
    print('\n\nfinal:\n', instructions)
else:
    print(instructions)