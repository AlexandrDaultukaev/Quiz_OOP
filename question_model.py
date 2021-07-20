class Question:
    def __init__(self, question="", answer=""):
        if question != "" and answer != "":
            self.text = question
            self.answer = answer

    def print_dict(self):
        print(f"{self.text} {self.answer}")
