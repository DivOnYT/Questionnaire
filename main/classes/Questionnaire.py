class Questionnaire:
    def __init__(self, questionList : list, score: int):
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
        
    def isEmpty(self):
        """
        Fonction qui permet de savoir si la liste de questions est vide
        """
        
        
    def __str__(self):
        return("salut")
    
    def game(self):
        pass        
        
        
