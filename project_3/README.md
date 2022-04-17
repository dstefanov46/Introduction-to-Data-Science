# Project 3: Predictive Modeling on the Datasets Provided by the Company Celtra

## Environment setup

- The distribution which was used during the development of this project is the **Anaconda distribution**
of Python.
- So, in order to setup the environment in which the **predictive_modeling.ipynb** notebook was developed, you 
need to run the following command in **Anaconda prompt**:
> conda env create -f project_3_environment.yml 

- The **project_3_environment.yml** file has also been added to the repo.
- The  **project_3_environment.yml** file contains all the packages needed to run our Jupyter notebook, so no additional 
installations are needed.
- Our dynamic report is written in the **predictive_modeling.ipynb** notebook.
- Our report (the .pdf file) and the other necessary files to run the report are all located in the folder **report**.


# Project 3: Predictive modeling

You will use the same data provided by Celtra that you have used in project 2. Data and details on the data set can be found [here](https://classroom.github.com/a/GSP5KZ49).


## Instructions

You should use the knowledge, understanding and preprocessing of data gained in project 2 to build a few predictive models that provide actionable results. For example, their predictions could be used to improve Celtra's business directly. By understanding why a model works well and when does it fail, we could gain new knowledge and plan new improvements in the data collection and modeling.

Here are some questions you may want to answer (pick at least two, and, of course, you can identify and answer your own questions):

* Anonymous `Users` appear in the Celtra platform usage data. How precisely can we predict and identify a real (true) user?
* Can we predict the probability that ads will not reach the final user's device (Celtra sessions data)?
* Can we predict the probability that users will interact with ads (Celtra sessions data)?
* Can we predict how long ads will be visible (Celtra sessions data)?
* Can we predict the whole "ads serving" funnel? That is, how many (or proportion of) sessions do we loose at each step: requested -> loaded -> rendered -> interacted?

When thinking about "ads" you should think in the context of a `CampaignID` and in the context of a `CreativeID`.

When modeling, evaluating and thinking about the above questions, you should be clear what data (attributes) are actually available at the time of prediction in a real-life business situation.

As a data scientist, your main task is to provide insights into the data to the reader by using predictive modeling. Importantly, you should estimate the expected predictive performance on new examples and select the best predictive model for each type of outcome you want to predict. Also, you should try to identify the most important attributes for the prediction task and try to explain why (and when) the model performs well and when does it fail. Aim for a concise, efficient, and effective solution.

In doing so, you should:

* Be careful on which data you train and test your models. For example, split the data into a training and a test set by selecting an arbitrary point in time to divide the two (*i.e.*, a rolling time window approach in case of temporal data).
* What measure(s) of predictive performance should you use?
* What are the costs associated with different prediction errors? How should they be reflected in the predictive performance measure that you will use to rank the various predictive models?
* What is the reference (baseline) performance that your best models should improve on?
* **Build and evaluate models to predict** a selected outcome.
* Report the predictive performance scores obtained.
* Based on the evaluation, propose the best models to be used in "production."
* Discuss other (practical) considerations when selecting the best model that should be used in "production."
* Depending on the learning algorithm used, you may not be able to use the entire data set. Use appropriate data sampling methods (be careful not to ignore the temporal component when sampling).
* Discuss why and when models perform well, and why and when they fail.

During the analysis you should also:

* Implement dynamic reports and provide all the code with instructions for your code to be reproducible.
* Produce appropriate visualisations of your results that are aesthetic, make sense and are without major technical flaws. Comment and discuss your work.

**Focus on quality, not quantity!** If you believe you cannot find appropriate solutions, justify and discuss that in the report.

In the report you should describe your insights into the modeling and the obtained models to the reader through text, tables, and visualisations.

Submit your work within the assignment repository and organise it sensibly (code, visualisations, reports in separate folders). Along with the dynamic reports and source code you should also submit a short PDF 3-4 pages analysis report. In the README.md of your repository explain the structure of your files within the repository and also provide all the instructions to reproduce your work.


## Expected results

- Fully implemented and reproducible Jupyter notebook (predictive_modeling.ipynb)
- Short report, 3-4 pages PDF, use template.
