import pandas
import duckdb
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

qbStatTable = "backend/quarterbackDataset.csv"
columns = ["Player", "Age", "Team", "G", "QBrec", "Cmp", "Att", "Cmp%", "Yds", "TD", "Int", "1D", "Succ%", "Lng", "Y/A", "Y/C", "Rate", "QBR", "Sk", "4QC", "GWD"]
colLabels = ["Player", "Age", "Team", "Games Played", "Record", "Completions", "Attempts", "Completion %", "Pass Yards", "Touchdowns", "Interceptions", "First Downs Passing", "Success Rate", "Longest Pass", "Yards/Attempt", "Yards/Completion", "Rate", "QBR", "Sacks", "4Q Comebacks", "Game Winning Drives"]
dataset = pandas.read_csv(qbStatTable, usecols=columns)

dataset.columns = colLabels

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

sns.set_theme()

def create_graph(stat, limit, ascending):
    query = '''SELECT Player, Team, "''' + stat + '''" FROM dataset ORDER BY "''' + stat + '''" ''' + ascending + ''' LIMIT ''' + str(limit)
    result = duckdb.query(query).to_df()
    imgSrc = "backend/graphs/" + stat + str(limit) + ascending + ".png"
    
    plt.figure(figsize=(max(7, limit * 0.5), 7))
    graph = sns.barplot(result, x="Player", y=stat, hue='Team', palette=teamColors, legend=False)
    for i in range(len(graph.containers)):
        graph.bar_label(graph.containers[i])
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(imgSrc)

    return imgSrc;