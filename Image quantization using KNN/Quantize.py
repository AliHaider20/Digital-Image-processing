from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import cv2

img = plt.imread("nature.jpg")
img = cv2.resize(img, (500, 500))
print(img.shape)

(h, w, c) = img.shape
img2D = img.reshape(h * w, c)
print(img2D.shape)

Kmeans_model = KMeans(n_clusters=3)
cluster_labels = Kmeans_model.fit_predict(img2D)

print(cluster_labels)
labels_count = Counter(cluster_labels)
print(labels_count)
print(Kmeans_model.cluster_centers_)

rgb_colors = Kmeans_model.cluster_centers_.round(0).astype(int)
print(rgb_colors)


img_quant = np.reshape(rgb_colors[cluster_labels], (h, w, c))
plt.imshow(np.hstack([img, img_quant]))

plt.show()
