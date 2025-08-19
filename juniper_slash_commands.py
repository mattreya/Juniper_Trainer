
import typer
from typing import Optional, List

from juniper_question_bank import load_questions
from juniper_question_generator import JuniperQuestionGenerator

app = typer.Typer()

@app.command()
def quiz(
    num_questions: int = typer.Option(5, "--num-questions", "-n", help="Number of questions for the quiz."),
    topics: Optional[List[str]] = typer.Option(None, "--topic", "-t", help="Specify topics to include in the quiz (e.g., -t ospf -t bgp).")
):
    """
    Starts a Juniper OS quiz.
    """
    typer.echo("Loading questions...")
    all_questions = load_questions()

    if not all_questions:
        typer.echo("No questions found. Please add questions to the 'question_bank' directory.")
        return

    generator = JuniperQuestionGenerator(all_questions)
    selected_topics = topics if topics else list(all_questions.keys())

    typer.echo(f"Starting quiz with {num_questions} questions from topics: {', '.join(selected_topics)}")

    quiz_questions = generator.generate_quiz(num_questions=num_questions, topics=selected_topics)

    if not quiz_questions:
        typer.echo("Could not generate quiz questions. Check your topics or question bank.")
        return

    score = 0
    for i, q in enumerate(quiz_questions):
        typer.echo(f"\nQuestion {i+1}: {q['question']}")
        for option_key, option_value in q['options'].items():
            typer.echo(f"  {option_key}. {option_value}")

        user_answer = typer.prompt("Your answer (A, B, C, or D)")

        if generator.check_answer(q, user_answer):
            typer.echo("Correct!")
            score += 1
        else:
            typer.echo(f"Incorrect. The correct answer was {q['answer']}.")

    typer.echo(f"\nQuiz finished! You scored {score} out of {len(quiz_questions)}.")

if __name__ == "__main__":
    app()
