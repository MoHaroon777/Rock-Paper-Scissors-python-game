import random
class game():
    def __init__(self):
        print("Welcome to My game. I made this game as a python practice"
            "\nlets begin...")
        print("In this game, you will play agains a computer")
        print("Enter the following choices:")
        print("Rock [0], Paper [1], Scissors[2]")
        self.__rock = 0
        self.__paper = 1
        self.__scissors = 2

        self.__wins = 0
        self.__total_games = 0
    def winner(self):
        self.__wins += 1
        print(f"{self.__wins} wins")
    
    def get_score(self):
        return self.__wins, self.__total_games
    
    def user_choice(self):
        # Take player input
        self.__user_input = int(input("Enter Choice: "))
        inp = True
        while inp:
            # if player inputs a value that is out of bound
            if 0 < self.__user_input > 2:   
                print("wrong Input, try again..")
                self.__user_input = int(input("Re-Enter Choice: "))
            else:
                inp = False
        return self.__user_input
    
    def play_again(self):
        # validate player input
        valid_inp = True
        while valid_inp:
            self.__p_agian = input("Play Again? [ y / n  ]: ")
            if self.__p_agian.lower() == "y" or "Y":
                return True
            elif self.__p_agian.lower() == "n" or "N":
                return False
            else:
                print("Huh?, I don't Understand that input, please try again")
                
    def start_game(self):
        choices = [self.__rock, self.__paper, self.__scissors]
        play = True
        while play:
            # Select a random option of the three possible options
            computer = random.choice(choices) 
            player = self.user_choice()
            if player == computer:
                print(f"Its a tie. Both you and your opponent have chosen {computer}")
                # if player is Rock and computer is paper
            elif player == 0 and computer == 1:
                print("Rock vs Paper")
                print("Paper beats Rock")
                print("Computer wins")
                # if player is Paper and computer is Rock
            elif player == 1 and computer == 0:
                print("Paper vs Rock")
                print("Paper beats Rock")
                print("You win")
                self.winner()
                # if player is Paper and computer is Scissors
            elif player == 1 and computer == 2:
                print("Paper vs Scissor")
                print("Scissor beats Paper")
                print("Computer Wins")
                # if player is scissors and computer is paper
            elif player == 2 and computer == 1:
                print("Scissor vs Paper")
                print("Scissor beats Paper")
                print("You win")
                self.winner()
            self.__total_games += 1
            #if False is returned, i.e player do not want to play again,
            #  quit the while loop
            if not self.play_again():   
                play = False
p1 = game()
p1.start_game()
player_score, total_games = p1.get_score() # Assign tuple values to variables
print(f"{player_score} wins out of {total_games} games")
