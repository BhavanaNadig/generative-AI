import random
import re

def generate_quiz(text, num_questions=5):
    sentences = re.split(r'\.|\?|!', text)
    random.shuffle(sentences)
    quiz = []
    for sentence in sentences:
        words = sentence.split()
        if len(words) > 6:
            blank_index = random.randint(0, len(words)-1)
            question = " ".join(words[:blank_index]) + " ____ " + " ".join(words[blank_index+1:])
            quiz.append(question)
        if len(quiz) >= num_questions:
            break
    return quiz
