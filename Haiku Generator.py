from ai import call_gpt

def main():
    name = input("Enter your name: ")
    topic = input("Enter a topic: ")  
    print("Creating your haiku...")
    haiku=call_gpt(f"create haiku with {name} and {topic}")
    print(haiku)


if __name__ == "__main__":
    main()
