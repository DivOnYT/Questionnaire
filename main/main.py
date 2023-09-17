from classes.Questionnaire import Questionnaire
from classes.Question import Question

def doList():
    return []


run = True
while run:
    liste = doList()
    q = Questionnaire(liste, 20)
    print(q)
    q.game()

    answer = input("Voulez vous recommencer un questionnaire ?? O/N \n >>>")
    if answer.upper() in ["N", "NO", "NON", "NOPE"]:
        run = False
        print("Merci beaucoup et à une prochaine fois .")