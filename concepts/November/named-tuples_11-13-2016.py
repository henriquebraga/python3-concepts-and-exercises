from collections import namedtuple

'''Here's what's like:
    1- 'Color' is just the name of the tuple.
    2- The list ['red', 'green', 'blue'] contains all the parameters
    from the tuple.
    Look at the examples below and notice that's somewhere between a regular tuple and a dictionary 
    structure. (It's more READABLE than a tuple and less verbose(more typing) to create and access
     a structure color
    than a dictionary.)
More info: https://www.youtube.com/watch?v=GfxJYp9_nJA
'''
Color = namedtuple('Color', ['red', 'green', 'blue'])

color = Color(255, 0, 255)
#Below, it's quite noticeable that a namedtuple in this would be more readable than 
#a conventional tuple. In a regular tuple structure, we would have to write color[0] in order
#to get the first value (red from RGB). That is hard to be understood by developers.
#Below we can acess the value by its property(red).
print(color.red) 

#You could also pass the values by parameters name.
color = Color(red=255, green=0, blue=255)
print(color.red)

#Even if we change the parameters' sequence, the result's going to be the same!
color = Color(blue=255, green=0, red=255)
print(color.red)

