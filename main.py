from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    question_incorrect = question["incorrect_answers"]
    difficulty = question["difficulty"]
    game_type = question["type"]
    category = question["category"]
    new_question = Question(question_text, question_answer, question_incorrect, difficulty, game_type, category)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print("\n\nYou have completed the game")
print(f"Your final score is {quiz.score}/{len(question_bank)}\n")
