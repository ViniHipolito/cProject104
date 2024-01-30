import cv2
sistemasolar = cv2.imread("solar-system.jpg")

sol = "Sol"
mer = "Mercurio"
ve = "Venus"
te = "Terra"
mar = "Marte"
jup = "Jupiter"
sat = "Saturno"
ur = "Urano"
ne = "Neturno"


cv2.putText(sistemasolar,sol,(100, 80),fontFace=cv2.FONT_ITALIC,fontScale=2.5,color=(0,255,255))
cv2.putText(sistemasolar,mer,(110, 180),fontFace=cv2.FONT_ITALIC,fontScale=0.55,color=(255,255,255))
cv2.putText(sistemasolar,ve,(190, 265),fontFace=cv2.FONT_ITALIC,fontScale=0.55,color=(255,255,255))
cv2.putText(sistemasolar,te,(285, 170),fontFace=cv2.FONT_ITALIC,fontScale=0.55,color=(255,255,255))
cv2.putText(sistemasolar,mar,(380, 260),fontFace=cv2.FONT_ITALIC,fontScale=0.55,color=(255,255,255))
cv2.putText(sistemasolar,jup,(560, 50),fontFace=cv2.FONT_ITALIC,fontScale=0.8,color=(255,255,255))
cv2.putText(sistemasolar,sat,(760, 280),fontFace=cv2.FONT_ITALIC,fontScale=0.6,color=(255,255,255))
cv2.putText(sistemasolar,ur,(970, 140),fontFace=cv2.FONT_ITALIC,fontScale=0.7,color=(255,255,255))
cv2.putText(sistemasolar,ne,(1110, 285),fontFace=cv2.FONT_ITALIC,fontScale=0.6,color=(255,255,255))

cv2.imshow("Sistema Solar Nomeado e Mapeado",sistemasolar)

cv2.waitKey(0)