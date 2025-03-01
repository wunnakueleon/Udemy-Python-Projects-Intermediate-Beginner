from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    question_text = i['text']
    question_answer = i['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_questions():
    quiz.next_question()

print('The quiz is completed.')
print(f'Your total score is {quiz.score} out of {quiz.question_numbers}')
