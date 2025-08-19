
import random
from typing import List, Dict, Any

class JuniperQuestionGenerator:
    def __init__(self, questions: Dict[str, List[Dict[str, Any]]]):
        self.questions = questions

    def generate_quiz(self, num_questions: int = 5, topics: List[str] = None) -> List[Dict[str, Any]]:
        """
        Generates a quiz with a specified number of questions from given topics.

        Args:
            num_questions (int): The number of questions to include in the quiz.
            topics (List[str]): A list of topics to draw questions from. If None, use all available topics.

        Returns:
            List[Dict[str, Any]]: A list of selected questions for the quiz.
        """
        available_questions = []
        if topics:
            for topic in topics:
                if topic in self.questions:
                    available_questions.extend(self.questions[topic])
        else:
            for topic_questions in self.questions.values():
                available_questions.extend(topic_questions)

        if len(available_questions) < num_questions:
            print(f"Warning: Not enough questions available ({len(available_questions)}) for the requested quiz size ({num_questions}). Returning all available questions.")
            return available_questions

        return random.sample(available_questions, num_questions)

    def check_answer(self, question: Dict[str, Any], user_answer: str) -> bool:
        """
        Checks if the user's answer is correct.

        Args:
            question (Dict[str, Any]): The question dictionary.
            user_answer (str): The user's answer (e.g., "A", "B").

        Returns:
            bool: True if the answer is correct, False otherwise.
        """
        return question['answer'].upper() == user_answer.upper()

