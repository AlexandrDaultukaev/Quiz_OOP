class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_q(self):
        self.question_number += 1

    def ask_q(self):
        text = self.question_list[self.question_number].text
        ans = self.question_list[self.question_number].answer
        if input(text+"(True/False)").title() == ans:
            print("You got it!")
            return False
        else:
            print("Nope...")
            return True

