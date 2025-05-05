def evaluate(p, q, t, c):
    score = p + q + t + c
    if score >= 32:
        return "Excellent"
    elif score >= 24:
        return "Good"
    else:
        return "Needs Improvement"

def get_score(prompt):
    value = int(input(prompt))
    if 1 <= value <= 10:
        return value
    else:
        raise ValueError("Score must be between 1 and 10.")

def main():
    print("Employee Performance Evaluation")

    try:
        p = get_score("Punctuality (1-10): ")
        q = get_score("Quality of Work (1-10): ")
        t = get_score("Teamwork (1-10): ")
        c = get_score("Communication (1-10): ")

        result = evaluate(p, q, t, c)
        print("Performance:", result)

    except ValueError as e:
        print("Error:", e)

main()




