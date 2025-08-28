"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

def main():
    num1 = input("Enter a weight on Earth: ")
    num1 = float(num1)
    total = num1 *0.378
    print("The equivalent weight on Mars: " + str(total))

if __name__ == "__main__":
    main()
