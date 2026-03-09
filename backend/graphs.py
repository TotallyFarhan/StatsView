import pandas
import duckdb
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import io
import os

# Headless Backend
matplotlib.use("Agg")

baseDirectory = os.path.dirname(__file__)
qbStatTable = os.path.join(baseDirectory, "quarterbackDataset.csv")
# Array of all the column names to be used in our dataset
columns = ["Player", "Age", "Team", "G", "QBrec", "Cmp", "Att", "Cmp%", "Yds", "TD", "Int", "1D", "Succ%", "Lng", "Y/A", "Y/C", "Rate", "QBR", "Sk", "4QC", "GWD"]
# Array of all the column labels to be used in the dataset
colLabels = ["Player", "Age", "Team", "Games Played", "Record", "Completions", "Attempts", "Completion Percentage", "Pass Yards", "Touchdowns", "Interceptions", "First Downs Passing", "Success Rate", "Longest Pass", "Yards/Attempt", "Yards/Completion", "Rate", "QBR", "Sacks", "4Q Comebacks", "Game Winning Drives"]
# Creates a Pandas Dataframe using the CSV file created from database.py with the columns specified in the columns array
dataset = pandas.read_csv(qbStatTable, usecols=columns)
# Sets the labels of the columns to the array of column labels above
dataset.columns = colLabels
# Dictionary containing each team name's abbreviation (as found in the dataset) and its designated color for the bar plot bars
teamColors = {
    "WAS": "#5A0C0C",
    "PHI": "#004C54",
    "DAL": "#002244",
    "NYG": "#031C65",
    
    "TAM": "#AD1A2E",
    "CAR": "#0085CA",
    "NOR": "#D4BD8E",
    "ATL": "#BF1329",
    
    "SEA": "#69BE28",
    "SFO": "#C89D6C",
    "ARI": "#9F2845",
    "LAR": "#FFD101",
    
    "CHI": "#E64100",
    "MIN": "#592A83",
    "DET": "#0076B4",
    "GNB": "#1A342D",
    
    "KAN": "#E31837",
    "LVR": "#1D1D1B",
    "LAC": "#0081C7",
    "DEN": "#FB4F14",
    
    "MIA": "#008A96",
    "BUF": "#143D75",
    "NWE": "#001C42",
    "NYJ": "#105840",
    
    "BAL": "#221361",
    "CIN": "#FC4F15",
    "PIT": "#FFC20F",
    "CLE": "#EB3624",
    
    "IND": "#013369",
    "JAX": "#CB962B",
    "HOU": "#03202F",
    "TEN": "#0193DD"
}
# Sets the theme to default
sns.set_theme()

# Function to create a graph given a specified statistic, number of quarterbacks to view and whether data should be ascending or descending
def create_graph(stat, limit, ascending):
    # Prevent potential SQL Injection
    if stat not in colLabels:
        return "Invalid Stat"
    # String of SQL query to find the data based on the parameters passed into the function
    query = '''SELECT Player, Team, "''' + stat + '''" FROM dataset ORDER BY "''' + stat + '''" ''' + ascending + ''' LIMIT ''' + str(limit)
    result = duckdb.query(query).to_df() # Uses duckdb library to use the query on the quarterback dataset and convert it to another mini dataframe of specified data for graph creation
    #imgSrc = "graphs/" + stat + str(limit) + ascending + ".png" # Creates unique image filename based on user form submission
    
    plt.figure(figsize=(max(7, limit * 0.5), 7)) # Creates graph figure size based on how much data is in it
    graph = sns.barplot(result, x="Player", y=stat, hue='Team', palette=teamColors, legend=False) # Creates the bar plot based on the query and sets color palette to each quarterback's team color
    # Adds label containing the number for each statistic for each quarterback on top of their bar
    for i in range(len(graph.containers)):
        graph.bar_label(graph.containers[i])
    plt.xticks(rotation=45, ha='right') # Rotates the Quarterback name label on the x axis by 45 degrees
    plt.tight_layout() 

    buffer = io.BytesIO() # Create memory buffer
    plt.savefig(buffer, format="png") # Saves created graph to the buffer
    plt.close()

    buffer.seek(0)

    return buffer # Return buffer