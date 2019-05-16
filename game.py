"""THIS WILL CONTAIN MULTIPLE WORD GAMES"""
# First game is that of questions to see how much your partner knows you.
# list of questions
# The asker inputs his/her answers of the questions provided.
# Then in random order, the partner is asked the questions, one by one they answer.
# The answers of the asked are marked against the answers of the asker and the meaning of their result is revealed.



questions = ["What's your favourite color ?", "Question2 ?", "Question3 ?", "Question4 ?", "Question5 ?"]
ready_ques = {}
marks=0
total = len(questions)

class Question:

    def __init__(self, que, ans):
        self.que = que
        self.ans = ans

def asker():
    for question in questions:
        answer = input(question)
        ready_ques[question] = answer
    print (ready_ques)

def asked():
    global marks
    for que, e_ans in ready_ques.items():
        ans = input(que)
        if ans == e_ans:
            marks += 1
        
    
    print(f"You have got {marks}/{total}")
        
        
if __name__ == "__main__":
    asker()
    asked()

