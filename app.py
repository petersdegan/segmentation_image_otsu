import numpy as np
import matplotlib.pyplot as plt
import cv2

# Charger l'image en niveaux de gris il ne sera pas lu en BGR mais en niveaux de gris 
image = cv2.imread("gazelle.jpg", cv2.IMREAD_GRAYSCALE)

# Appliquer le seuillage d'Otsu 
# ret, seuil = cv2.threshold(image, seuil_initial, valeur_max, type_seuillage) les parametres de la fonction threshold
seuil_de_otsu, seuil = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Afficher la valeur du seuil trouvé par Otsu
print(f"Seuil trouvé par la méthode Otsu : {seuil_de_otsu}")

# Affichage des images sur une figure  de largeur  10  et de hauteur 4 pouces 
plt.figure(figsize=(10, 4))

#   l'image originale en niveaux de gris de ligne 1 , de colonne 3 et d'index 1 
plt.subplot(1, 3, 1)

"""le fait d'utiliser cmap= gray fais que les pixels de couleur noir seront soir
c'est a dire 0, les pixels de couleur blanc
seront blanc 255 et les autres seront affichées en nuance  de gris """ 
plt.imshow(image, cmap="gray")
plt.title("Image en niveau de gris ")
#les axes seront invisibles 
plt.axis("off")

#  Affichage de l'image obtenu apres méthode d'Otsu de ligne 1 de colonne 3 et d'index 3
plt.subplot(1, 3, 3)
plt.imshow(seuil, cmap="gray")
plt.title("Image après seuillage de la méthode d'Otsu")

plt.axis("off")

# Affichage de la figure avec les deux graphes 
plt.show()
