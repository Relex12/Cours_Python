def entrez_numero:
	x = imput ("Entrez un numéro entre 0 et 49 compris")
	try:
		int(x)
	except Exception as e:
		raise
	return x


print ("Bienvenue dans le jeu du ZCasino, ici on joue à la roulette")
print ("Le ZCasino vous donne 50$, ce sera votre somme de départ")
somme_joueur = 50

while continue:
	num_parie = entrez_numero()
	num_bille = 
