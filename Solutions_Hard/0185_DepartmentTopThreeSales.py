import numpy as np
import pandas as pd


def top_three_salaries(
    employee: pd.DataFrame, department: pd.DataFrame
) -> pd.DataFrame:
    if employee.empty or department.empty:
        return pd.DataFrame([], columns=["Department", "Employee", "Salary"])
    employee.sort_values("salary")
    high_performers_df = pd.DataFrame()

    for dept_id, df in employee.groupby("departmentId"):
        distinct_salaries = np.unique(df.salary)

        if len(distinct_salaries) <= 2:
            high_performers = df
        else:
            high_performers = df[df.salary >= distinct_salaries[-3]]

        high_performers_df = pd.concat(
            [high_performers_df, high_performers], ignore_index=True
        )

    merged_frames = high_performers_df.merge(
        department, how="left", left_on="departmentId", right_on="id"
    )
    renamed_frames = merged_frames.rename(
        columns={"name_y": "Department", "name_x": "Employee", "salary": "Salary"}
    )
    return renamed_frames[["Department", "Employee", "Salary"]]
