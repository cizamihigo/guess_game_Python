print("Welcome To Guess: The Game")
print("You can guess which word is that one: ")
def check_guess(guess, answer):
    global score
    Still = True
    attempt = 0
    var = 2
    global NuQuest
    while Still and attempt < 2 :

        if guess.lower() == answer.lower() :
            print("\nCorrect Answer " + answer)
            Still = False
            score = score + 3 - attempt
            NuQuest += 1
        else :
            if attempt < 1 :
                
                
                guess = input("Wrong answer. Try again. {0} chance(s) reamining . . .".format(var))
                var = 2 - 1
            attempt += 1
    pass
    if attempt == 2 :
        
        print("The correct answer is " + answer)
        NuQuest += 1

score = 0
NuQuest = 0
guess1 = input("Designe une oeuvre littéraire en vers: \
    A. Poème\t B. Poésie\t C. Rymes\t D. Rhums\t E. Rien  ==>")
check_guess(guess1,'A')
guess1 = ""
guess1 = input("Designe ce qui est produit par un  ouvrier un artisan un travail quelconque: \
    A. Art\t B. Dessin\t C. Oeuvre\t D. Ouvrage\t E. Statue  ==>")
check_guess(guess1,'D')
guess1 = ""
guess1 = input("En anglais DOOM quelle est sa variance en français???:\
    A. Franternité\t B. Finalité\t C.Nulité\t D. Maison\t E. Destinée   ==>")
check_guess(guess1,'E')
guess1 = ""
guess1 = input("Désigne Un Habittant de Rome:\
    A. Roumain\t B. Roman\t C. Romains\t D. Romain\t E. Romulus  ==>")
check_guess(guess1,'D')
guess1 = ""
guess1 = input("Ce qui forme Un angle droit est dit:\
    A. Droite\t B. Perpendiculaire\t C. Tangente\t D. Abscisse\t E. Adjascent ==>")
check_guess(guess1,'B')
guess1 = ""
guess1 = input("Adjectif, désignant ce qui est rélatif aux femmes:\
    A. Femme\t B. Female\t C. Féminin\t D. feminin\t E. Feminal  ==>")
check_guess(guess1,'C')
guess1 = ""
guess1 = input("Nom masculin désignant le corps céleste: \
    A. Astre\t B. Bombe\t C. Cosmos\t D. Dracula\t E. Terre ")
check_guess(guess1,'A')

##################################################
#      OTHER QUESTIONS CAN BE ADDED LATERLY.     #
##################################################
 
Prcentage = (((score/3) * 100 ) / NuQuest)
print("Votre Pourcentage a ce test a ete de : {0}".format(Prcentage))
print("Your score is : " +str(score) + " Sur " + str(NuQuest) +" Questions")

######################################## THE END ######################################