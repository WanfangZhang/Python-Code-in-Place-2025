SET_PLAYER = 0

def main():
    if SET_PLAYER == 0:
        turns = 0
    else :
        turns = 1
    stones = 20
    while stones > 0:
        print("There are", stones, "stones left.")
        if turns % 2 == 0: 
            player = "Player 1 "
            one_or_two = int(input(player + "would you like to remove 1 or 2 stones? "))
            while one_or_two > 2 or one_or_two < 1:
                one_or_two = int(input("Please enter 1 or 2: "))
            print()
        else :
            player = "Player 2 "
            one_or_two = int(input(player + "would you like to remove 1 or 2 stones? "))
            while one_or_two > 2 or one_or_two < 1:
                one_or_two = int(input("Please enter 1 or 2: "))
            print()
        stones = stones - one_or_two
        turns = turns + 1
    if turns % 2 == 0 and stones == 0: 
        print("Player 1 wins!")
    elif turns % 2 == 1 and stones == 0: 
        print("Player 2 wins!")
    else:
        print("Game over")

if __name__ == '__main__':
    main()
