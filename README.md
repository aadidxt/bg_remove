# 🪄 AI Background Remover

A full-stack web application that removes image backgrounds using deep learning.  
Users can upload an image, process it using an AI model, and download the result with a transparent background.

---

## 🚀 Features

- 📁 Upload image (JPG, PNG)
- 🧠 AI-based background removal
- ⚡ Fast processing using Python backend
- 🖼 Preview original and processed image
- ⬇ Download final output (PNG with transparent background)
- 🌐 CORS-enabled API for frontend-backend communication

---

## 🛠 Tech Stack

### Frontend
- HTML
- CSS
- JavaScript (Fetch API)

### Backend
- Python
- Flask

### AI Model
- rembg (uses U²-Net for background removal)

---

## 📂 Project Structure

project/
│
├── app.py # Flask backend
├── index.html # Frontend UI
├── requirements.txt # Python dependencies
└── venv/ # Virtual environment


---

## ⚙️ Setup Instructions (SOP)

### 1️⃣ Clone the Repository


git clone <your-repo-link>
cd project


---

### 2️⃣ Create Virtual Environment


python -m venv venv


Activate:

**Windows:**

venv\Scripts\activate


---

### 3️⃣ Install Dependencies



pip install flask flask-cors rembg[cpu]


---

### 4️⃣ Run Backend Server


python app.py


Server will start at:

http://127.0.0.1:5000


---

### 5️⃣ Run Frontend

- Open `index.html` in browser  
OR  
- Use Live Server in VS Code  

---

### 6️⃣ Use the Application

1. Upload an image  
2. Click "Remove Background"  
3. Wait for processing  
4. Download result  

---

## 🔄 How It Works

1. User uploads image via frontend  
2. JavaScript sends image using `fetch()`  
3. Flask receives image  
4. `rembg` processes it using U²-Net  
5. Background is removed  
6. Processed image is sent back  
7. Frontend displays and allows download  

---

## ⚠️ Notes

- First run may download AI model (~170MB)
- Ensure internet connection for first execution
- Use CPU version for simplicity (`rembg[cpu]`)

---

## 🧠 Statement of Purpose (SOP)

This project was developed to explore the integration of artificial intelligence with web technologies to solve real-world problems. The primary objective was to build a system capable of automatically removing backgrounds from images without requiring manual editing.

Through this project, I aimed to understand how deep learning models like U²-Net can be deployed in practical applications using a backend framework such as Flask. Additionally, the project demonstrates how frontend and backend systems communicate effectively using APIs.

This project also helped me gain hands-on experience in handling image data, managing virtual environments, and integrating machine learning models into web applications. It reflects my interest in full-stack development combined with artificial intelligence and showcases my ability to build end-to-end solutions.

Overall, this project represents my effort to bridge the gap between theoretical machine learning concepts and real-world implementation, making AI accessible and usable through simple web interfaces.

---

