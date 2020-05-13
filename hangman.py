#Welcome the player
current_player = input("What is your name? ")
print("Welcome to hangman,", current_player, '!')

# Read text file words and put into list
filename = "C:/Users/Shmuel Weinfeld/Desktop/Hangman Game/words.txt"
file = open(filename, 'r')
words = []
for word in file.read().split():
    words.append(word)

#select a word and print blanks
from random import randrange

def play_game():
    # Set the variables
    secret_word = ''
    wrong_guesses = []
    mistakes = 0
    max_mistakes = 6
    secret_word = words[randrange(0, len(words))]
    print("Fill in these", len(secret_word), "letters. You have six lives. Good luck!")
    blanks = list("_ " * len(secret_word))
    print(' '.join([str(elem) for elem in blanks]) )
    while mistakes < max_mistakes:
        guess = input("select a letter: \n")
        while not guess.isalpha():
            print("That's not a letter. Please enter a lower case letter")
            guess = input("select a letter: \n")
        guess = guess.lower()
        if guess in secret_word:
            print("good guess! You still have", max_mistakes-mistakes,"lives")
            for index, char in enumerate(secret_word):
                if char == guess:
                    blanks[index*2] = guess
            print("Your correct letters are: ", ' '.join([str(elem) for elem in blanks]))
            print("your wrong letters are:", wrong_guesses)
            myword = (''.join(map(str, blanks)))

            winning_word = (secret_word.replace("", " ")[1: ])
            if winning_word == myword:
                print("Congrats! You won!")
                print("the secret word is ", secret_word)
                again = input("Do you want to play again? Enter y for yes or any other key for no.\n")
                if again == 'y':
                    play_game()
                else:
                    print("thanks for playing")
        else:
            print("sorry, wrong guess")
            wrong_guesses.append(guess)
            print("your wrong guesses are:",wrong_guesses)
            mistakes += 1
            lives = max_mistakes - mistakes
            print("you have" ,lives, " live(s) reamaining" )
            print("your correct guesses are: ", ' '.join([str(elem) for elem in blanks]))

    print("game over")
    print("the secret word is " + secret_word)
    again = input("Do you want to play again? Enter y for yes or any other key for no.\n")
    if again == 'y' :
        play_game()
    else:
        print("Thanks for playing!")

play_game()
