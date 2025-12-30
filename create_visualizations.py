import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# Load combined dataset
df = pd.read_csv('/Users/tylerpayne/Personal/NCAA-Analytics/Dataset/combined_cbb_data.csv')

print("Creating Visualizations")
print("="*50 + "\n")

# Offensive vs Defensive Efficiency with Win Distribution
plt.figure(figsize=(12, 8))
scatter = plt.scatter(df['ADJOE'], df['ADJDE'], c=df['W'], cmap='RdYlGn', alpha=0.6, s=50, edgecolors='black', linewidth=0.5)
plt.colorbar(scatter, label='Wins')
plt.title('Offensive vs Defensive Efficiency (Colored by Wins)', fontsize=16, fontweight='bold')
plt.xlabel('Offensive Efficiency', fontsize=12)
plt.ylabel('Defensive Efficiency', fontsize=12)
plt.axhline(y=df['ADJDE'].median(), color='gray', linestyle='--', alpha=0.5, label='Median Defense')
plt.axvline(x=df['ADJOE'].median(), color='gray', linestyle='--', alpha=0.5, label='Median Offense')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('offense_defense_scatter.png', dpi=300)
print("Saved: offense_defense_scatter.png")
plt.close()

# 3-Point vs 2-Point Shooting Efficiency
plt.figure(figsize=(12, 8))
plt.scatter(df['2P_O'], df['3P_O'], c=df['W'], cmap='plasma', alpha=0.6, s=50, edgecolors='black', linewidth=0.5)
plt.colorbar(label='Wins')
plt.title('2-Point vs 3-Point Shooting Efficiency', fontsize=16, fontweight='bold')
plt.xlabel('2-Point Shooting %', fontsize=12)
plt.ylabel('3-Point Shooting %', fontsize=12)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('shooting_efficiency.png', dpi=300)
print("Saved: shooting_efficiency.png")
plt.close()

print("\n" + "="*40)
print("All visualizations created successfully")
print("="*40)
