import random

class WordAssociationGame:
    def __init__(self):
        self.words = {
            "Apple": ["Pie", "Orange", "Banana", "Tree"],
            "Blue": ["Sky", "Green", "Red", "Yellow"],
            "Computer": ["Mouse", "Keyboard", "Monitor", "Book"]
        }
        self.score = 0

    def display_word(self, word, options):
        # Shuffle options
        random.shuffle(options)
        
        print("What word do you associate with '{}'?".format(word))
        for idx, option in enumerate(options, start=1):
            print("{}. {}".format(idx, option))
        choice = input("Enter the number corresponding to your choice: ")
        return int(choice)

    def play_game(self):
        print("Welcome to the Word Association Game!")
        print("Associate the following words with the correct options:")
        for word, options in self.words.items():
            # Ensure the word itself is in the options
            if word not in options:
                options.append(word)
            correct_index = options.index(word) + 1  # Index of the correct answer
            user_choice = self.display_word(word, options)
            if user_choice == correct_index:
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect! The correct answer is:", options[correct_index - 1])
            print()
        print("Game Over!")
        print("Your final score is:", self.score)

if __name__ == "__main__":
    game = WordAssociationGame()
    game.play_game()
