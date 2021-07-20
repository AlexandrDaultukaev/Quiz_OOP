class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_q(self):
        self.question_number += 1

    def ask_q(self):
        text = self.question_list[self.question_number].text
        ans = self.question_list[self.question_number].answer
        if input(text+"(True/False)").title() == ans:
            self.score += 1
            print(f"You got it!\nScore: {self.score}")
            return False
        else:
            print(f"Nope...\nScore: {self.score}")
            return True

