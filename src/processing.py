import pandas as pd
import numpy as np

def clean_data(df):
    """Normalize numerical columns and handle non-numeric values"""
    try:
        # Convert all numeric columns to float64
        for column in df.columns:
            df[column] = pd.to_numeric(df[column], errors="coerce")

        # Drop rows with missing values
        df = df.dropna()

        # Normalize numeric data
        for column in df.select_dtypes(include=[np.number]).columns:
            if df[column].std() != 0:  # Avoid division by zero
                df[column] = (df[column] - df[column].mean()) / df[column].std()
        
        print("Data cleaned successfully!")
        return df

    except Exception as e:
        print(f"Error during data cleaning: {e}")
        return None

