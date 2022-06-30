'''
Assignment Initiation Date: 9/8/2021
Author:Kevin Do
Last Modification Date: 9/11/2021
Due Date: 9/13/2021 @ 11:59 PM
'''
import board
import time
import copy

chessboard = board.Board(5)
chessboard.fitness()
numReset = 0

def HillClimbing(boardInput):
    #Take the current board and store it right now
    numQueens = boardInput.n_queen
    currentFit = boardInput.get_fit()
    currentBoard = boardInput

    futureBoards = []
    bestBoardNumber = 0

    numReset = 0

    while(currentFit != 0):
        #print("Number of reset: ", numReset)
        #Create the list of possible states
        for n in range(numQueens):
            # Gimmie all possible realities
            futureBoards.append(copy.deepcopy(currentBoard))
        
        for currentRow in range(numQueens):

            #Create the list of possible states
            for n in range(numQueens):
                # Gimmie all possible realities
                futureBoards.append(copy.deepcopy(currentBoard))

            currentBoard.clear_list_of_Coords()
            currentBoard.generate_ListOfCoords()
            ListOfQueenCoords = currentBoard.get_QueenCoords()
            #print(ListOfQueenCoords)
            currentQueenCoords = ListOfQueenCoords[currentRow]
        
            #flip the queen coords at current row to a 0 for preparation
            for Possibleboard in futureBoards:
                #try to get 
                Possibleboard.flip(currentRow,currentQueenCoords[1])

                
            #Set all possible boards queen position while also revaluating their fitness
            for currentColumn in range(numQueens):
                futureBoards[currentColumn].flip(currentRow,currentColumn)
                futureBoards[currentColumn].fitness()
                #print("Fitness: ", futureBoards[currentColumn].get_fit())
                #futureBoards[currentColumn].show()
                #input()

            #Compare our current board with each of possible future boards
            for NumBoards in range(len(futureBoards)):
                #print(currentBoard.get_fit()," vs", futureBoards[NumBoards].get_fit())
                if (currentBoard.get_fit() > futureBoards[NumBoards].get_fit()):
                    bestBoardNumber = NumBoards
        
            # We found the best board so make it our current board and update our fit
            currentBoard = futureBoards[bestBoardNumber]
            bestBoardNumber = 0
            currentFit = currentBoard.get_fit()

            futureBoards.clear()
        
        if(currentFit == 0):
            break
        #If we cannot get h = 0 then we reset and try again
        currentBoard.reset()
        numReset = numReset + 1


    return currentBoard, numReset

#print("Before Hill-Climbing:")
#chessboard.show()

startTime = time.perf_counter()
#input()
chessboard, numReset = HillClimbing(chessboard)

endTime = time.perf_counter()
runningTime = (endTime - startTime) * 1000

print("Hill-Climbing:")
chessboard.fitness()
print("Running Time:",runningTime, "ms")
print("# of Restarts:",numReset)
chessboard.show()