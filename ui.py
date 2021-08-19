from tkinter import *

class QuizUI:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz APP")
        self.window.maxsize(500, 600)
        self.window.minsize(500, 600)
        self.bg_canvas = Canvas(width=500, height=600, bg="#375362", highlightthickness=0)
        true_img = PhotoImage(file="./images/true.png")
        self.bg_canvas.create_image(350, 470, image=true_img)
        false_img = PhotoImage(file="./images/false.png")
        self.bg_canvas.create_image(150, 470, image=false_img)
        self.bg_canvas.pack()
        self.window.config(bg="black")
        self.canvas = Canvas(width=350, height=350, bg="white", highlightthickness=0)
        self.canvas.place(x=75, y=45)
        self.score = self.bg_canvas.create_text(125, 20, text="score: 0", font=("Arial", 20, "normal"), fill="white")

        self.window.mainloop()


q = QuizUI()
