"""
Global AI Attitudes Analysis - Interdisciplinary Analysis of Pew 2025 Survey
Analyzes awareness, concern, trust patterns across education, region, internet use
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from pathlib import Path
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json

# Setup output directory
Path("output/tables").mkdir(parents=True, exist_ok=True)
Path("output/figures").mkdir(parents=True, exist_ok=True)

def load_and_clean_data(csv_path="data/raw/ai_global_attitudes_2025.csv"):
    """Load and standardize survey data"""
    df = pd.read_csv(csv_path)
    
    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('[^a-z0-9_]', '', regex=True)
    
    # Recode key variables (adjust based on your exact column names)
    df['awareness'] = pd.to_numeric(df.get('ai_awareness', 0), errors='coerce')
    df['concern_excited'] = pd.Categorical(df.get('ai_attitude', ''), 
                                         categories=['excited', 'concerned', 'equal'])
    df['trust_own_country'] = pd.to_numeric(df.get('trust_own_country', 0), errors='coerce')
    df['education'] = pd.Categorical(df.get('education', ''), 
                                   categories=['primary', 'secondary', 'post_secondary'])
    df['internet_use'] = pd.to_numeric(df.get('internet_frequency', 6), errors='coerce')
    df['region'] = df.get('region', 'Other')
    
    # Save cleaned data
    df.to_csv("output/cleaned_data.csv", index=False)
    return df

def descriptive_tables(df):
    """Create summary tables by region and education"""
    
    # Table 1: Awareness by country/region
    awareness_table = (df.groupby(['region', 'country'])['awareness']
                      .agg(['mean', 'count']).round(3))
    awareness_table.to_csv("output/tables/awareness_by_region.csv")
    
    # Table 2: Concern vs excitement
    attitude_table = (df.groupby('region')['concern_excited']
                     .value_counts(normalize=True).unstack().fillna(0)*100)
    attitude_table.to_csv("output/tables/attitude_by_region.csv")
    
    print("Descriptive tables saved to output/tables/")

def regression_models(df):
    """Run main regression models"""
    
    # Model 1: Awareness (OLS)
    ols_model = smf.ols('awareness ~ education + internet_use + age + C(region)', data=df).fit()
    ols_model.summary()
    with open("output/tables/ols_awareness.txt", "w") as f:
        f.write(ols_model.summary().as_text())
    
    # Model 2: Concern (logit)
    df['concern_binary'] = (df['concern_excited'] == 'concerned').astype(int)
    logit_model = smf.logit('concern_binary ~ awareness + education + internet_use + C(region)', 
                           data=df).fit()
    with open("output/tables/logit_concern.txt", "w") as f:
        f.write(logit_model.summary().as_text())
    
    # Model 3: Trust (logit)
    logit_trust = smf.logit('trust_own_country ~ awareness + education + C(region)', data=df).fit()
    with open("output/tables/logit_trust.txt", "w") as f:
        f.write(logit_trust.summary().as_text())
    
    print("Regression results saved to output/tables/")

def create_figures(df):
    """Generate publication-ready figures"""
    
    # Figure 1: Awareness by education and region
    fig1 = px.box(df, x='education', y='awareness', color='region',
                 title="AI Awareness by Education Level and Region")
    fig1.write_image("output/figures/awareness_by_education.png")
    
    # Figure 2: Concern vs Excitement Heatmap
    attitude_pivot = df.groupby(['region', 'concern_excited']).size().unstack(fill_value=0)
    fig2 = px.imshow(attitude_pivot.T, aspect="auto", 
                    title="Concern vs Excitement by Region (%)")
    fig2.write_image("output/figures/concern_heatmap.png")
    
    # Figure 3: Trust by Awareness
    fig3 = px.scatter(df, x='awareness', y='trust_own_country', 
                     color='education', trendline="ols",
                     title="Trust in National AI Regulation by Awareness")
    fig3.write_image("output/figures/trust_regression.png")
    
    # Metadata for figures
    for fig_name in ['awareness_by_education.png', 'concern_heatmap.png', 'trust_regression.png']:
        meta = {
            "caption": f"Figure: {fig_name.replace('.png', '').title()}",
            "description": f"Analysis of Pew 2025 Global AI Attitudes Survey"
        }
        with open(f"output/figures/{fig_name}.meta.json", "w") as f:
            json.dump(meta, f, indent=2)
    
    print("Figures saved to output/figures/")

def main():
    """Main analysis pipeline"""
    print("Loading and cleaning data...")
    df = load_and_clean_data()
    
    print("Creating descriptive tables...")
    descriptive_tables(df)
    
    print("Running regression models...")
    regression_models(df)
    
    print("Generating figures...")
    create_figures(df)
    
    print("Analysis complete! Check output/ folder for results.")
    print("\nKey files generated:")
    print("- output/cleaned_data.csv")
    print("- output/tables/*.csv, *.txt") 
    print("- output/figures/*.png + *.meta.json")

if __name__ == "__main__":
    main()
