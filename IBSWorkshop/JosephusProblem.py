'''
Flavius Josephus was a famous historian of the first century. During the Jewish-Roman war, he was among a band of 41 Jewish rebels 
trapped in a cave by the Romans. Preferring suicide to capture, the rebels decided to kill themselves. Using a method to form a circle 
and in clockwise direction everybody kills the person on his left side until everyone dies. But Josephus, wanted none of this suicide 
nonsense and therefore quickly calculated where he should stand in the circle so that he will be the last one 
(he knew who is the first one). So basically Josephus Problem is when you have a circle of n people standing and you want to cross out 
every second person step-by-step until only one remains.

Write a function to solve Josephus Problem. The program should ask for a number which represents the number of people playing the "game".
The return value should be the number of the "winning" seat.
'''
def Josephus(num):
    ParticpantList = []
    counter = 0
    while counter < num:
        ParticpantList.append(1)
        counter += 1
    
    StartPoInd = 0
    DelPoInd = 0    
    while sum(ParticpantList) != 1:
        if StartPoInd != len(ParticpantList)-1 and sum(ParticpantList[StartPoInd+1:]) > 0:
             DelPoInd = ParticpantList.index(1, StartPoInd+1, len(ParticpantList))
        else: DelPoInd = ParticpantList.index(1, 0, len(ParticpantList))
        ParticpantList[DelPoInd] = 0
        if DelPoInd != len(ParticpantList)-1 and sum(ParticpantList[DelPoInd+1:]) > 0:
            StartPoInd = ParticpantList.index(1, DelPoInd+1, len(ParticpantList))
        else: StartPoInd = ParticpantList.index(1, 0, len(ParticpantList))
    WinnerPlace = ParticpantList.index(1)
    return WinnerPlace+1

participant_num = int(input('Enter the number of participants: '))
print(Josephus(participant_num))        

        

            
            
