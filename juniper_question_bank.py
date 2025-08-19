
import os
import json
from typing import List, Dict, Any

def load_questions(question_bank_path: str = 'question_bank') -> Dict[str, List[Dict[str, Any]]]:
    """
    Loads all questions from the question bank.

    Args:
        question_bank_path (str): The path to the question bank directory.

    Returns:
        Dict[str, List[Dict[str, Any]]]: A dictionary where keys are topics and values are lists of questions.
    """
    questions = {}
    for root, _, files in os.walk(question_bank_path):
        for file in files:
            if file.endswith('.json'):
                topic = os.path.splitext(file)[0]
                with open(os.path.join(root, file), 'r') as f:
                    questions[topic] = json.load(f)
    return questions

