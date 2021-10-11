# movies recommender System
  



<!-- # Project Name
This project is a part of the [Data Science Working Group](http://datascience.codeforsanfrancisco.org) at [Code for San Francisco](http://www.codeforsanfrancisco.org).  Other DSWG projects can be found at the [main GitHub repo](https://github.com/sfbrigade/data-science-wg).-->

<!-- #### -- Project Status: [Active, On-Hold, Completed]-->

## Objective
The purpose of this project is to recommend movies which have similar story.Sometimes when we like a movie we want to find similar movies like it but the recommendations
we get on online platforms by other people are very weird so I build this projects to recommend people movies that they like to watch next.This model is trained on 5000 movies data and it uses cosine similarity to recommend movies.


### Approach Used:
* **Data Collection**: Data was collected from: https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv.It has two files movies.csv and credits.csv
* **Merging data** : The data from two files is merged so that we can use the tags of cast,crew along side tags of movies.csv
* **Feature Used**: 'movie_id','title','overview','genres','keywords','cast','crew' are the features I used to create tags
* **Data Cleaning** : There were 3 movies where overview was missing so I removed these movies.Genres,keywords,cast are crew columns are list of dictionaries so I wrote some functions to extract only genre name and keyword name,top 3 actors/actresses from cast and name of the director from crew column.
* **Creating Tags**: After cleaning Genres,keywords,cast are crew columns I merged them with the overview column to create tags which will be useful when we make our model.
* NLP preprocessing: Then I removed html tags from tags column and converted it into lowercase.Then I tokenized it and removed english stop words and then ran stemming on it.
* Data Visualization
* Predictive Modeling
* etc.

### Technologies
* R 
* Python
* D3
* PostGres, MySql
* Pandas, jupyter
* HTML
* JavaScript
* etc. 

## Project Description
(Provide more detailed overview of the project.  Talk a bit about your data sources and what questions and hypothesis you are exploring. What specific data analysis/visualization and modelling work are you using to solve the problem? What blockers and challenges are you facing?  Feel free to number or bullet point things here)

## Needs of this project

- frontend developers
- data exploration/descriptive statistics
- data processing/cleaning
- statistical modeling
- writeup/reporting
- etc. (be as specific as possible)

## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Raw Data is being kept [here](Repo folder containing raw data) within this repo.

    *If using offline data mention that and how they may obtain the data from the froup)*
    
3. Data processing/transformation scripts are being kept [here](Repo folder containing data processing scripts/notebooks)
4. etc...

*If your project is well underway and setup is fairly complicated (ie. requires installation of many packages) create another "setup.md" file and link to it here*  

5. Follow setup [instructions](Link to file)

## Featured Notebooks/Analysis/Deliverables
* [Notebook/Markdown/Slide Deck Title](link)
* [Notebook/Markdown/Slide DeckTitle](link)
* [Blog Post](link)


## Contributing DSWG Members

**Team Leads (Contacts) : [Full Name](https://github.com/[github handle])(@slackHandle)**

#### Other Members:

|Name     |  Slack Handle   | 
|---------|-----------------|
|[Full Name](https://github.com/[github handle])| @johnDoe        |
|[Full Name](https://github.com/[github handle]) |     @janeDoe    |

## Contact
* If you haven't joined the SF Brigade Slack, [you can do that here](http://c4sf.me/slack).  
* Our slack channel is `#datasci-projectname`
* Feel free to contact team leads with any questions or if you are interested in contributing!
