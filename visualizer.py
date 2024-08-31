import os

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output

# Total number of problems on LeetCode
TOTAL_PROBLEMS = 3273
PROBLEMS_PER_ROW = 30  # Reduced number of problems per row to 30


# Function to count and organize solved problems by difficulty
def get_solved_problems(directory, include_cpp=True, include_py=True, include_rs=True):
    solved_problems = {"Easy": set(), "Medium": set(), "Hard": set()}

    extensions = []
    if include_cpp:
        extensions.append(".cpp")
    if include_py:
        extensions.append(".py")
    if include_rs:
        extensions.append(".rs")

    for root, _, files in os.walk(directory):
        if "WIP" in root:
            continue

        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                parts = root.split("_")
                if len(parts) < 2:
                    continue
                difficulty = parts[1]
                problem_id = file.split("_")[0]

                if problem_id:
                    if difficulty in solved_problems:
                        solved_problems[difficulty].add(problem_id)

    return solved_problems


# Initialize Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Colors for each difficulty
colors = {
    "Easy": "lightgreen",
    "Medium": "yellow",
    "Hard": "lightcoral",
    "Unsolved": "#1c1c1c",  # Darker gray for unsolved problems
}


# Function to create the grid of squares
def create_problem_grid(solved_problems):
    grid = []
    row = []

    # Iterate over all possible problem IDs from 1 to TOTAL_PROBLEMS
    for i in range(1, TOTAL_PROBLEMS + 1):
        problem_id = str(i).zfill(4)  # Convert number to a 4-digit string, e.g., "0001"

        # Determine the color based on problem difficulty
        if problem_id in solved_problems["Easy"]:
            color = colors["Easy"]
        elif problem_id in solved_problems["Medium"]:
            color = colors["Medium"]
        elif problem_id in solved_problems["Hard"]:
            color = colors["Hard"]
        else:
            color = colors["Unsolved"]

        # Create a square for this problem and add it to the current row
        row.append(
            html.Div(
                style={
                    "backgroundColor": color,
                },
                className="grid-item",
            )
        )

        # When a row is complete, append it to the grid and start a new row
        if i % PROBLEMS_PER_ROW == 0 or i == TOTAL_PROBLEMS:
            # Ensure that the counter and the row of squares are wrapped in the same div
            grid_row = html.Div(
                [
                    html.Div(f"{i - PROBLEMS_PER_ROW + 1}", className="counter"),
                    html.Div(row, className="grid-container"),
                ],
                style={
                    "display": "flex",
                    "alignItems": "center",
                    "justifyContent": "center",
                },
            )
            grid.append(grid_row)
            row = []  # Reset row for the next batch of problem squares

    return html.Div(
        grid,
        style={"display": "flex", "flexDirection": "column", "alignItems": "center"},
    )


# Define the app layout
app.layout = html.Div(
    [
        html.H1("Daniels"),
        html.H1("LeetCode Problem Tracker"),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                dcc.Checklist(
                                    id="language-selector",
                                    options=[
                                        {
                                            "label": "",
                                            "value": "cpp",
                                        },  # Empty label since label is added manually below
                                        {"label": "", "value": "py"},
                                        {"label": "", "value": "rs"},
                                    ],
                                    value=[
                                        "cpp",
                                        "py",
                                        "rs",
                                    ],  # All selected by default
                                    inline=False,  # Makes the checkboxes stack vertically
                                )
                            ],
                            style={
                                "display": "flex",
                                "flexDirection": "column",
                                "alignItems": "center",
                            },
                        ),
                        html.Div(
                            [
                                html.Div(
                                    "C++",
                                    className="label",
                                    style={"marginLeft": "10px"},
                                ),
                                html.Div(
                                    "Python",
                                    className="label",
                                    style={"marginLeft": "10px"},
                                ),
                                html.Div(
                                    "Rust",
                                    className="label",
                                    style={"marginLeft": "10px"},
                                ),
                            ],
                            style={
                                "display": "flex",
                                "flexDirection": "column",
                                "justifyContent": "center",
                                "alignItems": "flex-start",
                            },
                        ),
                    ],
                    style={
                        "display": "flex",
                        "justifyContent": "center",
                        "alignItems": "center",
                        "marginBottom": "20px",
                    },
                )
            ],
            style={"textAlign": "center"},
        ),
        html.Div(id="grid-container"),
    ]
)


# Callback to update the grid based on selected languages
@app.callback(
    Output("grid-container", "children"), [Input("language-selector", "value")]
)
def update_grid(selected_languages):
    include_cpp = "cpp" in selected_languages
    include_py = "py" in selected_languages
    include_rs = "rs" in selected_languages

    solved_problems = get_solved_problems(".", include_cpp, include_py, include_rs)
    return create_problem_grid(solved_problems)


# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
