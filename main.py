from os import remove
from random import randint

# initial game
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10 ]
score=0
def pick() -> int:
    if cards:
        return cards.pop(randint(0 , len(cards) - 1))
    else:
        raise ValueError("No more cards to pick from")

gameon = True
more = True
while gameon:
    print(flush=True)
    answer = input('Do you want to play a game of Blackjack? (y) or (n): ')
    if answer == 'y':
        gameon = True
    elif answer == 'n':
        print("That's bad luck!")
        break
    else:
        print('invalid entry!')

    computer = [pick() , pick()]
    user = [pick() , pick()]

    while more:
        user_score = sum(user)
        if user_score > 21:
            break
        pc_score = sum(computer)
        print(f'     Your cards: {user}, current score: {user_score}')
        print(f"     Computer's first card: {computer[0]}")
        answer = input(f"Type 'y' to get another card, type 'n' to pass: ")
        if answer == 'y':
            more = True
            user.append( pick() )
        elif answer == 'n':
            more = False
        else :
            print('invalid entry!')

    print(f'    Your final hand: {user}, final score: {user_score}')
    print(f'    Your final hand: {computer}, final score: {pc_score}')

    # Process result
    if user_score > 21:
        print("You went over. You lose 😭")
        score += -1 if score>0 else 0
    elif user_score > pc_score:
        print('Opponent went over. You win 😁')
        score += 1
    elif user_score < pc_score:
        print("You lose 😤")
    else:
        print('draw')


print(f'Your score: {score} !')