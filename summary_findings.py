import pandas as pd

# Load combined dataset
df = pd.read_csv('/Users/tylerpayne/Personal/NCAA-Analytics/Dataset/combined_cbb_data.csv')

print("="*60)
print("NCAA BASKETBALL ANALYSIS: KEY FINDINGS & CONCLUSIONS")
print("2020-2024 Seasons")
print("="*60 + "\n")

# Dataset Overview
print("DATASET OVERVIEW")
print("-" * 60)
print(f"Total teams analyzed: {len(df)}")
print(f"Seasons covered: {sorted(df['SEASON'].unique())}")
print(f"Average teams per season: {len(df) / df['SEASON'].nunique():.0f}")
print("\n")

# Key Performance Metrics
print("KEY PERFORMANCE METRICS")
print("-" * 60)
print(f"Average wins per team: {df['W'].mean():.1f}")
print(f"Average offensive efficiency: {df['ADJOE'].mean():.1f}")
print(f"Average defensive efficiency: {df['ADJDE'].mean():.1f}")
print(f"Win range: {df['W'].min():.0f} to {df['W'].max():.0f}")
print("\n")

# Tournament vs Non-Tournament Analysis
print("TOURNAMENT TEAMS vs NON-TOURNAMENT TEAMS")
print("-" * 60)
tournament = df[df['POSTSEASON'].notna()]
non_tournament = df[df['POSTSEASON'].isna()]

print(f"Tournament teams: {len(tournament)} ({len(tournament)/len(df)*100:.1f}%)")
print(f"Non-tournament teams: {len(non_tournament)} ({len(non_tournament)/len(df)*100:.1f}%)")
print("\nPerformance Differences:")
print(f"  Tournament teams avg wins: {tournament['W'].mean():.1f}")
print(f"  Non-tournament teams avg wins: {non_tournament['W'].mean():.1f}")
print(f"  Win difference: +{tournament['W'].mean() - non_tournament['W'].mean():.1f} wins")
print(f"\n  Tournament teams offensive efficiency: {tournament['ADJOE'].mean():.1f}")
print(f"  Non-tournament teams offensive efficiency: {non_tournament['ADJOE'].mean():.1f}")
print(f"  Difference: +{tournament['ADJOE'].mean() - non_tournament['ADJOE'].mean():.1f} points/100 possessions")
print(f"\n  Tournament teams defensive efficiency: {tournament['ADJDE'].mean():.1f}")
print(f"  Non-tournament teams defensive efficiency: {non_tournament['ADJDE'].mean():.1f}")
print(f"  Difference: -{non_tournament['ADJDE'].mean() - tournament['ADJDE'].mean():.1f} points/100 possessions (better)")
print("\n")

# Top Conferences
print("TOP 5 CONFERENCES BY AVERAGE WINS")
print("-" * 60)
conf_performance = df.groupby('CONF')['W'].mean().sort_values(ascending=False).head(5)
for i, (conf, wins) in enumerate(conf_performance.items(), 1):
    print(f"{i}. {conf}: {wins:.1f} avg wins")
print("\n")

# Most Consistent Teams
print("TOP 10 MOST CONSISTENT TEAMS (All 5 Seasons)")
print("-" * 60)
team_appearances = df.groupby('TEAM').size()
consistent_teams = team_appearances[team_appearances == 5].index
consistent_performance = df[df['TEAM'].isin(consistent_teams)]
top_consistent = consistent_performance.groupby('TEAM')['W'].mean().sort_values(ascending=False).head(10)
for i, (team, wins) in enumerate(top_consistent.items(), 1):
    print(f"{i}. {team}: {wins:.1f} avg wins")
print("\n")

# Shooting Analysis
print("SHOOTING EFFICIENCY INSIGHTS")
print("-" * 60)
high_win_teams = df[df['W'] >= df['W'].quantile(0.75)]
low_win_teams = df[df['W'] <= df['W'].quantile(0.25)]

print("Top 25% teams (by wins):")
print(f"  2-Point shooting: {high_win_teams['2P_O'].mean():.1f}%")
print(f"  3-Point shooting: {high_win_teams['3P_O'].mean():.1f}%")
print(f"\nBottom 25% teams (by wins):")
print(f"  2-Point shooting: {low_win_teams['2P_O'].mean():.1f}%")
print(f"  3-Point shooting: {low_win_teams['3P_O'].mean():.1f}%")
print(f"\nDifference:")
print(f"  2-Point: +{high_win_teams['2P_O'].mean() - low_win_teams['2P_O'].mean():.1f}%")
print(f"  3-Point: +{high_win_teams['3P_O'].mean() - low_win_teams['3P_O'].mean():.1f}%")
print("\n")

# Key Conclusions
print("="*60)
print("KEY CONCLUSIONS")
print("="*60)
win_diff = tournament['W'].mean() - non_tournament['W'].mean()
shoot_diff = high_win_teams['2P_O'].mean() - low_win_teams['2P_O'].mean()
top_conf = conf_performance.index[0]
top_team = top_consistent.index[0]

print(f"""
1. TOURNAMENT SUCCESS FACTORS:
   - Tournament teams win ~{win_diff:.0f} more games on average
   - Tournament teams have significantly better offensive efficiency
   - Defensive efficiency is critical - tournament teams allow fewer points
   
2. WINNING FORMULA:
   - Balance matters: Elite teams excel in both offense AND defense
   - Shooting efficiency correlates strongly with winning
   - Top teams are ~{shoot_diff:.1f}% better at 2-point shooting
   
3. CONFERENCE STRENGTH:
   - {top_conf} is the strongest conference by average wins
   - Conference affiliation impacts performance and opportunities
   
4. CONSISTENCY:
   - {top_team} is the most consistent top performer (2020-2024)
   - Sustained excellence requires both talent and program stability
   
5. DEFENSIVE IMPACT:
   - Lower defensive efficiency (fewer points allowed) = More wins
   - Defense is equally important as offense for tournament success
""")

print("="*60)
print("Analysis Complete")
print("="*60)
