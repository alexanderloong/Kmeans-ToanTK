import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import random as rd

im = Image.open('image.jpg')
img_array = np.asarray(im, dtype ='int64')
      
height= len(img_array)
weight = len(img_array[0])

img_array = np.asarray(im)
img_array = np.reshape(img_array, (height * weight, 3))




def init_centroids(img, num_cluster):         # Khởi tạo 5 màu ban đầu
    ctr =[]
    for i in range(num_cluster):
        ctr.append([rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255)])

    ctr = np.array(ctr)


    return ctr


def point_group(imgarr, centroids): # Ảnh, điểm point cần xét, màu ban đầu

            
def kmeans(img, k_clusters, max_iter, init_centroids):
    height = len(img)
    weight = len(img[0])
    img_size = height * weight