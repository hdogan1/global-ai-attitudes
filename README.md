# Global AI Attitudes (Pew Research Center Data)

## Overview
This repository provides code and documentation for analyzing publicly available survey data from the Pew Research Center related to public attitudes toward artificial intelligence (AI). The goal of this project is to support reproducible analysis and exploration of AI perceptions across demographic groups.

The dataset itself is not originally collected or owned by the author of this repository. It is sourced from Pew Research Center and redistributed for analytical and educational purposes in accordance with Pew’s data usage policies.

---

## Data Source
The original dataset was collected and published by:

**Pew Research Center**

For access to the original dataset and documentation, please refer to the official source:
https://www.pewresearch.org/

Any redistributed or processed versions used in this repository should be considered derivative and for research/educational use only.

---

## Repository Contents
/scripts # Python scripts for data cleaning, analysis, and visualization
/data # Optional (if included): processed or sample data only
/docs # Supporting documentation (codebook summaries, notes)
/figures # Output visualizations (if applicable)
README.md # Project documentation


---

## Important Notes on Data Use

- The original dataset is owned and maintained by Pew Research Center.
- This repository does not claim ownership of the raw data.
- Users should consult Pew Research Center’s terms of use before redistributing or publishing derived datasets.
- Any reuse should properly cite Pew Research Center as the original data source.

---

## Methods (Summary)

This project includes secondary data analysis using Python. Typical processing steps include:
- Data cleaning and filtering  
- Variable recoding and transformation  
- Descriptive statistical analysis  
- Visualization of key trends in AI attitudes  

All analysis is reproducible using the scripts provided in this repository.

---

## How to Reproduce

1. Obtain the original dataset from Pew Research Center  
2. Place the dataset (or approved subset) in the `/data` directory  
3. Run the analysis scripts in order:

```bash
python scripts/01_clean_data.py
python scripts/02_analysis.py
python scripts/03_visualizations.py
Citation

Please cite the original data source:

Pew Research Center. (Year). [Title of dataset/report]. https://www.pewresearch.org/

If using this repository, please also cite:

Dogan, H. (2026). Global AI Attitudes Analysis (Pew Research Data). GitHub.
https://github.com/hdogan1/global-ai-attitudes

License

This repository’s code is released under the MIT License.

Note: The underlying dataset is subject to Pew Research Center’s data usage policies and is not redistributed here.

Contact

For questions or collaboration inquiries:
Hulya Dogan
Virginia Tech
