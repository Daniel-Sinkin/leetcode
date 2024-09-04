import pandas as pd


def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    stadium_temp = stadium[stadium.people >= 100]
    if len(stadium_temp) <= 2:
        return pd.DataFrame([], columns=["id", "visit_date", "people"])

    diffs = stadium_temp.id.diff()
    splitting_ids = stadium_temp[(diffs != 1) | diffs.isna()]["id"]

    concatenated_df = pd.DataFrame(columns=stadium_temp.columns)

    slice = stadium_temp[stadium_temp.id < splitting_ids.iloc[0]]
    if len(slice) >= 3:
        concatenated_df = pd.concat([concatenated_df, slice])

    for idx0, idx1 in zip(splitting_ids, splitting_ids[1:]):
        slice = stadium_temp[(stadium_temp.id >= idx0) & (stadium_temp.id < idx1)]
        if len(slice) >= 3:
            concatenated_df = pd.concat([concatenated_df, slice])

    slice = stadium_temp[stadium_temp.id >= splitting_ids.iloc[-1]]
    if len(slice) >= 3:
        concatenated_df = pd.concat([concatenated_df, slice])

    return concatenated_df
