import cv2
import matplotlib.pyplot as plt
import numpy as np


def inverter(image):
    w,h,_ = image.shape

    for u in range(w):
        for v in range(h):
            p = image[u,v] # Obtiene el pixel
            image[u,v] = 255 - p # invierte su valor restando 255 menos el valor original

    return image


if __name__ == '__main__':

    img1 = cv2.imread('assets/1.jpeg')
    img2 = cv2.imread('assets/2.png')
    img2 = cv2.resize(img2,None,fx=0.5,fy=0.5, interpolation=cv2.INTER_CUBIC)

    cv2.imshow('Imagen 1', img1)
    cv2.imshow('Imagen 2', img2)
    
    img1 = inverter(img1)
    img2 = inverter(img2)
    cv2.imshow('Image Inverted 1', img1)
    cv2.imshow('Image Inverted 2', img2)
    # print(img1,'\n')
    # print(img2)
    cv2.waitKey()