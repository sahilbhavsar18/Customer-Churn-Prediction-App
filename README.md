# 🔮 Telco Customer Churn Prediction

An end-to-end Machine Learning web application designed to predict whether a customer will leave the company (Churn).

## 🚀 Key Features
* **High Recall Model:** Tuned AdaBoost Classifier achieving **77% Recall**, ensuring the majority of at-risk customers are identified.
* **Interactive Frontend:** Built with Streamlit for easy, real-time predictions.
* **Smart Preprocessing:** Handles missing values and scales inputs automatically.
* **Business Logic:** Prioritizes "Catching Churners" (False Positives accepted) over missing them (False Negatives).

## 🛠️ Tech Stack
* **Language:** Python
* **Machine Learning:** Scikit-Learn (AdaBoost, Decision Trees, GridSearchCV)
* **Frontend:** Streamlit
* **Data Processing:** Pandas, NumPy

## 📊 Model Performance
* **Accuracy:** 77%
* **Recall (Churners):** 77%
* **ROC-AUC Score:** 0.76

## 📸 Screenshots
<img width="1131" height="865" alt="image" src="https://github.com/user-attachments/assets/b4ccfdfa-85f4-4a69-82e4-a83d425f6ee6" />
<img width="1101" height="897" alt="image" src="https://github.com/user-attachments/assets/60686525-24fe-4213-b585-a3dcd49d0156" />
<img width="953" height="890" alt="image" src="https://github.com/user-attachments/assets/0184f0b8-cb5b-4b4a-bd59-8f105e866a43" />
<img width="1121" height="883" alt="image" src="https://github.com/user-attachments/assets/5264ee40-b14e-451e-b29a-55121fb29553" />


## 📦 How to Run
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`
