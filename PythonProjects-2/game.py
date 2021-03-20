import turtle 
import random,time

player1=turtle.Turtle()
player1.shape("turtle")
player1.penup()
player1.goto(10,20)
player1.pendown()
player1.color('blue')
player1.write('player 1')

player2=turtle.Turtle()
player2.shape("turtle")
player2.penup()
player2.goto(10,80)
player2.pendown()
player2.color('red')
player2.write('player 2')

start1 = 0
start2 = 0
end = 180
endTurtle1 = turtle.Turtle()
endTurtle1.penup()
endTurtle1.goto(200,20)
endTurtle1.pendown()

endTurtle1.shape('circle')
endTurtle1.fillcolor('white')

endTurtle2 = turtle.Turtle()
endTurtle2.penup()
endTurtle2.goto(200,80)
endTurtle2.pendown()

endTurtle2.shape('circle')
endTurtle2.fillcolor('white')
wn = turtle.Screen()


while start1<=end or start2<=end:
  if start1>=end:
    wn.title(f"Player1 position is {start1}, Player2 posiion is {start2}, Player1 wins ")
    time.sleep(5)
    break

  elif start2>=end:
    wn.title(f"Player1 position is {start1}, Player2 posiion is {start2}, Player2 wins ")
    time.sleep(5)
    break

    dice1=random.randrange(1,6)
    dice2= random.randrange(1,6)

    player1.forward(dice1*2)
    time.sleep(1)

    player2.forward(dice2 * 2)
    time.sleep(1)
    start1 += dice1*2
    start2 += dice2*2
    wn.title(f"Player1 position is {start1}, Player2 position is {start2}, no one wins ")

time.sleep(3)
turtle.bye()











