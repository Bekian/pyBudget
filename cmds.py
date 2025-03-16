import pandas as pd

testDf = pd.read_csv("../pyBudget/data/checking1.csv")


def add_headers(df: pd.DataFrame, new_headers: list[str]) -> tuple[pd.DataFrame | None, str | None]:
    """
    Add headers using an existing dataframe.
    Args:
        df (pd.DataFrame): a dataframe to add headers to
        new_headers (list[str]): a list of strings to create the new headers.

    Returns:
        tuple[pd.DataFrame | None, str | None]: a tuple containing the resulting dataframe or an error message
    """
    if df.columns.__len__() != new_headers.__len__():
        print("err incoming")
        return None, f"New headers and Df column mismatch: {new_headers.__len__()}, {df.columns.__len__()}"
    df.columns = new_headers
    print("success")
    return df, None

def test_add_headers():
    data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    df = pd.DataFrame(data)
    print(df.columns.__len__())
    headers = ["A", "B", "C"]
    print(headers.__len__())
    df, err = add_headers(df, headers)
    if err:
        print(err)
    elif df is not None:
        print(df.head())

# test_add_headers()

def remove_pii(df: pd.DataFrame, pii: list[str], remove_pii: bool=False, mask_str: str="X") -> pd.DataFrame:
    """
    Remove Personally Identifiable Information from a dataframe. Optionally, set remove_pii to False to use the masking_str to replace your pii strings with this value instead of removing them. You may also provide your own masking string. Additionally, for simplicity the replacement function is regex based, if you want more (or less) functionality, you'll need to roll your own function to do this.
    Args:
        df (pd.DataFrame): the dataframe to remove pii from
        pii (list[str]): a list of pii strings to remove from the dataframe
        remove_pii (bool): flag to tell the function to remove the strings from the dataframe. If this is True, the strings will be completely removed from the strings. The intent with this being False by default is an attempt to maintain sentence structure, obviously this depends on your own data so this option was proivded.
        mask_str (str): a single string character used to redact the original string. The intent with this value being "X", is to have a character that is obvious that the underlying value has been masked and that is easy to use semantically, for example: "Purchase was made at X by X."
    Returns:
        df (pd.DataFrame): a dataframe with redacted strings
    """
    if remove_pii:
        for pii_val in pii:
            df.replace(pii_val, '', regex=True)
    else:
        print('replace pii with mask')
        for pii_val in pii:
            df = df.replace(pii_val, mask_str, regex=True)

    return df

testDf = remove_pii(testDf, ['MN']) 
testDf.to_csv("data/test_output.csv")
