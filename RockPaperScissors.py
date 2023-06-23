import random
try:
    def play():
        user = input("Which do you choose?'Rock', 'Paper','Scissors'\n")
        computer = random.choice(['Rock','Paper','Scissors'])
        print('My/Your input: ',user)
        print('Computer input: ',computer)

        if str(user) == computer:
            return 'TIE!'
    
        if winner(str(user), computer):
            return 'You WON!'
        return 'You LOST to a computer!'

    def winner(player,opponent):
            if(player == 'Rock' and opponent == 'Scissors') or (player == 'Scissors' and opponent == 'Paper') or (player == 'Paper' and opponent == 'Rock'):
                return True
    
    print(play())
except:
    print('Invalid option...Please start over!')