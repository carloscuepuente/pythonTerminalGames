import random
from words import filtered_words # tengo un problema con la asignacion de los path de los modulos y demás
from hangman_visual import lives_visual_dict

#print(filtered_words)

def num_check(*num):
    """
    Check if the keybord user input is a integer number
    """
    for i in num:
        try:
            int(i)
        except:
            print("Sorry {} is not a number".format(i))
            return False
    return True

def answer_check(answer):
    """
    check for valid user input
    """
    import string
    answer = answer.lower()
    if (answer in string.ascii_lowercase) and len(answer) == 1:
        return True
    else:
        print("not a valid answer")
        return False

#funcion que selecciona una palabra de la lista de palabras filtradas ya en el otro archivo
def random_word_choice(words):
    word = random.choice(words)
    return word
    
#va a mostrar _ por cada letra de la palabra y la cambia por la letra actual si el usuario adivina una letra bien
def show_word(word,user_bag = None):
    if user_bag == None:
        for i in [letter for letter in word]:
            print(" _ ", end="")
    else:
        for i in word:
            if i in user_bag:
                print(i, end ="")
            else:
                print(" _ ",end="")
      
#el juego como tal 
def main_game():
    conceiled_word = random_word_choice(filtered_words)
    bag_of_letters = set(conceiled_word)
    bag_of_correct_user_letters = set()
    bag_of_all_the_letters = set()
    #print(conceiled_word,bag_of_letters)
    lives = 6
    print("You have {} lives left to guess a {} letter word:".format(lives,len(conceiled_word)))
    show_word(word=conceiled_word,user_bag=None)
    print("\n")
    print(lives_visual_dict[lives])
    
    #loop principal
    while (len(bag_of_letters) != len(bag_of_correct_user_letters)) and lives > 0:
        user_letter = input("type a letter: \n >").lower()
        while not answer_check(user_letter):
            user_letter = input("type a letter: \n >").lower()
        bag_of_all_the_letters.add(user_letter)
        if user_letter in bag_of_letters:
            bag_of_correct_user_letters.add(user_letter)
        else:
            lives -= 1
        print(lives_visual_dict[lives])
        if lives != 0:
            print("\n You have {} lives left to guess a {} letter word".format(lives,len(conceiled_word)))
        show_word(word=conceiled_word, user_bag=bag_of_correct_user_letters)
        print("\n You have used so far this letters {}".format(bag_of_all_the_letters))


    if len(bag_of_letters) == len(bag_of_correct_user_letters):
        print("You Win!")
    if lives == 0:
        print("You Lose!, the word was {}".format(conceiled_word))

#main menu loop

print(
    """
     =====================================
    | Welcome to Hangman                  |
     =====================================
    """)
print(
    """
     =====================================================
    | What do you want to do?                             |
    |                                                     |
    |    1) Play                                          |
    |                                                     |
    |        or                                           |
    |                                                     |
    |    2) Exit                                          |
    |                                                     |
     =====================================================
    """
)

game = input("type 1 to play or 2 to exit \n\n >")
while True:
    if len(game) == 1 and num_check(game):
        game = int(game)
        if game == 1:
            main_game()
            break
        elif game == 2:
            print("Bye, hope you had fun!")
            break
        else:
            print("Sorry {} it is not an option".format(game))
            game = input("type 1 to play or 2 to exit \n\n >")
    else:
        print("Sorry {} it is not an option".format(game))
        game = input("type 1 to play or 2 to exit \n\n >")

input() #para que no se cierre la terminal al culminar el programa
