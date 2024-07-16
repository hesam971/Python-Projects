class UserQuestions:
    def __init__(self):
        self.game_over = False
        self.point = 0
        self.question = 0

    def analyze_questions(self, user_data):
        for key in user_data:
            print(key["text"])
            self.question += 1
            answer = input(f"Q.{self.question} what is your answer? Type 'True' or 'False' ").lower()
            if answer == key["answer"].lower():
                self.point += 1
                print("You got it right! ")
            else:
                print("That is wrong! ")
            print(f"your current score is {self.point}/{self.question}")