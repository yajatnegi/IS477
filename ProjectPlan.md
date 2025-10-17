# Project Plan (Milestone 2)


## Overview
The goal of this project is to analyze the relationship between median household income and median home values across U.S. counties.  
Using data from the Zillow Home Value Index (ZHVI) and the USDA Economic Research Service (ERS), we aim to determine whether counties with higher income levels also have higher home prices.  


## Research Questions
1. Do U.S. counties with higher median household incomes have higher median home values?  
2. How strong is the correlation between income and home prices across counties?  


## Team

**Arnav Theppasandra:** Focuses on data acquisition, organization, and integration.  
**Yajat Negi:** Focuses on analysis, documentation, and visualization.  

Both members will contribute to the project equally. 


## Datasets

**1. Zillow Home Value Index (ZHVI)**  
Source: [Zillow Research Data](https://www.zillow.com/research/data/)  
Description: County-level monthly estimates of typical single-family home values across the United States.  
Format: CSV
Purpose: Provides housing price data to compare against household income levels.

**2. USDA Economic Research Service (ERS) – Median Household Income**  
Source: [USDA County-Level Data Sets](https://www.ers.usda.gov/data-products/county-level-data-sets/download-data/)  
Description: Annual estimates of median household income by county in the United States.  
Format: CSV
Purpose: Provides socioeconomic data to analyze its relationship with housing prices.


## Timeline
For Milestone 2 (Project Plan), we are finalizing our topic, defining our research question, and selecting datasets. This stage focuses on outlining our goals, roles, and approach for integrating the data sources.

During Milestone 3 (Interim Status Report), we will collect, clean, and integrate both datasets. The Zillow data will be aggregated from monthly to yearly values, and the USDA income dataset will be formatted and aligned for merging. We will then perform exploratory analysis, document our process, and prepare an updated timeline with progress details.

For Milestone 4 (Final Project Submission), we will complete our analysis, produce visualizations, and create the final report summarizing our workflow, findings, and metadata. We will also automate the workflow to ensure full reproducibility and prepare the GitHub release with all scripts, data documentation, and results.

## Constraints
- Some county names may differ between datasets 
- Zillow data is monthly while income data is annual meaning it requires aggregation.  
- Missing data may occur in small or rural counties.  


## Gaps 
- Still finalizing the specific analysis methods and metrics to use  
- Need to decide how to visualize and present results  
- Plan to refine data cleaning and automation steps after integration 
