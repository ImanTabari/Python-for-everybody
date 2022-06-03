'''
Write a program which first chooses a number between 1 and 100. 
The player is then asked to enter a guess. If the player guesses wrong the program gives 
feedback and asks for new guesses until one is correct.
Make the range customizable (ask for it before starting the guessing).
You can add lives. (optional)
'''

def GuessMyNum(lives, Num):
    count = 0
    MyGuess = None
    StartPoint = 1
    EndPoint = 100
    while True:
        if count < lives: 
            MyGuess = StartPoint + (EndPoint-StartPoint)//2
            print(MyGuess)
            if MyGuess == Num:
                print('Congratulations. You won!')
                break
            else:
                count += 1
                if MyGuess > Num:
                    print(f'Too high. You have {lives-count} lives')
                    EndPoint = MyGuess - 1
                else:
                    print(f'Too low. You have {lives-count} lives') 
                    StartPoint = MyGuess + 1
        else:
            print('You ran out of lives.')
            break
         
Number, Lives = map(int, input('Enter the number between 1-100 and the lives: ').split())
print(f"I'v the number between 1-100. you have {Lives} lives.")
GuessMyNum(Lives,Number)         