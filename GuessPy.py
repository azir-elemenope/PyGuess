import random # Import the random module for generating random numbers.
# colors
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
reset = '\033[0m'
italics = '\033[3m'


print(f"{yellow}╔════════════════════════════╗")
print("║      ██████╗ ██╗   ██╗     ║")
print("║      ██╔══██╗╚██╗ ██╔╝     ║")
print("║      ██████╔╝ ╚████╔╝      ║")
print("║      ██╔═══╝   ╚██╔╝       ║")
print("║      ██║        ██║        ║")
print("║      ╚═╝        ╚═╝        ║")
print("║       P Y G U E S S        ║")
print("╚════════════════════════════╝")
print(f" THINK SMART, GUESS WISELY! {reset}")


# Game introduction and explanation
print(f"{italics}\nWelcome to PyGuess, an enchanting game of logic and deduction where Python becomes the detective!\nDeep in the heart of the Algorithmic Realm, a curious Python thrives on solving mysteries of hidden numbers.\nYou, the Keeper of Secrets, must guide it by answering a series of pre-set questions, helping it unravel the puzzle step by step.\nPython will work tirelessly, combining clues to deduce the secret number you've chosen, while you marvel at its analytical prowess.\nWill you be the Keeper who outwits Python, or will Python prove to be the ultimate number sleuth? Let’s find out!{reset}")


def input_yn(prompt):
# Function to handle yes/no questions from the user
  while True:
      ans = input(prompt).strip().lower() # Get input from the user, strip any whitespace, and convert it to lowercase
      if ans == 'yes':
          return True
      elif ans == 'no':
          return False
      else:
      # If the input is invalid, prompt the user to respond with 'yes' or 'no'
          print(f"{italics}{red}Wait a second—that doesn’t seem right!\nPlease respond with 'yes' or 'no' when asked that question.{reset}")
          continue


def input_int(prompt, min_val=None, max_val=None):
# Function to get an integer input from the user with optional range validation


  while True:
      try:
          num = int(input(prompt).strip()) # Trying to convert into an integer
          if (min_val is None or num >= min_val) and (max_val is None or num <= max_val):  # To check if the number is within the specified range, if applicable
              return num # Return the valid integer
          print(f"Enter a number between {min_val} and {max_val}.")
          if int(prompt) > min_val or int(prompt) < max_val:
              print(f"{italics}{red}Whoops! That number is outside the valid range.\nPlease choose a number within the specified limits to help Python narrow down its guess.\nLet’s stay within the boundaries and try again!{reset}")
              continue
      except ValueError: # Handles non-integer inputs
          print(f"{italics}{red}Oops! That’s not a number Python can work with.\nPlease enter an integer between {min_val} and {max_val} to continue.\nPython’s logic only works with numbers, so let’s give it a try again!{reset}")
          continue


def is_prime(n):
# Function to check if a number is a prime
  if n < 2: # Numbers less than 2 cannot be prime.
      return False
  for i in range(2, int(n**0.5) + 1): # Loop through potential divisors up to the square root of n.
      if n % i == 0:
          return False # If n is divisible by i, it is not a prime number
  return True # If no divisors are found, the number is prime


def is_square(n): # Function to check if a number is a perfect square
  r = int(n**0.5) # Check the square root of a number
  return r ** 2 == n # Check if the square root of the root equals the number


def is_cube(n): # Function to check if a number is a perfect cube
  r = int(round(n**(1/3))) # Check the square root of a number
  return r ** 3 == n # Check if the cube root of the root equals the number


def filter_prime(nums, prime): # Function to filter numbers based on primality
  return [n for n in nums if is_prime(n) == prime] # To keep only the prime of non-prime numbers


def filter_even(nums, even): # Function to filter numbers based on even/odd property
  return [n for n in nums if (n % 2 == 0) == even] # To keep even or odd numbers


def filter_divisible(nums, divisor): # Function to filter numbers divisible by a specific divisor
  return [n for n in nums if n % divisor == 0] # To keep numbers divisible by a specific divisor


def filter_digit_props(nums, s_sum, s_diff, s_prod): # Function that checks if a number satisfies the given digit properties
  def matches_props(n): # Check if the sum of the digits of n equals s_sum, the difference of the digits of n equals s_diff, and if the product of digits is either 0 or equals s_prod
      return (digit_sum(n) == s_sum and
              digit_diff(n) == s_diff and
              (s_prod == 0 or digit_prod(n) == s_prod))
  return [n for n in nums if matches_props(n)] # Return a list of numbers from nums where matches_props evaluates to True


def filter_zero(nums, zero_count, zero_pos): # Function to filter numbers based on the number of zeros and the position of the first zero
  def matches_zero(n):
      s = str(n) # Convert the number to a string to count zeros and find positions of ‘0’
      return s.count('0') == zero_count and (s.find('0') + 1 == zero_pos)
  return [n for n in nums if matches_zero(n)] # Return a list of numbers from nums that match the given zero_count and zero_pos criteria


def filter_length(nums, length): # Function to filter numbers based on their length (number of digits)
  return [n for n in nums if len(str(n)) == length] # Return a list of numbers whose length (number of digits) matches the given length


def digit_sum(n): # Function to calculate the sum of digits of a number
  return sum(int(d) for d in str(n)) # Convert the number to a string and sum the integer values of each digit


def digit_diff(n): # Function to calculate the absolute difference between the first and last digits of a number
  s = str(n) # Convert the number to a string to extract the first and last digits
  return int(s[0]) - int(s[-1]) # Calculate the absolute difference between the first and last digits


def digit_prod(n): # Function to calculate the product of digits of a number
  p = 1 # Initialize the product as 1
  for d in str(n): # Multiply the product by each digit of the number
      p *= int(d)
  return p




def random_guess(min_val, max_val, exclude): # Function to make a random guess within a specified range.
  while True: # Loop to keep trying until a valid guess is made.
      guess = random.randint(min_val, max_val) # Generate random number in the range.
      if guess not in exclude: # Ensure the guessed number is not in the exclusion list.
          return guess # Return valid guess.


def guess():
  print(f"{italics}\nIt’s great to know you’re interested!\nGo ahead and think of a number—don’t tell me, just keep it in your mind.\nI’ll use my skills to guess it, step by step.\nLet’s get started!{reset}")


  # Step 1: Define the range
  low = input_int("\nEnter the minimum value: ", 0, 1000000) # Get the minimum value of value.
  high = input_int("Enter the maximum value: ", low, 1000000) # Get the maximum value.
  nums = list(range(low, high + 1)) # Create a list of all numbers in the range.


  def check(a): # Nested helper function to check the length of the list.
      if len(a) == 1: # Conclude the game if only one number remains.
          return True
      if len(a) == 0: # Indicate something went wrong if no numbers remain (invalid state).
          return False


  def validate(secret_number, nums):
      # Validate if the user's secret number satisfies all conditions.
      if secret_number in nums:
          return True
      return False


  def guessed_number(nums):
      if len(nums) == 1:
          print(f"The number is {nums[0]}!")
          conclusion = input_yn(f"{italics}\nDid I get the answer right? (yes/no): \n{reset}")
          if conclusion:
              print(f"{italics}{green}Eureka! Python cracked the code—it was {nums[0]} all along!\nWhat a brilliant display of deduction!{reset}")  # Print statement for successful answers
          elif not conclusion:
              secret_number = input_int(f"{italics}Then, what is the secret number?: {reset}")  # If Python’s answer is incorrect, print to ask for the secret number
              if validate(secret_number, nums):
                  print(f"{italics}{yellow}Python admits defeat this time—your number was {secret_number}.\nWell played, Keeper of Secrets!{reset}")
              else:
                  print(f"{italics}{red}Wait a second! The number {secret_number} doesn't match the clues provided earlier.\nNo cheating, Keeper of Secrets!\nAs a punishment, you are banished from this land.{reset}")
                  exit()
          print(f"{italics}\nBravo, Keeper of Secrets!\nThe game has come to an end.\nWhether Python cracked the code or you held your ground, it’s the journey of logic and deduction that truly matters.\nThank you for playing PyGuess and sharpening your problem-solving skills with us.\nWe hope to see you again in the Algorithmic Realm for another round of intriguing fun.\nUntil next time, keep your secrets safe and your logic sharper!{reset}")  # Print statement to conclude the game.
          exit()


      elif len(nums) == 0:
          print(f"{italics}{red}Uh-oh! It seems no numbers fit the conditions you provided.\nPlease double-check your answers and make sure everything is accurate.\nOnce you're certain, try again and we'll get back on track!{reset}")
          exit()


  # Prime Number Check
  if input_yn("Is the number prime? (yes/no): "): # Ask the user if the number is prime or not
      nums = filter_prime(nums, True) # If prime number, filter out non-prime numbers
  else: # If not a prime number, filter out prime numbers
      nums = filter_prime(nums, False)
      guessed_number(nums) # Check if only one number remains after filtering


      is_even = input_yn("Is the number even? (yes/no): ") # Ask if the number is even
      if is_even:
          nums = filter_even(nums, True) # If even number, filter out odd numbers
          guessed_number(nums) # Check if only one number remains after filtering
      else:
          nums = filter_even(nums, False) # If odd number, filter out even numbers


      # Divisibility check of the number
      divisors = [3, 4, 5, 7, 8, 9] if is_even else [3, 5, 7, 9, 11, 13] # For even numbers, check divisibility by 3,4,5,7,8, and 9. For odd numbers, check divisibility by 3,5,7,9,11, and 13.
      for divisor in divisors:
          if input_yn(f"Is the number divisible by {divisor}? (yes/no): "): # Filter the list accordingly when known that the number is divisible by the given divisor
              nums = filter_divisible(nums, divisor)
              guessed_number(nums) # Check if one number remains after filtering


      # Square/Cube Checks
      if input_yn("Is it a perfect square? (yes/no): "):
          nums = [n for n in nums if is_square(n)] # Remain the perfect squares
          guessed_number(nums) # Check if one number remains after filtering
      if input_yn("Is it a perfect cube? (yes/no): "):
          nums = [n for n in nums if is_cube(n)] # Remain the perfect cubes
          guessed_number(nums) # Check if one number remains after filtering
  if len(str(low)) == len(str(high)):  # if min and max are of same number of digits, length of the number is the same as the two
      num_len = len(str(low))
      guessed_number(nums)
  elif len(str(low)) != len(str(high)):  # if min and max have different number of digits
      if high < 10:  # Check if the range of possible numbers is less than 10.
          num_len = 1  # Only one digit if the highest possible number is less than 10.
          nums = filter_length(nums, num_len)  # Filters to include only 1-digit numbers.
          guessed_number(nums)  # Check if only one number remains.


      elif high >= 10:
          num_len = input_int("How many digits does the number have?: ", 1, len(str(nums[-1])))
          nums = filter_length(nums, num_len)
          guessed_number(nums)


  # Digit Properties
  else:
      if len(str(low)) == len(str(high)): # if min and max are of same number of digits, length of the number is the same as the two
          num_len = len(str(low))
      elif len(str(low)) != len(str(high)): # if min and max have different number of digits
          num_len = input_int("How many digits does the number have?: ", 1, len(str(nums[-1]))) # Ask how many digits the number has.
          nums = filter_length(nums, num_len) # Filter numbers to match the specified digit length.
          guessed_number(nums) # Check if only one number remains.


  if num_len == 1:
      thriple = input_int("What is the number obtained by triple your number?: ",0,27)
      nums = [n for n in nums if 3*n == thriple]
      guessed_number(nums)


  elif num_len > 1: # Additional digit-related properties questions.
      s_sum = input_int("What is the sum of its digits?: ", 0, 54) # Ask for the sum of the digits.
      s_diff = input_int("What is the difference between the first and last digit?: ", -8,9) # Ask for the difference between the first and last digit.
      s_prod = input_int("What is the product of its digits?: ", 0, 531441)
      nums = filter_digit_props(nums, s_sum, s_diff, s_prod)
      guessed_number(nums) # Ask for the product of the digits.


# Handle special case where all digit properties point to zero.
      if s_sum == 0 and s_diff == 0 and s_prod == 0:
          nums = [0]
          guessed_number(nums) # Check if the result is consistent.


      # Handle Zero Details
      if s_prod == 0: #special case
          zero_count = input_int("How many zeroes does the number have?: ", 1, len(str(high))) # Ask how many zeros are present.
          zero_pos = input_int("Where is the first zero located? (1-based index): ", 1, len(str(nums[-1]))) # Ask where the first zero is located.
          nums = filter_zero(nums, zero_count, zero_pos) # Filter numbers based on the number of zeros and positions.
          guessed_number(nums) # Check if only one number remains.


      # Higher/Lower Dynamic Guesses
  while len(nums) > 1:
      guess = random.randint(low, high)  # To make a random guess
      if guess in nums:  # To skip if already guessed
          continue


      if input_yn(f"Is the number higher than {guess}? (yes/no): "):  # To adjust range based on user feedback
          low = max(low,guess + 1)  # Adjust the lower bound to exclude the guess and all numbers less than or equal to guess.
          nums = [n for n in nums if n > guess]  # Filter the list to keep only numbers greater than the guess.
      else:
          high = min(high,guess - 1)  # Adjust the upper bound to exclude the guess and all numbers greater than guess.
          nums = [n for n in nums if n <= guess]  # Filter to keep only numbers less than or equal to guess.
      guessed_number(nums)
  return check(nums)


print(f"{italics}\nGreetings, Keeper of Secrets!\n") # Print statement for introductory message.
print("Welcome to PyGuess, where numbers come alive, and deduction meets fun!\nThink of a number and hold it tight—it’s your mission to keep it hidden.\nPython, the clever problem-solver, will try to guess your number based on your responses.")
game_start = input_yn(f"\nPrepare for a thrilling battle of wits and logic as Python narrows down possibilities one clue at a time.\nRemember to answer honestly and clearly to give Python a fair chance.\nLet’s embark on this numerical adventure together—ready to begin? (yes/no): {reset}") # Prompt the user to begin the game by asking a ‘yes’ or ‘no’ response.


if game_start: # Check if the game is starting
  answer = guess() # Call the function to start guessing the number


elif not game_start:
  print(f"{italics}\nAh, the Keeper of Secrets decides to remain mysterious!\nThat’s perfectly fine—Python will wait patiently for the day you’re ready to embark on this adventure.\nUntil then, the Algorithmic Realm remains open, should you choose to return.\nFarewell, and may your secrets stay hidden!{reset}") # Print statement if the user does not want to start the game
