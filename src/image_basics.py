from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

image = Image.open("assets/test_leaf.jpg")

image = image.resize((224,224))

image_array = np.array(image)

print("Before Normalization")
print(image_array.min(), image_array.max())

image_array = image_array / 255.0

print("After Normalization")
print(image_array.min(), image_array.max())

plt.imshow(image_array)
plt.axis("off")
plt.show()