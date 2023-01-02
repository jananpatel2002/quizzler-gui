from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        self.window.wm_minsize(height=500, width=300)

        self.score_label = Label(text="Score: 0 ", bg=THEME_COLOR, font=("Arial", 9, "bold"))
        self.score_label.grid(row=0, column=1, pady=20, padx=20)
        self.canvas = Canvas(height=250, width=300, highlightthickness=0, bg="white")
        self.canvas_text = self.canvas.create_text(150, 125, font=FONT,
                                                   text="[Placeholder]",
                                                   width=260)
        self.canvas.grid(columnspan=2, row=1, column=0)

        self.false_photo = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.false_photo, highlightthickness=0, command=self.false_clicked)
        self.false_button.grid(row=2, column=0, pady=20)

        self.true_photo = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.true_photo, highlightthickness=0, command=self.true_clicked)
        self.true_button.grid(row=2, column=1, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        question_text = self.quiz.next_question()
        self.canvas.itemconfig(self.canvas_text, text=question_text)

    def true_clicked(self):
        if self.quiz.check_answer() == "true":
            self.update_scoreboard()
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

    def false_clicked(self):
        if self.quiz.check_answer() == "false":
            self.update_scoreboard()
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

    def update_scoreboard(self):
        self.quiz.score += 1
        self.score_label.config(text=f"Score: {self.quiz.score}")
