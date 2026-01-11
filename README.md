# Customer Churn Prediction - ANN

A deep learning-based customer churn prediction system using Artificial Neural Networks (ANN) to predict whether a bank customer will leave or stay.

## 📋 Overview

This project uses a neural network model to predict customer churn based on customer demographics, account information, and banking behavior. The system includes an interactive Streamlit web application for real-time predictions.

## 🎯 Features

- **Neural Network Model**: TensorFlow/Keras-based ANN for churn prediction
- **Interactive Web App**: Streamlit interface for easy predictions
- **Data Processing**: Automated preprocessing with encoding and scaling
- **Real-time Predictions**: Instant churn probability estimates
- **Visual Results**: Risk gauge and probability metrics

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

### Prerequisites

- Python 3.8+
- pip package manager

### Installation

1. Clone the repository
```bash
git clone https://github.com/iGufrankhan/Customer-Churn-Prediction-ANN-.git
cd ANN_PROJECT
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

### Running the Application

Launch the Streamlit app:
```bash
streamlit run app.py
```

## 💻 Usage

The web application accepts the following customer inputs:
- **Credit Score** (300-900)
- **Geography** (France, Germany, Spain)
- **Gender** (Male, Female)
- **Age** (18-100)
- **Tenure** (0-10 years)
- **Balance** ($0-$300,000)
- **Number of Products** (1-4)
- **Has Credit Card** (Yes/No)
- **Is Active Member** (Yes/No)
- **Estimated Salary** ($0-$200,000)

The model returns a churn probability percentage and risk classification.

## 📊 Model Details

- **Type**: Sequential Neural Network
- **Framework**: TensorFlow/Keras
- **Input Features**: 10 customer attributes
- **Output**: Binary classification (Churn/No Churn)
- **Preprocessing**: OneHotEncoding, LabelEncoding, StandardScaling

## 🛠️ Technologies Used

- **TensorFlow 2.15.0** - Deep learning framework
- **Streamlit** - Web application framework
- **Pandas** - Data manipulation
- **Scikit-learn** - Data preprocessing
- **NumPy** - Numerical computations
- **Matplotlib** - Data visualization
- **TensorBoard** - Model training visualization

## 📈 Development

- `experiments.ipynb`: Contains model training, data exploration, and experimentation
- `predicatopn.ipynb`: Testing and validation of predictions
- `logs/`: TensorBoard logs for monitoring training progress

## 📝 License

This project is open source and available for educational purposes.

## 👤 Author

**Gufran Khan**
- GitHub: [@iGufrankhan](https://github.com/iGufrankhan)
