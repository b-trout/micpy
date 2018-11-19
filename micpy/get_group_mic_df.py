"""
Compute mic and related indicators for each group \
and return as flat DataFrame.
"""

import pandas as pd
from get_mic_df import get_mic_df


def get_group_mic_df(df, group_key, **kwargs):

    gr = df[group_key].unique()

    res = pd.DataFrame()
    for g in gr:
        df_g = df[df[group_key] == g]
        res_g = get_mic_df(df_g, **kwargs)
        res_g['group'] = g
        res = pd.concat([res, res_g], axis=0)

    res = res.filter(
        items=[
            'group',
            'col',
            'col2',
            'MIC',
            'MAS',
            'MEV',
            'MCN',
            'TIC',
            'MICR2'
            ]
            )

    res.reset_index(drop=True, inplace=True)
    return res
