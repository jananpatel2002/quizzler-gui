from ui import QuizInterface
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import html

question_bank = []
for question in question_data:
    question_text = html.unescape(question["question"])
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)
gui = QuizInterface(quiz_brain)

# while quiz_brain.still_has_questions():
#     question = quiz_brain.next_question()
#     gui.canvas.itemconfig(gui.canvas_text, text=question.text)

# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
