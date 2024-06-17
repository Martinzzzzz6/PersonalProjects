from question_model import Question
from data import question_data
from quiz_brain import Quiz

question_bank = []

for question in question_data:
    q = question["text"]
    a = question["answer"]

    new_question = Question(q,a)

    question_bank.append(new_question)

quiz = Quiz(question_bank)

while quiz.continue_quiz and quiz.question_number < len(quiz.question_l):
    quiz.next_question()