---

# 🌟 Gemini Health App 🌟

Welcome to **Gemini Health App**! This AI-powered application leverages the Google Gemini Pro Vision API to analyze food items in uploaded images and provide detailed calorie information for each item. Whether you’re a nutritionist, fitness enthusiast, or simply curious about your meals, this app offers insightful nutritional data in seconds.

---

## 📖 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Example](#-example)
- [Tech Stack](#-tech-stack)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌐 Overview
The **Gemini Health App** uses advanced AI to detect and analyze food items from user-uploaded images, providing a breakdown of each item’s calorie count. Built with **Streamlit**, this web app is a friendly and efficient tool that integrates seamlessly with Google Gemini's cutting-edge vision and generative capabilities.

---

## 🚀 Features
- **Image Upload**: Upload images of food items and receive calorie information instantly.
- **Automatic Analysis**: The app identifies and categorizes each food item, displaying a detailed calorie count.
- **Clean UI**: Built on Streamlit, with an intuitive interface for easy use.
- **Error Handling**: Smooth experience with prompts and warnings to guide users.

---

## 🛠 Installation

### Prerequisites
- Python 3.7 or higher
- A Google Gemini Pro Vision API key

### Clone the Repository
```bash
git clone https://github.com/Lavishgangwani/Nutritionist-Generative-AI-Doctor-Using-Google-Gemini-Pro-Vision.git
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Set Up Environment Variables
Create a `.env` file in the project root and add your Google Gemini API key:
```bash
GOOGLE_API_KEY=your_google_gemini_api_key
```

---

## 🧑‍💻 Usage
1. **Start the Streamlit App**:
   ```bash
   streamlit run health.py
   ```

2. **Upload an Image**:
   - Click on **"Choose an image..."** to upload a photo of food items (supports `.jpg`, `.jpeg`, and `.png` formats).

3. **Get Calorie Breakdown**:
   - Click **"Tell me the total calories"** to receive a calorie breakdown for each item in the image.
   - The app will display a detailed response including calorie information for each detected item.

---

## 🎉 Example

### Input
- **Image**: Upload an image containing multiple food items (e.g., a plate with fruits, vegetables, and grains).

### Expected Output
```
1. Apple - 52 calories
2. Broccoli - 55 calories
3. Rice - 130 calories
----
Total Calories: 237 calories
```

---

## ⚙️ Tech Stack
- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: Python with [Pillow (PIL)](https://pillow.readthedocs.io/)
- **AI Model**: Google Gemini Pro Vision API

---

## 🤝 Contributing
We welcome contributions! Please follow these steps:

1. **Fork the repository**.
2. **Create a new branch** for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. **Commit your changes**:
   ```bash
   git commit -m "Add new feature"
   ```
4. **Push to your branch**:
   ```bash
   git push origin feature-name
   ```
5. **Create a Pull Request** on GitHub.

For major changes, please open an issue first to discuss your ideas.

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments
- Thanks to [Google Gemini Pro Vision](https://cloud.google.com/) for the API that powers this app.
- Built with [Streamlit](https://streamlit.io/) for quick and interactive data apps.

---

Happy calorie counting! 🍎🥦🍚

---

Feel free to personalize the repository links and other details to match your specific project setup. This README aims to be both informative and visually engaging for anyone exploring your project.
