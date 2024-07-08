import random 
import questionary
import question
import inspect
class quiz: 
    def __init__(self,questions,num):
        self.num=num
        self.questions=random.sample(questions,self.num) #choosing random n question
        
    def start(self):
        score=0
        for question in self.questions:
            answer = questionary.select(    #questionary is use to select options on command kine interface
                question["question"],    # question string type
                choices=question["options"],   # options as list of strings
                style=questionary.Style([('selected', 'white bold')]) # it is use to add style like color hower effect etc
            ).ask() # user input and store in 'answer'
            if (answer == question["answer"]):
                score += 1
                print(f"\033[1;32m Correct \033[1;32m ") # \033[1;32m it is a ANSI escape sequence for green ,bold text
            else:
                print(f"\033[1;31m Wrong!\033[0m The correct answer is \033[1;32m{question['answer']}.")
        print(f"Your final score is {score}/{self.num}") # print the score
        


if __name__ == "__main__":
    n=int(input("Enter number of questions you want to answer [ at least 3] : "))
    q=input("Enter subject 'dsa' or 'python'")
    q=quiz(getattr(question,q),n)
    print("[ RULE: choose your answer by entering UP and DOWN button and ENTER to submit it ]")
    q.start()
    
