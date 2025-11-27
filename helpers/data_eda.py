
import pandas as pd
import matplotlib.pyplot as plt


def remove_outliers_by_zscore(df, threshold=3, columns=None) -> pd.DataFrame:
    
    df = df.copy()

    # Select columns to check for outliers
    if columns is None:
        # Use all numeric columns
        num_cols = df.select_dtypes(include='number').columns.tolist()
    else:
        # Use specified columns and verify they're numeric
        num_cols = []
        for col in columns:
            if col not in df.columns:
                print(f"Warning: Column '{col}' not found in dataframe. Skipping.")
            elif df[col].dtype not in ['int64', 'float64', 'int32', 'float32']:
                print(f"Warning: Column '{col}' is not numeric. Skipping.")
            else:
                num_cols.append(col)
    
    if not num_cols:
        print("No valid numeric columns to check for outliers.")
        return df
    
    print(f"Checking for outliers in columns: {num_cols}")

    #remove outliers
    for i in range(15):
        # Calculate z-scores for selected numeric columns
        z_scores = (df[num_cols] - df[num_cols].mean()) / df[num_cols].std()

        # Filter rows where all z-scores are within threshold
        original_len = len(df)
        df = df[(z_scores.abs() <= threshold).all(axis=1)]

        #print(f"Removed {original_len - len(df)} outlier rows ({((original_len - len(df)) / original_len * 100):.1f}%)")
        if(original_len - len(df) ==0 ) :
            break

    return df


def visualize_missing_values(data):
    ### Visualize the percentage of missing values in each column ###
    missing_values = (data.isna().sum()/data.shape[0]*100).plot(kind = "barh",color ="blue")
    plt.xlim(0,100)
    plt.ylabel("Columns Title")
    plt.xlabel("Missing Values %")
    plt.title("Percentage of Missing Value")
    plt.figure(figsize=(40, 20))
    for data_columns in missing_values.containers:
        missing_values.bar_label(data_columns, fmt="%.2f%%")
    plt.show()

def draw_distribution_chart(df,column):
    ### Draw a pie chart to show the distribution of a column ###
    plt.figure(figsize=(10,6))
    pie_data = df[column].value_counts()
    plt.pie(pie_data,labels=pie_data.index,autopct="%1.5f%%", startangle=140)
    plt.title(f"Distribution of {column}")
    plt.axis("equal")
    plt.show()
    print(df[column].value_counts().head(10))