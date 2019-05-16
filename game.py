"""THIS WILL CONTAIN MULTIPLE WORD GAMES"""
# First game is that of questions to see how much your partner knows you.
# list of questions
# The asker inputs his/her answers of the questions provided.
# Then in random order, the partner is asked the questions, one by one they answer.
# The answers of the asked are marked against the answers of the asker and the meaning of their result is revealed.



questions = ["Question1 ?", "Question2 ?", "Question3 ?", "Question4 ?", "Question5 ?", 
"Question6 ?", "Question7 ?", "Question8 ?", "Question9 ?", "Question10 ?", "Question11 ?", "Question12 ?", "Question13 ?",
 "Question14 ?", "Question15 ?", "Question16 ?", "Question17 ?", "Question18 ?", "Question19 ?", "Question20 ?", "Question21 ?"]
ready_ques = {}
marks=0
total = len(questions)

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
    if marks>= 16:
        remarks = "You know your partner very well. Scoring more than 16 and you've been with your partner for less than six months, you're probably a bit intense in your relationship style."    
        print(remarks)
    elif marks>=10 and marks<=15:
        remarks = "You know your partner pretty well. In what categories do you know them less well? Maybe the two of you haven't talked much about your childhood experiences, or you've shied away from talking about topics related to negative emotions. Aim to learn the answers now."
        print(remarks)
    elif marks>=5 and marks<=9:
        remarks = "Maybe you've only been together a short time, maybe you don't talk to each other much, or maybe your conversations tend to be of a particular type (e.g., you're both in the same profession and mainly talk about work.) Ask yourself now if your personal lives or careers are so demanding that you're not getting a chance to talk and connect. Would it be worth bringing more balance to your relationship?"
        print(remarks)
    elif marks<=4:
        remarks = "The good news is there's lots of room for improvement here."
        print(remarks)
    else:
        print("Something went wrong")

if __name__ == "__main__":
    asker()
    asked()

