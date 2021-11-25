def main():
#import all packages at the beginning of the script
  import random

  dice_rolls = 2
  dice_sum = 0

  #level of indentation defines what is and is not in the loop
  for i in range(0,dice_rolls):
    
    #the beginning and the end of rhe (1,6) range are inclusive
    roll = random.randint(1,6)
    dice_sum = dice_sum + roll
    print(f'You rolled a {roll}')

  print(f'Your dice roll total is {dice_sum}')


if __name__== "__main__":
  main()
