# Multiple-Linear-Regression-2

# 🏠 Housing Prices - Multiple Linear Regression

This project implements a **Multiple Linear Regression** model to predict housing prices using a dataset with both numerical and categorical features. The dataset includes missing values that are imputed and categorical values that are encoded.

---

## 📂 Dataset

A sample housing dataset with the following columns:

- `ID`: Unique identifier
- `Area (sq ft)`: Size of the house
- `Bedrooms`: Number of bedrooms
- `Location`: Categorical (Downtown, Suburb, Uptown)
- `Age (Years)`: Age of the house
- `Garage`: Categorical (Yes/No)
- `Price (USD)`: Target variable

Some rows contain missing values.

---

## ⚙️ Features

- 📉 Imputation of missing numerical and categorical data
- 🔁 One-Hot Encoding of categorical variables (`Location`, `Garage`)
- ✂️ Train-Test split (80/20)
- 🧠 Linear Regression model training and prediction
- 📊 Output comparison of predicted vs actual prices

---

## 🧪 Requirements

```bash
pip install numpy pandas scikit-learn matplotlib

🧑‍💻 Author
Adityaa Bandaru
