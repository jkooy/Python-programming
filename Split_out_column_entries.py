import pandas as pd
def split_count(x):
    '''
    The problem with this column is that there are multiple comma-separated values in it. 
    Please write a Python function called split_count that can take this column as input
     and output the following Pandas dataframe.
    '''
    assert isinstance(x, pd.Series)
    assert (len(x)>0)

    split = []
    for i in x.str.split(', '):
        split = split + [j for j in i ]

    return pd.DataFrame({'count': pd.Series(split).value_counts(ascending = True)})
    
     

# df = pd.read_csv('survey_data.csv', index_col='ID')
# series = df['Is there anything in particular you want to use Python for?']
# print(split_count(series))
