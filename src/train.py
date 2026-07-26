import tensorflow as tf
from pathlib import Path

# ==========================
# Load Dataset
# ==========================

dataset_path = Path("data/PlantVillage")

train_dataset = tf.keras.utils.image_dataset_from_directory(
    dataset_path,
    validation_split=0.2,
    subset="training",
    seed=42,
    image_size=(224, 224),
    batch_size=32
)

validation_dataset = tf.keras.utils.image_dataset_from_directory(
    dataset_path,
    validation_split=0.2,
    subset="validation",
    seed=42,
    image_size=(224, 224),
    batch_size=32
)

# Print class names (VERY IMPORTANT)
class_names = train_dataset.class_names

print("\nTraining Classes:")
print(class_names)

print("\nValidation Classes:")
print(validation_dataset.class_names)

AUTOTUNE = tf.data.AUTOTUNE

train_dataset = train_dataset.prefetch(AUTOTUNE)
validation_dataset = validation_dataset.prefetch(AUTOTUNE)

# ==========================
# MobileNetV2
# ==========================

base_model = tf.keras.applications.MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights="imagenet"
)

# Freeze pretrained layers
base_model.trainable = False

# ==========================
# Build Model
# ==========================

model = tf.keras.Sequential([
    tf.keras.layers.Rescaling(scale=1./127.5, offset=-1),

    base_model,

    tf.keras.layers.GlobalAveragePooling2D(),

    tf.keras.layers.Dropout(0.2),

    tf.keras.layers.Dense(
    len(class_names),
    activation="softmax"
)
])

# ==========================
# Compile
# ==========================

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# ==========================
# Model Summary
# ==========================

model.summary()

# ==========================
# Train
# ==========================

history = model.fit(
    train_dataset,
    validation_data=validation_dataset,
    epochs=5
)

# ==========================
# Save
# ==========================

model.save("model/plant_disease_model.keras")

print("\n✅ Model saved successfully!")