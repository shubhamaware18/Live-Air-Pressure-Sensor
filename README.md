# Automatic Air Pressure System (APS) Sensor Fault Detection for Heavy Vehicles

An end-to-end machine learning project for detecting **Air Pressure System (APS) related faults in heavy vehicles** using sensor data.

The primary objective is to identify APS-related failures while minimizing the **business cost of misclassification**, with particular emphasis on reducing false negatives because missing an actual APS failure is significantly more expensive than an unnecessary inspection.

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Problem Statement](#problem-statement)
- [Business Objective](#business-objective)
- [Cost of Misclassification](#cost-of-misclassification)
- [Total Business Cost](#total-business-cost)
- [Machine Learning Objective](#machine-learning-objective)
- [Project Workflow](#project-workflow)
- [Machine Learning Pipeline](#machine-learning-pipeline)
- [Dataset](#dataset)
- [Challenges](#challenges)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Environment Setup](#environment-setup)
- [Installation](#installation)
- [Usage](#usage)
- [Logging](#logging)
- [Exception Handling](#exception-handling)
- [Model Evaluation](#model-evaluation)
- [Threshold Optimization](#threshold-optimization)
- [Results](#results)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

# 📌 Project Overview

The **Air Pressure System (APS)** is a critical system in heavy vehicles. It generates pressurized air that is used for several vehicle functions, including:

- Braking
- Gear changes
- Other pneumatic operations

A failure in the APS can potentially lead to serious operational issues and vehicle breakdowns.

This project uses machine learning techniques to analyze sensor measurements and predict whether a vehicle has an **APS-related component failure**.

The project is designed as an **end-to-end machine learning pipeline**, covering data ingestion, validation, transformation, model training, evaluation, and prediction.

---

# 🎯 Problem Statement

The dataset contains sensor data collected from heavy vehicles.

The target variable represents whether the failure is related to the Air Pressure System.

There are two classes:

| Class | Description |
|:---:|---|
| **1 - Positive** | APS-related component failure |
| **0 - Negative** | Failure related to a component other than APS |

The objective is to build a binary classification model that can distinguish between APS-related and non-APS-related failures.

---

# 💼 Business Objective

The primary business objective is to **minimize the total cost associated with incorrect predictions**.

A classification model can make two important types of errors.

## False Positive

A **False Positive (FP)** occurs when:

> The model predicts an APS-related failure, but the vehicle does not actually have an APS-related failure.

This may result in:

- Unnecessary inspection
- Unnecessary maintenance
- Additional workshop/mechanic costs

The estimated cost of a false positive is:

```text
Cost of FP = 10
```

---

## False Negative

A **False Negative (FN)** occurs when:

> The model predicts that there is no APS-related failure, but the vehicle actually has an APS-related failure.

This is significantly more expensive because the faulty vehicle may not be identified and could potentially experience a breakdown.

The estimated cost of a false negative is:

```text
Cost of FN = 500
```

Therefore:

```text
500 / 10 = 50
```

> **One false negative has the same business cost as 50 false positives.**

Because of this large cost difference, reducing false negatives is particularly important.

---

# 💰 Cost of Misclassification

The business cost matrix is:

| Actual Class | Predicted Positive | Predicted Negative |
|:---|---:|---:|
| **Positive** | 0 - True Positive | **500 - False Negative** |
| **Negative** | **10 - False Positive** | 0 - True Negative |

Where:

- **TP** = True Positive
- **TN** = True Negative
- **FP** = False Positive
- **FN** = False Negative

---

# 🧮 Total Business Cost

The primary business metric is the **Total Business Cost**.

It is calculated as:

```text
Total Cost = (Cost of FP × Number of FP)
           + (Cost of FN × Number of FN)
```

For this project:

```text
Total Cost = (10 × FP) + (500 × FN)
```

The goal is therefore to find a model and classification threshold that minimizes this total cost.

---

# 🤖 Machine Learning Objective

This project is a **binary classification problem**.

The model predicts:

```text
1 → APS-related failure
0 → Non-APS-related failure
```

The model should not be selected based solely on accuracy.

Instead, model evaluation will consider:

- Precision
- Recall
- F1 Score
- ROC-AUC
- Confusion Matrix
- False Positives
- False Negatives
- Total Business Cost

Since the cost of a false negative is significantly higher than the cost of a false positive, **positive-class recall** is an important evaluation metric.

However, maximizing recall alone is not sufficient because predicting every vehicle as positive could result in a large number of unnecessary inspections.

The final model should therefore achieve an appropriate balance between predictive performance and business cost.

---

# 🔄 Project Workflow

```text
                         ┌─────────────────────┐
                         │    Raw Sensor Data  │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Data Ingestion    │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Data Validation   │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Data Transformation │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Feature Engineering │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Model Training    │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │  Model Evaluation   │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Threshold Optimization│
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │  Final Prediction   │
                         └─────────────────────┘
```

---

# 🔬 Machine Learning Pipeline

## 1. Data Ingestion

The data ingestion component is responsible for:

- Loading the raw sensor dataset
- Reading the input data
- Splitting data into training and testing datasets
- Saving relevant data artifacts

## 2. Data Validation

The data validation component checks:

- Dataset structure
- Expected columns
- Data types
- Missing values
- Target variable
- Data consistency
- Schema changes

## 3. Data Transformation

The data transformation stage prepares the raw data for machine learning.

Potential operations include:

- Missing-value treatment
- Feature preprocessing
- Feature scaling
- Encoding categorical variables
- Feature selection
- Data cleaning

## 4. Feature Engineering

Feature engineering may include:

- Removing irrelevant features
- Removing highly correlated features
- Handling skewed features
- Creating derived features
- Selecting informative features

## 5. Model Training

Multiple classification algorithms can be evaluated.

Potential models include:

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost
- LightGBM

The final model will be selected based on both predictive performance and business cost.

## 6. Model Evaluation

Models will be evaluated using:

- Confusion Matrix
- Precision
- Recall
- F1 Score
- ROC-AUC
- False Positive Rate
- False Negative Rate
- Total Business Cost

## 7. Threshold Optimization

The classification threshold will be optimized according to the business cost.

The default probability threshold of `0.5` will not automatically be considered optimal.

Different thresholds will be evaluated to determine the threshold that minimizes:

```text
Total Cost = (10 × FP) + (500 × FN)
```

This allows the model's prediction threshold to be aligned with the actual business objective.

---

# 📦 Dataset

The project uses sensor data collected from heavy vehicles.

The features represent various sensor measurements that can potentially be used to identify patterns associated with APS-related failures.

## Target Variable

| Value | Meaning |
|:---:|---|
| `1` | APS-related failure |
| `0` | Failure related to a component other than APS |

## Dataset Characteristics

The dataset contains:

- Multiple sensor features
- Numerical sensor measurements
- A binary target variable
- Missing values across multiple features
- Potential class imbalance
- High-dimensional sensor information

---

# ⚠️ Challenges

## 1. Missing Values

The dataset contains a significant number of missing values across multiple columns.

The project therefore investigates:

- Missing-value percentage
- Missing-value patterns
- Feature-level missingness
- Appropriate imputation strategies
- Impact of missing values on model performance

## 2. Class Imbalance

The target classes may not be evenly distributed.

Therefore, class distribution will be analyzed before model training.

Potential approaches include:

- Class weights
- Resampling
- SMOTE
- Threshold optimization

The final approach will be selected based on validation performance and business cost.

## 3. Cost-Asymmetric Errors

False positives and false negatives have significantly different business consequences.

```text
False Positive = 10
False Negative = 500
```

Therefore:

```text
FN Cost = 50 × FP Cost
```

This makes false-negative reduction particularly important.

## 4. No Low-Latency Requirement

There is no strict low-latency requirement for prediction.

Therefore, model selection can focus primarily on:

- Predictive performance
- Generalization
- Business cost
- False-negative reduction

rather than extremely fast inference.

## 5. Interpretability

Model interpretability is not a primary business requirement.

Therefore, model selection can focus mainly on predictive performance and business cost.

---

# 🏗️ Project Structure

```text
Live-Air-Pressure-Sensor/
│
├── sensor/
│   ├── __init__.py
│   ├── exception.py
│   ├── logger.py
│   │
│   ├── components/
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── entity/
│   │   ├── __init__.py
│   │   └── config_entity.py
│   │
│   ├── pipeline/
│   │   ├── __init__.py
│   │   └── prediction_pipeline.py
│   │
│   └── utils/
│       ├── __init__.py
│       └── common.py
│
├── notebooks/
│   └── exploratory_analysis.ipynb
│
├── artifacts/
│
├── logs/
│
├── main.py
├── setup.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

### Git-Ignored Directories

The following directories contain generated or environment-specific files and should not be committed to Git:

```text
venvsensor/
logs/
build/
dist/
*.egg-info/
__pycache__/
```

---

# 🛠️ Technologies Used

## Programming Language

- [Python](https://www.python.org/)

## Data Analysis

- [NumPy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)

## Data Visualization

- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)

## Machine Learning

- [Scikit-learn](https://scikit-learn.org/)
- XGBoost
- LightGBM

## Development Tools

- [Jupyter Notebook](https://jupyter.org/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)

> Additional technologies will be added as they are implemented in the project.

---

# ⚙️ Environment Setup

The project uses a Python virtual environment to isolate project dependencies.

## Create Virtual Environment

```powershell
python -m venv venvsensor
```

## Activate Virtual Environment

### Windows PowerShell

```powershell
.\venvsensor\Scripts\Activate.ps1
```

After activation, the terminal should display:

```text
(venvsensor)
```

---

# 📥 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/shubhamaware18/Live-Air-Pressure-Sensor.git
```

## 2. Navigate to the Project Directory

```bash
cd Live-Air-Pressure-Sensor
```

## 3. Create the Virtual Environment

```powershell
python -m venv venvsensor
```

## 4. Activate the Virtual Environment

```powershell
.\venvsensor\Scripts\Activate.ps1
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Usage

After installing the dependencies and activating the virtual environment, run:

```bash
python main.py
```

The application will execute the configured machine learning pipeline.

---

# 📝 Logging

The project implements centralized logging through:

```text
sensor/logger.py
```

Log files are generated inside:

```text
logs/
```

Example:

```text
logs/
├── 2026-09-13_10-30-15.log
└── 2026-09-13_11-45-20.log
```

Logging is used to track:

- Pipeline execution
- Data processing
- Model training
- Warnings
- Errors
- Important application events

---

# 🚨 Exception Handling

Custom exception handling is implemented through:

```text
sensor/exception.py
```

The custom `SensorException` provides additional debugging information such as:

- File name
- Line number
- Original exception message

Example:

```text
Error occurred in script: [main.py]
at line number: [25]
with error message: [division by zero]
```

This makes debugging easier across different components of the machine learning pipeline.

---

# 📈 Model Evaluation

The project uses both traditional machine learning metrics and a business-cost metric.

## Confusion Matrix

| Actual / Predicted | Positive | Negative |
|:---|---:|---:|
| **Positive** | True Positive | False Negative |
| **Negative** | False Positive | True Negative |

For this project:

```text
False Positive
→ Unnecessary inspection/repair

False Negative
→ APS failure may be missed
→ Potential vehicle breakdown
```

## Evaluation Metrics

### Precision

Measures how many vehicles predicted as APS failures are actually APS failures.

### Recall

Measures how many actual APS failures are correctly identified.

### F1 Score

Provides a balance between precision and recall.

### ROC-AUC

Measures the model's ability to distinguish between the two classes across different classification thresholds.

### Total Business Cost

The primary business metric:

```text
Total Cost = (10 × FP) + (500 × FN)
```

---

# 🎚️ Threshold Optimization

Most binary classification models produce a probability rather than a direct class prediction.

For example:

```text
Predicted probability = 0.72
```

A threshold is then used to convert the probability into a class.

The default threshold is commonly:

```text
Threshold = 0.50
```

However, a threshold of `0.5` may not be optimal for this business problem.

Because:

```text
FP Cost = 10
FN Cost = 500
```

the classification threshold will be evaluated based on the resulting business cost.

Example:

| Threshold | False Positives | False Negatives | Total Cost |
|:---:|---:|---:|---:|
| 0.30 | TBD | TBD | TBD |
| 0.40 | TBD | TBD | TBD |
| 0.50 | TBD | TBD | TBD |
| 0.60 | TBD | TBD | TBD |
| 0.70 | TBD | TBD | TBD |

The final threshold will be selected based on validation performance and minimum business cost.

---

# 📊 Results

This section will be updated after completing model development and evaluation.

| Metric | Result |
|---|---:|
| Best Model | TBD |
| Classification Threshold | TBD |
| Precision | TBD |
| Recall | TBD |
| F1 Score | TBD |
| ROC-AUC | TBD |
| False Positives | TBD |
| False Negatives | TBD |
| Total Business Cost | TBD |

---

# 🔍 Key Findings

This section will contain the major findings from exploratory data analysis and model development.

Examples of findings that may be documented:

- Important sensor features
- Missing-value patterns
- Class distribution
- Important correlations
- Model performance comparison
- Optimal classification threshold
- Business cost reduction

This section will be updated as the project progresses.

---

# 🚀 Future Improvements

Potential future improvements include:

- Hyperparameter optimization
- Advanced feature engineering
- Automated threshold optimization
- Ensemble modeling
- Model monitoring
- Data drift detection
- Model performance monitoring
- Automated model retraining
- REST API deployment
- Docker containerization
- CI/CD integration
- Cloud deployment

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

To contribute:

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/new-feature
```

3. Make your changes
4. Commit your changes

```bash
git commit -m "Add new feature"
```

5. Push the branch

```bash
git push origin feature/new-feature
```

6. Open a Pull Request

---

# 📄 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for details.

---

# 👤 Author

**Shubham**

GitHub: [@shubhamaware18](https://github.com/shubhamaware18)

---

# ⭐ Project Summary

This project demonstrates an end-to-end approach to solving a real-world **sensor fault detection problem** using machine learning.

The key focus is not simply achieving high classification accuracy, but designing a model around the actual business impact of prediction errors.

The core business objective is:

```text
Minimize:

Total Cost = (10 × False Positives)
           + (500 × False Negatives)
```

The final solution aims to identify APS-related failures effectively while minimizing the overall operational cost associated with incorrect predictions.
