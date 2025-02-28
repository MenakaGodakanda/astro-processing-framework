from data_loader import load_fits_data
from processing import clean_data
from parallel_processing import process_data_parallel
from visualization import plot_histogram

def main():
    file_path = "data/sample.fits"  # Update with actual dataset
    df = load_fits_data(file_path)
    
    print("Cleaning Data...")
    cleaned_df = clean_data(df)
    
    print("Processing Data in Parallel...")
    processed_df = process_data_parallel(cleaned_df)

    print("Displaying Results...")
    plot_histogram(processed_df, processed_df.columns[0])
    
    processed_df.to_csv("output/processed_data.csv", index=False)

if __name__ == "__main__":
    main()
