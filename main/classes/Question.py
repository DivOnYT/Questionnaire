class Question:
    def __init__(self, question: str, answers: tuple, good: str):
        """
        Méthode d'initialisation de la classe Question

        Parameters
        ----------
        question : str
            DESCRIPTION.
        answers : tuple
            DESCRIPTION.
        good : str
            DESCRIPTION.

        Returns
        -------
        None.

        """
        self.question = question 
        self.qA = answers[0] 
        self.qB = answers[1]
        self.qC = answers[2]
        self.qD = answers[3]
        self.good = good

    def isGood(self, reponse):
        """
        Fonction permettant de savoir si une réponse est juste
        :param reponse:
        :return:
        """
        if reponse.upper() == self.good.upper():
            return True
        return False

    def getBonneRep(self):
        """
        Methode permettant de recuperer la bonne reponse
        :return:
        """
        return self.good

    def numberProps(self):
        """
        Methode permettant de retourner le nombre de propositions enregistrées
        :return:
        """
        count = 0
        if self.qA != 0:
            count+=1
        if self.qB != 0:
            count +=1
        if self.qC != 0:
            count +=1
        if self.qD != 0:
            count +=1
        return count
        
    def __str__(self):
        """
        Renvoie la présentation de la question

        Returns
        -------
        presentation: str

        """
        
        presentation = f"""
        {self.question}\n
        A - {self.qA}
        B - {self.qB}
        C - {self.qC}
        """
        if self.qD != 0:
            presentation=presentation+f"D - {self.qD}"
        return presentation