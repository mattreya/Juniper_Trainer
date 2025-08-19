import unittest
import os
import json
from unittest.mock import patch, MagicMock

from juniper_question_bank import load_questions
from juniper_question_generator import JuniperQuestionGenerator

# Define paths for testing
TEST_QUESTION_BANK_DIR = "test_question_bank"
TEST_OSPF_JSON_PATH = os.path.join(TEST_QUESTION_BANK_DIR, "infrastructure", "ospf.json")

class TestJuniperQuiz(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a temporary question bank for testing
        os.makedirs(os.path.join(TEST_QUESTION_BANK_DIR, "infrastructure"), exist_ok=True)
        test_questions = [
            {
                "question": "What is the default administrative distance of OSPF in Juniper?",
                "options": {"A": "10", "B": "100", "C": "110", "D": "150"},
                "answer": "A"
            },
            {
                "question": "Which command is used to enable OSPF on a Juniper router?",
                "options": {"A": "set protocols ospf area 0.0.0.0 interface <interface-name>", "B": "enable ospf", "C": "ip ospf enable", "D": "ospf run"},
                "answer": "A"
            }
        ]
        with open(TEST_OSPF_JSON_PATH, 'w') as f:
            json.dump(test_questions, f)

    @classmethod
    def tearDownClass(cls):
        # Clean up the temporary question bank
        os.remove(TEST_OSPF_JSON_PATH)
        os.rmdir(os.path.join(TEST_QUESTION_BANK_DIR, "infrastructure"))
        os.rmdir(TEST_QUESTION_BANK_DIR)

    def test_load_questions(self):
        questions = load_questions(TEST_QUESTION_BANK_DIR)
        self.assertIn('ospf', questions)
        self.assertEqual(len(questions['ospf']), 2)
        self.assertEqual(questions['ospf'][0]['question'], "What is the default administrative distance of OSPF in Juniper?")

    def test_generate_quiz(self):
        questions = load_questions(TEST_QUESTION_BANK_DIR)
        generator = JuniperQuestionGenerator(questions)

        quiz = generator.generate_quiz(num_questions=1, topics=['ospf'])
        self.assertEqual(len(quiz), 1)
        self.assertIn('question', quiz[0])

        quiz_all_topics = generator.generate_quiz(num_questions=2)
        self.assertEqual(len(quiz_all_topics), 2)

    def test_check_answer(self):
        questions = load_questions(TEST_QUESTION_BANK_DIR)
        generator = JuniperQuestionGenerator(questions)

        question = questions['ospf'][0]
        self.assertTrue(generator.check_answer(question, 'A'))
        self.assertTrue(generator.check_answer(question, 'a'))
        self.assertFalse(generator.check_answer(question, 'B'))

    @patch('typer.prompt', side_effect=['A', 'C']) # Changed to 'C' for incorrect answer
    @patch('typer.echo')
    @patch('juniper_question_bank.load_questions')
    def test_quiz_command(self, mock_load_questions, mock_echo, mock_prompt):
        # Mock load_questions to return our test data
        mock_load_questions.return_value = {
            'ospf': [
                {
                    "question": "Test Question 1?",
                    "options": {"A": "OptA", "B": "OptB", "C": "OptC", "D": "OptD"},
                    "answer": "A"
                },
                {
                    "question": "Test Question 2?",
                    "options": {"A": "OptA", "B": "OptB", "C": "OptC", "D": "OptD"},
                    "answer": "B"
                }
            ]
        }

        from juniper_slash_commands import quiz

        # Run the quiz command with 2 questions
        quiz(num_questions=2, topics=['ospf'])

        # Assertions for output and score
        mock_echo.assert_any_call("Correct!")
        mock_echo.assert_any_call("Incorrect. The correct answer was B.")
        mock_echo.assert_any_call("\nQuiz finished! You scored 1 out of 2.")

if __name__ == '__main__':
    unittest.main()
