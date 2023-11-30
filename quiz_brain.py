class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):

        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: Type > {current_question.game_type}. Category >"
                            f" {current_question.category}.  Difficulty level > "
                            f"{current_question.difficulty}. "
                            f"\n{current_question.text} \n{current_question.answer,
        current_question.incorrect_options} \n").lower()
        self.correct_answer(user_answer, current_question.answer)

    def correct_answer(self, user_answer, current_question):

        if user_answer.lower() == current_question.lower():
            self.score += 1
            print("You got this, Your answer is correct")

        else:
            print(f"That's is wrong, the correct answer is {current_question}")
        print(f"your current score is {self.score}/{self.question_number}\n")
