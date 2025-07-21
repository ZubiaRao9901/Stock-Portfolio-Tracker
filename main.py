import random

# Hangman ASCII stages
hangman_stages = [
    '''
     -----
     |   |
     |   O
     |  /|\\
     |  / \\
     |
    ========
    ''',
    '''
     -----
     |   |
     |   O
     |  /|\\
     |  / 
     |
    ========
    ''',
    '''
     -----
     |   |
     |   O
     |  /|\\
     |  
     |
    ========
    ''',
    '''
     -----
     |   |
     |   O
     |  /|
     |  
     |
    ========
    ''',
    '''
     -----
     |   |
     |   O
     |   |
     |  
     |
    ========
    ''',
    '''
     -----
     |   |
     |   O
     |   
     |  
     |
    ========
    ''',
    '''
     -----
     |   |
     |   
     |   
     |  
     |
    ========
    '''
]

# Color formatting for terminal output
def colored(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

# Dictionary of categories with (word, hint) pairs
word_bank = {
    "Animal": [
        ("penguin", "A flightless bird found in Antarctica"),
        ("elephant", "The largest land animal with a trunk"),
        ("kangaroo", "An Australian marsupial that hops"),
        ("dolphin", "An intelligent sea mammal"),
        ("chameleon", "An animal that changes its color"),
    ],
    "Technology": [
        ("transmission", "Used in vehicles to transfer power"),
        ("codealpha", "A tech startup name or security term"),
        ("algorithm", "Step-by-step problem-solving instructions"),
        ("firewall", "Protects networks from unauthorized access"),
        ("cybersecurity", "Protection of computer systems from digital attacks"),
    ],
    "Nature Lover": [
        ("selenophile", "A person who loves the moon"),
        ("biophilia", "Love for all living things"),
        ("rainforest", "A dense forest with heavy rainfall"),
        ("avalanche", "A mass of snow falling down a mountain"),
        ("sunflower", "A plant that turns toward the sun"),
    ],
    "Space": [
        ("astronaut", "A person trained for space travel"),
        ("nebula", "A cloud of gas and dust in space"),
        ("supernova", "A powerful explosion of a star"),
        ("satellite", "Orbits a planet to collect data"),
        ("blackhole", "A region where gravity is so strong, nothing escapes"),
    ],
    "Food": [
        ("biryani", "A spicy South Asian rice dish"),
        ("lasagna", "An Italian layered pasta dish"),
        ("sushi", "A Japanese dish with rice and seafood"),
        ("pancake", "Flat, round breakfast food, often with syrup"),
        ("croissant", "A buttery, flaky French pastry"),
    ],
    "Emotions": [
        ("happiness", "A state of great joy"),
        ("fear", "A reaction to danger"),
        ("curiosity", "The desire to know or learn something"),
        ("jealousy", "An emotion of envy or insecurity"),
        ("gratitude", "The feeling of thankfulness"),
    ],
    "Occupations": [
        ("engineer", "Designs or builds structures or machines"),
        ("teacher", "Educates students"),
        ("doctor", "Cares for the sick and injured"),
        ("astronaut", "Trained for space missions"),
        ("chef", "Prepares meals in restaurants"),
    ],
    "Geography": [
        ("pakistan", "A country in South Asia"),
        ("everest", "The tallest mountain on Earth"),
        ("sahara", "The world’s largest hot desert"),
        ("amazon", "The largest rainforest in the world"),
        ("nile", "A famous African river"),
    ]
}

def play_game():
    # Randomly select a category and word
    category = random.choice(list(word_bank.keys()))
    word, hint = random.choice(word_bank[category])
    word = word.lower()
    guessed_word = ['_'] * len(word)
    attempts = 6
    guessed_letters = set()
    guessed_words = set()

    print("\n🎮 Welcome to the Hangman Game!")
    print(f"\n📂 Category: {colored(category, 96)}")
    print(f"💡 Hint: {colored(hint, 94)}")

    # Game loop
    while attempts > 0 and '_' in guessed_word:
        print(hangman_stages[6 - attempts])
        print("Word:", ' '.join(guessed_word))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print(f"Attempts left: {attempts}")
        guess = input("Enter a letter or guess the full word: ").lower().strip()

        if not guess.isalpha():
            print(colored("🚫 Invalid input! Please enter only letters.", 91))
            continue

        if len(guess) == 1:
            if guess in guessed_letters:
                print(colored("⚠️ You've already guessed that letter.", 93))
                continue
            guessed_letters.add(guess)

            if guess in word:
                for i in range(len(word)):
                    if word[i] == guess:
                        guessed_word[i] = guess
                print(colored("✅ Correct guess!", 92))
            else:
                attempts -= 1
                print(colored("❌ Wrong guess!", 91))
        else:
            if guess in guessed_words:
                print(colored("⚠️ You've already guessed that word.", 93))
                continue
            guessed_words.add(guess)

            if guess == word:
                guessed_word = list(word)
                print(colored("🎯 Correct! You guessed the full word!", 92))
                break
            else:
                attempts -= 1
                print(colored("❌ Incorrect word guess!", 91))

    # Final outcome
    print(hangman_stages[6 - attempts])
    if '_' not in guessed_word:
        print(colored(f"\n🎉 Congratulations! You guessed the word: {word}", 92))
    else:
        print(colored(f"\n💀 Game Over! The correct word was: {word}", 91))

# Game replay loop
while True:
    play_game()
    again = input("\n🔁 Do you want to play again? (y/n): ").strip().lower()
    if again != 'y':
        print("👋 Thanks for playing! Goodbye.")
        break
