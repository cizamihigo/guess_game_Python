print("Welcome To Guess: The Game")
print("You can guess which word is that one: ")
def check_guess(guess, answer):
    global score
    Still = True
    attempt = 0
    var = 2
    global NuQuest
    while Still and attempt < 3 :

        if guess.lower() == answer.lower() :
            print("\nCorrect Answer " + answer)
            Still = False
            score += 1
            NuQuest += 1
        else :
            if attempt < 2 :
                
                
                guess = input("Wrong answer. Try again. {0} chance(s) reamining . . .".format(var))
                var = 2 - 1
            attempt += 1
    pass
    if attempt == 3 :
        
        print("The correct answer is " + answer)
        NuQuest += 1

score = 0
NuQuest = 0
guess1 = input("Designe une oeuvre littéraire en vers: ")
check_guess(guess1,'Poème')
guess1 = ""
guess1 = input("Designe ce qui est produit par un  ouvrier un artisan un travail quelconque: ")
check_guess(guess1,'Ouvrage')
guess1 = ""
guess1 = input("En anglais DOOM quelle est sa variance en français???: ")
check_guess(guess1,'destin')
guess1 = ""
guess1 = input("Désigne Un Habittant de Rome: ")
check_guess(guess1,'Romain')
guess1 = ""
guess1 = input("Ce qui forme Un angle droit est dit: ")
check_guess(guess1,'Perpendiculaire')
guess1 = ""
guess1 = input("Adjectif, désignant ce qui est rélatif aux femmes: ")
check_guess(guess1,'Féminin')
guess1 = ""
guess1 = input("Nom masculin désignant le corps céleste: ")
check_guess(guess1,'astre')
guess1 = ""
guess1 = input("Ma messe, la voici ! c'est la Bible, et je n'en veux pas d'autre ! de qui on tient cette citation ")
check_guess(guess1,"Jean Calvin")
guess1 = ""
guess1 = input("Le vin est fort, le roi est plus fort, les femmes le sont plus encore, mais la vérité est plus forte que tout. ! de qui tenons-nous cette citation ")
check_guess(guess1,"Martin Luther")
guess1 = ""
mpt = "plrboèem"
guess1 = input("Voici Un anagramme: " + str(mpt.upper()) +" Trouvez en un mot complet : ")
check_guess(guess1,"Problème")
guess1 = ""
mpt = "uonjcgnaiso"
guess1 = input("Voici Un anagramme: " + str(mpt.upper()) +" Trouvez en un mot complet : ")
check_guess(guess1,"conjugaison")
guess1 = ""
guess1 = input("Which is the fastest land animal?")
check_guess(guess1,"Cheetah")
##################################################
#      OTHER QUESTIONS CAN BE ADDED LATERLY.     #
##################################################
 
Prcentage = (score * 100 ) / NuQuest
print("Votre Pourcentage a ce test a ete de : {0}".format(Prcentage))
print("Your score is : " +str(score) + " Sur " + str(NuQuest))

######################################## THE END ######################################