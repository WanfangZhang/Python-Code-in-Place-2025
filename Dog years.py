# Each year for a human is like 7.18 years for a dog
DOG_YEARS_MULTIPLIER = 7.18  

def main():
    num1 = input("Enter an age in calendar years: ")
    num1 = int(num1)
    total = num1 *7.18
    print("That's " + str(total) + " in dog years!")


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
