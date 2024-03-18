import pandas as pd


def read_csv(path):
    return pd.read_csv(path, keep_default_na=False, header=None)


def print_latex(df):
    rows = df.shape[0]
    columns = df.shape[1]
    print("\\begin{center}")
    print("\\begin{tabular}{ "+ " | ".join(["c" for i in range(columns)]) +" }")
    for i in range(rows):
        text = ""
        for j in range(columns):
            text = text + str(df.iloc[i, j]) + " "
            if j < columns - 1:
                text = text + "& "
            else:
                text = text + "\\\\"
        print(text)
        if i < rows - 1:
            print("\\hline")
    print("\\end{tabular}")
    print("\\end{center}")


if __name__ == '__main__':
    path = ""
    csv = read_csv(path)
    print_latex(csv)

