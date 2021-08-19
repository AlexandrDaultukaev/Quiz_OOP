from tkinter import *
import quiz_brain


class QuizUI:

    def __init__(self, qb):
        self.qb = qb
        self.window = Tk()
        self.window.title("Quiz APP")
        self.window.maxsize(500, 600)
        self.window.minsize(500, 600)
        self.bg_canvas = Canvas(width=500, height=600, bg="#375362", highlightthickness=0)
        true_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")
        self.button_true = Button(image=true_img, borderwidth=0, highlightthickness=0, state="normal", command=lambda:
        self.true_click())
        self.button_false = Button(image=false_img, borderwidth=0, highlightthickness=0, state="normal", command=lambda:
        self.false_click())
        self.button_true.place(x=300, y=470)
        self.button_false.place(x=100, y=470)
        self.bg_canvas.pack()
        self.window.config(bg="black")
        self.canvas = Canvas(width=350, height=350, bg="white", highlightthickness=0)
        self.canvas.place(x=75, y=45)
        self.score = self.bg_canvas.create_text(125, 20, text="score: 0", font=("Arial", 20, "normal"), fill="white")
        self.text_question = self.canvas.create_text(150, 150, text=self.qb.ask_q(), font=("Arial", 10,
                                                                                           "normal"),
                                                     fill="black")

        self.window.mainloop()

    def new_score(self):
        self.bg_canvas.itemconfig(self.score, text=f"score: {self.qb.score}")
        if self.qb.score == 10:
            self.canvas.itemconfig(self.text_question, text="You win!")
            self.button_true["state"] = "disabled"
            self.button_false["state"] = "disabled"

    def true_click(self):
        if self.qb.score < 10:
            new_q = self.qb.check_q("True")
            if new_q == "You lose":
                self.button_true["state"] = "disabled"
                self.button_false["state"] = "disabled"
            self.new_score()
            self.canvas.itemconfig(self.text_question, text=new_q)

    def false_click(self):
        if self.qb.score < 10:
            new_q = self.qb.check_q("False")
            if new_q == "You lose":
                self.button_true["state"] = "disabled"
                self.button_false["state"] = "disabled"
            self.new_score()
            self.canvas.itemconfig(self.text_question, text=new_q)
