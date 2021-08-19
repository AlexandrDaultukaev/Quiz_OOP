import html

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.answer = None

    def next_q(self):
        self.question_number += 1
        self.score += 1

    def check_q(self, response):
        if response == self.answer:
            self.next_q()
            return self.ask_q()
        else:
            return "You lose"

    def ask_q(self):
        text = html.unescape(self.question_list[self.question_number].text)
        self.answer = self.question_list[self.question_number].answer
        return text.title()
        # self.next_q()
        # print(f"You got it!\nScore: {self.score}")
        # return False
        # else:
        #     print(f"Nope...\nScore: {self.score}")
        #     return True

