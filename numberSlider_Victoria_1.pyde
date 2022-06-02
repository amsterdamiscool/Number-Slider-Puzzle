# Program: 6 * 6 Number Slider Puzzle
# Developer: Albert Hong, Victoria Jiang
# Purpose: To complete a game using processing (python-mode)
#          and express the game rules with correctly written code.
# To-Do: Check if the scoring system is too hard or too easy.

# import libraries for random numbers and sound effects
import random
add_library('Minim')

def blankFinder():
# to find coordinate (index) of blank space on tablet
    global tileImages
    y = [ element for element in tileImages if None in element] # finding which row blank space is in
    return (tileImages.index(y[0]), y[0].index(None)) # returning location of that row on tablet and location of blank space in that row
