import random

def main():
    num1 = input("How many sides does your dice have? ")
    num1 = int(num1)
    die1 = random.randint(1, num1)
    print("Your roll is " + str(die1))

if __name__ == '__main__':
    main()
