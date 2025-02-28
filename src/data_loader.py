from astropy.io import fits
import pandas as pd

def load_fits_data(file_path):
    """Load a FITS file and convert it to a Pandas DataFrame"""
    with fits.open(file_path) as hdul:
        data = hdul[1].data  # Assuming data is in the second HDU
        df = pd.DataFrame(data)
    return df

