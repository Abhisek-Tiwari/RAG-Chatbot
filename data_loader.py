import pandas as pd

def load_data(filepath: str) -> pd.DataFrame:
    """
    Takes filepath of CSV file and gives pandas dataframe as
    :param filepath: filepath of CSV file
    :return: pandas dataframe
    """
    df = pd.read_csv(filepath)
    return df