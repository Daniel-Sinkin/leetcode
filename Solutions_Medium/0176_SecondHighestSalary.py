import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    distinct_salaries = employee.salary.unique()
    if len(distinct_salaries) < 2:
        return pd.DataFrame({"secondHighestSalary": [None]})

    distinct_salaries.sort()
    return pd.DataFrame({"secondHighestSalary": [distinct_salaries[-2]]})
