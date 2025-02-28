from dask import dataframe as dd

def process_data_parallel(df):
    """Use Dask to parallelize processing"""
    ddf = dd.from_pandas(df, npartitions=4)
    ddf = ddf.dropna()
    ddf = ddf.map_partitions(lambda df: (df - df.mean()) / df.std())
    return ddf.compute()

