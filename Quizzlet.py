def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    correct_count = 0
    total_questions = len(translations)

    for english, spanish in translations.items():
        answer = input("What is the Spanish translation for " + english + "?").strip().lower()
        if answer == spanish:
            print("That is correct!")
            correct_count += 1
        else:
            print("That is incorrect, the Spanish translation for " + english + " is " + spanish + ".")
        print()
    print("You got " + str(correct_count) + "/" + str(total_questions) + " words correct, come study again soon!")          




if __name__ == '__main__':
    main()
