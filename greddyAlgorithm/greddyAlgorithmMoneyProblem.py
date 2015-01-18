def greedyMethod(moneySystem, giveBack, solution):
  if giveBack == 0:
    return solution
    while giveBack >= moneySystem[0]:
      giveBack -= moneySystem[0]
      solution.append(moneySystem[0])
  else:
    return greedyMethod(moneySystem[1:len(moneySystem)], giveBack, solution)

def retrievingData():
  moneySystem = input("Entrez le système monétaire de façon décroissante sous forme de liste (e.g. [200,100,50,20,10,5,2,1] pour le système européen)")
  giveBack = input("Entrez la somme à rendre")
  solution = []
  if moneySystem == [] or giveBack <= 0:
    print "Vous vous êtes trompé lors de l'encodage des données"
  else:
    return greedyMethod(moneySystem, giveBack, solution)

  print "Le choix proposé par la méthode gloutonne est :", retrievingData()
