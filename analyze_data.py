import pandas as pd
import matplotlib.pyplot as plt

# Load combined dataset
combined_df = pd.read_csv('/Users/tylerpayne/Personal/NCAA-Analytics/Dataset/combined_cbb_data.csv')

print("Exploring Combined NCAA Basketball Dataset")
print("="*40 + "\n")

# Basic Statistics
print("Dataset Overview:")
print(f"Total teams across 5 seasons: {len(combined_df)}")
print(f"Seasons covered: {combined_df['SEASON'].nunique()}")
print(f"Teams per season: {combined_df.groupby('SEASON')['TEAM'].nunique().to_dict()}")
print("\n" + "="*40 + "\n")

# Statistical Summary
print("Statistical Summary of Key Metrics:")
metrics_df = combined_df[['W', 'ADJOE', 'ADJDE', 'BARTHAG']].copy()
metrics_df.columns = ['Wins', 'Offensive Efficiency', 'Defensive Efficiency', 'Power Rating']
print(metrics_df.describe())
print("\n" + "="*40 + "\n")

print("Top 10 Teams by Wins:")
top_teams = combined_df.nlargest(10, 'W')[['SEASON', 'TEAM', 'CONF','W', 'G']].copy()
top_teams.columns = ['Season', 'Team', 'Conference', 'Wins', 'Games Played']
print(top_teams)
print("\n" + "="*40 + "\n")

# Tournament teams vs Non-tournament teams analysis
tournament_teams = combined_df[combined_df['POSTSEASON'].notna()]
print(f"Tournament Teams: {len(tournament_teams)}")
print(f"Non-Tournament Teams: {len(combined_df) - len(tournament_teams)}")


# Data Visualization ------------
print("="*40 + "\n")
print("Creating Visualizations")
print("\n" + "="*40 + "\n")

# Distribution of Wins
plt.figure(figsize=(10, 6))
plt.hist(combined_df['W'], bins=20, edgecolor='black')
plt.title('Distribution of Wins Across All Teams (2020-2024)')
plt.xlabel('Number of Wins')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.5)
plt.savefig('wins_distribution.png')
print("Saved: wins_distribution.png")
plt.close()

# Wins by Season
plt.figure(figsize=(10, 6))
combined_df.groupby('SEASON')['W'].mean().plot(kind='bar')
plt.title('Average Wins by Season')
plt.xlabel('Season')
plt.ylabel('Average Wins')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.5)
plt.savefig('wins_by_season.png')
print("Saved: wins_by_season.png")
plt.close()

# Offensive vs Defensive Rating
plt.figure(figsize=(10, 6))
plt.scatter(combined_df['ADJOE'], combined_df['ADJDE'], alpha=0.5)
plt.title('Offensive vs Defensive Efficiency')
plt.xlabel('Adjusted Offensive Efficiency')
plt.ylabel('Adjusted Defensive Efficiency')
plt.grid(alpha=0.3)
plt.savefig('offense_vs_defense.png')
print("Saved: offense_vs_defense.png")
plt.close()

print("\nAll visualizations completed and saved.")

# Analyze Performance Trends
print("\n" + "="*40 + "\n")
print("Analyzing Performance Trends")
print("\n" + "="*40 + "\n")

# Tournament vs Non-Tournament Teams
tournament_teams = combined_df[combined_df['POSTSEASON'].notna()]
non_tournament = combined_df[combined_df['POSTSEASON'].isna()]

print("Tournament Teams vs Non-Tournament Teams:")
print(f"Tournament teams average wins: {tournament_teams['W'].mean():.2f}")
print(f"Non-tournament teams average wins: {non_tournament['W'].mean():.2f}")
print(f"Tournament teams average Offensive Efficiency: {tournament_teams['ADJOE'].mean():.2f}")
print(f"Non-tournament teams average Offensive Efficiency: {non_tournament['ADJOE'].mean():.2f}")
print(f"Tournament teams average Defensive Efficiency: {tournament_teams['ADJDE'].mean():.2f}")
print(f"Non-tournament teams average Defensive Efficiency: {non_tournament['ADJDE'].mean():.2f}")
print("\n")

# Best Conferences
print("Top 5 Conferences by Average Wins:")
conf_performance = combined_df.groupby('CONF')['W'].mean().sort_values(ascending=False)
print(conf_performance.head())
print("\n")

# Most Consistent Teams (appeared in all 5 seasons with good records)
team_appearances = combined_df.groupby('TEAM').size()
consistent_teams = team_appearances[team_appearances == 5].index
consistent_performance = combined_df[combined_df['TEAM'].isin(consistent_teams)]
print("Teams that appeared all 5 seasons - Average Wins:")
print(consistent_performance.groupby('TEAM')['W'].mean().sort_values(ascending=False).head(10))
print("\n")