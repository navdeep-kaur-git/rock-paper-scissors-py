from random import randint

# constants
ROCK = "ROCK"
PAPER = "PAPER"
SCISSORS = "SCISSORS"
EXIT = "EXIT"

# possible plays
plays = [ROCK, PAPER, SCISSORS]

# vars
player_name = input("Enter you name: ").upper()
player_score = 0
computer_score = 0

# random play for computer
computer = plays[randint(0,2)]

while True:
  # ask user for a play
  player = input("\nRock, Paper, Scissors? or Exit? --> ").upper()

  if player == EXIT:
    print("\nFinal Score is ", player_name, ":", player_score, "and COMPUTER:", computer_score)
    break
  elif player == computer:
    print("It's a tie!")
  elif player == ROCK:
    if computer == PAPER:
      print("You lose!", computer, "covers", player)
      computer_score += 1
    else:
      print("You win!", player, "smashes", computer)  
      player_score += 1
  elif player == PAPER:
    if computer == SCISSORS:
      print("You lose!", computer, "cut", player)
      computer_score += 1
    else:
      print("You win!", player, "covers", computer)
      player_score += 1
  elif player == SCISSORS:
    if computer == ROCK:
      print("You lose!", computer, "smashes", player)
      computer_score += 1
    else:
      print("You win!", player, "cut", computer)  
      player_score += 1  
  else:
    print("It's an invalid play! Please try again.")

  # print current score and continue
  print(player_name, ":", player_score, "\t COMPUTER:", computer_score, end = "\n\n")
  computer = plays[randint(0,2)]  
