## Functions

### `isin()`
- param: values -> (dict, list, series)
    - If values is a series: checks index
    - If dict: keys are the column names
        - In effect, `dict{"column name": [list_iterables]}`
    - If DF: index and column labels must match

- returns: A dataframe of booleans as to whether each element is contained in values
