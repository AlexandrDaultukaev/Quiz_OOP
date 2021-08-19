import html

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.answer = None

    def increase_score(self):
        self.score += 1

    def check_q(self, response):
        if response == self.answer:
            self.increase_score()
            self.question_number += 1
            return True
        else:
            self.question_number += 1
            return False

    def ask_q(self):
        text = html.unescape(self.question_list[self.question_number].text)
        self.answer = self.question_list[self.question_number].answer
        return text.title()
