# Scalable Astronomical Data Processing Framework

This project is a scalable computing framework for processing astronomical datasets using parallel processing techniques. It leverages Dask for distributed data handling and Astropy for working with FITS files.

## Overview
<img width="1379" alt="Screenshot 2025-02-28 at 5 12 52 pm" src="https://github.com/user-attachments/assets/cd0b8b91-97c7-4adc-a740-996d392bf011" />

## Explanation:

### 1. Load FITS File (`data_loader.py`)
- Download FITS Data (`data/sample.fits`)
- Read FITS HDUs
- Use Astropy to read astronomical datasets.
- Convert to Pandas DF

### 2. Data Cleaning (`processing.py`)
- Convert to Numeric
- Handle Missing Values
- Normalize Data

### 3. Parallel Processing (`main.py` and `parallel_processing.py`)
- Use Dask for Scaling
- Process Data in Chunks
- Save as CSV (`output/processed_data.csv`)

### 4. Data Visualization (`visualization.py`)
- Generate Histogram
- Save as Image (`output/histogram.png`) 

## Features
- **Load FITS Data** using `Astropy`
- **Data Cleaning & Normalization**
- **Parallel Processing** with `Dask`
- **Visualization** with `Matplotlib`

## Installation and Setup

### 1. Prerequisites
- Ubuntu (20.04+)
- Python 3.8+
- Virtual Environment (Recommended)


### 2. Clone the repository
```
git clone https://github.com/MenakaGodakanda/astro-processing-framework.git
cd astro-processing-framework
```

### 3. Create a virtual environment
```
python3 -m venv astro
source astro/bin/activate # On Windows use `astro\Scripts\activate`
```

### 4. Install dependencies
```
pip install dask[complete] astropy pandas numpy matplotlib
```

### 5. Download Astronomical Data
- Download a sample FITS dataset and save it in the `data/` folder.
- Download data manually from:
  - <a href="https://fits.gsfc.nasa.gov/fits_samples.html">NASA FITS Samples</a>
  - <a href="https://dr17.sdss.org/optical/spectrum/search">SDSS SkyServer</a>
  - <a href="https://gea.esac.esa.int/archive/">ESA Gaia Archive</a>

- The FITS (Flexible Image Transport System) format is widely used in astronomy.

## Usage
### Run the Framework:
```
python3 src/main.py
```
![Screenshot 2025-02-28 161158](https://github.com/user-attachments/assets/3224598d-bc19-4572-93cd-42b826b57eae)

### Expected Output:
- A histogram plot of the processed dataset will be displayed.
  - **X-axis**: Column values (e.g., wavelength, flux, magnitude, or intensity).
  - **Y-axis**: Frequency (number of occurrences).
  - A bell-shaped or skewed distribution based on the dataset.

### Sample Output
- Processed CSV Output: `output/processed_data.csv`
- Histogram Image: `output/histogram.png`

## Project Structure
```
astro-processing-framework/
│── data/                     # Directory for raw and processed data
│── output/                   # Stores processed results (CSV, images)
│── src/                      # Source code directory
│   │── main.py               # Main script to run the pipeline
│   │── data_loader.py        # Loads and parses FITS files
│   │── processing.py         # Cleans and normalizes data
│   │── visualization.py      # Generates plots
│── README.md                 # Project documentation
```

## License

This project is open-source under the MIT License.
