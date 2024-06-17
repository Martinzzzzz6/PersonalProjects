import random
class Quiz:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_l = question_list
        self.continue_quiz = True
        self.score = 0


    def next_question(self):
        if self.question_number < len(self.question_l):
            question_number = random.randint(0, len(self.question_l))
            current_question = self.question_l[question_number]
            self.question_number += 1
            user_answer = input(f"Q.{self.question_number}: {current_question.ques} (True/False)? \n")
            self.check_answers(user_answer, current_question.ans)
            print(f"Your score is: {self.score}/{self.question_number}")
        else:
            print("Quiz over")

    def check_answers(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You are right")
            self.score += 1
        else:
            print("You are wrong")
            self.continue_quiz = False
