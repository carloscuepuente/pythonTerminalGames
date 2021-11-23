import random
import time

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
    answer = answer.lower()
    if answer in ["yes", "no", "r", "p", "s"]:
        return True
    else:
        print("not a valid answer")
        return False

#funcion del juego principal, harcodear el numero de intentos o dar la opcion de que el jugador los ponga?
def rock_paper_scissor():
    #[["R","S"],["P","R"],["S","P"]]
    player_win_moves = [("r","s"), ("p","r"),("s","p")]
    win = 0
    lost = 0
    draw = 0
    while win < 3 and lost < 3:
        #score_board(win=win,lost=lost,draw=draw)
        player_choice = input("Type r for rock, p for paper or s for scissors: \n >").lower()
        while not answer_check(player_choice):
            player_choice = input("Type r for rock, p for paper or s for scissors: \n >").lower()
        
        cpu_choice = random.choice(["r","p","s"])

        print("PLAYER: {} <---vs---> CPU: {}\n".format(player_choice,cpu_choice))

        contested_move = list(zip(player_choice,cpu_choice))
        #[("r","s")]

        if contested_move[0][0] == contested_move[0][1]:
            draw += 1
        elif contested_move[0] in player_win_moves:
            win += 1
        else:
            lost += 1
        score_board(win=win,lost=lost,draw=draw)

    if win == 3:
        print("You win")
        return
    if lost == 3:
        print("You lose")
        return


#actualizar la puntuacion con cada jugada
def score_board(win,lost,draw):
    print("\n SCORE:   PLAYER:{}   CPU:{}   DRAWS:{}\n".format(win,lost,draw))
    pass

#main menu loop
print(
    """
     =====================================
    | Welcome to rock paper scissors      |
     =====================================
    """)
time.sleep(2)
print(
    """
     =====================================================
    | What do you want to do?                             |
    |                                                     |
    |    1) Play Rock, Paper, Scissor (best out of 3)     |
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
            rock_paper_scissor()
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

"""
ganadas = 0
perdidas = 0
empates = 0

opciones = ["R", "P", "S"]
resultadosPosibles = [["R","P"],["R","S"],["P","R"],["P","S"],["S","R"],["S","P"]]
resultadosganarplayer = [["R","S"],["P","R"],["S","P"]]
resultadosperderplayer =[["R","P"], ["P","S"],["S","R"]]

while ganadas <3 and perdidas <3:
    cpu_choice = random.choice(opciones)
    player_choice = input("ROCK [R]   PAPER [P]   SCISSORS [S]: ")
    resultado = [player_choice,cpu_choice]
    print("player choice: {} ".format(player_choice))
    print("cpu choice: {}".format(cpu_choice))
    
    if player_choice == cpu_choice:
        empates +=1
        ganadas
        perdidas
        print("MARCADOR:   GANADAS:{}   PERDIDAS:{}   EMPATES:{}".format(ganadas,perdidas,empates))
    else:
        for i in resultadosganarplayer:
            if resultado == i:
                ganadas +=1
                perdidas
                empates
                print("MARCADOR:   GANADAS:{}   PERDIDAS:{}   EMPATES:{}".format(ganadas,perdidas,empates))
            else:
                pass
        for i in resultadosperderplayer:
            if resultado == i:
                perdidas +=1
                ganadas
                empates
                print("MARCADOR:   GANADAS:{}   PERDIDAS:{}   EMPATES:{}".format(ganadas,perdidas,empates))
            else:
                pass

if ganadas == 3:
    print("has ganado")

else:
    print("has perdido")"""