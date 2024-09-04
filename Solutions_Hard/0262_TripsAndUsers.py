import pandas as pd


def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    trips = trips[
        (trips.request_at >= "2013-10-01") & (trips.request_at <= "2013-10-03")
    ]

    merged = trips.merge(users, how="left", left_on="client_id", right_on="users_id")
    merged = merged.merge(users, how="left", left_on="driver_id", right_on="users_id")
    merged_clean = merged[(merged.banned_x == "No") & (merged.banned_y == "No")]

    if merged_clean.empty:
        return pd.DataFrame([], columns=["Day", "Cancellation Rate"])

    result = []
    for date, df in merged_clean.groupby("request_at"):
        n_cancelled = len(df) - len(df[df.status == "completed"])
        cancellation_rate = n_cancelled / len(df)

        result.append((date, round(cancellation_rate, 2)))
    return pd.DataFrame(result, columns=["Day", "Cancellation Rate"])
