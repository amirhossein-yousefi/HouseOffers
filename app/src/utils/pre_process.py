import numpy as np
def get_rid_outl(df, list_num_cols, percentile):
    perc_dict = {}
    for col in list_num_cols:  # first, calculate all the percentiles before removing any
        # row, otherwise you will remove more rows than necessary
        value_perc = np.nanpercentile(df[col], percentile)
        value_perc_dict = {col: value_perc}
        perc_dict.update(value_perc_dict)

    for var in list_num_cols:
        df = df.loc[(df[var] <= perc_dict[var]) ^ (df[var].isnull())]  # include nan values

    return df