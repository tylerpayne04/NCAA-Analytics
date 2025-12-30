# NCAA-Analytics

NCAA Basketball Data Cleaning & Exploratory Analysis (2020-2024)

## Overview
This project explores 5 seasons of NCAA basketball data (2020-2024) through data cleaning and data analysis. The goal is to transform raw, messy sports data into a clean, analyzable format and to produce meaningful insights about team performance, offensive/defensive efficiency, and tournament success factors.

## Objectives

 - Clean and preprocess raw NCAA basketball data across 5 seasons
 - Standardize inconsistent column names and handle missing values
 - Identify trends in team performance and tournament success
 - Analyze correlations between efficiency metrics and winning
 - Create clear visualizations to communicate insights

## Dataset
The dataset contains NCAA basketball team-level statistics across 5 seasons (2020-2024), including:
- **1,783 total team records** (353-363 teams per season)
- Performance metrics: wins, adjusted offensive/defensive efficiency, power ratings
- Shooting statistics: 2-point and 3-point percentages
- Rebounding and turnover rates
- Tournament participation data

## Tools & Technologies

 - **Python** - Primary programming language
 - **pandas** - Data manipulation and cleaning
 - **matplotlib & seaborn** - Data visualization

## Key Analysis & Visualizations

### 1. Offensive vs Defensive Efficiency
- Scatter plot showing the relationship between offensive and defensive efficiency, colored by wins
- **Key Insight**: Elite teams excel in both offense AND defense - the top-performing teams cluster in the high offense/low defense (good) region
- Teams with balanced efficiency metrics have significantly more wins

### 2. Shooting Efficiency Correlation
- Analysis of 2-point vs 3-point shooting percentages and their impact on winning
- **Key Insight**: Top 25% of teams (by wins) shoot ~3-4% better from both 2-point and 3-point range
- Shooting efficiency strongly correlates with success

### 3. Tournament Success Factors
- Comparison of tournament vs non-tournament teams across multiple metrics
- Win distribution analysis showing clear performance gaps

## Key Findings

### Tournament Success
- Tournament teams win **~8 more games** on average than non-tournament teams
- Tournament teams have significantly better **offensive efficiency**
- **Defensive efficiency is critical**: Tournament teams allow fewer points per possession
- Only ~15% of teams make the tournament, highlighting the competitive threshold

### Winning Formula
- **Balance matters**: Success requires excellence in both offense and defense
- Top teams demonstrate **3-4% better shooting efficiency** from the field
- Defensive efficiency is equally important as offensive output
- Consistency across multiple metrics predicts tournament success

### Conference Performance
- Conference affiliation  impacts team performance
- Top conferences show higher average wins and tournament representation

### Team Consistency (2020-2024)
- Teams appearing in all 5 seasons show varying levels of consistency
- Top consistent performers average 25+ wins per season
- Program stability and sustained excellence correlate with tournament success

## Results & Insights

This analysis demonstrates how cleaned, standardized data enables meaningful insights into NCAA basketball performance:

1. **Data quality matters**: Standardizing 5 seasons of data with inconsistent formats was essential for accurate analysis
2. **Multiple factors drive success**: Winning teams excel across offense, defense, and shooting efficiency
3. **Tournament threshold is clear**: A measurable performance gap separates tournament and non-tournament teams
4. **Visualizations reveal patterns**: Scatter plots effectively show the relationship between efficiency metrics and wins

## Project Structure
```
NCAA-Analytics/
├── Dataset/
│   ├── cbb20.csv - cbb24.csv (individual season data)
│   └── combined_cbb_data.csv (cleaned, combined dataset)
├── explore_data.py (initial data exploration)
├── clean_data.py (data cleaning and standardization)
├── combine_data.py (merge all seasons)
├── data_exploration.py (statistical analysis)
├── create_visualizations.py (generate plots)
├── summary_findings.py (key findings report)
└── README.md
```

## How to Run
1. Install dependencies: `pip install pandas matplotlib seaborn`
2. Clean the data: `python clean_data.py`
3. Combine datasets: `python combine_data.py`
4. Run analysis: `python data_exploration.py`
5. Create visualizations: `python create_visualizations.py`
6. View findings: `python summary_findings.py`