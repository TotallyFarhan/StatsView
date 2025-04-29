import pandas

qbStatTable = "backend/quarterbackDataset.csv"
columns = ["Player", "Age", "Team", "G", "QBrec", "Cmp", "Att", "Cmp%", "Yds", "TD", "Int", "1D", "Succ%", "Lng", "Y/A", "Y/C", "Rate", "QBR", "Sk", "4QC", "GWD"]
colLabels = ["Player", "Age", "Team", "Games Played", "Record", "Completions", "Attempts", "Completion %", "Pass Yards", "Touchdowns", "Interceptions", "First Downs Passing", "Success Rate", "Longest Pass", "Yards/Attempt", "Yards/Completion", "Rate", "QBR", "Sacks", "4Q Comebacks", "Game Winning Drives"]
dataset = pandas.read_csv(qbStatTable, usecols=columns)

dataset.columns = colLabels

print("The file " + qbStatTable + " has data with the dimensions: " + str(dataset.shape))

print()

# Prints the first 20 rows of the dataset
print("First 20 peices of data from dataset: ")
print(dataset.head(20))

print()

# Prints statistics about each column in the dataset, including how much data it has in each column, and its average value, standard deviation and maximum/minimum value.
print("Statistics about dataset for each column (mean, standard deviation, count, min, max): ")
print(dataset.describe())

print()
