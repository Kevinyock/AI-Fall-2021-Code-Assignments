'''
Assignment Initiation Date: 9/8/2021
Author:Kevin Do
Last Modification Date: 9/13/2021
Due Date: 9/14/2021 @ 11:59 PM
'''
import board
import time
import random
import copy

# 5 Queens
chessboard = board.Board(5)
chessboard.fitness()
numGenerations = 0

'''
Side Note:
Lower the actual mutation rate seems 
to cause the same gene in both current and next generation
Current Bugs:
'''

def Genetic(InputBoard):

    numQueens = InputBoard.n_queen
    # Number of States
    numStates = 8
    currentRow = 0
    totalFitness = 0

    # Current Generation, their fitness and Selection 
    CurrentGenes = []
    ListOfBoards = []
    BoardsFitness = []
    BoardsSelection = []

    #Organize their gene by the highest chance of passing their genes
    CurrentGeneDictionary = []

    # Store the Mutated Genes
    MutationGenes = []

    # Store the Next Generation after the current one dies off due to old age/natural selection
    NextGenerationGenes = []
    #
    NumGeneration = 0
    
    PossibleBestBoard = InputBoard

    ### Generate a list of Genes
    for eachState in range(numStates):
        newGene = ""
        for eachGene in range(InputBoard.n_queen):
            newGene = newGene + str(random.randint(0,InputBoard.n_queen - 1))
        CurrentGenes.append(newGene)

        
    for val in range(numStates):
        ListOfBoards.append(copy.deepcopy(InputBoard))

    while True:
        '''
        # Print the current list of Genes
        print("Current Generation")
        for eachGene in CurrentGenes:
            print(eachGene)
        #input()
        '''

        ### get me the their what they look like on the chess board
        for val in range(numStates):
            ListOfBoards[val].wipeBoardClean()
            ListOfBoards[val].SetBoardQueens(CurrentGenes[val])
            ListOfBoards[val].fitness()
            # Give me each of the boards fitness
            BoardsFitness.append(ListOfBoards[val].get_fit())

        # Calculate the total fitness
        totalFitness = 0
        for val in range(len(BoardsFitness)):
            totalFitness = totalFitness + BoardsFitness[val]

        # Give me the selections
        for val in range(len(BoardsFitness)):
            BoardsSelection.append(BoardsFitness[val]/totalFitness)

        # Assign each gene and chance of survivability into a dictionary
        for val in range(len(BoardsFitness)):
            CurrentGeneDictionary.append([CurrentGenes[val],BoardsSelection[val]])
        
        #for val in range(len(BoardsFitness)):
            #print(CurrentGeneDictionary[val])

        #input()
        # then sort it by chance of surviving
        CurrentGeneDictionary.sort(key = lambda Survivability: Survivability[1],reverse=False)
    
        #for val in range(len(BoardsFitness)):
            #print(CurrentGeneDictionary[val])

        #input()

        # Test
        #for GeneNum in range(len(BoardsFitness)):
            #print("Gene Number ", GeneNum, " - ", CurrentGeneDictionary[GeneNum][0],"-", CurrentGeneDictionary[GeneNum][1])

        totalPercentage = 0.0
        for val in range(len(BoardsFitness)):
            totalPercentage = totalPercentage + BoardsSelection[val]

        #print("Total Number of Genes:", len(BoardsFitness), totalFitness, totalPercentage)

        #input()

        chanceOfSurvival = 0

        ListOfchanceOfSurvival = []

        for val in range(len(BoardsFitness)):
            chanceOfSurvival = chanceOfSurvival + CurrentGeneDictionary[val][1]
            ListOfchanceOfSurvival.append(chanceOfSurvival)

        #print(ListOfchanceOfSurvival)
        #input()

        ################
        # Paring Stage #
        ################

        # Store the genes we are prepare to Pair
        PairingGenes = []

        for eachGene in range(len(BoardsFitness)):
            #Generate a number between 0.0 and 1.0
            randNum = random.random()
            if randNum >= 0 and randNum < ListOfchanceOfSurvival[0]:
                PairingGenes.append(CurrentGeneDictionary[0][0])
            elif randNum >= ListOfchanceOfSurvival[0] and randNum < ListOfchanceOfSurvival[1]:
                PairingGenes.append(CurrentGeneDictionary[1][0])
            elif randNum >= ListOfchanceOfSurvival[1] and randNum < ListOfchanceOfSurvival[2]:
                PairingGenes.append(CurrentGeneDictionary[2][0])
            elif randNum >= ListOfchanceOfSurvival[2] and randNum < ListOfchanceOfSurvival[3]:
                PairingGenes.append(CurrentGeneDictionary[3][0])
            elif randNum >= ListOfchanceOfSurvival[3] and randNum < ListOfchanceOfSurvival[4]:
                PairingGenes.append(CurrentGeneDictionary[4][0])
            elif randNum >= ListOfchanceOfSurvival[4] and randNum < ListOfchanceOfSurvival[5]:
                PairingGenes.append(CurrentGeneDictionary[5][0])
            elif randNum >= ListOfchanceOfSurvival[5] and randNum < ListOfchanceOfSurvival[6]:
                PairingGenes.append(CurrentGeneDictionary[6][0])
            else:
                PairingGenes.append(CurrentGeneDictionary[7][0])

        #print("Before CrossOver")
        #for each in PairingGenes:
            #print(each)

        #input()
        ####################
        # Cross-Over Stage #
        ####################
        CrossoverGenes = []

        for eachPair in range(int(len(PairingGenes)/2)):
            # Get Me a random Position to do the crossover
            randomPosition = random.randint(0,numQueens - 1)
            # print(randomPosition)
            # Store the Cross Over Genes
            GeneOne = PairingGenes[eachPair * 2]
            GeneTwo = PairingGenes[(eachPair * 2)+1]
            #print("Before Crossover")
            #print(GeneOne)
            #print(GeneTwo)
            #input()

            GeneOneParts = []
            GeneTwoParts = []

            # Gene Splicing

            GeneOneParts.append(GeneOne[0:randomPosition])
            GeneOneParts.append(GeneOne[randomPosition:len(GeneOne)])

            GeneTwoParts.append(GeneTwo[0:randomPosition])
            GeneTwoParts.append(GeneTwo[randomPosition:len(GeneTwo)])

            GeneOne = GeneOneParts[0] + GeneTwoParts[1]
            GeneTwo = GeneTwoParts[0] + GeneOneParts[1]

            CrossoverGenes.append(GeneOne)
            CrossoverGenes.append(GeneTwo)

            #print("After Crossover")
            #print(GeneOne)
            #print(GeneTwo)
            #input()

            #print("After CrossOver")
            #for each in CrossoverGenes:
                #print(each)
    
        ####################
        #  Mutation Stage  # 
        ####################

        # If it below this number, the gene has just mutated
        mutationChance = random.random()

        #print("Crossover Genes")
        #for eachGene in CrossoverGenes:
            #print(eachGene)

        for val in range(len(CrossoverGenes)):
            if(random.random() < mutationChance):
                randomMutation = str(random.randint(0,numQueens - 1))
                randomPosition = random.randint(0,numQueens - 1)
                #print("Random Mutation:", randomMutation)
                #print("position:", randomPosition)
                LeftSideGene = slice(0,randomPosition)
                RightSideGene = slice(randomPosition + 1,numQueens)

                newMutation = CrossoverGenes[val][LeftSideGene] + randomMutation + CrossoverGenes[val][RightSideGene]
                #print("Before Mutation")
                #print(CrossoverGenes[val])
                CrossoverGenes[val] = newMutation
                #print("After Mutation")
                #print(CrossoverGenes[val])
                #input()
          
        #print("Crossover Genes")
        #for eachGene in CrossoverGenes:
            #print(eachGene)
        #input()
        
        #for row in range(InputBoard.n_queen):
            #for column in range(InputBoard.n_queen):
                #print("")

        
        CurrentGenes.clear()
        CurrentGeneDictionary.clear()
        BoardsSelection.clear()
        BoardsFitness.clear()

        CurrentGenes = CrossoverGenes
        
        '''
        print("Next Generation")
        for eachGene in CurrentGenes:
            print(eachGene)
        input()
        '''

        NumGeneration = NumGeneration + 1
        #Check if the next generation got the best solution
        for eachGene in CurrentGenes:
            PossibleBestBoard.wipeBoardClean()
            PossibleBestBoard.SetBoardQueens(eachGene)
            PossibleBestBoard.fitness()
            #PossibleBestBoard.show()
            if(PossibleBestBoard.get_fit() == 0):
                BestBoard = PossibleBestBoard
                return BestBoard, NumGeneration

'''
print("Before Genetic-Algorithm:")
chessboard.fitness()
chessboard.show()
'''

startTime = time.perf_counter()

chessboard, numGenerations = Genetic(chessboard)

endTime = time.perf_counter()
runningTime = (endTime - startTime) * 1000

print("Genetic-Algorithm:")
chessboard.fitness()
print("Running Time:",runningTime, "ms")
print("Number of Generation:",numGenerations)
chessboard.show()