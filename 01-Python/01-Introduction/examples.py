"""Runnable examples for Chapter 1 - Introduction to Python.

Python Version: 3.12+
Status: Tested
Expected Output: Yes
Dependencies: None
"""


def summarize_scores(scores):
    """Return the average score and number of passing scores."""
    if not scores:
        raise ValueError("scores must not be empty")

    average = sum(scores) / len(scores)
    passed = sum(score >= 50 for score in scores)
    return average, passed


def main():
    name = "Harish"
    print(f"Welcome, {name}!")

    score = 82
    result = "pass" if score >= 50 else "review"
    print(result)

    average, passed = summarize_scores([72, 48, 91, 65])
    print(f"Average: {average:.1f}")
    print(f"Passed: {passed}")


if __name__ == "__main__":
    main()
