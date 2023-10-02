class Questionnaire:
    def __init__(self, questionList: list, score: int):
        """
        Méthode d'initialisation de la classe Questionnaire

        Parameters
        ----------
        questionList : list
            DESCRIPTION.
        score : int
            DESCRIPTION.

        Returns
        -------
        None.

        """
        self.questionList = questionList if (questionList != []) else []
        self.score = score
        self.bonus = 3
        self.malus = 1

    def questionsLen(self):
        """
        Methode permettant de calculer la longueur de la pile
        :return:
        """
        temp = []
        count = 0
        while not self.isEmpty():
            temp.append(self.depiler())
            count += 1

        while temp:
            self.empiler(temp.pop(0))
        return count

    def bonneRep(self):
        """
        Methode permettant l'incrémentation du score pour une bonne réponse donnée
        :return:
        """
        self.score += self.bonus
        print('Bravo tu as trouvé la bonne réponse. +3 points')

    def mauvRep(self):
        """
        Méthode permttant la décrémentation du score pour une mauvaise réponse
        :return:
        """
        self.score -= self.malus
        print("Aille tu n'as pas trouvé la bonne réponse . -1 points")

    def getScore(self):
        return self.score

    def rules(self):
        """
        Methode permettant d'afficher les règles du questionnaire
        :return:
        """
        self.rules = """
        QCM prenant les questions dans le fichier texte dans ./misc .\n 
        Vous pouvez répondre à ces questions par A, B, C ou D.
        Vous gagnez 3 points par bonne réponse.
        Vous perdez 1 point par mauvaise réponse.
        A la fin les resultats sont ramenés sur une note de 20
        """
        print(self.rules)

    def isEmpty(self):
        """
        Fonction qui permet de savoir si la liste de questions est vide
        """
        if self.questionList:
            return False
        return True

    def depiler(self):
        """
        Methode permettant de depiler une question et qui la renvoie
        :return:
        """
        return self.questionList.pop(0)

    def empiler(self, p):
        """
        Meyhode permettant d'empiler un element sur la pile de questions
        :param p:
        :return:
        """
        self.questionList.append(p)

    def game(self):
        """
        Methode permettant le lancement du jeu
        :return:
        """
        letters = "ABCD"
        wrong = True
        length = self.questionsLen()
        while not self.isEmpty():
            if wrong:
                question = self.depiler()
                print(question)
            response = input("Quelle est la réponse ?  >>> ")
            if response.upper() in letters[:question.numberProps()]:
                wrong = True
                if question.isGood(response):
                    self.bonneRep()

                else:
                    self.mauvRep()
                    print(f'La Bonne réponse était {question.getBonneRep()}')

                print(f"Ton Score est de {self.score}")
            else:
                print(f"La réponse {response} n'est pas proposée ...")
                wrong = False
        try:
            print(f'Ton score final est de {round(float((self.score / (length*self.bonus)) * 20), 2)}/20. Bravo !!')
        except:
            print("Tu n'as pas de questions dans le fichier texte")
