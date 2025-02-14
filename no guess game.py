import random
guess=random.randint(1,21)
print('Hi can you guess the number between 1 to 21')
#print(guess)
for i in range(5,0,-1):
    n=int(input('Guess the number:'))
    if n==guess:
        print('congrats you are guessing correct number')
        break
    else:
        print(f'Oops you are guessing incorrect number {i-1} life left')
if i==1 and guess!=n:
    print(f'You lost! the game The correct number was:{guess}')

