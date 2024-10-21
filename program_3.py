#Capital Quiz Joseph Rydberg 10/21/2024

def capital_quiz():
    capitals = {"Minnesota": "St. Paul", "New York": "Albany", "Arizona": "Phoenix", "Alaska": "Juneau"}
    correct = 0

    for i in capitals:
        guess = input("what is the capital of " + i)
        if guess == capitals[i]:
            correct += 1

    print(correct, "Correct")

capital_quiz()