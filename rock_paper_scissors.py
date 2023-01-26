import random

def judge(your_hand, ribal):
  if ribal == your_hand:
    again()
  if ribal == 'rock':
    if your_hand == 'paper':
      print('congratulation! you win!!')
    elif your_hand == 'scissors':
      print('you lose ...')
  if ribal == 'paper':
    if your_hand == 'rock':
      print('you lose ...')
    elif your_hand == 'scissors':
      print('congratulation! you win!!')
  if ribal == 'scissors':
    if your_hand == 'rock':
      print('congratulation! you win!!')
    elif your_hand == 'paper':
      print('you lose ...')

def again():
  your_hand = input('1 , 2 .. : ')
  ribal = random.choice(cpu_hand)
  judge(your_hand,ribal)

cpu_hand =['rock', 'paper', 'scissors']
ribal = random.choice(cpu_hand)
your_hand =input("choose your hand: ")

judge(your_hand, ribal)