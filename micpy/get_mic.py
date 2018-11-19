"""
Utility function of get_mic_df and get_group_mic_df.
"""

from get_mic_df import get_mic_df
from get_group_mic_df import get_group_mic_df


def get_mic(df, group_key=None, **kwargs):

    if group_key is None:
        res = get_mic_df(df, **kwargs)
    else:
        res = get_group_mic_df(df, group_key, **kwargs)

    return res
