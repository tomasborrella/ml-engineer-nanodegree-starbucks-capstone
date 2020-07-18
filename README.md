# Starbucks Capstone Challenge

This repository contains my delivery of the Machine Learning Engineer Capstone Project from the [Udacity Machine Learning Engineer Nanodegree Program](https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009t). This is the project statement:

>#### Introduction
>
>This data set contains simulated data that mimics customer behavior on the Starbucks rewards mobile app. Once every few days, Starbucks sends out an offer to users of the mobile app. An offer can be merely an advertisement for a drink or an actual offer such as a discount or BOGO (buy one get one free). Some users might not receive any offer during certain weeks. 
>
>Not all users receive the same offer, and that is the challenge to solve with this data set.
>
>Your task is to combine transaction, demographic and offer data to determine which demographic groups respond best to which offer type. This data set is a simplified version of the real Starbucks app because the underlying simulator only has one product whereas Starbucks actually sells dozens of products.
>
>Every offer has a validity period before the offer expires. As an example, a BOGO offer might be valid for only 5 days. You'll see in the data set that informational offers have a validity period even though these ads are merely providing information about a product; for example, if an informational offer has 7 days of validity, you can assume the customer is feeling the influence of the offer for 7 days after receiving the advertisement.
>
>You'll be given transactional data showing user purchases made on the app including the timestamp of purchase and the amount of money spent on a purchase. This transactional data also has a record for each offer that a user receives as well as a record for when a user actually views the offer. There are also records for when a user completes an offer. 
>
>Keep in mind as well that someone using the app might make a purchase through the app without having received an offer or seen an offer.
>
>#### Example
>
>To give an example, a user could receive a discount offer buy 10 dollars get 2 off on Monday. The offer is valid for 10 days from receipt. If the customer accumulates at least 10 dollars in purchases during the validity period, the customer completes the offer.
>
>However, there are a few things to watch out for in this data set. Customers do not opt into the offers that they receive; in other words, a user can receive an offer, never actually view the offer, and still complete the offer. For example, a user might receive the "buy 10 dollars get 2 dollars off offer", but the user never opens the offer during the 10 day validity period. The customer spends 15 dollars during those ten days. There will be an offer completion record in the data set; however, the customer was not influenced by the offer because the customer never viewed the offer.
>
>#### Cleaning
>
>This makes data cleaning especially important and tricky.
>
>You'll also want to take into account that some demographic groups will make purchases even if they don't receive an offer. From a business perspective, if a customer is going to make a 10 dollar purchase without an offer anyway, you wouldn't want to send a buy 10 dollars get 2 dollars off offer. You'll want to try to assess what a certain demographic group will buy when not receiving any offers.
>
>#### Final Advice
>
>Because this is a capstone project, you are free to analyze the data any way you see fit. For example, you could build a machine learning model that predicts how much someone will spend based on demographics and offer type. Or you could build a model that predicts whether or not someone will respond to an offer. Or, you don't need to build a machine learning model at all. You could develop a set of heuristics that determine what offer you should send to each customer (i.e., 75 percent of women customers who were 35 years old responded to offer A vs 40 percent from the same demographic to offer B, so send offer A).
>
>#### Data Sets
>
>The data is contained in three files:
>
>* portfolio.json - containing offer ids and meta data about each offer (duration, type, etc.)
>* profile.json - demographic data for each customer
>* transcript.json - records for transactions, offers received, offers viewed, and offers completed
>
>Here is the schema and explanation of each variable in the files:
>
>**portfolio.json**
>* id (string) - offer id
>* offer_type (string) - type of offer ie BOGO, discount, informational
>* difficulty (int) - minimum required spend to complete an offer
>* reward (int) - reward given for completing an offer
>* duration (int) - time for offer to be open, in days
>* channels (list of strings)
>
>**profile.json**
>* age (int) - age of the customer 
>* became_member_on (int) - date when customer created an app account
>* gender (str) - gender of the customer (note some entries contain 'O' for other rather than M or F)
>* id (str) - customer id
>* income (float) - customer's income
>
>**transcript.json**
>* event (str) - record description (ie transaction, offer received, offer viewed, etc.)
>* person (str) - customer id
>* time (int) - time in hours since start of test. The data begins at time t=0
>* value - (dict of strings) - either an offer id or transaction amount depending on the record

## Installation

This project had been tested with python 3.6, 
so it's recommended to have an environment with this version of python to make it work.

As this package has `setup.py` aligned with `requirements.txt`, 
you only need to clone this repository and execute `pip install .` in the root of the project.

It's suggested to have an isolated environment activated before doing `pip install .`
(conda, venv, pipenv...).

## How To Run?

It is necessary to have installed all of the requirements before running the notebooks.

## File Descriptions

```text
├── data
│   ├── portfolio.json
│   ├── profile.json
│   └── transcript.json
├── notebooks
│   ├── 1_Data_Exploration_and_Cleaning.ipynb
│   ├── 2_Data_Visualization_and_EDA.ipynb
│   └── 3_Model_Uplift.ipynb
├── README.md
├── reports
│   ├── images
│   │   ├── pandas_profiling_logo.png
│   │   └── shap.png
│   └── starbucks_profiling.html
├── requirements.txt
├── setup.py
└── starbucks_campaigns_analytics
    ├── constants.py
    ├── helpers.py
    ├── __init__.py
    └── plotting.py
```

#### 1. Data exploration & ETL Pipeline

**data** folder contains the three original data files.

**notebooks** folder contains several jupyter notebooks, the first of them
(```1_Data_Exploration_and_Cleaning.ipynb```) has all the code for data exploration, cleaning and transformations.

**starbucks_campaigns_analytics** is the folder of the module developed for this project. 
Once the data transformations have been tested in a notebook all the code have been moved to helpers functions in 
```helpers.py```.

#### 2. Data visualization & Exploratory Data Analysis

There is separate notebook in **notebooks** folder for visualizations and EDA 
(```2_Data_Visualization_and_EDA.ipynb```)

Some of the visualizations are enabled by a function in **starbucks_campaigns_analytics** folder in 
```plotting.py``` file.

**reports** folder contains the profile report of the final dataframe generated with 
[pandas profiling](https://github.com/pandas-profiling/pandas-profiling).

#### 3. Machine Learning

Two machine learning techniques have been used in this project, both are in  notebooks (in **notebooks** folder):

1. Unsupervised learning
   
   KMeans clustering have been used in data exploration to determine user clusters 
   (```1_Data_Exploration_and_Cleaning.ipynb```).

2. Supervised learning

    Uplift model have been used to determine optimum campaign target (```3_Model_Uplift.ipynb```).

## Results

TO DO (work in progress)

## Acknowledgements

Data come from [Starbucks](https://www.starbucks.com/).

Project idea and guidance comes from [Udacity Machine Learning Engineer Nanodegree Program](https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009t)