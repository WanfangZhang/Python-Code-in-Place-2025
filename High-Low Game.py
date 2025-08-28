import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    score = 0
    for i in range(NUM_ROUNDS):
        print("Round",i+1)
        my_num = random.randint(1,100)
        pc_num = random.randint(1,100)
        print("Your number is",my_num)
        answer = input("Do you think your number is higher or lower than the computer's?: ")
        if (answer == "lower" and my_num<pc_num) or (answer == "higher" and my_num>pc_num):
            print("You were right! The computer's number was",pc_num)
            score = score + 1
            print("Your score is now",score)
        else:
            print("Aww, that's incorrect. The computer's number was",pc_num)
            print("Your score is now",score)
        print()
    print("Thanks for playing!")



if __name__ == "__main__":
    main()
