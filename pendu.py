#
#
# Maxime Lecomte
# Pendu game
# 24/11/19
#
#
#




#! /usr/bin/python3


import os

## --------------------------------------------------- FUNCTION -------------------------------------- ##


class Pendu:

    def __init__(self, prenom, nom, letterUsed, motSplitted,wordToFind,letterTrash,turn):
        self.prenom = prenom
        self.nom = nom
        self.letterUsed = []
        self.motSplitted = []
        self.wordToFind = []
        self.letterTrash = []
        self.turn = 0

    def wordToBeFind(self,letterUsed,motSplitted,wordToFind,letterTrash,turn):
        mot = ""
        mot+=(str(input("which word ? \n")))
        os.system('cls' if os.name == 'nt' else 'clear')
        Pendu.splitMot(self,mot,motSplitted)
        Pendu.tries(self,letterUsed,motSplitted,mot,wordToFind,letterTrash,turn)
        return mot

    def tries(self,letterUsed,motSplitted,mot,wordToFind,letterTrash,turn):
        tryy = ""
        tryy += (str(input("try something to find the word, only letter\n")))
        letterUsed.insert(0,tryy)
        Pendu.compare(self,letterUsed,motSplitted,mot,wordToFind,letterTrash,turn)
        return letterUsed


    def splitMot(self,mot,motSplitted):
        for char in mot:
            motSplitted.append(char)
        return motSplitted

    def splitWordToFind(self,wordToFind,motSplitted):
        for char in motSplitted:
            wordToFind.append("")


    def compare(self,letterUsed,motSplitted,mot,wordToFind,letterTrash,turn):
        if len(wordToFind) != len(motSplitted):
            Pendu.splitWordToFind(self,wordToFind,motSplitted)
        for element in range(len(motSplitted)):
            if letterUsed[0]==motSplitted[element]:
                wordToFind[element]+=motSplitted[element]
        if letterUsed[0] not in motSplitted:
            turn+=1
            Pendu.looseCondition(self,letterTrash,letterUsed,turn,mot)

        print('wordToFind : \n',wordToFind)
        print('bad letter : \n',letterTrash)

        if Pendu.winCondition(self,mot,wordToFind) == True:
            print('\n !!!!!!!!!!!!! you win !!!!!!!!!!!!!!!')
            return mot

        elif Pendu.winCondition(self,mot,wordToFind) == False:
            Pendu.tries(self,letterUsed,motSplitted,mot,wordToFind,letterTrash,turn)


    def looseCondition(self,letterTrash,letterUsed,turn,mot):
        letterTrash+=letterUsed[0]
        if turn == 1:
            print("_____________")
        elif turn == 2:
            print("      |      ")
            print("      |      ")
            print("      |      ")
            print("      |      ")
            print("      |      ")
            print("      |      ")
            print("      |      ")
            print("______|______")
        elif turn == 3:
            print("      |___________")
            print("      |      ")
            print("      |      ")
            print("      |      ")
            print("      |      ")
            print("      |      ")
            print("      |      ")
            print("______|______")
        elif turn == 4:
            print("      |___________")
            print("      |          |")
            print("      |          |")
            print("      |      ")
            print("      |      ")
            print("      |      ")
            print("______|______")
        elif turn == 5:
            print("      |___________")
            print("      |          |")
            print("      |          |")
            print("      |          O")
            print("      |      ")
            print("      |      ")
            print("______|______")

        elif turn == 6:
            print("      |___________")
            print("      |          |")
            print("      |          |")
            print("      |          O")
            print("      |          |")
            print("      |      ")
            print("______|______")

        elif turn == 7:
            print("      |___________")
            print("      |          |")
            print("      |          |")
            print("      |          O")
            print("      |          |/")
            print("      |      ")
            print("______|______")
        elif turn == 8:
            print("      |___________")
            print("      |          |")
            print("      |          |")
            print("      |          O")
            print("      |         \\|/")
            print("      |      ")
            print("______|______")
        elif turn == 9:
            print("      |___________")
            print("      |          |")
            print("      |          |")
            print("      |          O")
            print("      |         \\|/")
            print("      |          /")
            print("______|______")

        elif turn == 10:
            print("      |___________")
            print("      |          |")
            print("      |          |")
            print("      |          O")
            print("      |         \\|/")
            print("      |          /\\")
            print("______|______")
            Pendu.loose(self,mot)


    def winCondition(self,mot,wordToFind):
        wordToFind="".join(wordToFind)
        if wordToFind == mot:
            return True
        else:
            return False

    def loose(self,mot):
        print( " \n ____________________ You loose ___________________ \n")
        print("The word was : ----------- ",mot,"-----------")
        print(" ------------------   1 - try again  ------------------   2 - exit -------")
        a = str(input("1 or 2 \n"))
        if a == "1":
            Pendu.wordToBeFind(self,[],[],[],[],0)
        else :
            exit()


    def __repr__(self):
        return ("The user {} {} start the game".format(self.prenom,self.nom))



## -----------------------------------------------------  MAIN ------------------------------------------------ ##

test = Pendu("maxime","Lecomte",[],[],[],[],0)
print(test)
test.wordToBeFind([],[],[],[],0)
