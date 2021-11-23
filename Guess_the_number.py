import random
import time

def num_check(*num):
    for i in num:
        try:
            int(i)
        except:
            print("Sorry {} is not a number".format(i))
            return False
    return True

def answer_check(answer):
    answer = answer.lower()
    if answer in ["yes", "no", "low", "high"]:
        return True
    else:
        print("not a valid answer")
        return False

def computer_guess_player_number():
    print("So you want me to guess the number you're thinking of?")
    time.sleep(1)
    print("Give me a hint, it can be any number, at least tell me what numbers yours is between.")
    time.sleep(1)
    low = input("the lower bound is: \n >")
    high = input("And the upper bound is \n >:")
    print("Ok, almost ready, but first, let's establish how many attempts I have?")
    counter= input("number of tries: \n >")
    #check = num_check(low,high,counter)
    while not num_check(low,high,counter):
        low = input("the lower bound is: \n >")
        high = input("And the upper bound is is \n >:")
        counter= input("number of tries: \n >")

    low = int(low)
    high = int(high)
    counter = int(counter)
    print("All set, game on...")
    cpu_lower_boundry, cpu_upper_boundry = low , high
    cpu_guess = random.randint(cpu_lower_boundry,cpu_upper_boundry)
    counter -= 1
    print("Your number is {} ?".format(cpu_guess))
    answer = input("type yes or no \n >").lower()
    while not answer_check(answer):
        answer = input("type yes or no \n >").lower()
    

    if answer == "yes":
        print("I Won : ) your number was {}".format(cpu_guess))
        return

    while answer != "yes":
        if counter <= 0:
            print("I Lost : (")
            return

        print("my guess was to high or to low?")
        adjuster = input("type low or high: \n >").lower()
        while not answer_check(adjuster):
            adjuster = input("type low or high: \n >").lower()
        
        if adjuster == "low":
            cpu_lower_boundry = cpu_guess
        elif adjuster == "high":
            cpu_upper_boundry = cpu_guess
        
        cpu_guess = random.randint(cpu_lower_boundry,cpu_upper_boundry)
        print("Your number is {} ?".format(cpu_guess))
        counter -= 1

        answer = input("type yes or no \n >").lower()
        while not answer_check(answer):
            answer = input("type yes or no \n >").lower()
    
    print("I Won : ) your number was {}".format(cpu_guess))
    return
        

def player_guess_computer_number():

    cpu_lower_boundry = 0
    cpu_upper_boundry = 100
    cpu_number = random.randint(cpu_lower_boundry,cpu_upper_boundry)
    counter = random.randint(3,5)
    print("Ok, first let me think of a number...")
    time.sleep(2)
    print("Ready i got it")
    time.sleep(1)
    print("my secret number is between {} and {}, you have {} tries to guess it ".format(cpu_lower_boundry,
    cpu_upper_boundry,
    counter))
    time.sleep(2)
    print("game on...")
    time.sleep(1)
    player_guess = input("What number i'm thinking of? \n >")

    while not num_check(player_guess):
        player_guess = input("What number i'm thinking of? \n >")
    
    player_guess = int(player_guess)

    if player_guess == cpu_number:
        print("You have won! = ) {} was the number I was thinking of".format(player_guess))
        return
    
    while player_guess != cpu_number:
        print("Nop thats not my number")
        counter -= 1
        time.sleep(1)
        if player_guess > cpu_number:
            print("Your guess was to high")
        else:
            print("Your guess was to low")
        
        player_guess = input("What number i'm thinking of? \n >")
        while not num_check(player_guess):
            player_guess = input("What number i'm thinking of? \n >")
        player_guess = int(player_guess)

        if counter <= 0:
            print("Game over, I was thinking in {}".format(cpu_number))
            return
    print("You have won! = ) {} was the number i was thinking of".format(player_guess))
    return

#Main menu

print(
    """
     =====================================
    | Welcome to the number guessing game |
     =====================================
    """)
time.sleep(2)

print(
    """
     =====================================================
    | What do you want to play?                           |
    |                                                     |
    |    1) You think of a number and I try to guess it.  |
    |                                                     |
    |        or                                           |
    |                                                     |
    |    2) I think of a number and you try to guess it.  |
    |                                                     |
     =====================================================
    """
)
game = input("type 1 or 2 to play, 3 to exit \n\n >")
while True:
    if len(game) < 2 and num_check(game):
        game = int(game)
        if game == 1:
            computer_guess_player_number()
            break
        elif game == 2:
            player_guess_computer_number()
            break
        elif game == 3:
            print("Bye, hope you had fun!")
            break
        else:
            print("Sorry {} it is not an option".format(game))
            game = input("type 1 or 2 to play, 3 to exit \n\n >")
    else:
        print("Sorry {} it is not an option".format(game))
        game = input("type 1 or 2 to play, 3 to exit \n\n >")

input() # esto esta aqui porque no encontre bien eso de read que me comentaste. 


