#---------import laiberaries----------
import turtle 
import winsound
import time

#----------------variable game control-------------
game_mode = None             # "Player" vs "Player" OR vs "computer"
difficulty = None
game_started = False
paused = False 
score1 = 0
score2 = 0
button_pvp =  None
button_ai = None
button_easy = None
button_medium = None
button_hard = None
button_start = None
end_screen = None

#=================create the game window============

wind = turtle.Screen()                         # initialize screen
wind.title("Ping Pong")                        # set the title of the window
wind.bgcolor("#0f172a")                      # set the bg color
wind.setup(width = 1000 , height= 700)
wind.tracer(0)                                 # stop updating auto 

#==================== create a start menu screen =========================
bg_box = turtle.Turtle()
bg_box.color("#1e1e3f")
bg_box.penup()
bg_box.goto(-300, 250)
bg_box.begin_fill()

for _ in range(2):
    bg_box.forward(600)
    bg_box.right(90)
    bg_box.forward(500)
    bg_box.right(90)
bg_box.end_fill()
bg_box.hideturtle()

#===========================button FUNCTION=========================

def create_button(text, color, position, font_size = 16):
    button = turtle.Turtle()
    button.hideturtle()
    button.penup()
    button.color(color)
    button.goto(position)
    button.speed(0)
    button.write(text, align="center" , font= ("Arial" , font_size, "bold"))
    return button

#=======================Make button =============
def create_buttons():
    global button_pvp , button_ai , button_easy , button_medium , button_hard , button_start
    button_pvp = create_button(" 1 - Player vs Player" , "white" , (0, 180))
    button_ai = create_button(" 2 - Player vs Computer" , "white", (0, 140))
    button_start = create_button("SPACE - Start Game" , "cyan" , (0, -40) , font_size=14)

#=========================message===================
message = turtle.Turtle()
message.hideturtle()
message.color("gold")
message.penup()
message.goto(0 , -100)

#========================= PVP FUNCTION=====================
def set_mode_pvp():
    global game_mode , button_pvp , button_ai , button_easy , button_medium , button_hard
    game_mode = "pvp"
    print("Mode: Player vs Player")
    
    if button_ai:
        button_ai.clear()
        button_ai.hideturtle()
        button_ai = None
    
    if button_pvp:
        button_pvp.clear()
        button_pvp.hideturtle()
        button_pvp = None
        
    if button_easy:
        button_easy.clear()
        button_easy.hideturtle()
        button_easy = None
        
    if button_medium:
        button_medium.clear()
        button_medium.hideturtle()
        button_medium = None
    
    if button_hard:
        button_hard.clear()
        button_hard.hideturtle()
        button_hard = None

#==============AI FUNCTION ======================

def set_mode_ai():
    global game_mode , button_easy , button_medium , button_hard , button_pvp , button_ai
    game_mode = "ai"
    print("Mode : Player vs Computer")
    
    if button_pvp:
        button_pvp.clear()
        button_pvp.hideturtle()
        button_pvp = None
        
    if button_ai:
        button_ai.clear()
        button_ai.hideturtle()
        button_ai = None
        
    if button_easy is None:
        button_easy = create_button(" E - Easy" , "lightgreen" , (0 , 80) , font_size= 14)
        
    if button_medium is None:
        button_medium = create_button("M - Medium" , "orange" , (0, 50) , font_size= 14)
        
    if button_hard is None:
        button_hard = create_button (" H - Hard", "red" , (0, 20) , font_size= 14)
        
    
#====================Difficulty FUNCTION==========================
#=======Easy

def set_difficutly_easy():
    global difficulty , button_easy , button_medium , button_hard
    difficulty = "easy"
    print("Difficulty: Easy")
    
    if button_easy:
        button_easy.clear()
        button_easy.hideturtle()
        button_easy = None
        
    if button_medium:
        button_medium.clear()
        button_medium.hideturtle()
        button_medium = None
        
    if button_hard:
        button_hard.clear()
        button_hard.hideturtle()
        button_hard = None
        
#====== Medium

def set_difficulty_medium():
    global difficulty , button_easy , button_medium , button_hard
    difficulty = "medium"
    print("Difficulty: Medium")
    
    if button_easy:
        button_easy.clear()
        button_easy.hideturtle()
        button_easy = None
        
    if button_medium:
        button_medium.clear()
        button_medium.hideturtle()
        button_medium = None
        
    if button_hard:
        button_hard.clear()
        button_hard.hideturtle()
        button_hard = None
        
        
#======Hard

def set_difficulty_hard():
    global difficulty , button_easy , button_medium , button_hard
    difficulty = "hard"
    print("Difficulty: Hard")
    
    if button_easy:
        button_easy.clear()
        button_easy.hideturtle()
        button_easy = None
        
    if button_medium:
        button_medium.clear()
        button_medium.hideturtle()
        button_medium = None
        
    if button_hard:
        button_hard.clear()
        button_hard.hideturtle()
        button_hard = None
        
        
#=======================Drawing the madrab and tha ball==================

#mdarab1
madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.shapesize(stretch_wid = 5 , stretch_len = 1.2)
madrab1.color("#38bdf8")
madrab1.penup()
madrab1.goto(-420 , 0)

# madrab2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.shapesize(stretch_wid= 5 , stretch_len= 1.2)
madrab2.color("#f43f5e")
madrab2.penup()
madrab2.goto(420 , 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("#facc15")
ball.penup()
ball.goto(0 , 0)
ball.dx = 0.4
ball.dy = 0.4

#score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("#22c55e")
score.penup()
score.goto(0 , 260)
score.write("Player1 : 0       |       Player2 : 0" , align="center" , font=("courier" , 24 , "normal"))


#=========OBJECT FUNCTION=========================

def madrab1_up():
    if paused:
        return
    y = madrab1.ycor()
    y += 40
    madrab1.sety(y)
    
def madrab1_down():
    if paused:
        return
    y = madrab1.ycor()
    y -= 40
    madrab1.sety(y)
    
def madrab2_up():
    if paused:
        return
    y = madrab2.ycor()
    y += 40
    madrab2.sety(y)
    
def madrab2_down():
    if paused:
        return
    y = madrab2.ycor()
    y -= 40
    madrab2.sety(y)
    
    
#================start game function=======================

def start_game():
    global game_started
    
    if game_mode is None:
        message.clear()
        message.write("Please select game mode." , align="center" , font=("Arial" , 16 , "bold"))
        return
        
    if game_mode == "ai" and difficulty is None:
        message.clear()
        message.write(" Please select difficulty level." , align="center" , font=("courier" , 16 , "bold"))
        return

    game_started = True
    
    bg_box.clear()
    
    if button_easy:
        button_easy.clear()
        button_easy.hideturtle()
        
    if button_medium:
        button_medium.clear()
        button_medium.hideturtle()
        
    if button_hard:
        button_hard.clear()
        button_hard.hideturtle()
        
    if button_pvp:
        button_pvp.clear()
        button_pvp.hideturtle()
        
    if button_ai:
        button_ai.clear()
        button_ai.hideturtle()
        
    if button_start:
        button_start.clear()
        button_start.hideturtle()
        
    
    #======speed based on the level
    if difficulty == "easy":
        ball.dx = 0.3
        ball.dy = 0.3
    elif difficulty == "medium":
        ball.dx = 0.5
        ball.dy = 0.5
    elif difficulty == "hard":
        ball.dx = 0.8
        ball.dy = 0.8
        
    # if mode pvp make the speed  
    if game_mode == "pvp":
        ball.dx = 1
        ball.dy = 1
    
    winsound.PlaySound("background.wav" , winsound.SND_ASYNC | winsound.SND_LOOP) # SOUND WHEN GAME START
    
    
   

    #=======time count============
    countdown = turtle.Turtle()
    countdown.color("yellow")
    countdown.hideturtle()
    countdown.penup()
    countdown.goto(0,0)

    for i in range(3, 0, -1):
        countdown.clear()
        countdown.write(str(i), align="center" , font=("Arial" , 48, "bold"))
        time.sleep(1)

    countdown.clear()
    countdown.write("GO!" , align="center" , font=("Arial" , 48 , "bold"))
    time.sleep(1)
    countdown.clear()

    message.clear()


#==============RESTART FUNCTION=================
def restart_game():
    global score1 , score2 , game_started , paused
    score1 = 0
    score2 = 0
    ball.goto(0 , 0)
    ball.dx = 0.4
    ball.dy = 0.4
    game_started = False
    paused = False
    score.clear()
    score.write("Player1 : 0              Player2:0" , align="center" , font=("courier" , 24 , "normal"))
    
    for button in [button_pvp , button_ai , button_easy , button_medium , button_hard , button_start]:
        if button:
            button.clear()
            button.hideturtle()
            
    bg_box.clear()
    bg_box.penup()
    bg_box.goto(-300 , 250)
    bg_box.begin_fill()
    
    for _ in range(2):
        bg_box.forward(600)
        bg_box.right(90)
        bg_box.forward(500)
        bg_box.right(90)
    bg_box.end_fill()
    
    if end_screen:
        end_screen.clear()
    
    create_buttons()
    
#============paused FUNCTION=================

pause_screen = turtle.Turtle()
pause_screen.color("yellow")
pause_screen.hideturtle()
pause_screen.penup()
pause_screen.goto(0 , 0)

def toggle_pause():
    global paused
    paused = not paused
    
    if paused:
        pause_screen.clear()
        score.goto(0 , 0)
        score.write("Game Paused \n" " Press Enter to play" , align="center" , font=("courier" , 30, "bold"))
    else:
        score.clear()
        score.goto(0 , 260)
        score.write("Player1:  {}       Player2 : {}".format(score1 , score2) , align="center" , font=("courier" , 24 , "normal"))
        
        
        
#=================== BACK TO MENU ==========================

def back_to_menu():
    global game_mode , button_pvp , button_ai , difficulty , button_easy , button_medium , button_hard
    global game_started, button_start , paused , score1 , score2
    
    game_mode = None
    difficulty = None
    game_started = False
    paused = False
    score1 = 0
    score2 = 0
    
    ball.goto(0,0)
    ball.dx = 0.4
    ball.dy = 0.4
    
    score.clear()
    bg_box.clear()
    score.write("Player1 : 0         Player2 : 0" , align="center" , font=("courier" , 24, "normal"))
    
    if end_screen:
        end_screen.clear()
        
    for button in [button_pvp , button_ai , button_easy , button_medium, button_hard , button_start]:
        if button:
            button.clear()
            button.hideturtle()
            
    bg_box.clear()
    bg_box.penup()
    bg_box.goto(-300,250)
    bg_box.begin_fill()
    
    for _ in range(2):
        bg_box.forward(600)
        bg_box.right(90)
        bg_box.forward(500)
        bg_box.right(90)
    bg_box.end_fill()
    
    message.clear()
    pause_screen.clear()
    create_buttons()
    
    if button_easy:
        button_easy.clear()
        button_easy.hideturtle()
        button_easy = None
        
    if button_medium:
        button_medium.clear()
        button_medium.hideturtle()
        button_medium = None
        
    if button_hard:
        button_hard.clear()
        button_hard.hideturtle()
        button_hard = None
create_buttons()
    
#=================== WISN ==========

def show_winner(winner_text):
    global game_started, end_screen
    game_started = False
    score.clear()
    score.goto(0, 206)
    winsound.PlaySound("win.wav" , winsound.SND_ASYNC)
    
    if end_screen is None:
        end_screen = turtle.Turtle()
        end_screen.hideturtle()
        end_screen.penup()
        end_screen.color("gold")
        end_screen.goto(0,0)
        end_screen.write(winner_text , align="center" , font=("courier", 32, "bold"))
    else:
        end_screen.clear()
        
# KEYBOARD BINDING
wind.listen()
wind.onkeypress(madrab1_up , "Up")
wind.onkeypress(madrab1_down, "Down")
wind.onkeypress(madrab2_up , "w")
wind.onkeypress(madrab2_down , "s")
wind.onkeypress(set_mode_pvp , "1")
wind.onkeypress(set_mode_ai , "2")
wind.onkeypress(set_difficutly_easy , "e")
wind.onkeypress(set_difficulty_medium , "m")
wind.onkeypress(set_difficulty_hard , "h")
wind.onkeypress(start_game , "space")
wind.onkeypress(restart_game , "r")
wind.onkeypress(toggle_pause , "Return")
wind.onkeypress(back_to_menu , "Escape")


#========================== MAIN GAME LOOP========================
while True:
    wind.update()
    
    if not game_started or paused:
        continue
    
    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # boreder check 
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav" , winsound.SND_ASYNC)
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        
    if ball.xcor() > 490:
        ball.goto(0 , 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("Player1 : {}     Player2 : {}".format(score1 , score2) , align="center" , font=("courier" , 14 , "normal"))
        winsound.PlaySound("hit.wav" , winsound.SND_ASYNC)
        continue
    
    if ball.xcor() < -490:
        ball.goto(0 , 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player1 : {}     Player2 : {}".format(score1 , score2) , align="center" , font=("courier" , 14 , "normal"))
        winsound.PlaySound("hit.wav" , winsound.SND_ASYNC)
        continue
    
    # tasadom (collision) madrab & ball
    
    if (ball.xcor() > 410 and ball.xcor() < 430 and 
        ball.dx > 0 and 
        ball.ycor() < madrab2.ycor() + 50 and ball.ycor() > madrab2.ycor() - 50):
        ball.dx *= -1.05
        ball.dy *= 1.05
        winsound.PlaySound("hit.wav" , winsound.SND_ASYNC)
        
    if (ball.xcor() < -410 and ball.xcor() > -430 and
        ball.dx < 0 and 
        ball.ycor() < madrab1.ycor() + 50 and ball.ycor() > madrab1.ycor() - 50):
        ball.dx *= -1.05
        ball.dy *= 1.05
        
        
    if score1 == 9 and score2 == 9:
        ball.dx *= 2
        ball.dy *= 2
        
    if game_mode == "ai" and game_started and not paused:
        ai_speed = 0.2 if difficulty == "easy" else 0.4 if difficulty == "medium" else 0.6
        if madrab2.ycor() < ball.ycor():
            madrab2.sety(madrab2.ycor() + ai_speed)
        elif madrab2.ycor() > ball.ycor():
            madrab2.sety(madrab2.ycor() - ai_speed)
            
        
    if score1 == 15:
        show_winner("Player 1 WINS!🥳 \n" " Please Enter ESC to return menu")
    if score2 == 15:
        show_winner("Player 2 WINS!🥳 \n" " Please Enter ESC to return menu")
        
