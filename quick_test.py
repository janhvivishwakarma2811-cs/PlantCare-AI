import tensorflow as tf
import numpy as np
from pathlib import Path

model = tf.keras.models.load_model("model/plant_disease_model.keras")

dataset = tf.keras.utils.image_dataset_from_directory(
    "data/PlantVillage",
    validation_split=0.2,
    subset="validation",
    seed=42,
    image_size=(224, 224),
    batch_size=1,
    shuffle=False
)

class_names = dataset.class_names

for images, labels in dataset.take(5):
    prediction = model.predict(images, verbose=0)

    print("True:", class_names[labels.numpy()[0]])
    print("Predicted:", class_names[np.argmax(prediction)])
    print()