import random
secret = 22

guess = 10

# while guess != secret:
#     print("Try to guess the secret number!")
#     guess = int(input('Guess a number: '))
#     if guess == secret:
#         print('Congratulations')
#         break
#     else:
#         pass
#     print('Ponovno ugibaj')

secret = 18

lower_guess = 0
upper_guess = 20
guess = 10
for i in range(5):
    if secret > guess:
        lower_guess = guess
        print('večji od {}'.format(guess))
        guess = guess + round((upper_guess - guess)/2)
    elif secret == guess:
        print('Bravo')
        break
    elif secret < guess:
        upper_guess = guess
        print('Manjsi od {}'.format(guess))
        guess = lower_guess + round((guess - lower_guess)/2)


