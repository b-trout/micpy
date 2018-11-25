"""
Compute mic and its related indicators and return as DataFrame.
"""

import itertools
import pandas as pd
import minepy


def get_mic_df(df, **kwargs):

    df = df.select_dtypes(include=['int', 'float'])
    cols_product = list(itertools.product(df.columns, repeat=2))

    mic = []

    for i in range(len(cols_product)):
        mi = minepy.MINE(**kwargs)
        mi.compute_score(df[cols_product[i][0]], df[cols_product[i][1]])

        mic_i = [
            cols_product[i][0],
            cols_product[i][1],
            mi.mic(),
            mi.mas(),
            mi.mev(),
            mi.mcn(0),
            mi.tic()
            ]

        mic.append(mic_i)

    df_mic = pd.DataFrame(mic)
    df_mic.columns = ['col', 'col2', 'MIC', 'MAS', 'MEV', 'MCN', 'TIC']

    df_corr = df.corr()
    df_corr = pd.DataFrame(df_corr.stack()).reset_index()
    df_corr = df_corr.rename(
        columns={
            'level_0': 'col',
            'level_1': 'col2',
            0: 'corr'
            }
            )

    df_corr['R2'] = df_corr['corr'].apply(lambda x: x**2)
    df_r2 = df_corr.filter(items=['col', 'col2', 'R2'])

    res = pd.DataFrame.merge(df_mic, df_r2, on=['col', 'col2'])
    res['MICR2'] = res['MIC'] - res['R2']
    res = res.filter(
        items=[
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

    return res
