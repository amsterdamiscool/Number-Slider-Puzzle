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

def troubleMaker():
# to create new puzzle to solve based on entropy (5*levelNum)
# scrambling up tablet FROM GOAL to let user undo the scramble and successfully get to the goal
    global  tile1,  tile2,  tile3,  tile4,  tile5,  tile6
    global  tile7,  tile8,  tile9, tile10, tile11, tile12
    global tile13, tile14, tile15, tile16, tile17, tile18
    global tile19, tile20, tile21, tile22, tile23, tile24
    global tile25, tile26, tile27, tile28, tile29, tile30
    global tile31, tile32, tile33, tile34, tile35, levelNum
    newProblem = [ [  tile1,  tile2,  tile3,  tile4,  tile5,  tile6 ],
                   [  tile7,  tile8,  tile9, tile10, tile11, tile12 ],
                   [ tile13, tile14, tile15, tile16, tile17, tile18 ],
                   [ tile19, tile20, tile21, tile22, tile23, tile24 ],
                   [ tile25, tile26, tile27, tile28, tile29, tile30 ],
                   [ tile31, tile32, tile33, tile34, tile35,   None ] ] # creating goal
    
    # deciding series of directions to scramble up tablet
    blank = [5,5] # keeping track of blank space coordinates (for checkings)
    disarray = [[0,0]]
    while len(disarray) <= (5*levelNum):
        lottery = random.randrange(4)
        if lottery == 0:
            direction = [ -1,  0 ]
        elif lottery == 1:
            direction = [  0, -1 ]
        elif lottery == 2:
            direction = [ +1,  0 ]
        elif lottery == 3:
            direction = [  0, +1 ]
        if not( direction[0] + disarray[-1][0] == 0 and direction[1] + disarray[-1][1] == 0 ): # making sure the chosen direction is not meaningless
            if (blank[0] + direction[0] >= 0) and (blank[0] + direction[0] <= 5): # checking that sure the scramble action does not go beyond game rules
                if (blank[1] + direction[1] >= 0) and (blank[1] + direction[1] <= 5): # checking that the scramble action does not go beyond game rules
                    disarray.append(direction)
                    blank = [ blank[0] + direction[0], blank[1] + direction[1] ] # keeping track of blank space coordinates (for checkings)
    
    # scrambling
    blank = [5,5] # keeping track of blank space coordinates (for scramblings)
    for vector in disarray:
        newProblem[ blank[0] ][ blank[1] ], newProblem[ blank[0]+vector[0] ][ blank[1]+vector[1] ] = newProblem[ blank[0]+vector[0] ][ blank[1]+vector[1] ], None
        blank = [ blank[0] + vector[0], blank[1] + vector[1] ]
    
    # returning scrambled tablet
    return newProblem

def rememberMe():
# to record statistics
    global levelNum, goldNum
    data = open('LevelAndGold.txt','w')
    data.write(str(levelNum)+"\n"+str(goldNum))
    data.close()
