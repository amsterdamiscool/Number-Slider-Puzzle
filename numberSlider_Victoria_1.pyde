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

def setup():
    size(650,975)
    welcomeScreen = loadImage("welcome.png")
    image(welcomeScreen,0,0)
    
    global audio
    audio = Minim(this)
    
    caveat = createFont("caveat.ttf",45)
    textFont(caveat)
    fill(0)
    textAlign(RIGHT)
    
    # loading images
    global ruleBoard, ruleFlag, gameFlag, gameBoard, gameDetails, goldImage, congrats
    ruleBoard = loadImage("ruleBoard.png")
    ruleFlag = loadImage("ruleFlag.png")
    gameFlag = loadImage("gameFlag.png")
    gameBoard = loadImage("gameBoard.png")
    gameDetails = loadImage("gameDetails.png")
    goldImage = loadImage("gold.png")
    congrats = loadImage("congrats.png")
    # loading tile images
    global  tile1,  tile2,  tile3,  tile4,  tile5,  tile6
    global  tile7,  tile8,  tile9, tile10, tile11, tile12
    global tile13, tile14, tile15, tile16, tile17, tile18
    global tile19, tile20, tile21, tile22, tile23, tile24
    global tile25, tile26, tile27, tile28, tile29, tile30
    global tile31, tile32, tile33, tile34, tile35
    tile1, tile2, tile3, tile4, tile5, tile6 = loadImage("1.png"), loadImage("2.png"), loadImage("3.png"), loadImage("4.png"), loadImage("5.png"), loadImage("6.png")
    tile7, tile8, tile9, tile10, tile11, tile12 = loadImage("7.png"), loadImage("8.png"), loadImage("9.png"), loadImage("10.png"), loadImage("11.png"), loadImage("12.png")
    tile13, tile14, tile15, tile16, tile17, tile18 = loadImage("13.png"), loadImage("14.png"), loadImage("15.png"), loadImage("16.png"), loadImage("17.png"), loadImage("18.png")
    tile19, tile20, tile21, tile22, tile23, tile24 = loadImage("19.png"), loadImage("20.png"), loadImage("21.png"), loadImage("22.png"), loadImage("23.png"), loadImage("24.png")
    tile25, tile26, tile27, tile28, tile29, tile30 = loadImage("25.png"), loadImage("26.png"), loadImage("27.png"), loadImage("28.png"), loadImage("29.png"), loadImage("30.png")
    tile31, tile32, tile33, tile34, tile35= loadImage("31.png"), loadImage("32.png"), loadImage("33.png"), loadImage("34.png"), loadImage("35.png")
    
    # importing statistics
    global levelNum, goldNum
    data = open('LevelAndGold.txt','r')
    levelNum = int(data.readline())
    goldNum = int(data.readline())
    data.close()
    
    # initializing variable
    global procedure, display, moves, tileCoordinates, tileImages, tileGoal
    procedure = 0.5 # 0.5 for welcome screen # odd for congrats # even for game
    display = True # True for gameBoard # False for ruleBoard
    moves = 0 # how many moves done in current game
    tileCoordinates = [ [ (20+103*a,186+103*b) for a in range(6) ] for b in range(6) ]
        # x-coordinats 20 123 226 329 432 535 # y-coordinates 186 289 392 495 598 701
    tileImages = troubleMaker()
    tileGoal = [ [  tile1,  tile2,  tile3,  tile4,  tile5,  tile6 ],
                 [  tile7,  tile8,  tile9, tile10, tile11, tile12 ],
                 [ tile13, tile14, tile15, tile16, tile17, tile18 ],
                 [ tile19, tile20, tile21, tile22, tile23, tile24 ],
                 [ tile25, tile26, tile27, tile28, tile29, tile30 ],
                 [ tile31, tile32, tile33, tile34, tile35,   None ] ]
        
def draw():
    global tileImages, tileGoal, procedure, goldImage, goldNum, gameDetails, levelNum, moves, ruleFlag, gameBoard, tileCoordinates
    global display, ruleBoard, audio, congrats
    # print(mouseX,mouseY)
    # print(procedure)
    
    # checking if goal reached
    if tileImages == tileGoal:
        procedure = procedure + 1
        # print("for reaching goal")
        
    # background images (some are always displayed and others cover over if propriates)
    if procedure % 1 == 0: # display following images if not on welcome screen
        background(0)
        image(goldImage,345,35)
        text(str(goldNum),600,117)
        image(gameDetails,0,827)
        text("Level: %3d     Moves: %5d"%(levelNum,moves),600,880)
        image(ruleFlag,75,90)
        image(gameFlag,13,90)
        image(gameBoard,0,167)
        for a in range(6):
            for b in range(6):
                if tileImages[a][b] != None:
                    image(tileImages[a][b],tileCoordinates[a][b][0],tileCoordinates[a][b][1])
    if procedure % 2 == 0: # cover gameBoard with ruleBoard if user chooses to read rules
        if display == False:
            image(ruleFlag,75,90)
            image(ruleBoard,0,167)
            
    elif procedure % 2 == 1: # if goal achieved
        clapSound = audio.loadFile("applause.mp3") # clapping sound
        clapSound.play() # play clapping sound
        image(congrats,0,0) # cover gameBoard with congrats screen 
        textAlign(CENTER)
        if moves <= 10*levelNum: ################################################# Is this a good scoring system? #################################################
            levelNum = levelNum + 1 ############################################## Is this a good scoring system? #################################################
            goldNum = goldNum + 5*(10*levelNum-moves) ############################ Is this a good scoring system? #################################################
            text("Gold +"+str(5*(10*levelNum-moves))+"   Level +1",325,520) ###### Is this a good scoring system? #################################################
        else: #################################################################### Is this a good scoring system? #################################################
            goldNum = goldNum + 5 ################################################ Is this a good scoring system? #################################################
            text("Gold + 5",325,520) ############################################# Is this a good scoring system? #################################################
        rememberMe() # save level and gold information if a game is completed
        textAlign(RIGHT)
        noLoop() # NO LOOP (THE TABLET IS PRESENTLY PERFECT SO LOOP WOULD ADD ONE TO VARIABLE PROCEDURE IN EVERY SINGLE FRAME AND MAKE THINGS OUT OF CONTROL)

def keyReleased():
    global audio, procedure, display, tileImages, moves
    slideSound = audio.loadFile("slide.mp3")
    
    if procedure % 2 == 0 and display == True: # when playing game (not reading rules nor celebrating with congrats screen)
        if key == 'W' or key == 'w' or keyCode == UP: # user wants to move a tile up towards the blank space
            blank = blankFinder() # first find the blank
            if blank[0] != 5: # if it is not at bottom row
                tileImages[blank[0]][blank[1]], tileImages[blank[0]+1][blank[1]] = tileImages[blank[0]+1][blank[1]], None # exchange coordinates (move tile)
                moves = moves + 1 # this counts as a move
                slideSound.play() # play slide sound
        elif key == 'A' or key == 'a' or keyCode == LEFT: # user wants to move a tile left towards the blank space
            blank = blankFinder() # first find the blank
            if blank[1] != 5: # if it is not at right-most column
                tileImages[blank[0]][blank[1]], tileImages[blank[0]][blank[1]+1] = tileImages[blank[0]][blank[1]+1], None # exchange coordinates (move tile)
                moves = moves + 1 # this counts as a move
                slideSound.play() # play slide sound
        elif key == 'S' or key == 's' or keyCode == DOWN: # user wants to move a tile down towards the blank space
            blank = blankFinder() # first find the blank
            if blank[0] != 0: # if it is not at top row
                tileImages[blank[0]][blank[1]], tileImages[blank[0]-1][blank[1]] = tileImages[blank[0]-1][blank[1]], None # exchange coordinates (move tile)
                moves = moves + 1 # this counts as a move
                slideSound.play() # play slide sound
        elif key == 'D' or key == 'd' or keyCode == RIGHT: # user wants to move a tile right towards the blank space
            blank = blankFinder() # first find the blank
            if blank[1] != 0: # if it is not at left-most column
                tileImages[blank[0]][blank[1]], tileImages[blank[0]][blank[1]-1] = tileImages[blank[0]][blank[1]-1], None # exchange coordinates (move tile)
                moves = moves + 1 # this counts as a move
                slideSound.play() # play slide sound
                
    elif procedure % 2 == 1: # when celebrating with congrats screen any key pressed starts a new game
        slideSound.play() # play slide sound when creating new puzzle
        tileImages = troubleMaker() # create new puzzle
        moves = 0 # reset moves
        procedure = procedure + 1 # and go on to next game
        # print("for next level")
        loop()
        
    elif procedure == 0.5: # in welcome screen any key pressed starts the first game.
        procedure = 2 # go on to first game
        slideSound.play() # pretend that we are creating the new puzzle now so there are sliding sounds

def mouseReleased():
    global audio, procedure, display
    clickSound = audio.loadFile("click.mp3")
    if procedure % 2 == 0: # clicking the mouse is only meaningful during game time (not during celebrating time)
        if mouseX > 14 and mouseX < 166 and mouseY > 90 and mouseY < 166: # user can click on gameFlag to play game
            display = True
            clickSound.play()
        elif mouseX > 174 and mouseX < 326 and mouseY > 90 and mouseY < 166: # user can click on ruleFlag to read rules
            display = False
            clickSound.play()

# 225 = 15 x 15
