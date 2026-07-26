from src.predict import predict_image

disease, confidence = predict_image("test_images/tomato.jpg")

print("Disease:", disease)
print("Confidence:", confidence)
