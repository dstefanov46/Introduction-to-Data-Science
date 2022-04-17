# Project 2: Initial exploration and data visualization

## Environment setup

- The distribution which was used during the development of this project is the **Anaconda distribution**
of Python.
- So, in order to setup the environment in which the **data_exploration.ipynb** notebook was developed, you 
need to run the following command in **Anaconda prompt**:
> conda env create -f project_2_environment.yml 

- The **project_2_environment.yml** file has also been added to the repo.
- The  **project_2_environment.yml** file contains all the packages needed to run our Jupyter notebook, so no additional 
installations are needed.
- Our dynamic report is written in the **data_exploration.ipynb** notebook.
- Our report (the .pdf file) and the other necessary files to run the report are all located in the folder **report**.

## Project 2 Description

Celtra company provided an anonymized and sampled dataset on their platform usage data.

The two datasets are contained in the file [*Celtra example datasets (shared externally).zip*](https://drive.google.com/file/d/18rVfAmCZ5TmGLXSqlSzEvIGDFrTa44VC/view?usp=sharing). Below we overview the attributes provided in the datasets.


## Celtra platform usage data.csv

Platform user activity:

| Attribute | Description |
| --- | ----------- |
| `Account` | Unique ID for each user (company) |
| `User`    | Unique ID for each user on the platform (company employee) |
| `Session` | Unique ID of (web) session using the platform |
| `ActivityLocation` | Which part of the platform is used by the `User` |
| `Activity` | Coarse grouping of ActivityLocation |
| `Timestamp` |  |


## Celtra sessions data.csv

Advertisement traffic on Celtra servers, data on ads shown on internet users' devices:

| Attribute | Description |
| --- | ----------- |
| `Date` |  |
| `AccountID` |  Unique ID for each user (company) |
| `CampaignID` | Unique ID for campaign produced by a `User` (company employee) |
| `CreativeID` | Unique ID for each creative (group of ads - creative) |
| `Platform` | Platform where ads shown |
| `SDK` |  Software environment on device where ads shown |
| `Requested sessions` |  Number of requests to the server from the (internet) users' devices |
| `Creative load attempts` |  Number of ads that were attempted to be loaded on the devices |
| `Loaded sessions` | Number of ads that were successfully loaded on the devices |
| `Rendered sessions` | Number of ads that were successfully shown on the devices |
| `Sessions with interaction` | Number of ads that the internet users interacted with |
| `Viewable time` | Number of seconds the ads were visible to users |

Detailed description of attributes can be [found here](https://support.celtra.com/trafficking-and-analytics/analytics-glossary).


## Instructions

Your main task is to provide insights into the data to the reader through text, tables, and visualisations. Aim for a concise, efficient, and effective solution.

You, as a data scientist, need first to fully grasp the dataset's domain and clearly understand all the data. Your goal is to analyse the dataset (describe it) and to propose further analyses/research based on your intuition. Also, comment on the shortcomings of the dataset, so the company could improve by gathering more or different types of data. During the analysis you should also:

* Implement dynamic reports and provide all the code with instructions for your code to be reproducible.
* Produce visualisations that are aesthetic, make sense and are without major technical flaws. Take into account univariate and multivariate distributions along with appropriate techniques. Comment and discuss your work.
* Apply data summarisation techniques to obtain insights from data. In case of unexpected results, comment on your *logical* hypothesis and try to find out why it is not true.

**Focus on quality, not quantity!** If you believe you cannot find appropriate attributes for a specific visualisation type, justify and discuss that in the report.

Submit your work within the assignment repository and organise it sensibly (code, visualisations, reports in separate folders). Along with the dynamic reports and source code you should also submit a short PDF 3 pages analysis report. In the README.md of your repository explain the structure of your files within the repository and also provide all the instructions to reproduce your work.


## Expected results

- Fully implemented and reproducible Jupyter notebook (data_exploration.ipynb)
- Short report, 3 pages PDF, use template.
