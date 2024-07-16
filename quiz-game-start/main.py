from data import question_data
from question_model import UserQuestions

question_model_user = UserQuestions()

#question_model_user.analyze_questions(question_data)

# with a function declaration

def ask_question(questions):
    question_number = 0
    right_answer = 0
    for key in questions:
        print(key["text"])
        question_number += 1
        answer = input(f"Q.{question_number} what is your answer? Type 'True' or 'False' ").lower()
        if answer == key["answer"].lower():
            right_answer += 1
            print("You got it right! ")
        else:
            print("That is wrong! ")
        print(f"your current score is {right_answer}/{question_number}")


ask_question(question_data)
