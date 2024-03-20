import os

def main() -> None:
    folder_names = ["Solutions_Easy", "Solutions_Medium", "Solutions_Hard"]

    counts = []

    cwd = os.getcwd()

    for folder_name in folder_names:
        folder_path = os.path.join(cwd, folder_name)
        count = sum(not f.startswith('.') for f in os.listdir(folder_path))
        counts.append(count)

    file_name = f"_num_solved_{counts[0]}_{counts[1]}_{counts[2]}.txt"

    for f in os.listdir(cwd):
        if f.startswith("_num_solved_"):
            os.remove(os.path.join(cwd, f))

    open(os.path.join(cwd, file_name), 'w').close()

    print(f"File '{file_name}' created.")

if __name__ == "__main__":
    main()