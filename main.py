import random  #Allows random numbers to be generated to convert units
import time # Allows small breaks to be added to make game seem more calm

question_data = [
    ("meters", "kilometers", 1000),
    ("days", "years", 365),
    ("pounds", "kilograms", 2.205),
    ("days", "weeks", 7),
    ("megabytes", "gigabytes", 1000),
    ("acres", "hectares", 2.471),
    ("arcseconds", "degrees", 3600),
    ("inches", "feet", 12),
    ("feet", "miles", 5280),
    ("ounces", "pounds", 16),
    ("milliliters", "liters", 1000),
]

def question_generation(small_unit, large_unit, conversion_factor):
    # Create a random unit conversion question
    big_value = random.randint(1, 25)
    correct_answer = big_value * conversion_factor
    return {
        "question": f"How many {small_unit} are in {big_value} {large_unit}?",
        "answer": correct_answer,
        "big_value": big_value,
        "small_unit": small_unit,
        "large_unit": large_unit
    }

def answer_check(user_input, right_answer):
    # Checks whether answer is correct
    try:
        user_answer = float(user_input) 
        assert user_answer == right_answer
        return True
    except AssertionError as e:
        return False

def run_quiz():
    # How the quiz runs
    print("Welcome to the Unit Conversion Quiz!\nYou'll have 10 questions.\nIf you want to stop or give up, type 'quit'. GOOD LUCK!")

    score = 0
    asked_questions = 0
    
    #Selecting random question from the dictionary
    selected_question = random.sample(question_data, 10)
    for i, (small, large, conversion) in enumerate(selected_question, 1):
        question = question_generation(small, large, conversion)
        print(f"Question {i}/10")
        print("-" * 35 + "\n")
        print(question["question"])
        time.sleep(0.5)
        user_input = input("\nYour answer: ").strip()
        asked_questions += 1
        if user_input.lower() == "quit":
            print("You have quit the quiz. Enjoy the rest of your day!")
            break
        if answer_check(user_input, question["answer"]):
            score += 1
            time.sleep(0.5)
            print("Correct!")
            time.sleep(0.5)
        else:
            time.sleep(0.5)
            print(f"That's not right, the correct answer was {question["answer"]}")
    
    percentage = (score / asked_questions) * 100
    print("**********CALCULATING SCORE**********")
    time.sleep(2)
    print(f"Congratulations! Your final score was {score}/{asked_questions}, which is {percentage}%!")
    time.sleep(0.5)
    print("I hope you enjoyed playing this quiz, enjoy the rest of your day!")
            
                

run_quiz() 

