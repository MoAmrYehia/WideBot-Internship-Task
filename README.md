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

## Task 2 - Binary Classification Problem

I created a web scraper script using python to test the phenomenon that clicking the first link in the main text of a Wikipedia article, and then repeating the process for subsequent articles, will usually lead to the 'Philosophy' article. This script simply checks a random Wikipedia article, follows the first real link, and lists the chain of articles. It's where I got the chains from the above description. If it doesn't find the Philosophy article in 25 links or if it determines a loop it will aborts.

### Prerequisites

What things you need to install the software and how to install them

```
conda create --name yourenvname python=3.6
conda activate yourenvname
pip install pycaret==2.0
python -m ipykernel install --user --name yourenvname --display-name "display-name"
```
