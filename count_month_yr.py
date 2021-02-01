import pandas as pd
def add_month_yr(x):
    '''
    Create a dataframe column month-yr with ID as row-index
    '''
    assert isinstance(x, pd.DataFrame)
    assert (len(x)>0)

    month_dict = {'1': 'Jan', '2': 'Feb', '3': 'Mar', '4': 'Apr',
                  '5': 'May', '6': 'Jun', '7': 'Jul', '8': 'Aug',
                  '9': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}

    outlist = []
    # print(str(x['Timestamp']))
    # print(str(x['Timestamp']).split('/| '))
    # print(str(x['Timestamp']).split('/| ')[0])
    # print(str(x['Timestamp']).split('/| ')[1])
    mlist = [month_dict[i[0]] + "-" + i[2] for i in x['Timestamp'].str.split('/| ')]
    
    ind = x.iloc[:]
    ind['month-yr'] = mlist
    return ind
    

def count_month_yr(x):
    '''
    ount_month_yr is a function to create the dataframe using the new column month-yr
    '''
    assert isinstance(x, pd.DataFrame)
    assert (len(x)>0)

    return pd.DataFrame(x['month-yr'].value_counts())

# df = pd.read_csv('survey_data.csv', index_col='ID')
# df = add_month_yr(df)
# print(count_month_yr(df))
