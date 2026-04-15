# 🎬 Advanced Movie Recommender System

## 🖥️ Application Interface
![App UI](./ui.png)

## 📊 Sample Output
![Output](./output.png)

---

## 🚀 Overview
An advanced hybrid movie recommendation system that suggests movies using both content similarity and user behavior patterns.  
The system combines Content-Based Filtering and Collaborative Filtering to improve recommendation accuracy and provide meaningful suggestions.

---

## 🎯 Key Features
- Content-Based Filtering using TF-IDF and Cosine Similarity  
- Collaborative Filtering using user-item interactions  
- Hybrid recommendation model (weighted combination)  
- Real-time recommendations using Streamlit  
- Top-N personalized movie suggestions  

---

## ⚙️ How It Works

### Content-Based Filtering
- Extracts movie features such as genres  
- Converts text into vectors using TF-IDF  
- Computes similarity using cosine similarity  

### Collaborative Filtering
- Uses user ratings data  
- Builds interaction matrix  
- Identifies similar users/movies  

### Hybrid Model
Final Score = 0.6 × Content Score + 0.4 × CF Score  

---

## 🛠️ Tech Stack
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Streamlit  

---

## 📂 Project Structure

advanced-movie-recommender-system/
│
├── app.py
├── movies.pkl
├── requirements.txt
├── README.md
├── ui.png
└── output.png

---

## 💡 Business Impact
- Improves user engagement through personalized recommendations  
- Helps users discover relevant content  
- Demonstrates real-world recommender system design  

---

## 👨‍💻 Author
MANNETI YESWANTH REDDY  

---

## ⭐ If you like this project
Give it a star ⭐
