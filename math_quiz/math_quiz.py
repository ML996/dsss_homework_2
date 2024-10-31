import random


def generate_random_number(min_value, max_value):
    """
    Generate a random integer within a specified range.
    
    Parameters:
    - min_value (int): The minimum value in the range.
    - max_value (int): The maximum value in the range.
    
    Returns:
    - int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)


def choose_operator():
    """
    Choose a random mathematical operator.
    
    Returns:
    - str: A random operator ('+', '-', or '*').
    """
    return random.choice(['+', '-', '*'])


def generate_problem(num1, num2, operator):
    """
    Generate a math problem and calculate its answer based on the operator.
    
    Parameters:
    - num1 (int): The first number in the problem.
    - num2 (int): The second number in the problem.
    - operator (str): The mathematical operator to use ('+', '-', '*').
    
    Returns:
    - tuple: A string representation of the problem and the correct answer.
    """
    problem_statement = f"{num1} {operator} {num2}"
    
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    
    return problem_statement, answer


def math_quiz():
    """
    Run the math quiz game, where users answer randomly generated math questions.
    The game will display the final score at the end.
    """
    score = 0
    total_questions = 3  # Setting a fixed number of questions for simplicity

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_number(1, 10)
        num2 = generate_random_number(1, 5)
        operator = choose_operator()

        problem_statement, correct_answer = generate_problem(num1, num2, operator)
        print(f"\nQuestion: {problem_statement}")
        
        # Error handling for invalid user input
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a numeric answer.")
            continue  # Skip this question if input is invalid

        # Check if the user's answer is correct
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()

