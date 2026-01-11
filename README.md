<div align="center">

# 🎯 Customer Churn Prediction - ANN

### *Predict Customer Churn with Deep Learning*

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://hsxvhkpisqglgcjn3jpts9.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.18+-orange.svg)](https://www.tensorflow.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

[🚀 Live Demo](https://hsxvhkpisqglgcjn3jpts9.streamlit.app/) | [📖 Documentation](#-features) | [🤝 Contributing](#-author)

---

</div>

## 📋 Overview

A powerful **deep learning-based customer churn prediction system** using Artificial Neural Networks (ANN) to predict whether a bank customer will leave or stay. Built with TensorFlow and deployed on Streamlit Cloud for real-time predictions.

🔗 **Try it live:** [https://hsxvhkpisqglgcjn3jpts9.streamlit.app/](https://hsxvhkpisqglgcjn3jpts9.streamlit.app/)

### 🎯 What is Customer Churn?

Customer churn refers to when customers stop doing business with a company. This project helps banks identify at-risk customers before they leave, enabling proactive retention strategies.

---

## ✨ Features

<table>
<tr>
<td>

### 🧠 **Machine Learning**
- Advanced ANN architecture
- 10 input features
- Binary classification
- Real-time inference

</td>
<td>

### 🎨 **User Interface**
- Interactive Streamlit app
- Clean, modern design
- Real-time predictions
- Visual risk indicators

</td>
</tr>
<tr>
<td>

### 📊 **Data Processing**
- Automated preprocessing
- OneHot & Label encoding
- Standard scaling
- Feature engineering

</td>
<td>

### 🚀 **Deployment**
- Cloud-hosted on Streamlit
- Zero setup required
- Instant predictions
- Accessible anywhere

</td>
</tr>
</table>

---

## 📂 Project Structure

```
├── app.py                      # Streamlit web application
├── experiments.ipynb           # Model training and experimentation
├── predicatopn.ipynb          # Prediction testing notebook
├── model.h5                   # Trained ANN model
├── Churn_Modelling.csv        # Dataset
├── requirements.txt           # Python dependencies
└── logs/                      # TensorBoard training logs
```

## 🚀 Getting Started

### 🌐 Online Demo

No installation required! Try the live app: **[https://hsxvhkpisqglgcjn3jpts9.streamlit.app/](https://hsxvhkpisqglgcjn3jpts9.streamlit.app/)**

### 💻 Local Setup

#### Prerequisites

- Python 3.8+
- pip package manager

#### Installation

1. **Clone the repository**
```bash
git clone https://github.com/iGufrankhan/Customer-Churn-Prediction-ANN-.git
cd Customer-Churn-Prediction-ANN-
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 💻 Usage

### Input Features

The web application accepts the following customer inputs:

| Feature | Range/Options | Description |
|---------|---------------|-------------|
| 💳 **Credit Score** | 300-900 | Customer's credit score |
| 🌍 **Geography** | France, Germany, Spain | Customer's country |
| 👤 **Gender** | Male, Female | Customer's gender |
| 📅 **Age** | 18-100 | Customer's age |
| ⏱️ **Tenure** | 0-10 years | Years with the bank |
| 💰 **Balance** | $0-$300,000 | Account balance |
| 📦 **Products** | 1-4 | Number of bank products |
| 🏧 **Credit Card** | Yes/No | Has credit card |
| ⭐ **Active Member** | Yes/No | Is active member |
| 💵 **Salary** | $0-$200,000 | Estimated salary |

### Output

The model provides:
- **Churn Probability**: Percentage likelihood of customer leaving (0-100%)
- **Risk Classification**: 🔴 High Risk or 🟢 Low Risk
- **Visual Indicators**: Progress bar and metrics dashboard

---

## 📊 Model Details

- **Type**: Sequential Neural Network
- **Framework**: TensorFlow/Keras
- **Input Features**: 10 customer attributes
- **Output**: Binary classification (Churn/No Churn)
- **Preprocessing**: OneHotEncoding, LabelEncoding, StandardScaling

## 🛠️ Technologies Used

<div align="center">

| Technology | Purpose |
|------------|---------|
| ![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white) | Deep Learning Framework |
| ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) | Web Application |
| ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) | Data Manipulation |
| ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) | Preprocessing & ML |
| ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) | Numerical Computing |
| ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white) | Visualization |

</div>

---

## 📈 Development

- `experiments.ipynb`: Contains model training, data exploration, and experimentation
- `predicatopn.ipynb`: Testing and validation of predictions
- `logs/`: TensorBoard logs for monitoring training progress

---

## 🌟 Key Highlights

- ✅ **Deployed on Streamlit Cloud** - Live and accessible 24/7
- ✅ **Production-Ready** - Optimized for real-time predictions
- ✅ **User-Friendly** - Intuitive interface with visual feedback
- ✅ **Scalable Architecture** - Built with modern ML practices
- ✅ **Well-Documented** - Comprehensive code and README

---

## 📝 License

This project is open source and available for educational purposes.

## 👤 Author

**Gufran Khan**
- GitHub: [@iGufrankhan](https://github.com/iGufrankhan)
