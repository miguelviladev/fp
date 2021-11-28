'''
Nome do Aluno:
Número Mecanográfico:
'''

import turtle
import random
import time

click = False
x1=0
y1=0
x0=0
y0=0

height=500
width=50
padding=5
message=["Exit","Human vs Human","Human vs PC","PC vs PC"]

WIDTH, HEIGHT = 500, 230

ws=turtle.Screen()
ws.setup(WIDTH, HEIGHT,startx=None,starty=None)
ws.setworldcoordinates(0,0,WIDTH,HEIGHT)
 
# Defining Turtle instance
t=turtle.Turtle()

turtle.title("Tic Tac Toe Game")

canvas = turtle.getcanvas()

boardPositions = ((30,30),(130,30),(230,30),\
                (30,130),(130,130),(230,130),\
                (30,230),(130,230),(230,230))

x1=0
y1=0


def click(x,y):
    """
    click  is called when a mouse click is detected in the canvas
    
    :param x: mouse x coordinate
    :param y: mouse y coordinate
    """
    
    global click
    global x1
    global y1
    x1=x
    y1=y
    click = True 
    print('click: {}, {}'.format(x1, y1))
    
def waitforclick():
    """
    waitforclick  stops the program from running until a mouse click is detected
    """
    global click

    turtle.update()
    click = False

    while not click:
        turtle.update()
        time.sleep(.1)

    click = False

def detectButtonInGame(x,y):
    """
    detectButtonInGame  detects which button was pressed when the game is over
    
    :param x: mouse x coordinate
    :param y: mouse y coordinate
    """
    i=0
    global message
    
    if 0<x<150 and 350<y<400:
        createButton(t,50,135,135,350, "black")
        buttonName(t,"Play again?",5,365,12)   
        time.sleep(1)
        createButton(t,50,135,135,350, "grey")
        buttonName(t,"Play again?",5,365,12)  
        return 0
        
    if 150<x<300 and 350<y<400:
        createButton(t,50,120,290,350, "black")
        buttonName(t,"Exit",210,365,12)
        createButton(t,50,120,290,350, "grey")
        buttonName(t,"Exit",210,365,12) 
        return 1

    return -1

    
def detectButton(x,y):
    """
    detectButton  detects which menu button was pressed
    
    :param x: mouse x coordinate
    :param y: mouse y coordinate
    """
    i=0
    global message
    global x0
    global y0
    
    for i in range(4):
        if (x0*(i+1))<x<((x0*(i+1)+height)) and (y0*(i+1))<y<((y0+1)*(i+1)*(width+padding)):
            print('Valors detectButton {}, {}'.format(x, y))
            createButton(t,height,width,x0,i*(width+padding),"black")
            buttonName(t,message[i],x0+(height-18*len(message[i]))//2, (i*(width+padding)+5),22)
            time.sleep(1)
            createButton(t,height,width,x0,i*(width+padding),"gray")
            buttonName(t,message[i],x0+(height-18*len(message[i]))//2, (i*(width+padding)+5),22)
            print (f"Return value: {i}")
            return i
    return -1
            
def createButton(t,height,width,x,y,color):
    """
    createButton  creates a button to be used in the menu or when the game is over

    :param t: turtle instance
    :param height: button height  
    :param width: button width 
    :param x: x coordinate
    :param y: y coordinate
    :param color: fill color of the button
    """
    t.fillcolor(color)
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    t.color(color)
    for i in range(4):
        if (i%2)==0:
            #Character size 18
            t.forward(height)
        else:
            t.forward(width)
        t.left(90)
    t.end_fill()        
        
    
def buttonName(t,message,x,y,font_size):
    """
    buttonName  adds a label to the button

    :param t: turtle instance
    :param message: button label
    :param x: x coordinate
    :param y: y coordinate
    :param font_size: font size of the label
    """
    t.hideturtle()
    t.speed(0)
    t.color('white')
    t.fillcolor('green')
    t.begin_fill()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.write(message,font=("Verdana",font_size, "normal"))
    t.end_fill()
    

def designMenu(t):
    """
    designMenu  designs the game start up menu. 

    :param t: turtle instance
    """
    global x0
    global y0
    global height
    global width
    global padding
    global message
    t.clear()
    t.reset()
    for i in message:
        if (len(i)*18)>height:
            height=(len(i)*18+100)
    
    for i in range(4):
        createButton(t,height,width,x0,i*(width+padding),"gray")
        buttonName(t,message[i],x0+(height-18*len(message[i]))//2, (i*(width+padding)+5),22)

 
def designBoardGame(t,ws): 
    """
    designBoardGame  designs the tic tac toe board game

    :param t: turtle instance
    :param ws: screen instance to be configure
    """
    WIDTH,HEIGHT=450,450
    ws.setup(WIDTH, HEIGHT)  # fudge factors due to window borders & title ba
    ws.setworldcoordinates(-150,-150,WIDTH,HEIGHT)
    ws.update()
    
    t.clear()
    t.reset()
    # setting up turtle color to green
    t.color("Green")
     
    # Setting Up width to 2
    t.width("2")
    t.speed(0)
     
    # Setting up speed to 2
    # Loop for making outside square of
    # length 300
    t.goto(0,0)
    for i in range(4):
        t.forward(300)
        t.left(90)
     
     
    # code for inner lines of the square
    t.penup()
    t.goto(0,100)
    t.pendown()
     
    t.forward(300)
     
    t.penup()
    t.goto(0,200)
    t.pendown()
     
    t.forward(300)
     
    t.penup()
    t.goto(100,0)
    t.pendown()
     
    t.left(90)
    t.forward(300)
     
    t.penup()
    t.goto(200,0)
    t.pendown()
     
    t.forward(300)
    t.penup()
    t.hideturtle()
    
def placeCircle(t,x,y):
    """
    placeCircle  places a grey circle in the board game, indicating a player move

    :param t: turtle instance
    :param x: x coordinate
    :param y: y coordinate
    """
    # setting up turtle color to green
    t.color("Grey")
    t.speed(6)
    # Setting Up width to 2
    t.width("10")
    t.goto(x,y)
    t.left(-135)
    t.pendown()
    t.circle(30)
    t.right(-135)
    t.penup()   

def placeCross(t,x,y):
    """
    placeCross  places a red cross in the board game, indicating a player move

    :param t: turtle instance
    :param x: x coordinate
    :param y: y coordinate
    """
    # setting up turtle color to green
    t.color("Red")
    t.speed(6)
    # Setting Up width to 2
    t.width("10")
    size = 30
    t.goto(x,y)
    t.pendown()
    t.right(45)
    t.forward(size*2)
    t.backward(size)
    t.left(90)
    t.forward(size)
    t.backward(size*2)
    t.penup() 
    t.right(90) 
    t.left(45)

def playerWon(lst):
    """
    playerWon  detects if a player wins the game. Reads the list to detect horizontal, vertical or diagonal lines

    :param lst: list of moves of the player
    :return: if a player wins the gam 
    """
    if len(lst) < 3:
        return False
    count=0
    count2=0
    res1, res2 = map(list, zip(*lst))
    
    # detects horizontal or vertical lines
    for i in [30,130,230]:
        if (res1.count(i)==3) or (res2.count(i)==3):
            return True
            
    # detects a diagonal line
    for i in lst:
        if i[0] == 130 and i[1] == 130:
            count += 1
            count2 += 1
            continue
        if (i[0]+i[1])==260:
            count+=1
        if (i[0]+i[1])==60 or (i[0]+i[1])== 460:
            count2+=1

    # Falta detectar uma das diagonais
    if count == 3:
            return True

    if count2 == 3:
            return True

    return False

def playerMove(x, y):
    """
    playerMove maps mouse coordinates to board positions

    :param x: x coordinate
    :param y: y coordinate
    :return: board position or square retrieved from the boardPositions tuple
    """
    xpos_final=0
    ypos_final=0
    global boardPositions
    
    for k in boardPositions:
        if ((x < k[0]+70) and (x > k[0]-30)) and ((y < k[1]+70) and (y > k[1]-30)):
                xpos_final= k[0]
                ypos_final= k[1]
    print(f"Coordinates input: {x},{y}")
    print(f"Coordinates: {xpos_final},{ypos_final}")
    return xpos_final,ypos_final
    
def endGame(t,player):
    """
    endGame shows the player message in case of victory or draw. Designs 2 buttons to play again or exit to the main menu.

    :param t: turtle instance
    :param player: player number, in case of 0 it's a draw
    """
    x=-100
    y=-50
    if player==1:
        t.color("grey")
        message = f"Player {player} wins the game!"
    elif player ==2:
        t.color("Red")
        message = f"Player {player} wins the game!"
    elif player ==0:
        t.color("green")
        message = f"It's a draw!!"
        x=50
                
    t.goto(x,y)
    t.write(message, font=("Verdana",22, "normal"))
    createButton(t,50,135,135,350, "grey")
    buttonName(t,"Play again?",5,365,12)
    createButton(t,50,120,290,350, "grey")
    buttonName(t,"Exit",210,365,12)
    
def computerMove(lst, player, player_moves):
    """
    computerMove computer move in the game. Generates a random coordinate from lst

    :param lst: list of moves available
    :param player: player number
    :param player_moves: list of moves of the player
    :return: new list of moves available and player moves
    """
    
    values = random.choice(lst)
    x,y = values
    lst.pop(lst.index(values))
    if player == 1:
        placeCircle(t,x,y)
        player_moves[0].append(values)
    elif player == 2:
        placeCross(t,x,y)
        player_moves[1].append(values)
    return lst,player_moves

def humanMove(lst, player, player_moves):
    """
    humanMove human move. detects if is a valid click in the board and places a circle or cross

    :param lst: list of moves available
    :param player: player number
    :param player_moves: list of moves of the player
    :return: new list of moves available and player moves
    """
    
    global x1
    global y1
    xpos_final = 0
    ypos_final = 0 
    
    print('humanMove {}, {}'.format(x1, y1))

    # Keeps reading mouse positions until we get a valid one
    while (xpos_final == 0 and ypos_final == 0) or not((xpos_final, ypos_final) in lst):
        waitforclick()
        xpos_final, ypos_final=playerMove(x1,y1)

    values = (xpos_final, ypos_final)
    x,y = values
    lst.pop(lst.index(values))
    if player == 1:
        placeCircle(t,x,y)
        player_moves[0].append(values)
    elif player == 2:
        placeCross(t,x,y)
        player_moves[1].append(values)
    
    return lst,player_moves
        
def playGame(playerType1, playerType2):
    """
    playGame based of the type of game (e.g. computer vs computer) the required fucntion is called to place a move until we reach the end of the game

    :param playerType1: player type can be computer or human
    :param playerType2: player type can be computer or human
    """
    
    lst=list(boardPositions)
    
    player_moves = [[],[]]
    
    print("Tamanho array: ", len(lst))
    
    number_moves = len(lst)
    move=0
    #Who plays first
    player1 = True
    player2 = False
    print(f"Player 1:{playerType1} and Player 2: {playerType2}")
    
    # Condições do jogo
    while move < number_moves:
        if player1:
            if playerType1 == "computer":
                lst,player_moves = computerMove(lst,1,player_moves)
                print(f"Player 1:{playerType1}: computer")
            if playerType1 == "human":
                lst,player_moves = humanMove(lst,1,player_moves)
                print(f"Player 1:{playerType1}: human")
            player2 = True
            player1 = False
            
        elif player2:
            if playerType2 == "computer":
                lst,player_moves = computerMove(lst,2,player_moves)
                print(f"Player 2:{playerType2}: computer")
            if playerType2 == "human":
                lst,player_moves = humanMove(lst,2,player_moves)
                print(f"Player 2:{playerType2}: human")
            player2 = False
            player1 = True
        
        move+=1
        if playerWon(player_moves[0]):
            with open("resultados.txt","a") as f:
                f.write(f"{playerType1.capitalize()} vs {playerType2.capitalize()}: Player 1 wins.\n")
            print("Player 1 wins the game!")
            endGame(t,1)
            break
                
        if playerWon(player_moves[1]):
            with open("resultados.txt","a") as f:
                f.write(f"{playerType1.capitalize()} vs {playerType2.capitalize()}: Player 2 wins.\n")
            print("Player 2 wins the game!")
            endGame(t,2)
            break
            
    if (not playerWon(player_moves[0])) and (not playerWon(player_moves[1])):
        with open("resultados.txt","a") as f:
                f.write(f"{playerType1.capitalize()} vs {playerType2.capitalize()}: Draw.\n")
        print("It's a draw!")
        endGame(t,0)
    
    #Fim do Jogo espera para clicar num dos butões
    result = -1
    while True:   
        turtle.update()
        waitforclick()
        result=detectButtonInGame(x1,y1)
        if result != -1: break
    # Falta o código para dar continuidade ao jogo ou voltar ao menu anterior
    if result == 0:
        #Play again
        designBoardGame(t,ws)
        playGame(playerType1,playerType2)
        

def main():
    """
    main when the game starts the main menu is designed and waits for a click in one of the 4 options
    """
       
    global x1
    global y1
    
    # Calls the click function when an mouse click is detected in the canvas 
    turtle.onscreenclick(click)
    
    while True:
       
        WIDTH, HEIGHT = 500, 230
        ws.setup(WIDTH, HEIGHT)  # fudge factors due to window borders & title ba
        ws.setworldcoordinates(0,0,WIDTH,HEIGHT)
        ws.update()
                     
        designMenu(t)
    
        turtle.update()
        waitforclick()
        menu=detectButton(x1,y1)
        
        if menu == 0:
            # exit game
            print("Exit Game")
            exit()
        elif menu == 1: 
            # Human vs Human
            designBoardGame(t,ws)
            playGame("human","human")
            print("Human vs Human")
        elif menu == 2: 
            # Human vs Computer
            print("Human vs Computer")
            designBoardGame(t,ws)
            playGame("computer","human")
        elif menu == 3: 
            # Computer vs Computer
            print("Computer vs Computer")
            designBoardGame(t,ws)
            playGame("computer","computer")
        else:
            # not valid
            print("Not a valid choice")

if __name__ == "__main__":
    main()

