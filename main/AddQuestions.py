
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
    letters = "ABCD"
    f = open(path, "r", encoding='Utf-8')
    read = f.read()
    f.close()
    myQuestion = listaddAll[0] + " ? "
    for indx, x in enumerate(listaddAll[1]):
        myQuestion = myQuestion + letters[indx] + "- " + str(x) + " "
    myQuestion = myQuestion + " [" + listaddAll[2] + "];"
    read = read+"\n"+myQuestion
    f = open(path, "w+", encoding="Utf-8")
    f.write(read)
    f.close()


def addQuestion(path): # fonction qui ajoute la question les réponses et les propositions
    listaddP = []
    listaddQ = []
    listaddB = []
    quitté_repadd = False 
    count = 0
    while quitté_repadd != True :
        if len(listaddQ) == 0 : 
            question = str(input('la question : '))  
            listaddQ.append(question)

        
        while count < 4 and quitté_repadd != True  :
            prop = str(input('quel est la propostition ? Q=quitter '))
            if prop == 'Q' or prop == 'q' and count <= 3 :
                quitté_repadd = True 
            else : 
                listaddP.append(prop)
            count+=1  

        if quitté_repadd == True : 
            bonneRep = str(input('ducoup quel est la bonne réponse la A,B,C,D : '))
            listaddB.append(bonneRep)

    print('donc vous avez comme liste de question : ',listaddQ)
    print('donc vous avez comme liste de propositions : ',listaddP)
    print('donc vous avez comme liste de bonne Réponse : ',listaddB)

    question = (listaddQ[0], listaddP, listaddB[0])

    save_question(path, question)

    
    
running = True
while running:
    
    
    print(banner)
    print("Logiciel additionnel a QCM Maker pour ajouter des questions au Fichier de QCM")

    x = str(input('vous-voulez ajouter une question o-n ? '))
    if x == 'o' : 
        addQuestion('./misc/fichier_questions_2.txt')
        
    else : 
        running = False 

print(('merci et bonne journee n\'hesitez pas a revenir ! '))