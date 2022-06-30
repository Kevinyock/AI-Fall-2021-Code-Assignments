''' Assignment # 9
Monte Carlo Markov Chain
Author: Kevin Do
File Creation Date: 10/25/2021
Last Modified Date: 10/29/2021
Due Date: 11/2/2021 @ 11:59 PM
'''

import random
# Number of samples
sampleSize = 1000000

#P(C|-s,r)
prob_of_C_given_Not_S_and_R = (0.878,0.122)
#P(C|-s,-r)
prob_of_C_given_Not_S_and_Not_R = (0.31,0.69)
#P(R|c,-s,w)
prob_of_R_given_C_not_S_and_W = (0.9863,0.0137)
#P(R|-c,-s,w)
prob_of_R_given_not_C_not_S_and_W = (0.8182,0.1818)



StateTransitionMatrix = (( 0.9322, 0.0068, 0.0610, 0.0000),
                         ( 0.4932, 0.1618, 0.0000, 0.3450),
                         ( 0.4390, 0.0000, 0.4701, 0.0909),
                         ( 0.0000, 0.1550, 0.4091, 0.4359))

def samplingProbabilities():
    print("Part A. The sampling probabilities")
    print("P(C|-s,r)    = <{:.4f},{:.4f}>".
          format(prob_of_C_given_Not_S_and_R[0],
                 prob_of_C_given_Not_S_and_R[1]))
    print("P(C|-s,-r)   = <{:.4f},{:.4f}>".
          format(prob_of_C_given_Not_S_and_Not_R[0],
                 prob_of_C_given_Not_S_and_Not_R[1]))
    print("P(R|c,-s,w)  = <{:.4f},{:.4f}>".
          format(prob_of_R_given_C_not_S_and_W[0],
                 prob_of_R_given_C_not_S_and_W[1]))
    print("P(R|-c,-s,w) = <{:.4f},{:.4f}>".
          format(prob_of_R_given_not_C_not_S_and_W[0],
                 prob_of_R_given_not_C_not_S_and_W[1]))
    print()

def displayTransitionProbabilities():
    print("Part B The transition probability matrix")
    print("----------------------------------")
    print("|    |  S1  |  S2  |  S3  |  S4  |")
    print("| S1 |0.9322|0.0069|0.0610|0.0000|")
    print("| S2 |0.4931|0.1618|0.0000|0.3450|")
    print("| S3 |0.4390|0.0000|0.4701|0.0909|")
    print("| S4 |0.0000|0.1550|0.4091|0.4359|")
    print("----------------------------------")
    print()

def displayRequestedQuery(states,sampleSize):
    #print(states)
    profOfC = (states[0] + states[1]) / sampleSize
    profOfNotC = (states[2] + states[3]) / sampleSize
    print("Part C The probability for the query")
    print("P(C|-s,r) = <{:.4f},{:.4f}>".format(profOfC,profOfNotC))


def MarkovChainMonteCarlo():
    #initialization 
    #States [S1,S2,S3,S4]
    states = [0,0,0,0]
    stateNum = random.randint(0,3)
    states[stateNum] = states[stateNum] + 1
    for val in range (sampleSize - 1):
        nextState = random.choices([0,1,2,3],StateTransitionMatrix[stateNum])
        stateNum = nextState[0]
        states[stateNum] = states[stateNum] + 1
    return states
    
    

samplingProbabilities()
displayTransitionProbabilities()
currentState = MarkovChainMonteCarlo()
displayRequestedQuery(currentState,sampleSize)