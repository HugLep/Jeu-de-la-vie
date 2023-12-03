# Jeu-de-la-vie - Python
En 1970, John Horton Conway a conceptualisé le Jeu de la Vie, un automate cellulaire. Il s'agit d'une simulation mathématique captivante.

![image](https://github.com/HugLep/Jeu-de-la-vie/assets/55044990/2a1b714f-1e8e-4269-aaae-5441fe12fe3c)

## Comment jouer ?
1. Exécuter le programme : *main.py*
2. Un page va s'ouvrir et vous pourrez modifier l'état d'une cellule en cliquant sur la case, appuyer sur *Evolution* pour évoluer la simulation, ou appuyer sur *clear* pour réinitialisé toutes les cellules.
   À l'ouverture il y a déjà un planeur, appuyer plusieurs fois sur *Evolution* pour comprendre ce qu'il peut faire.
3. Si vous voulez changer le nombre de cases vous pouvez ouvrir le programme *main.py* et modifier : *NBj* pour changer le nombre de colonnes et *NBi* pour changer le nombre de lignes.


## Règles
- Si une cellule morte possède 3 cellules voisines elle deviendra elle naitra.
- Si une cellule vivante possède 2 ou 3 cellules voisines elle reste vivante.
- Si une cellule vivante possède 1 ou plus de 3 cellules voisines elle meurt.

## Structures
- les structures stables
  
    ![image](https://github.com/HugLep/Jeu-de-la-vie/assets/55044990/b5168b7f-62cd-4998-844d-34e0313d1829)
  
- les structures périodiques, ou oscillateurs
- les vaisseaux
- les mathusalems
- bloc de quatre cellules
- les puffeurs
- les canons
- les jardins d’Éden
- les spacefillers
