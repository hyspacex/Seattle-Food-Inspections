'''
Tests for the cleaning_functions.py file
'''
# Now you can import your module
import pandas as pd

# Import the cleaning_functions
from .. import cleaning_functions as cf
from .. import merging_functions as mf

def test_dataframe_with_columns1():
    '''
    tests cf.dataframe_with_columns
    '''
    data_frame = pd.DataFrame({'A':[1, 2], 'B':[2, 3]})
    correct_dataframe = pd.DataFrame({'V':[1, 2]})
    new_df = cf.dataframe_with_columns(data_frame, ['A'], ['V'])
    assert new_df.equals(correct_dataframe)

def test_remove_row():
    '''
    tests cf.remove_row_from_data_frame
    '''
    data_frame = pd.DataFrame({'A':[1, 2], 'B':[2, 3]})
    new_df = cf.remove_row_from_data_frame(data_frame)
    correct_dataframe = pd.DataFrame({'A':[2], 'B':[3]})
    correct_dataframe.index = [1]
    assert new_df.equals(correct_dataframe)

def test_remove_dashes():
    '''
    tests cf.remove_dashes_from_data
    '''
    data_frame = pd.DataFrame({'A':[1, '-'], 'B':[2, 3]})
    new_df = cf.remove_dashes_from_data(data_frame, ['A'])
    correct_dataframe = pd.DataFrame({'A':[1, 0], 'B':[2, 3]})
    assert new_df.equals(correct_dataframe)

def test_col_to_float():
    '''
    tests cf.columns_to_float
    '''
    data_frame = pd.DataFrame({'A':[1, '2.4'], 'B':[2, 3]})
    new_df = cf.columns_to_float(data_frame, ['A'])
    correct_dataframe = pd.DataFrame({'A':[1.0, 2.4], 'B':[2, 3]})
    assert new_df.equals(correct_dataframe)

def test_col_to_int():
    '''
    tests cf.columns_to_int
    '''
    data_frame = pd.DataFrame({'A':[1, 2.4], 'B':[2, 3]})
    new_df = cf.columns_to_int(data_frame, ['A'])
    correct_dataframe = pd.DataFrame({'A':[1, 2], 'B':[2, 3]})
    assert new_df.equals(correct_dataframe)

def test_percents():
    '''
    Tests cf.data_from_percents_and_raw_totals
    '''
    data_frame = pd.DataFrame({'A':[50.0, 2.4], 'B':[100, 2001]})
    new_df = cf.data_from_percents_and_raw_totals(data_frame,
                                                  ['A'], 'B', ['C'])
    c_df = pd.DataFrame({'A':[50.0, 2.4], 'B':[100, 2001],
                         'C':[50.0 * 100 / 100, 2.4 * 2001 / 100]})
    assert new_df.equals(c_df)

def test_merge():
    '''
    tests mf.merge_dataframes
    '''
    df1 = pd.DataFrame({'A':[1, 2], 'B':[2, 3]})
    df2 = pd.DataFrame({'A':[1, 2], 'C':[4, 5]})
    c_df = pd.DataFrame({'A':[1, 2], 'B':[2, 3], 'C':[4, 5]})
    new_df = mf.merge_dataframes(df1, df2, 'A')
    assert new_df.equals(c_df)
