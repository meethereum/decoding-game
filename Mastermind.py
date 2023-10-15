import random

print('Welcome to Mastermind. This is a game where your intuition and logic '
      'will be tested on the basis of a simple decoding game which '
      'involves cracking a 4-digit secret code.\nYou will be given '
      '10 chances to guess the code, but there will be indicators '
      'telling you to what extent your guess is correct:\n'
      ':) means one of your guesses is correct and correctly placed.\n'
      ':| means one of your guesses is correct but placed incorrectly.\n'
      ':( means one of your guesses is completely wrong.\n'
      'You will get 4 indicators for every guess. Try not to repeat numbers. Cheers!\n')

code = str(random.randint(1000, 9999))
i = 0

while i < 10:
    i += 1
    user_guess = input('Enter your guess to crack the code: ')

    if user_guess == code:
        print("CONGRATULATIONS. YOU CRACKED THE CODE TO BECOME THE MASTERMIND!")
        break

    correctList = [1 if user_guess[j] == code[j] else 0 for j in range(4)]
    partially_correctList = [1 if user_guess[j] in code and user_guess[j] != code[j] else 0 for j in range(4)]

    correct_count = sum(correctList)
    partially_correct_count = sum(partially_correctList)
    wrong_count = 4 - correct_count - partially_correct_count

    feedback = ':) ' * correct_count + ':| ' * partially_correct_count + ':( ' * wrong_count
    print(feedback, i)

if i == 10:
    print('GAME OVER!')

print('The correct secret code is ' + code)
