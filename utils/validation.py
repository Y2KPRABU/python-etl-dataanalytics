import pandas as pd

def check_if_valid_data(df: pd.DataFrame):
    """
    Function to check if the date is in a valid format
    """
    # Check if the DataFrame is empty
    if df.empty:
        print('No songs in the past 24hs!')
        return False
    
    # Since you can't simultaneously listen to 2 different songs
    # our primary key is played_at
    if  pd.Series(df['Names']).is_unique:
        # If the played at is not unique, then primary key check is violated
        raise Exception('Names need to be same!')
    
    # Check for empty values
    if df.isnull().values.any():
        raise Exception('Null values!')
