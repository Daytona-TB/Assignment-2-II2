Project ReadMe: NBA Player Metrics Analysis

Project Purpose:

This project focuses on analyzing basketball player performance metrics using NumPy and Python. The dataset includes detailed statistics for players across multiple seasons, and the goal is to extract insights that are useful for analysts, coaches, and teams. Specifically, the project computes shooting accuracy metrics, points per minute, and defensive statistics, and identifies the top 100 players for each metric in an easily digestible format.

Class Design and Implementation:

While this project primarily utilizes procedural programming, here is a suggested class design that could enhance its structure:

Class: PlayerStatsAnalyzer

This class encapsulates the functionality of loading, analyzing, and saving basketball player statistics.

Attributes:

data_path: The file path for the input dataset (string).

output_path: The file path for saving the output CSV (string).

data: The loaded dataset as a NumPy structured array.

metrics: A dictionary holding the top 100 players for each computed metric.

Methods:

__init__(self, data_path, output_path):
Initializes the class with file paths and sets up placeholders for the dataset and metrics.

load_data(self):
Loads the dataset from the specified file path using NumPy.

compute_metrics(self):
Calculates field goal accuracy, three-point accuracy, free throw accuracy, points per minute, overall shooting accuracy, blocks per game, and steals per game.

get_top_100(self, metric_name):
Retrieves the top 100 players for a specific metric.

save_to_csv(self):
Compiles all top 100 lists into a single CSV file with clear sections.

Limitations:

This class assumes clean and correctly formatted data.

The dataset must contain all required columns; missing values are not handled explicitly.

The analysis is limited to predefined metrics and does not account for advanced metrics like player impact estimate (PIE).

