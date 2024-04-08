class TriviaQuiz:
    def __init__(self):
        self.questions = {
            "What is the capital of France?": {"A": "Paris", "B": "London", "C": "Berlin", "D": "Rome"},
            "Which planet is known as the Red Planet?": {"A": "Mars", "B": "Venus", "C": "Jupiter", "D": "Saturn"},
            "Who painted the Mona Lisa?": {"A": "Leonardo da Vinci", "B": "Pablo Picasso", "C": "Vincent van Gogh", "D": "Claude Monet"}
        }
        self.score = 0

    def display_question(self, question, options):
        print(question)
        for key, value in options.items():
            print(key + ": " + value)
        answer = input("Your answer (A/B/C/D): ").upper()
        return answer

    def play_game(self):
        print("Welcome to the Trivia Quiz Challenge!")
        print("Answer the following questions:")
        for question, options in self.questions.items():
            user_answer = self.display_question(question, options)
            correct_answer = [key for key, value in options.items() if value == options['A']][0]
            if user_answer == correct_answer:
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect! The correct answer is:", options['A'])
            print()
        print("Quiz Over!")
        print("Your final score is:", self.score)

if __name__ == "__main__":
    quiz = TriviaQuiz()
    quiz.play_game()
