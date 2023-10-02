# LE BONUS DU PROJET NSI ------------------------------------------------------------------------

banner = r""" 
 ________  ________  _____ ______   ________  ___  __    _______   ________     
|\   __  \|\   ____\|\   _ \  _   \|\   __  \|\  \|\  \ |\  ___ \ |\   __  \    
\ \  \|\  \ \  \___|\ \  \\\__\ \  \ \  \|\  \ \  \/  /|\ \   __/|\ \  \|\  \   
 \ \  \\\  \ \  \    \ \  \\|__| \  \ \   __  \ \   ___  \ \  \_|/_\ \   _  _\  
  \ \  \\\  \ \  \____\ \  \    \ \  \ \  \ \  \ \  \\ \  \ \  \_|\ \ \  \\  \| 
   \ \_____  \ \_______\ \__\    \ \__\ \__\ \__\ \__\\ \__\ \_______\ \__\\ _\ 
    \|___| \__\|_______|\|__|     \|__|\|__|\|__|\|__| \|__|\|_______|\|__|\|__|
          \|__|                                              by Ilian & Côme  """


def save_question(path: str, listaddAll: tuple):
    letters = "ABCD" # chaine de caractère servant a parcourir les propositions ABC ou D 
    f = open(path, "r", encoding='Utf-8') # ouverture du fichier texte avec en parametre sa valeur 
    read = f.read() # lecture du fichier texte  
    f.close() # fermeture du fichier texte 
    myQuestion = listaddAll[0] + " ? " # liste de fin qui est pour le moment juste la question et le point d'interrogation 
    for indx, x in enumerate(listaddAll[1]): # x parcours la liste des propositions ou prend la valeur de chaque index 
        myQuestion = myQuestion + letters[indx] + "- " + str(x) + " " # formation de la question avec ses propositions 
    myQuestion = myQuestion + " [" + listaddAll[2] + "];" # reprise de la bonne réponse 
    read = read+"\n"+myQuestion # lecture de la question finale 
    f = open(path, "w+", encoding="Utf-8") # ouverture du fichier texte 
    f.write(read) # ecriture dans le fichier texte 
    f.close() # fermeture du fichier texte 


def addQuestion(path): # fonction qui ajoute la question les réponses et les propositions
    listaddP = [] # création de la liste de propositions 
    listaddQ = [] # création de la liste de questions 
    listaddB = [] # création de la liste de bonne réponse een fonction du nombre de questions 
    quitté_repadd = False # initialisation de valeur booléene à quitté_repadd
    count = 0 # compteur pour permettre de fermé le while suivant pour que, quand l'utilisateur aura écrit les 4 propositions ou les 3 ou 2 (!=1) l'utilisateur sera automatiquement ejecté de la boucle 
    while quitté_repadd != True : # condition tant que l'utilisateur n'a pas fini d'écrire sa question 
        if len(listaddQ) == 0 : # si la liste ne contient rien 
            question = str(input('la question : '))  # demande a l'utilisateur quelle est la question 
            listaddQ.append(question) # ajout de la question dans la liste 

        
        while count < 4 and quitté_repadd != True  : # tant que la liste prop n'a 
            prop = str(input('quel est la propostition PS : vous êtes obligé d\'avoir au moins trois propositions ? Q=quitter ')) # demande des propositions après avoir demander la question
            if prop == 'Q' or prop == 'q' and count <= 3 : # si l'utilisateur veux quitté la demande de proposistions 
                quitté_repadd = True 
            else : 
                listaddP.append(prop) # ajout des propositiions dans la liste 
            count+=1  # le compteur augmente de 1 à chaque propositions donné par l'utilisateur pour faire savoir a la boucle quand il faut s'arreter 

        if quitté_repadd == True : # si l'utilisateur a quitté la demande de propositions ou a fini de mettre ses 4 propositions alors : 
            bonneRep = str(input('ducoup quel est la bonne réponse la A,B,C,D : ')) # demande a l'utilisateur de rentré la bonne réponse entre ABC ou D (cela dépend du nombre de prop qu'il a rentré)
            listaddB.append(bonneRep) # ajout de la bonne réponse dans la listaddB
    # affiche les liste pour une première fois 
    print('donc vous avez comme liste de question : ',listaddQ) 
    print('donc vous avez comme liste de propositions : ',listaddP)
    print('donc vous avez comme liste de bonne Réponse : ',listaddB)

    question = (listaddQ[0], listaddP, listaddB[0])

    save_question(path, question) # ajoute la question au fichier texte avec la fonction précédente 

