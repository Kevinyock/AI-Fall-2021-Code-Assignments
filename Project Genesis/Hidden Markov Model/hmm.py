'''
Assignment # 11
Hidden Markov Model
Author: Kevin Do
File Creation Date: 11/7/2021
Last Modified Date: 11/17/2021
Due Date: 11/19/2021 @ 11:59 PM
'''

import sys
import numpy
 
file_import = open("cpt.txt")

def print_Probability(independent_Variables,resultProb):
    print(independent_Variables.rstrip(),"--> <{:.4f},{:.4f}>".format(resultProb[0],resultProb[1]))

# Hidden Markov Model
def calculate_probability(listOfVariables):
    listOfVariables = listOfVariables.rstrip().split(",")
    #Store the Initial Probability
    #P(X0) = <a, 1 - a>
    initProb = float(listOfVariables[0]) # A

    '''
    Transition
    -------------------------------------
    | X_t-1 |          P(x_t)           |
    |-----------------------------------|
    | True  | float(listOfVariables[1]) |
    |-----------------------------------|
    | False | float(listOfVariables[2]) |
    |-----------------------------------|
    '''
    prob_NextState = [float(listOfVariables[1]),float(listOfVariables[2])] # B, C
    #Transition
    '''
    Sensor
    -------------------------------------
    | X_t   |          P(e_t)           |
    |-----------------------------------|
    | True  | float(listOfVariables[3]) |
    |-----------------------------------|
    | False | float(listOfVariables[4]) |
    |-----------------------------------|
    '''
    EvidenceProb = [float(listOfVariables[3]),float(listOfVariables[4])] # D, F
    #Sensor

    ObservationList = listOfVariables[5:]
    
    CurrentState = [initProb, 1 - initProb]
    for eachObservation in ObservationList:
        CurrentState = [(prob_NextState[0] * CurrentState[0]) + (prob_NextState[1] * CurrentState[1]),
                        ((1 - prob_NextState[0]) * CurrentState[0]) + ((1 - prob_NextState[1]) * CurrentState[1])]
        if(eachObservation == 't'):
            CurrentState = [EvidenceProb[0] * CurrentState[0],EvidenceProb[1] * CurrentState[1]]

        else:
            CurrentState = [(1 - EvidenceProb[0]) * CurrentState[0],(1 - EvidenceProb[1]) * CurrentState[1]]

        
        alphaCurrent = 1 / (CurrentState[0] + CurrentState[1])
        CurrentState = [alphaCurrent * CurrentState[0],alphaCurrent * CurrentState[1]]

    return CurrentState[0] , CurrentState[1]

for eachLine in file_import:
    calc_prob = calculate_probability(eachLine)
    print_Probability(eachLine,calc_prob)

#Get the number of arguements
#if len(sys.argv) == 2:
    #with open(sys.argv[1],'r') as textFile:
        #lines = textFile.readlines()
        #for eachLine in lines:
            #calc_prob = calculate_probability(eachLine)
            #print_Probability(eachLine,calc_prob)
#else:
    #print("Incorrect use of the program")
