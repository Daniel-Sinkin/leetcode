import numpy as np
import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    col_name = f"getNthHighestSalary({N})"
    distinct_salaries = np.unique(employee.salary)
    if len(distinct_salaries) < N or N <= 0:
        return pd.DataFrame({col_name: [None]})

    distinct_salaries.sort()
    return pd.DataFrame({col_name: [distinct_salaries[-N]]})
