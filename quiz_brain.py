class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def next_question(self) -> str:
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return self.current_question.text
        # self.check_answer(user_answer)

    def check_answer(self) -> str:
        print(self.current_question.answer.lower())
        return self.current_question.answer.lower() + 1
