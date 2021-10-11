# Movies Recommender System
  
Demo: <a href="https://movie-recommender-saqib.herokuapp.com/">Movie Recommender System</a>


<!-- # Project Name
This project is a part of the [Data Science Working Group](http://datascience.codeforsanfrancisco.org) at [Code for San Francisco](http://www.codeforsanfrancisco.org).  Other DSWG projects can be found at the [main GitHub repo](https://github.com/sfbrigade/data-science-wg).-->

<!-- #### -- Project Status: [Active, On-Hold, Completed]-->

## Objective
The purpose of this project is to recommend movies which have similar story.Sometimes when we like a movie we want to find similar movies like it but the recommendations
we get on online platforms by other people are very weird so I build this projects to recommend people movies that they like to watch next.This model is trained on 4809 movies data and it uses cosine similarity to recommend movies.


### Approach Used:
* **Data Collection**: Data was collected from: https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv.It has two files movies.csv and credits.csv
* **Merging data** : The data from two files is merged so that we can use the tags of cast,crew along side tags of movies.csv
* **Feature Used**: 'movie_id','title','overview','genres','keywords','cast','crew' are the features I used to create tags
* **Data Cleaning** : There were 3 movies where overview was missing so I removed these movies.Genres,keywords,cast are crew columns are list of dictionaries so I wrote some functions to extract only genre name and keyword name,top 3 actors/actresses from cast and name of the director from crew column.
* **Creating Tags**: After cleaning Genres,keywords,cast are crew columns I merged them with the overview column to create tags which will be useful when we make our model.
* **NLP preprocessing**: Then I removed html tags from tags column and converted it into lowercase.Then I tokenized it and removed english stop words and then ran stemming on it.
* **Word Embedding**: Then I used Count Vectorizer(Bag of words) to create 5000 features on 4806 movies.
* **Cosine Similarity**: On top of these 4806 vectors I ran cosine similarity to find nearest vectors and we use 10 of most similar vectors to recommend movies
* **Deployment**: Deployment is done on **heroku** using streamlit.Check out the <a href="https://movie-recommender-saqib.herokuapp.com/">demo</a> here: 
* etc.

### Technologies Used:
* Python
* Pandas,Sklearn, jupyter
* Streamlit



