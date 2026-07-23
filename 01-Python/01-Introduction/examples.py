"""Runnable examples for Chapter 1: Introduction to Python."""


def main():
    analyst = "Amina"
    completed_projects = 3
    average_score = 91.5
    is_learning = True

    print(f"Analyst: {analyst}")
    print(f"Projects: {completed_projects}")
    print(f"Average score: {average_score}")
    print(f"Currently learning: {is_learning}")

    daily_sales = [120, 150, 90, 200, 175]
    total_sales = sum(daily_sales)
    average_sales = total_sales / len(daily_sales)
    highest_day = max(daily_sales)

    print(f"Total sales: ${total_sales}")
    print(f"Average sales: ${average_sales:.2f}")
    print(f"Highest daily sales: ${highest_day}")

    target = 150
    target_days = [sales for sales in daily_sales if sales >= target]
    print(f"Days meeting target: {len(target_days)}")

    if average_sales >= target:
        print("The average sales target was met.")
    else:
        print("The average sales target was not met.")


if __name__ == "__main__":
    main()