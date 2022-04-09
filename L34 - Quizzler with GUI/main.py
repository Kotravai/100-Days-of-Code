from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for qa in question_data:
    q = Question(qa["question"], qa["correct_answer"])
    question_bank.append(q)


quiz = QuizBrain(question_bank)
quiz_ui= QuizInterface(quiz)
# while quiz.still_has_question():
#     quiz.next_question()

# print ("You've completed the quiz!")
# print (f"Your final score was: {quiz.score} / {quiz.question_number}")