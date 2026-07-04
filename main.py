    from random import randint

    def number_generator(min, max):
            ergebnis = randint(min, max)
            return ergebnis
    wins = 0
    while True:
        
        print("Random Number Generator")
        def number_generator(min, max):
            ergebnis = randint(min, max)
            return ergebnis

        while True:
            try:
                level = int(input("Choose a Level: lvl 1 (until 10), lvl 2 (until 100), lvl 3 (until 1000): "))
                break
            except:
                print("Put in a number!!!")

        while True:
            try:
                nummer_chance = int(input("How many tries do you need? :"))
                break
            except:
                print("Put in a number!!!")

        if (level == 1):
            geheimnis = number_generator(1, 10)
        elif (level == 2):
            geheimnis = number_generator(1, 100)
        else:
            geheimnis = number_generator(1, 1000)

        versuche = 0    
        while versuche < nummer_chance:
            
            while True:
                try:
                    antwort = int(input("Your number:"))
                    break
                except:
                    print("Put in a number!!!")
                
            versuche = versuche + 1

            print("Tries: ",versuche)

            if (antwort == geheimnis):
                print("Excellent you guessed the right number!")
                wins= wins + 1
                break

            elif (antwort == 9999):
                versuche = versuche - 999999999999999999999999999999999999999999999999999999999999999999999999
                print("Ouhhh Hacks activated, you have unlimited tries now!")
            
            elif (antwort > geheimnis):
                    print("lower")

            else:
                    print("higher")

        if geheimnis != antwort:
            print("Game Over. The right number was",geheimnis)
            

        again = input("Do you wanna restart?: ")

        try:
            if again.lower() != "yes":
                print("Thanks for playing!")
                print("You have",wins,"wins!!! Good Job!")
                    break
        except:
            print ("Type yes or no!")
