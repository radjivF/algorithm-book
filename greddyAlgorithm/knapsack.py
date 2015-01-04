def knapSack(totalWeight, objects):
	currentWeight = 0
	subSet = []
	for counter in range(len(objects):
		if currentWeight + objects[counter][-1] <= totalWeight:
			currentWeight += objects[counter][-1]
			subSet.append(objects[counter])
        return subSet

def retrivevingData():
	objects = input("Veuillez entrer le set d'objets sous la forme \"liste de liste\" (e.g. [[objet1, valeur1, poids1],[objet2,valeur2,poids2]]) par ordre décroissant de valeur :")
	totalWeight = input("Veuillez entrer la capacité maximale de votre sac à dos :")
	return knapSack(totalWeight, objects):

print "La proposition de la méthode gloutonne est :", retrievingData()
