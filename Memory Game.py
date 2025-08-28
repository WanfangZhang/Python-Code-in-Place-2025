import random

# Constants
NUM_PAIRS = 3


def create_truth_list():
    truth = []
    for i in range(NUM_PAIRS):
        truth.append(i)
        truth.append(i)
    return truth

def create_displayed_list(length):
    return ['*'] * length

def get_valid_index(displayed, taken_indices):
    while True:
        index_input = input("Enter an index: ")
        if not index_input.isdigit():
            print("Not a number. Try again.")
            continue
        index = int(index_input)
        if index < 0 or index >= len(displayed):
            print("Invalid index. Try again.")
        elif displayed[index] != '*':
            print("This number has already been matched. Try again.")
        elif index in taken_indices:
            print("You entered the same index twice. Try again.")
        else:
            return index

def play_turn(truth, displayed):
    print(displayed)
    index1 = get_valid_index(displayed, [])
    index2 = get_valid_index(displayed, [index1])

    if truth[index1] == truth[index2]:
        displayed[index1] = truth[index1]
        displayed[index2] = truth[index2]
        print("Match!")
        clear_terminal()

    else:
        print("Value at index", index1, "is", truth[index1])
        print("Value at index", index2, "is", truth[index2])
        print("No match. Try again.")
        input("Press Enter to continue...")
        clear_terminal()

def main():
    truth = create_truth_list()
    random.shuffle(truth)
    displayed = create_displayed_list(len(truth))

    while '*' in displayed:
        play_turn(truth, displayed)

    print(displayed)
    print("Congratulations! You won!")


def clear_terminal():
    for i in range(20):
      print('\n')

if __name__ == '__main__':
    main()
