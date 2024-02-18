def buildPyramid(length):
    
    #declare output symbols variables
    spaceChar = ' '
    asteriskChar = '*'


    #iterate through size of length, each iteration corresponds to one level of the pyramid
    for i in range(1, length + 1):

        #calculate number of asterisks for the current level, this makes asteriskCount odd on every iteration
        asteriskCount = 2 * i - 1
        
        #print(str(asteriskCount))
        #calculate number of spaces for each level relative to pyramid's maximum base length which is defined by the formula (2 * length - 1) then subtract asterisk and finally divide by 2 to get each side
        spaces = (2 * length - 1 - asteriskCount) // 2

        #print("Asterisk count: " + str(asteriskCount) + ", Number of spaces: " + str(spaces * 2))

        levelOutput = spaceChar * spaces + asteriskChar * asteriskCount + spaceChar * spaces
        print(levelOutput)


buildPyramid(50)