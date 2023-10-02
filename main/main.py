from classes.Questionnaire import Questionnaire
from classes.Question import Question
import random
from Bonus import *

banner = r"""
 ________  ________  _____ ______   ________  ___  __    _______   ________     
|\   __  \|\   ____\|\   _ \  _   \|\   __  \|\  \|\  \ |\  ___ \ |\   __  \    
\ \  \|\  \ \  \___|\ \  \\\__\ \  \ \  \|\  \ \  \/  /|\ \   __/|\ \  \|\  \   
 \ \  \\\  \ \  \    \ \  \\|__| \  \ \   __  \ \   ___  \ \  \_|/_\ \   _  _\  
  \ \  \\\  \ \  \____\ \  \    \ \  \ \  \ \  \ \  \\ \  \ \  \_|\ \ \  \\  \| 
   \ \_____  \ \_______\ \__\    \ \__\ \__\ \__\ \__\\ \__\ \_______\ \__\\ _\ 
    \|___| \__\|_______|\|__|     \|__|\|__|\|__|\|__| \|__|\|_______|\|__|\|__|
          \|__|                                              by Illian & Côme  """



def search_char(list_char, ligne: str, mainList=None):
    """
    Fonction permettant de faire une liste avec la ligne de question
    :param list_char: la liste des caractères a reécuperer
    :param ligne: la ligne sur laquelle le programme travaille
    :param count: le nombre
    :param mainList: liste principale avec les différentes questions etc
    :return:  mainList
    """
    if mainList is None:
        mainList = []

    charlist = list_char # pour ne pas modifier la liste accidentellement

    if charlist == []:
        return mainList

    elif list_char[0] not in ligne: # si le symbole n'est pas dans ce qu'il reste de la ligne on passe exemple le D dans une ligne a seulement 3 questions
        mainList = search_char(charlist[1:], ligne, mainList) # on cherche la prochaine reponse
        return mainList # on retourne le mainList sans y toucher
    else:
        for index, x in enumerate(ligne): # pour chaque caractère de la ligne
            if charlist[0] == ligne[index:index + len(charlist[0])]: # si le symbole A est le caractère x par ex et que après il y a un - donc A- a la suite
                mainList.append(ligne[:index]) # on ajoute l'avant de la ligne
                mainList = search_char(charlist[1:], ligne[index:], mainList) # recursivité
                return mainList # on renvoie la liste finie


def doList(char_searched: list):
    """
    Fonction permettant de faire la liste
    :param char_searched:  ["A-", "B-", "C-", "D-", "[", "]"]
    :return:
    """
    qList = []  # Notre Pile de questions
    f = open('./misc/fichier_questions_2.txt', 'r') # ouverture du fichier"
    fichier = f.readlines() # lecture des lignes et renvoie sous une forme []
    random.shuffle(fichier) # on melange les questions
    for ligne in fichier: # pour chaque ligne du fichier (question)
        q = search_char(char_searched, ligne) # on recupere la liste finie
        for x in q: # on parcourt les donnees de chaque question
            for y in char_searched: # si il y a toujours le caractère A- dans la ligne
                try: # on teste
                    if x[:len(y)] == y: # si A- est toujours la
                        q[q.index(x)] = x[len(y):] # one le supprime
                except:
                    pass

        if len(q) == 6: # Empilement des questions pour les questions avec 4 propo
            qList.append(Question(q[0], (q[1], q[2], q[3], q[4]), q[5]))
        elif len(q) == 5: # pour les questions a 3 propos
            qList.append(Question(q[0], (q[1], q[2], q[3], 0), q[4]))

    return qList


run = True
while run:
    liste = doList(["A-", "B-", "C-", "D-", "[", "]"]) # on recupere la liste de questions
    q = Questionnaire(liste, 0) # on cree un nouveau Questionnaire
    print(banner)  # on affiche la bannière de l'application
    your_choice = input("Que voulez vous faire ?\n 1) Faire un QCM \n 2) Lire les règles \n 3) Ajouter une question au QCM \n >>>")
    if your_choice == "1":
        q.game()  # on lance le jeu
        while 1:  # a la fin du jeu
            answer = input("Voulez vous recommencer un questionnaire ?? O/N \n >>>")
            if answer.upper() in ["N", "NO", "NON", "NOPE"]:  # le joueur veut quitter
                run = False  # on mets a false la condition principale du jeu
                print("Merci beaucoup et à une prochaine fois .")  # on remercie le joueur
                break  # on casse la boucle active
            elif answer.upper() in ["Y", "O", "Oui", "OUI", "YES", "YEAH", "yeah", "yes"]:  # si le joueur veut rejouer
                break  # on casse la boucle active

    elif your_choice == "2":
        q.rules() # on affiche les règles
        input("Appuyez sur entrée pour quitter les règles ...")

    elif your_choice == "3":
        print(banner)
        running = True
        while running:  # condition pour faire tourner le programme

            print("Logiciel additionnel a QCM Maker pour ajouter des questions au Fichier de QCM")

            x = str(input(
                'vous-voulez ajouter une question o-n ? '))  # première demande a l'utilisateur si il veut ajouter une question ou non
            if x == 'o':
                addQuestion('./misc/fichier_questions_2.txt')  # appel la fonction d
            else:
                running = False  # sort de la condition de base pour le programme de base

        print(('merci et bonne journee n\'hesitez pas a revenir ! '))

    else:
        print("Ce choix n'est pas proposé")


