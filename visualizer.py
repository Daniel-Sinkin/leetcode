import os

import dash
import dash_bootstrap_components as dbc
from dash import html

# Total number of problems on LeetCode
TOTAL_PROBLEMS = 3273
PROBLEMS_PER_ROW = 30  # Reduced number of problems per row to 30


# Function to count and organize solved problems by difficulty
def get_solved_problems(directory):
    solved_problems = {"Easy": set(), "Medium": set(), "Hard": set()}

    for root, _, files in os.walk(directory):
        if "WIP" in root:
            continue

        for file in files:
            if file.endswith((".cpp", ".py", ".rs")):
                parts = root.split("_")
                if len(parts) < 2:
                    continue
                difficulty = parts[1]
                problem_id = file.split("_")[0]

                if problem_id:
                    if difficulty in solved_problems:
                        solved_problems[difficulty].add(problem_id)

    return solved_problems


# Get the solved problems
directory = "."  # Use current directory, modify if needed
solved_problems = get_solved_problems(directory)

# Initialize Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Colors for each difficulty
colors = {
    "Easy": "lightgreen",
    "Medium": "yellow",
    "Hard": "lightcoral",
    "Unsolved": "#1c1c1c",
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
    [html.H1("LeetCode Problem Tracker"), create_problem_grid(solved_problems)]
)

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
