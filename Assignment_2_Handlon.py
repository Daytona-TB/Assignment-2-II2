import numpy as np
import pandas as pd


data = np.genfromtxt('/Users/lucashandlon/Desktop/I.I. 2/NBA_Player_Stats.tsv', delimiter='\t', dtype=None, encoding=None, names=True)

# Extract necessary columns
fgm = data['FGM']
fga = data['FGA']
three_pm = data['3PM']
three_pa = data['3PA']
ftm = data['FTM']
fta = data['FTA']
pts = data['PTS']
minutes = data['MIN']
games_played = data['GP']
blocks = data['BLK']
steals = data['STL']

# Compute metrics using NumPy
fg_percentage = np.divide(fgm, fga, out=np.zeros_like(fgm, dtype=float), where=fga != 0)
three_p_percentage = np.divide(three_pm, three_pa, out=np.zeros_like(three_pm, dtype=float), where=three_pa != 0)
ft_percentage = np.divide(ftm, fta, out=np.zeros_like(ftm, dtype=float), where=fta != 0)
pts_per_min = np.divide(pts, minutes, out=np.zeros_like(pts, dtype=float), where=minutes != 0)
overall_shooting = np.divide((fgm + three_pm + ftm), (fga + three_pa + fta), out=np.zeros_like(fgm, dtype=float), where=(fga + three_pa + fta) != 0)
blocks_per_game = np.divide(blocks, games_played, out=np.zeros_like(blocks, dtype=float), where=games_played != 0)
steals_per_game = np.divide(steals, games_played, out=np.zeros_like(steals, dtype=float), where=games_played != 0)

# Combine results into a structured NumPy array
structured_array = np.array(
    list(zip(data['Season'], data['Player'], fg_percentage, three_p_percentage, ft_percentage,
             pts_per_min, overall_shooting, blocks_per_game, steals_per_game)),
    dtype=[('Season', 'U20'), ('Player', 'U50'), ('FG%', 'f4'), ('3P%', 'f4'), ('FT%', 'f4'),
           ('PTS_per_MIN', 'f4'), ('Overall_Shooting%', 'f4'), ('BLK_per_GP', 'f4'), ('STL_per_GP', 'f4')]
)

# Extract the top 100 players for each metric
def get_top_100_players(metric_name):
    return np.sort(structured_array, order=metric_name)[-100:]

# Create a dictionary to store each metric's top 100
metrics = {
    'FG%': get_top_100_players('FG%'),
    '3P%': get_top_100_players('3P%'),
    'FT%': get_top_100_players('FT%'),
    'PTS_per_MIN': get_top_100_players('PTS_per_MIN'),
    'Overall_Shooting%': get_top_100_players('Overall_Shooting%'),
    'BLK_per_GP': get_top_100_players('BLK_per_GP'),
    'STL_per_GP': get_top_100_players('STL_per_GP')
}

# Create a list to store data sections
csv_sections = []
for metric, data in metrics.items():
    df_metric = pd.DataFrame(data)
    df_metric.insert(0, 'Metric', metric)  # Insert metric name as first column
    csv_sections.append(df_metric)
    csv_sections.append(pd.DataFrame(columns=df_metric.columns))  # Blank row separator

# Combine sections and save to a single CSV file
output_path = '/Users/lucashandlon/Desktop/I.I. 2/NBA_Top_100_Combined.csv'
pd.concat(csv_sections).to_csv(output_path, index=False)

print("Analysis complete! All top 100 metrics have been saved in a single CSV file at:", output_path)
