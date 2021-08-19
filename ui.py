from tkinter import *

class QuizUI:

    def __init__(self):
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
        self.window.mainloop()

    def true_click(self):
        print("T")

    def false_click(self):
        print("F")

q = QuizUI()
