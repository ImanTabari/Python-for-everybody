'''
Write a function that takes a filename as a parameter
The file contains an ended Tic-Tac-Toe match
We have provided you some example files (draw.txt, win-x.txt, win-o.txt)
Return "X", "O" or "Draw" based on the input file's content
'''
def tic_tac_result(filename):
    try:
        fhand = open(filename)
    except IOError:
        print (f'The file name "{filename}" does exist.')
    X = ['x','x','x']
    O = ['o','o','o']    
    TicTacMatrix = []
    TrpsInnerList = []
    TrpsTicTacMatrix = []
    TicTacDiagnol = []
    TrpsTicTacDiagno = []

    for line in fhand:
        TicTacMatrix.append(list(line.strip().lower()))

    for i in range(len(TicTacMatrix)):
        TicTacDiagnol.append(TicTacMatrix[i][i])
        TrpsTicTacDiagno.append(TicTacMatrix[i][len(TicTacMatrix[0])-(i+1)])
        for j in range(len(TicTacMatrix[0])):
            TrpsInnerList.append(TicTacMatrix[j][i])
        TrpsTicTacMatrix.append(TrpsInnerList)        

    if  X in TicTacMatrix or  X in TrpsTicTacMatrix or X in TicTacDiagnol  or X in TrpsTicTacDiagno:
        print('X')
        
    elif O in TicTacMatrix or  O in TrpsTicTacMatrix or O in TicTacDiagnol or O in TrpsTicTacDiagno:
        print('O')    
    else:
         print('Draw')    


fname = input('Enter your file name: ')
tic_tac_result(fname)         


              
