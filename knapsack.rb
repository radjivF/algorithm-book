def knapSack(totalWeight, objects):
2    currentWeight = 0
3    subSet = []
4    for counter in range(len(objects):
5        if currentWeight + objects[counter][-1] <= totalWeight:
6            currentWeight += objects[counter][-1]
7            subSet.append(objects[counter])
8        return subSet
9
10def retrivevingData():
11    objects = input("Veuillez entrer le set d'objets sous la forme \"liste de liste\" (e.g. [[objet1, valeur1, poids1],[objet2,valeur2,poids2]]) par ordre décroissant de valeur :")
12    totalWeight = input("Veuillez entrer la capacité maximale de votre sac à dos :")
13    return knapSack(totalWeight, objects):
14
15print "La proposition de la méthode gloutonne est :", retrievingData()
