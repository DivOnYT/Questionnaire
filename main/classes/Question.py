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
        if answers[3] != 0:
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
        try:
            presentation=presentation+f"D - {self.qD}"
        except:pass
        return presentation