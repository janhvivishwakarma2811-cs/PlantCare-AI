import tensorflow as tf
from pathlib import Path

# Load model
model = tf.keras.models.load_model("model/plant_disease_model.keras")

# Load validation dataset
dataset_path = Path("data/PlantVillage")

validation_dataset = tf.keras.utils.image_dataset_from_directory(
    dataset_path,
    validation_split=0.2,
    subset="validation",
    seed=42,
    image_size=(224, 224),
    batch_size=32
)

loss, accuracy = model.evaluate(validation_dataset)

print(f"\nValidation Accuracy: {accuracy:.4f}")
print(f"Validation Loss: {loss:.4f}")