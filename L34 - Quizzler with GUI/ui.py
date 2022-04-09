from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score_label = Label(text="Score: 0", foreground="white", background=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.ques_text = self.canvas.create_text(
            100,
            50,
            width=240,
            text=self.get_next_question, fill=THEME_COLOR,
            font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        tick_image = PhotoImage(file="true.png")
        cross_image = PhotoImage(file="images/false.png")
        self.tick_button = Button(image=tick_image, command=self.tick_click)
        self.tick_button.grid(row=2, column=0)

        self.wrong_button = Button(image=cross_image, command=self.wrong_click)
        self.wrong_button.grid(row=2, column=1)

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question
            return self.canvas.itemconfig(self.ques_text, text=q_text)
        else:
            self.canvas.itemconfig(self.ques_text, text="You've reached the end of the quiz")
            self.tick_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def tick_click(self):
        if self.quiz.check_answer("True"):
            self.is_right()
        else:
            self.is_wrong()

    def wrong_click(self):
        if self.quiz.check_answer("False"):
            self.is_right()
        else:
            self.is_wrong()
        self.window.after(1000, self.get_next_question)

    def is_right(self):
        self.canvas.config(bg="green")
        self.score += 1
        self.score_label.config(text=f"Score: {self.score}")

    def is_wrong(self):
        self.canvas.config(bg="red")
        self.score_label.config(text=f"Score: {self.score}")