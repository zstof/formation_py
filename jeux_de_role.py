
import random

class var_colors:
    res_player = '\033[92m' 
    res_pc = '\033[91m'
    Cpotion = '\033[93m'
    reset = '\033[0m'
   


vie_player = 50
vie_pc = 50
potion = 3

print("*** Le jeu dr rôle ***")

while True:
    choix = input("Souitez-vous attaquer (1) ou utiliser une potion (2) ? ")
    print("")

    if not choix.isdigit() or int(choix) <= 0 or int(choix) > 2:
        continue
 
    else:
        choix = int(choix)

    if int(choix) == 1:
        # if vie_player >= 1 and vie_pc >=1:
            attaque_player = random.randint(5 , 10)
            attaque_pc = random.randint(5 , 15)
            vie_pc = vie_pc - attaque_player
            vie_player = vie_player - attaque_pc

            if vie_player >= 1 and vie_pc >=1 :

            
                print(f"Vous avez infligé {var_colors.res_player}{attaque_player}{var_colors.reset} points de dégats à l'ennemi \u2694\uFE0F")
                print(f"L'ennemie vous à infligé {var_colors.res_pc}{attaque_pc}{var_colors.reset}  points de dégats \U0001F4A5")
                print("")
                print(f"il vous reste {var_colors.res_player}{vie_player}{var_colors.reset} point de vie. \u2764\uFE0F")
                print(f"il reste {var_colors.res_pc}{vie_pc}{var_colors.reset} point de vie à l'ennemie \u2764\uFE0F ")
                print("----------------------------------------------------------")
                continue

            elif vie_player <= 0 :
                print("Vous avez perdu ! vous êtes mort \u2620\uFE0F \u2620\uFE0F \u2620\uFE0F ")
                print(f"L'ennemie vous à infligé {var_colors.res_pc}{attaque_pc}{var_colors.reset}  points de dégats \U0001F4A5")
                print(f"L'ennemie fini avec {var_colors.res_pc}{vie_pc}{var_colors.reset} point de vie \u2764\uFE0F ")
                break

            elif vie_pc <= 0 :
                print("vous avez gané \U0001F4AA")    
                print(f"Vous avez infligé {var_colors.res_player}{attaque_player}{var_colors.reset} points de dégats à l'ennemi \u2694\uFE0F")
                print(f"Vous finissez avec {var_colors.res_player}{vie_player}{var_colors.reset} point de vie. \u2764\uFE0F")
                break

    else:
            if potion > 0 :
                potion = potion -1
                potion_player = random.randint(15 , 50)
                vie_player = vie_player + potion_player 
                
                print(f"Vous, vous êtes injecté une protion \U0001F489 vous avez récupéré {potion_player} de point de vie \u2764\uFE0F")
                
                if potion == 0 :
                    print(f"Votre vie \u2764\uFE0F  est à {var_colors.res_player}{vie_player}{var_colors.reset} point. Vous n'avez plus de potion disponible \u274C\uFE0F")
                    print("")
 
                
                else:
                    print(f"Votre vie \u2764\uFE0F  est à {var_colors.res_player}{vie_player}{var_colors.reset} point.  Il vous reste {var_colors.Cpotion}{potion}{var_colors.reset} potion \U0001F9EA")
                    print("")
            


                attaque_pc = random.randint(5 , 15)
                vie_player = vie_player - attaque_pc
                print(f"L'ennemie vous à infligé {var_colors.res_pc}{attaque_pc}{var_colors.reset}  points de dégats \U0001F4A5")
                print(f"il vous reste {var_colors.res_player}{vie_player}{var_colors.reset} point de vie. \u2764\uFE0F")
                print(f"il reste {var_colors.res_pc}{vie_pc}{var_colors.reset} point de vie à l'ennemie \u2764\uFE0F ")
                print("----------------------------------------------------------")

                attaque_pc = random.randint(5 , 15)
                vie_player = vie_player - attaque_pc
                print("Vous passez Votre Tour ...")
                print(f"L'ennemie vous à infligé {var_colors.res_pc}{attaque_pc}{var_colors.reset}  points de dégats \U0001F4A5")
                print(f"il vous reste {var_colors.res_player}{vie_player}{var_colors.reset} point de vie. \u2764\uFE0F")
                print(f"il reste {var_colors.res_pc}{vie_pc}{var_colors.reset} point de vie à l'ennemie \u2764\uFE0F ")
                

            else:
                print("Vous n'avez plus de potion !\u274C\uFE0F")
                continue
      

  
