import streamlit as st
import cv2
import numpy as np
from PIL import Image

#on uploade un fichier image
fichier_image_telecharger = st.file_uploader("Entrez une image", type=['jpg', 'jpeg', 'png'])


if fichier_image_telecharger is not None:
    # Charger l'image avec PIL
    image = Image.open(fichier_image_telecharger)
    
    #Tranformation de l'image en tableau numpy   
    fabr=np.array(image)
    
    # OpenCv utilise  des tableaux Numpy  ce qui justifie la conversion en tableau avec la methode array 
    #OpenCv manipule les images en (BGR Blue Green Red)
    #le seuillage d'Otsu ne marche que sur des images en niveaux de gris
    

    # Convertir l'image en niveaux de gris avec OpenCV grace a cv2.COLOR_RGB2GRAY qui transforme l'image en niveaux de gris  et aussi cvtColor()
    image_converti = cv2.cvtColor(fabr, cv2.COLOR_RGB2GRAY)

    #Appliquer le seuillage d'Otsu  0 pour noir 255 pour blanc le seuil sera calculé pour chaque image 
    #il faut remarquer tous les pixels inférieur au seuil  deviennent noirs les autres supérieurs blancs si le pixel est gris pas de changement 

      
    
    seuil_de_otsu, seuil = cv2.threshold(image_converti, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    #on affiche  le seuil d'Otsu calculée pour chaque image 
    st.write("le seuil de Otsu pour cette image est",seuil_de_otsu)

    
    st.image(image, caption="Image originale")
    st.image(seuil, caption="Image après seuillage d'Otsu")

      