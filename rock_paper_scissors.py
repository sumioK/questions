import random

def judge(your_hand, ribal):
  if ribal == your_hand:
    again()
  if ribal == 'rock':
    if your_hand == 'paper':
      print('ribals hand is '+ribal,'\ncongratulation! you win!!')
    elif your_hand == 'scissors':
      print('ribals hand is '+ribal,'\nyou lose ...')
  if ribal == 'paper':
    if your_hand == 'rock':
      print('ribals hand is '+ribal,'\nyou lose ...')
    elif your_hand == 'scissors':
      print('ribals hand is '+ribal,'\ncongratulation! you win!!')
  if ribal == 'scissors':
    if your_hand == 'rock':
      print('ribals hand is '+ribal,'\ncongratulation! you win!!')
    elif your_hand == 'paper':
      print('ribals hand is '+ribal,'\nyou lose ...')

def again():
  your_hand = input('1 , 2 .. : ')
  ribal = random.choice(cpu_hand)
  judge(your_hand,ribal)

cpu_hand =['rock', 'paper', 'scissors']
ribal = random.choice(cpu_hand)
your_hand =input("choose your hand: ")

judge(your_hand, ribal)