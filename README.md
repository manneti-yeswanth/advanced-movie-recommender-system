# 🎬 Advanced Movie Recommender System

> 🚀 A production-style hybrid recommendation system combining Machine Learning techniques to deliver personalized movie suggestions.

---

## 📸 Demo

### 🖥️ Application Interface

![App UI](./ui.png)

### 📊 Recommendation Output

![Output](./output.png)

---

## 🚀 Project Overview

This project builds a **hybrid movie recommendation system** that combines:

* 🎯 Content-Based Filtering
* 🤝 Collaborative Filtering

to generate **high-quality personalized recommendations**.

The system integrates multiple techniques into a **single intelligent pipeline**, improving accuracy and real-world usability.

---

## 🎯 Problem Statement

Traditional recommendation systems rely on a single approach, leading to limited accuracy and personalization.

This project solves that by combining multiple techniques into a hybrid system that produces more reliable recommendations.

---

## 📂 Dataset

The system uses movie metadata such as:

* Genres
* Movie titles
* User interaction data

These features help capture both **content similarity** and **user behavior patterns**.

---

## ⚙️ How It Works

1. User selects a movie in the Streamlit UI
2. Content similarity is computed using TF-IDF
3. Collaborative similarity is computed using user interaction data
4. Hybrid score is calculated
5. Top-N recommended movies are displayed

---

## 🧠 Core Idea

Final Recommendation Score:

👉 **0.6 × Content Score + 0.4 × Collaborative Score**

✔ Combines strengths of both methods
✔ Improves recommendation quality
✔ More realistic system design

---

## ⚙️ System Architecture

### 🔹 Content-Based Filtering

* TF-IDF vectorization on movie features
* Cosine similarity computation

---

### 🔹 Collaborative Filtering

* User-item interaction matrix
* Behavioral similarity learning

---

### 🔹 Hybrid Engine

* Weighted combination of both models
* Handles missing similarity values
* Generates Top-N recommendations

---

## 🎯 Key Features

✔ Hybrid recommendation system
✔ Real-time recommendations using Streamlit
✔ Handles missing data effectively
✔ Interactive UI
✔ Scalable architecture

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit

---

## 📊 Results & Output

* Generates Top-N personalized movie recommendations
* Improves recommendation relevance compared to single-method systems
* Demonstrates practical hybrid modeling approach

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

## 💼 Business Impact

* 🎯 Improves user engagement
* 📈 Enhances recommendation quality
* 💡 Applicable to platforms like Netflix, Amazon, Spotify
* 🧠 Demonstrates real-world ML system design

---

## 🔥 Why This Project Stands Out

✔ Hybrid ML approach (advanced concept)
✔ End-to-end pipeline (data → model → UI)
✔ Combines ML + product thinking
✔ Practical and industry-relevant

---

## 👨‍💻 Author

**Yeshwanth Reddy M**
🔗 GitHub: https://github.com/manneti-yeswanth
🔗 LinkedIn: www.linkedin.com/in/manneti-yeswanth-reddy-2758693b6
