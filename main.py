import random
# The puzzle is a secret word randomly chosen from a list.
# The player guesses a letter in the puzzle.
# If the guess is correct, the letter is revealed.
# If the guess is incorrect, a line is cut on the player's parachute.
# If the puzzle is solved the game is over.
# If the player has no more parachute the game is over.

# Class for dirrector
# Class for image
# Class for guessing
# Class for words

class Director():
    # facilitates the game, 
    # keeps track of the guesses left, 
    # and if the game is playing,

    def __init__(self):
        self.is_playing = True
        self.guesses = 5

    def wrong_answer(self):
        # check to see if guess is in self.word
        pass

    def still_playing(self):
        # If the game has 0 guesses left or if the player wins, game over.
        pass

class Image():
    # display our stick man, our parachute, and our word count.

    def __init__(self):
        self.display_words = '_ _ _ _ _'
        self.display_parachute = {
            1:'',
            2:'',
            3:'',
            4:'',
            5:'',
        }

class Guessing():
    # takes the input of the player, and tells the game if the input is or is not correct.
    def __init__(self):
        self.player_guess = ''
        self.correct = None

    def get_input(self):
        # take user input, change self.player_guess to input.
        pass

    def is_correct(self):
        # check to see if user input is correct, changes self.correct to TRUE or FALSE .
        pass

class Words():
    # choose a random word out of out list.
    words = ['pzazz', 'pizza', 'books', 'chips', 'ghost', 'maize', 'peach', 'piano', 'apple']
    
    def __init__(self, words):
        self.word = random.choice(words)

def main():
    game = Director()
    image = Image()
    guess = Guessing()
    words = Words()

main()