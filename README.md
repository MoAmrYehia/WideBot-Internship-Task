# WideBot Internship
In this repo I worked on solving two tasks for [WideBot Internship](https://widebot.net/). I was applaying for a Data Engineer Internship and those taskes were designed to evaluate my data engineering skills.

## Task 1 - Getting to Philosophy

I created a web scraper script using python to test the phenomenon that clicking the first link in the main text of a Wikipedia article, and then repeating the process for subsequent articles, will usually lead to the 'Philosophy' article. This script simply checks a random Wikipedia article, follows the first real link, and lists the chain of articles. It's where I got the chains from the above description. If it doesn't find the Philosophy article in 25 links or if it determines a loop it will aborts.

### Prerequisites

What things you need to install the software and how to install them

```
pip install urllib3
pip install bs4
pip install requests
```

### Running the tests

```
cd/ Task 1 
python getting-to-philosphy.py 
```

### Output
![Getting to Philosophy](https://raw.githubusercontent.com/MoAmrYehia/WideBot_Internship_Task/master/res/0.png)

## Task 2 - Binary Classification Problem

Given the training and validation datasets, I created and trained a machine learning model using the training set that performs well on the validation set. I found it a good chance to play around with [PyCaret](https://pycaret.org/) for testing and exploration 

### PyCaret
PyCaret is an open source, low-code machine learning library in Python that allows you to go from preparing your data to deploying your model within minutes in your choice of notebook environment.

### Prerequisites

What things you need to install the software and how to install them

```
conda create --name yourenvname python=3.6
conda activate yourenvname
pip install pycaret==2.0
python -m ipykernel install --user --name yourenvname --display-name "display-name"
```
### ML pipeline 
Using PyCaret I implemented some steps of ML pipeline as following:

* **Getting Data**: How to import data from PyCaret repository
* **Setting up Environment**: How to setup an experiment in PyCaret and get started with building classification models
* **Create Model**: How to create a model, perform stratified cross validation and evaluate classification metrics
* **Tune Model**: How to automatically tune the hyper-parameters of a classification model
* **Plot Model**: How to analyze model performance using various plots
* **Finalize Model**: How to finalize the best model at the end of the experiment
* **Predict Model**: How to make predictions on new / unseen data
* **Save / Load Model**: How to save / load a model for future use


### Plosts
![AUC](https://raw.githubusercontent.com/MoAmrYehia/WideBot_Internship_Task/master/res/1.png)

![precision-recall](https://raw.githubusercontent.com/MoAmrYehia/WideBot_Internship_Task/master/res/2.png)
![Feature](https://raw.githubusercontent.com/MoAmrYehia/WideBot_Internship_Task/master/res/3.png)
![confugin metrics](https://raw.githubusercontent.com/MoAmrYehia/WideBot_Internship_Task/master/res/4.png)
