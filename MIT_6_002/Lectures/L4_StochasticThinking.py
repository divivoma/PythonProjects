# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 21:47:32 2018

@author: Markos
"""

import random
 
def rollDie():
    """returns a random int between 1 and 6"""
    return random.choice([1,2,3,4,5,6]) #uniformally distribuited!!
 
def testRoll(n = 10):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    print(result)

#testRoll(5)

random.seed(0) #use it to get always the same results !

#def runSim(goal, numTrials, txt):
#    total = 0
#    for i in range(numTrials):
#        result = ''
#        for j in range(len(goal)):
#            result += str(rollDie())
#        if result == goal:           
#            total += 1
#            print('get it at event = ',i)
#    print('Actual probability of', txt, '=',
#          round(1/(6**len(goal)), 8)) 
#    estProbability = round(total/numTrials, 8)
#    print('Estimated Probability of', txt, '=',
#          round(estProbability, 8))
#    
#runSim('11111', 1000000, '11111')

def sameDate(numPeople, numSame):
#    possibleDates = range(366)
#   Here below we are changing the model of the birtdhay
#   after looked to the heat map of all the USA birthday
#   to better predict the 3 people case
    
    possibleDates = 4*list(range(0, 57)) + [58]\
                    + 3*list(range(59, 366))\
                    + 4*list(range(180, 270))
    birthdays = [0]*366
    for p in range(numPeople):
        birthDate = random.choice(possibleDates)
        birthdays[birthDate] += 1
    return max(birthdays) >= numSame

def birthdayProb(numPeople, numSame, numTrials):
    numHits = 0
    for t in range(numTrials):
        if sameDate(numPeople, numSame):
            numHits += 1
    return numHits/numTrials

import math

for numPeople in [10, 20, 40, 100]:
    print('For', numPeople,
          'est. prob. of a shared birthday is',
          birthdayProb(numPeople, 3, 10000))
    numerator = math.factorial(366)#for 3 people the math model is more complex
    denom = (366**numPeople)*math.factorial(366-numPeople)
    print('Actual prob. for N = 100 =',
          1 - numerator/denom)