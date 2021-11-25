def main():
  #import all packages at the beginning of the script
  import random

  #dice_rolls = 2
  #note that the value a user inputs defaults to a string
  #need to encompass the "input" command into an int()
  dice_rolls = int(input('How many dice do you want to role?'))
  dice_size = int(input('How many sides are the dice?'))
  dice_sum = 0


  #level of indentation defines what is and is not in the for" loop
  for i in range(0,dice_rolls):
    
    #the beginning and the end of rhe (1,6) range are inclusive
    roll = random.randint(1,dice_size)
    dice_sum = dice_sum + roll      #alternatively: dice_sum += roll

    if roll == 1:
      print(f'You rolled a {roll}! Critical Fail!')
    elif roll == dice_size:
      print(f'You rolled a {roll}! Critical Success!')
    else:
      print(f'You rolled a {roll}')

  print(f'Your dice roll total is {dice_sum}')


if __name__== "__main__":
  main()
