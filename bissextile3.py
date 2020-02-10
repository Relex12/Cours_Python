def bissextile (annee):
    annee = int(annee)
    if annee % 4 == 0:
        if annee % 100 == 0:
            if annee % 400 == 0:
                bissextile = True
            else:
                bissextile = False
        else:
            bissextile = True
    else:
        bissextile = False
    print (bissextile)
