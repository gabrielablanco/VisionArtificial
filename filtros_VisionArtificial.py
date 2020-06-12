from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
import random
import math

def añadir_filtro(mascara, decision, txt):
    fila = matriz.shape[0]-mascara.shape[0]+1
    columnas = matriz.shape[1]-mascara.shape[1]+1
    m_aux = np.zeros((fila, columnas))
    #mascara_f = np.rot90(np.rot90(mascara))

    for i in range (0, m_aux.shape[0]):
        for j in range (0, m_aux.shape[1]):
            imagen2 = matriz[i:i+len(mascara), j:j+len(mascara)]
            m_aux[i][j] = ((mascara*imagen2).sum())//9
    
    if(decision == True): 
        m_aux2 = Image.fromarray(m_aux)
        m_final = m_aux2.convert("RGB")
        print('\n\n' ,txt)
        imprimir_imagenes(m_final)
        return m_aux
    else:
        print('\n\n', txt)
        imprimir_imagenes(m_aux) 
        return m_aux
    
    #print(m_aux)
    #desenfocar_funcion = ndimage.gaussian_filter(matriz, sigma=5) #Funcion desenfocar
    #imprimir_imagenes(desenfocar_funcion)
    #aux = 0
    #for a in range(0,3):
     #   for b in range (0,3):
     #       aux += (m_aux[a][b]*mascara[a][b])
            #print(aux)
    #aux = aux//9
    #print(aux)
    #imagen2[i+1][j+1] = aux
    #print(imagen2)

def raiz_cuadrada(m):
    fila = m.shape[0]
    columnas = m.shape[1]
    m_aux = np.zeros((fila, columnas))
    for i in range (0, fila-2):
        for j in range (0, columnas-2):
            m_aux[i][j] = math.sqrt(m[i][j])
    return m_aux

def imprimir_imagenes(m_aux):
    plt.imshow(m_aux, cmap = "gray")
    #plt.xticks([]), plt.yticks([])
    plt.show()

imagen_o = Image.open('img_persona.jpg')
imagen = imagen_o.convert("L")
matriz = np.asarray(imagen) #Guarda la imagen en un arreglo de numpy
print('\n\nImagen original')
imprimir_imagenes(imagen_o)
print('\n\nDetección de bordes Sobel (visto en clase)')
mascara = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]) #Detección de bordes Gx
gx = añadir_filtro(mascara, True, '1. Deteccion bordes vertical')
mascara = np.array([[1, 2, 1],[0, 0, 0],[-1, -2, -1]]) #Detección de bordes Gy
gy = añadir_filtro(mascara, True, '2. Deteccion bordes horizontal')
gt = ((gx**2)+(gy**2))
Gt = raiz_cuadrada(gt)
print('\n\n3. Bordes verticales y horizontales')
imprimir_imagenes(Gt)
print('Detección de bordes Prewitt (Propuesto)')
mascara = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]]) #Detección de bordes Gx
gx = añadir_filtro(mascara, True, '1. Deteccion bordes vertical')
mascara = np.array([[1, 0, -1],[1, 0, -1],[1, 0, -1]]) #Detección de bordes Gy
gy = añadir_filtro(mascara, True, '2. Deteccion bordes horizontal')
gt = ((gx**2)+(gy**2))
Gt = raiz_cuadrada(gt)
print('\n\n3. Bordes verticales y horizontales')
imprimir_imagenes(Gt)
mascara = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) #Enfoque
añadir_filtro(mascara, False, 'Filtro enfoque')
mascara = np.array([[-2, -1, 0],[-1, 1, 1],[0, 1, 2]]) #Repujado
añadir_filtro(mascara, False, 'Filtro repujado')


#print(matriz.shape)
#for i in range(0,915):
 #   for j in range(0, 915):
  #      m_aux = matriz[i:i + 3][j:j + 3]
   #     añadir_filtro(m_aux, mascara, i, j)
    #    m_aux = np.zeros((3,3))

#imprimir_imagenes()
#print('\n\nMatriz original\n')
#print(matriz)
