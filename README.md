# IFCSP-formative -- Unit Conversion Quiz
This project is a 10 question quiz which tests your unit conversion skills!

## User Documentation
### Step 1: Save the quiz
Save a copy of the quiz to your device by copying and pasting into a code editor of your choice, eg VS Code.  
### Step 2: Run the quiz
Either run the quiz through your code editor or in your terminal. To run it through your terminal, open the Command Prompt and type 'cd' followed by the path where you saved the file. Then simply type the file name followed by the extension '.py', and select where you want the code to run. If you choose python, it should show a window like this: 
![What running the quiz in Command Prompt should look like](https://github.com/abi-alice/IFCSP-formative/blob/main/quiz%20in%20cmd.png)
### Step 3: Play the quiz
The quiz provides instructions for you, feel free to use a calculator if you need to. Have fun and good luck!  

## Technical Documentation
### How the code works
The list ```question_data``` is a list of tuples, which is used to store the related groups of values for the unit conversion.
```import random``` allows a random number to be chosen so the conversion is unpredictable, and ```import time``` adds breaks in the output through ```time.sleep``` to make the experience seem less frantic.
#### Question Generation
This function allows a random question to be generated from the list of conversion tuples, creates the correct answer for that question and returns the data as a dictionary:
```
def question_generation(small_unit, large_unit, conversion_factor):
    big_value = random.randint(1, 25)
    correct_answer = big_value * conversion_factor
    return {
        "question": f"How many {small_unit} are in {big_value} {large_unit}?",
        "answer": correct_answer,
        "big_value": big_value,
        "small_unit": small_unit,
        "large_unit": large_unit
    }
```
#### Answer check
  The function ```answer_check()``` converts the user's input into a float, then checks it against the correct answer created in ```question_generation()```.   
#### Running the quiz
  ```run_quiz()``` is the main function where the quiz runs, printing the questions, allowing the user to answer, and calculating a final score at the end of the quiz. 
 ```
selected_question = random.sample(question_data, 10)
for i, (small, large, conversion) in enumerate(selected_question, 1):
```
These 2  lines pick 10 **different** questions from the options provided in the list of tuples; ```random.sample(question_data, 10)``` ensures there are no duplicates and each element is unique. Whether the answer is right or wrong, the quiz moves on to the next question.  

If the user wants to quit the quiz at any time, this code allows them to type 'quit' and the quiz will stop running. This is achieved by using *break*:
```
if user_input.lower() == "quit":
            print("You have quit the quiz. Enjoy the rest of your day!")
            break
```
The score is calculated at the very end of the function, no matter how many questions the user has answered. The percentage is calculated by the equation ``` (score / asked_questions) * 100 ```.
```score``` and ```asked_questions``` are set to 0 at the beginning of the function; ```score``` is increased by 1 for every question the user answers correctly, and ```asked_questions``` is increased by 1 no matter whether the question is answered right or wrong.
