import random

rock=''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

 '''
paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

 '''
scissor='''

   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
 '''
start_game= input(("input 'start' to play: ")).lower()

while start_game!= 'quit':
    if start_game== "start":
        player_choice = int(input("what do u choose? type 1 for rock,2 for paper, and 3 for scissors: "))
        computer = random.randint(1, 3)
        if player_choice==1 and computer ==2 :
            print(f'''your choice 
{rock}
computer choose
{paper}
You Lost''')
        elif player_choice==2 and computer==1:
            print(f'''your choice 
{paper}
computer choose
{rock}
You won''')
        elif player_choice ==2 and computer==3:
            print(f'''your choice 
{paper}
computer choose
{scissor}
You Lost''')
        elif player_choice==3 and computer==2:
            print(f'''your choice 
{scissor}
computer choose
{paper}
You Won''')
        elif player_choice==1 and computer==3 :
            print(f'''your choice 
{rock}
computer choose
{scissor}
You Won''')
        elif player_choice==3 and computer==1:
            print(f'''your choice 
{scissor}
computer choose
{rock}
You Lost''')
        elif player_choice==computer==1:
            print(f'''your choice 
{rock}
computer choose
{rock}
Tied''')
        elif player_choice == computer == 2:
            print(f'''your choice 
            {paper}
            computer choose
            {paper}
            Tied''')
        elif player_choice == computer == 3:
            print(f'''your choice 
            {scissor}
            computer choose
            {scissor}
            Tied''')
        elif player_choice>3 :
            print("I don't understand. run code again")
            break
        elif str(player_choice)=='quit':
            print('goodbye')
            break
    elif (start_game)=='quit':
        print('goodbye')
        break
    else :
        print('again run code')
        break



