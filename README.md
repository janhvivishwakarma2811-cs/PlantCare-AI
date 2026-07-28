🌿 PlantCare AI - Plant Disease Detection System

An AI-powered web application that detects plant diseases from leaf images using Deep Learning. Users can upload a plant leaf image and instantly receive the predicted disease, confidence score, and treatment/prevention recommendations.

## 🚀 Live Demo

🔗 https://plantcare-ai-production-983d.up.railway.app/

## 📂 GitHub Repository

🔗 https://github.com/janhvivishwakarma2811-cs/PlantCare-AI

---

📖 Overview

Plant diseases can significantly reduce crop yield if not identified early. This project uses a Convolutional Neural Network (CNN) trained on the PlantVillage dataset to classify plant leaf diseases.

The application provides:

- 🌿 Disease prediction
- 📊 Confidence score
- 📝 Disease description
- 💊 Treatment suggestions
- 🛡 Prevention tips

---

✨ Features

- Upload plant leaf images
- AI-powered disease prediction
- Confidence percentage
- Disease information
- Treatment recommendations
- Prevention methods
- Clean and responsive web interface
- Deployed online using Railway

---

🧠 Model Information

- Framework: TensorFlow / Keras
- Architecture: Convolutional Neural Network (CNN)
- Dataset: PlantVillage
- Image Size: 224 × 224
- Model Format: `.keras`

### Supported Classes

- Pepper Bell Bacterial Spot
- Pepper Bell Healthy
- Potato Early Blight
- Potato Late Blight
- Potato Healthy
- Tomato Bacterial Spot
- Tomato Early Blight
- Tomato Late Blight
- Tomato Leaf Mold
- Tomato Septoria Leaf Spot
- Tomato Spider Mites
- Tomato Target Spot
- Tomato Yellow Leaf Curl Virus
- Tomato Mosaic Virus
- Tomato Healthy

---

🛠 Tech Stack

### Backend
- Python
- Flask

### Machine Learning
- TensorFlow
- Keras
- NumPy

### Frontend
- HTML
- CSS

### Deployment
- Railway

### Version Control
- Git
- GitHub

---

📁 Project Structure

```
PlantCare-AI/
│
├── app.py
├── requirements.txt
├── runtime.txt
├── README.md
│
├── model/
│   └── plant_disease_model.keras
│
├── src/
│   ├── predict.py
│   ├── train.py
│   ├── load_data.py
│   └── disease_info.py
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── style.css
│
├── uploads/
│
└── data/
    └── PlantVillage/
```

---

⚙ Installation

### Clone the repository

```bash
git clone https://github.com/janhvivishwakarma2811-cs/PlantCare-AI.git

cd PlantCare-AI
```

### Create a virtual environment

Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

## 📷 How to Use

1. Open the web application.
2. Upload a plant leaf image.
3. Click **Predict Disease**.
4. View:
   - Disease name
   - Confidence score
   - Disease description
   - Treatment recommendations
   - Prevention tips

---

📸 Screenshots

### Home Page

> Add a screenshot here.

### Prediction Result

> Add a screenshot here.

---

📊 Dataset

**PlantVillage Dataset**

Contains over 20,000 labeled images of healthy and diseased plant leaves.

---

🔮 Future Improvements

- Support more crop species
- Mobile-friendly interface
- Camera capture support
- Grad-CAM visualization for model explanations
- Improved model using transfer learning (MobileNetV2/EfficientNet)
- REST API for mobile applications

---

👩‍💻 Author

**Janhvi Vishwakarma**

GitHub: https://github.com/janhvivishwakarma2811-cs

LinkedIn: *(Add your LinkedIn profile here)*

---

📄 License

This project is intended for educational and portfolio purposes.
