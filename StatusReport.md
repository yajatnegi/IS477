# Status Report (Milestone 3)

## Overview
After submitting our project plan for Milestone 2 our team has made  progress toward building the foundations of an end-to-end reproducible data workflow. We successfully acquired both datasets, created a complete repository structure, began planning cleaning and merging scripts, drafted a workflow outline, and began preparing exploratory analysis. While we still need to do the full cleaning, integration, and automation steps, this milestone is progress in data acquisition, workflow setup, and documentation.

## Progress Update

### Data Acquisition
We obtained both required datasets and added them to the project repository:

- **Zillow ZHVI (County-Level)** – Monthly county-level home value estimates  
- **USDA ERS Median Household Income** – Annual income estimates for U.S. counties  

Both datasets were renamed and stored in:

```
data/raw/zillow_zhvi_county.csv
data/raw/usda_median_income_county.csv
```

### Repository Structure
A complete reproducible folder structure was created:

```
analysis/
data/
   raw/
   cleaned/
   final/
docs/
scripts/
visuals/
workflows/
ProjectPlan.md
StatusReport.md
```

### Initial Scripts
Initial scripts were added under `scripts/` to outline the cleaning and merging workflow:

- `clean_income.py`
- `clean_zhvi.py`
- `merge_data.py`
- `run_workflow.py`

These scripts include early logic for reading data, standardizing column names, detecting FIPS codes, and preparing for merging. They serve as the foundation for the full cleaning and integration pipeline to be completed in Milestone 4.

### Workflow Automation
A placeholder `Snakefile` was added under `workflows/` to outline the workflow:

- Load raw data  
- Clean Zillow dataset  
- Clean USDA dataset  
- Merge datasets  
- Generate final dataset  
- Run exploratory analysis  

Full automation and reproducibility features will be implemented in Milestone 4.

### Exploratory Analysis
A draft notebook (`analysis/EDA.ipynb`) was added.  
While cleaned datasets are not yet available, the notebook outlines:

- Data preview  
- Summary statistics  
- Correlation matrix  
- Scatterplots (income vs. home value)

This notebook will serve as the analysis foundation once integrated data is available.

### Documentation
We updated:

- `ProjectPlan.md` (previous milestone)  
- `StatusReport.md` (this document)  
- Repository organization and file structure documentation  

More detailed metadata, ethical/legal considerations, and provenance documentation will be added in Milestone 4.


## Updated Timeline

Since the project plan submission, our timeline has shifted slightly to better reflect our current progress and remaining tasks. We have fully completed dataset acquisition and repository setup, and we have drafted initial scripts and exploratory notebooks. Our next steps involve finalizing the cleaning of both the Zillow and USDA datasets, aggregating the Zillow monthly values into annual estimates, and merging both datasets using FIPS codes. After that, we will implement the full automated workflow, generate cleaned and final datasets, and run a complete exploratory analysis. Once the data pipeline is finalized, we will focus on creating the visualizations, writing the final report, and preparing the full reproducible GitHub release. Overall, we remain on track, but cleaning, integration, workflow automation, and analysis will occupy the bulk of the remaining work before the final submission.


## Changes Since Project Plan
Since Milestone 2, we made several refinements:

- We will merge datasets using **FIPS codes**, not county names  
- Zillow ZHVI monthly data will be aggregated to **annual** values  
- Workflow steps are now clearly defined: cleaning → aggregation → integration → analysis  
- Timeline updated to reflect realistic pacing  
- Exploratory analysis plan expanded based on initial script and notebook setup  

These adjustments improve alignment, accuracy, and reproducibility.

## Remaining Gaps
The following tasks remain for Milestone 4:

- Final cleaning of Zillow data  
- Final cleaning of USDA income data  
- Aggregation of ZHVI to yearly values  
- Merging datasets using FIPS  
- Implementing complete Snakemake workflow  
- Creating cleaned (`data/cleaned/`) and final integrated datasets (`data/final/`)  
- Completing exploratory analysis and visualizations  
- Expanding ethical/legal and metadata documentation  
- Writing the final report  
- Preparing a reproducible GitHub release package  

These are expected and planned for the final milestone.


### Arnav Theppasandra
- Acquired Zillow dataset  
- Acquired USDA dataset  
- Renamed and organized both datasets in `data/raw/`  
- Assisted with repository structure and verification  
- Helped draft workflow components  
- Reviewed scripts and analysis notebook  
- Contributed to Status Report writing  

### Yajat Negi
- Wrote initial cleaning, merging, and workflow scripts  
- Created draft exploratory analysis notebook  
- Outlined early analysis direction  

## Next Steps
Before Milestone 4, we will:

1. Finalize cleaning scripts for Zillow and USDA  
2. Aggregate Zillow ZHVI into annual values  
3. Merge datasets using FIPS  
4. Implement full Snakemake workflow  
5. Generate cleaned and final datasets  
6. Produce exploratory analysis and visualizations  
7. Complete the final report  
8. Prepare the reproducible GitHub release  

We are on track to complete the project by the final deadline.
