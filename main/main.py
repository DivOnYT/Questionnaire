from classes.Questionnaire import Questionnaire
from classes.Question import Question

"""def search_Char(char: str, ligne: str):
    for index, x in enumerate(ligne):
        if char == ligne[index:index+len(char)]:
            print(ligne[:index])
            return(index, char)

"""

def search_char(list_char, ligne: str, mainList=None):
    """

    :param list_char: la liste des caractères a reécuperer
    :param ligne: la ligne sur laquelle le programme travaille
    :param count: le nombre
    :param mainList: liste principale avec les différentes questions etc
    :return:  mainList
    """
    if mainList is None:
        mainList = []

    charlist = list_char

    if charlist == []:
        return mainList

    elif list_char[0] not in ligne:
        mainList = search_char(charlist[1:], ligne, mainList)
        return mainList
    else:
        for index, x in enumerate(ligne):
            if charlist[0] == ligne[index:index + len(charlist[0])]:
                mainList.append(ligne[:index])
                mainList = search_char(charlist[1:], ligne[index:], mainList)
                return mainList


rep = ("Qui est le chef du nouveau gouvernement en France en 1936 ?", "Thorez", "Blum", "Daladier", "Petain", "Blum")


def doList(char_searched: list):
    qList = []  # Notre Pile de questions
    with open('./misc/fichier_questions_2.txt', 'r') as fichier:
        for ligne in fichier:
            q = search_char(char_searched, ligne)
            for x in q:
                for y in char_searched:
                    try:
                        if x[:len(y)] == y:
                            q[q.index(x)] = x[len(y):]
                    except:
                        pass

            if len(q) == 6:
                qList.append(Question(q[0], (q[1], q[2], q[3], q[4]), q[5]))
            elif len(q) == 5:
                qList.append(Question(q[0], (q[1], q[2], q[3], 0), q[4]))


run = True
while run:
    liste = doList(["A-", "B-", "C-", "D-", "[", "]"])
    q = Questionnaire(liste, 20)
    print(q)
    q.game()

    answer = input("Voulez vous recommencer un questionnaire ?? O/N \n >>>")
    if answer.upper() in ["N", "NO", "NON", "NOPE"]:
        run = False
        print("Merci beaucoup et à une prochaine fois .")
