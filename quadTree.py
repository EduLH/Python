import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def verifPoint (img, x, y):
    med = img[x-1][y+1] + img[x][y+1] + img[x-1][y+1]
    med = med + img[x-1][y] + img[x+1][y]
    med = med +img[x-1][y-1] + img[x][y-1] + img[x-1][y-1]
    if ((med/8) > (img[x][y]+63)):  #valor teste de 63 tons de cinza
        return true
    else:
        return false
#

def PintaPreto(img, x, y):
    for j in range(y, y+3):
        for i in range(x, x+3):
            img[x][y] = 255
#

def verifQuad(img, res, larg, alt, x, y):
    # 1 2    Ordem dos quadrantes
    # 3 4
    #N_Quadrante
    prim_quad = [x,y]
    segu_quad = [x, y+(larg/2)]
    terc_quad = [x+(alt/2), y]
    quar_quad = [x+(alt/2), y+(larg/2)]

    #N_mudanca
    prim_mud = false #verifica se ouve mudança no quadrante
    segu_mud = false
    terc_mud = false
    quar_mud = false

    #scan de cada pixel do quadrante
    for i in range(0,(alt/2)-2):
        for j in range(0,(larg/2)-2):
            prim_mud = verifPoint(img, prim_quad[0]+j, prim_quad[1]+i)
            segu_mud = verifPoint(img, segu_quad[0]+j, segu_quad[1]+i)
            terc_mud = verifPoint(img, terc_quad[0]+j, terc_quad[1]+i)
            quar_mud = verifPoint(img, quar_quad[0]+j, quar_quad[1]+i)

    if(alt>6 and larg>6):
        if(prim_mud = True)
            verifQuad(img, res, larg, alt, x, y)
        if(segu_mud = True)
            verifQuad(img, res, larg, alt, x, (y+larg))
        if(terc_mud = True)
            verifQuad(img, res, larg, alt, (x+alt), y)
        if(quar_mud = True)
            verifQuad(img, res, larg, alt, (x+alt), (y+larg))

    if(alt <= 6 or larg <= 6):
        PintaPreto(res, x, y)
#

plt.rcParams["axes.grid"] = False

img = cv.imread('/home/eduardo/Área de Trabalho/coins.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imwrite('gray_image.png',gray)

size = np.shape(np.copy(img))
larg = size[1]
altu = size[0]
res = np.ones(larg, altu)
verifQuad(gray, , larg, altu, 0, 0)

cv.imshow('gray_image',gray)
cv.imshow('color_image', res)
