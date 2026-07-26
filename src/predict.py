import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the model only once
model = tf.keras.models.load_model("model/plant_disease_model.keras")
print(model.summary())

class_names = [
    "Pepper__bell___Bacterial_spot",
    "Pepper__bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Tomato_Bacterial_spot",
    "Tomato_Early_blight",
    "Tomato_Late_blight",
    "Tomato_Leaf_Mold",
    "Tomato_Septoria_leaf_spot",
    "Tomato_Spider_mites_Two_spotted_spider_mite",
    "Tomato__Target_Spot",
    "Tomato__Tomato_YellowLeaf__Curl_Virus",
    "Tomato__Tomato_mosaic_virus",
    "Tomato_healthy"
]

def predict_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)

# Do NOT preprocess here.
# The model already contains the Rescaling layer.
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array, verbose=0)

    print("Image shape:", img_array.shape)
    print("Prediction:", prediction)
    print("Predicted index:", np.argmax(prediction))

    top5 = np.argsort(prediction[0])[-5:][::-1]

    print("\nTop 5 predictions:")
    for i in top5:
        print(f"{class_names[i]} : {prediction[0][i]*100:.2f}%")

    predicted_class = top5[0]
    confidence = float(np.max(prediction) * 100)

    return class_names[predicted_class], confidence