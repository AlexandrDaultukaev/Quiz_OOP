from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

q_brain = QuizBrain(question_bank)
end_the_game = False
while q_brain.question_number < len(question_bank) and not end_the_game:
    end_the_game = q_brain.ask_q()
    q_brain.next_q()