import pandas as pd
import pytest
from app.src.utils.pre_process import get_rid_outl

input_df = pd.DataFrame.from_dict({'A': [i for i in range(100)], 'B': [i*1000 for i in range(100)]})
def test_get_rid_outl():
    actual_df = get_rid_outl(input_df, ['A', 'B'], 90)
    assert actual_df.shape[0] == 90

