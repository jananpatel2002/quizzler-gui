from tkinter import *
from quiz_brain import QuizBrain
from tkinter import messagebox

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
        self.on_button_clicked("true")

    def false_clicked(self):
        self.on_button_clicked("false")

    def on_button_clicked(self, status):
        if self.quiz.check_answer() == status:
            self.update_scoreboard()
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.disable_buttons()
        self.window.after(ms=1000, func=self.change_canvas_to_white)  # This also changes the question if available

    def update_scoreboard(self):
        self.quiz.score += 1
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def change_canvas_to_white(self):
        self.enable_buttons()
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.get_next_question()
        else:
            messagebox.showinfo(title="Quiz finished",
                                message="The quiz has been finished, you may now exit out from the app")

    def disable_buttons(self):
        self.true_button["state"] = "disabled"
        self.false_button["state"] = "disabled"

    def enable_buttons(self):
        self.true_button["state"] = "normal"
        self.false_button["state"] = "normal"
