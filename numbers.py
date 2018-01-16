# Define secret number
secret_num = 3

# Get users input
guess = int(input('Try to guess my secret number: '))

# Correct / Wrong answer info
if guess == secret_num:
    print('You are right! My number was {}'.format(secret_num))
else:
    print('Sorry, you\'ve missed it')