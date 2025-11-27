# What factors are driving used car prices?

## Overview
In this application, we explore a dataset from Kaggle containing information on 426K used cars. The goal is to understand what factors make a car more or less expensive. As a result of this analysis, we provide clear recommendations to a used car dealership as to what consumers value in a used car.

## Business Understanding
The dealership is currently reliant on ad-hoc estimations for setting used car prices, leading to inconsistent profit margins and slow inventory turnover. A data-driven approach is needed to optimize pricing strategy.

**Goals:**
*   Improve consistency and reliability in the valuation process.
*   Understand what factors make a car more or less expensive.
*   Provide clear recommendations to a used car dealership.
*   Predict the price of a used car with high accuracy.
*   Identify top-selling brands, models, and key features affecting price.

## Data Understanding
*   **Source**: [Kaggle Used Car Dataset](https://www.kaggle.com/datasets/austinreese/used-car-dataset-for-ml-models)
*   **Size**: 426,880 rows and 18 columns.
*   **Key Features**: `id`, `region`, `price`, `year`, `manufacturer`, `model`, `condition`, `cylinders`, `fuel`, `odometer`, `title_status`, `transmission`, `VIN`, `drive`, `size`, `type`, `paint_color`, `state`.

## Methodology
We follow the **CRISP-DM** (Cross-Industry Standard Process for Data Mining) framework:
1.  **Business Understanding**: Defining objectives and requirements.
2.  **Data Understanding**: Initial data collection and exploration.
3.  **Data Preparation**: Cleaning data, handling missing values, removing outliers, and feature engineering.
4.  **Modeling**:
    *   Used **Ridge Regression** and **Lasso Regression**.
    *   Employed **GridSearchCV** for hyperparameter tuning.
    *   Utilized **PolynomialFeatures** to capture non-linear relationships.
    *   Applied **StandardScaler** and **OneHotEncoder** for preprocessing.
5.  **Evaluation**: Assessing model performance using MSE and R2 score.

## Project Structure
*   `UsedCarPriceEDAandModels.ipynb`: The main Jupyter Notebook containing the analysis and modeling code.
*   `data/`: Directory containing the dataset (`vehicles.csv`).
*   `helpers/`: Python scripts for helper functions:
    *   `data_eda.py`: Functions for outlier removal and visualization.
    *   `data_cleaners.py`: Functions for summary statistics.
*   `images/`: Directory containing images used in the notebook.

## Installation & Usage
To run this analysis locally:

1.  Clone this repository.
2.  Install the required dependencies:
    ```bash
    pip install pandas numpy matplotlib seaborn scikit-learn
    ```
3.  Open the notebook:
    ```bash
    jupyter notebook UsedCarPriceEDAandModels.ipynb
    ```
4.  Run the cells to reproduce the analysis.

## Key Findings
*   **Age and Odometer**: These are critical factors; price generally decreases as age and mileage increase.
*   **Manufacturer/Model**: Certain brands and models command higher prices.
*   **Condition**: Better condition ratings correlate with higher prices.
*   **Features**: Attributes like `fuel` type, `transmission`, and `drive` type significantly influence valuation.

## Future Work
*   Incorporate more recent data to capture current market trends.
*   Experiment with more advanced models (e.g., Random Forest, Gradient Boosting) if computational resources allow.
*   Develop a deployment strategy for the pricing model to be used directly by dealership staff.
