class QuizBrain:

    def __init__(self, q_list):
        self.question_numbers = 0
        self.question_list = q_list
        self.score = 0

    def still_questions(self):
        return self.question_numbers < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_numbers]
        self.question_numbers += 1
        user_answer = input(f'Q{self.question_numbers}. {current_question.text} (True/False)?: ').lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_input, correct_answer):
        if user_input.lower() == correct_answer.lower():
            self.score += 1
            print(f'Your answer is correct.')

        else:
            print("You're wrong.")
        print(f'The correct answer is {correct_answer}. Your current score is {self.score}/{self.question_numbers}')

