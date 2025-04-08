# 🏔️ Nepal Earthquake Building Survival Prediction

This project focuses on predicting whether buildings in Nepal are likely to **survive a future earthquake** or not, based on various structural and geospatial attributes. The motivation stems from the devastating 2015 Nepal earthquake, and the goal is to build a predictive model that could potentially support better infrastructure planning and disaster preparedness.

## 📊 Project Overview

- **Data Source:** Open dataset on building damage after the Nepal earthquake.
- **Tech Stack:** SQL, Python (Pandas, Scikit-learn), Jupyter Notebook
- **Goal:** Build predictive models to classify buildings as "safe" or "unsafe" based on their features.

## ⚙️ Workflow

1. **SQL Data Preprocessing**
   - The raw data was originally provided in SQL format.
   - Initial processing and table joins were performed using SQL to ensure a clean and relational structure before importing into Python.

2. **Data Cleaning & Exploration (Python)**
   - Loaded SQL-processed data into a Jupyter Notebook using Pandas.
   - Handled missing values, encoded categorical variables, and explored correlations among features.

3. **Model Building**
   - Built and evaluated two machine learning models:
     - **Decision Tree Classifier**
     - **Logistic Regression**
   - Assessed performance using metrics such as accuracy, precision, recall, and confusion matrix.
   - Performed hyperparameter tuning and cross-validation to optimize model performance.

## 🧠 Features Used

Some of the building characteristics used in the model:
- Age of the building
- Structural type
- Number of floors
- Foundation type
- Position (e.g. corner, center)
- Area and height
- Geographic region

## 📈 Results

- The models demonstrated promising accuracy in classifying buildings based on risk level.
- Decision Tree offered better interpretability, while Logistic Regression performed well on generalization.

## 💡 Key Takeaways

- SQL was crucial for preparing and structuring relational data.
- Python and Scikit-learn provided flexibility for preprocessing and model evaluation.
- The project highlights how simple ML models can assist in life-saving predictions with the right data.

## 🚀 Future Improvements

- Integrate geospatial analysis for mapping risk zones.
- Experiment with advanced models like Random Forest or XGBoost.
- Deploy as a web app using Streamlit or Flask.

## 🤝 Contributions

Contributions, feedback, and suggestions are welcome! Feel free to fork the repo and open a pull request.

## 📜 License

This project is open-source and available under the MIT License.


