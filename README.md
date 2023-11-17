# Movies that could have met a different success

## Abstract:
Imagine having a special tool that predicts if your movie will be a hit before you even start filming. If your movie is missing some key ingredients, don't worry! This tool also teaches you from the success stories of movies that defied the odds. Armed with this wisdom, you enter the filmmaking adventure with confidence, turning challenges into opportunities. It's not just about a perfect script. it's about the passion and creativity you bring to the screen. The project aims to explore the intriguing cases of movies  that should've been hits but missed the mark, and those surprising successes that defy the odds.  It consists of making a formula for a films’ success where the primary focus, lies in the outliers movies that diverge from conventional formula of success. We will then analyse case by case these outliers and try to find  global parameters and relationships explaining why films that should have made it, failed instead. By studying these cases, we're not simply telling stories, we're hunting for the universal reasons behind the reasons why success isn't always what it seems.

## Research Questions:

1. What are the key components that contribute to a movie's financial success  and how do these components interact within our predictive model ?
2. How do outliers in our model differ from the general trends in successful movies ?
3. How can revenue be effectively standardized in accordance with inflation rates to ensure accurate and meaningful comparisons over time?"
4. Is there a universal parameter or relationship that elucidates the unexpected success of movies that defy conventional expectations, providing insights into their distinctive trajectories ?

## Proposed Additional Datasets:
- IMDb dataset: We aim to broaden the way we define a movie's success beyond simple character and movie metrics by incorporating ratings of movies. To achieve this, we have obtained two datasets from IMDb, facilitating their integration with our existing movie data. We used the title-basics and ratings datasets to relate features from our original datasets and the new dataset in order to add ratings and votes to our initial features.[Download the IMDb dataset](https://developer.imdb.com/non-commercial-datasets/)
- The Movie Dataset: A dataset comprising movie budgets is added, to enhance our analysis. It is added to the movie dataset due to its high relevance to revenue within the domain  surpassing other features in terms of direct correlation. This addition enriches our analysis by providing a more closely aligned and impactful factor for exploring relationships with box office revenue.[Download the Movie Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?resource=download&select=movies_metadata.csv)
- Inflation dataset : Since we want to compare the revenue of movies over time, we need to take into account the inflation. The CPI-U (Consumer Price Index for All Urban Consumers) is a common measure to do so, and we will use a table of it's annual values since 1913 to accordingly equalize the revenue of movies over time. 
The dataset is available on the U.S. BUREAU OF LABOR STATISTICS website. [Download the Inflation dataset](https://data.bls.gov/timeseries/CUUR0000SA0?years_option=all_years)


## Methods:
1. **Preprocessing** Preprocess raw data by handdling missing and inconsistent data for regression analysis
2. **Regression Analysis:** Conduct a thorough analysis to identify the significant factors influencing a movie's success.
3. **Machine Learning Model:** Develop a predictive model using machine learning techniques to assess the impact of various features on box office revenue.
4. **Outlier Analysis:** Examine outliers from the model to understand why certain movies, despite non favorable characteristics, did succeed and why  films that should have made it, failed instead.

##  Internal milestones up until project Milestone P3 (19 Nov to 21 Dec):
#### Milestone 1: Data Collection and Preprocessing (19 Nov - 25 Nov)
- Gather relevant datasets, including information on movie characteristics and box office revenue.
- Preprocess the data, addressing missing values and standardizing revenue with inflation.

#### Milestone 2: Regression Analysis and Model Development (26 Nov - 5 Dec)
- Perform regression analysis to identify key components of a successful movie.
- Develop a machine learning model to predict box office revenue based on movie features.

#### Milestone 3: Outlier Analysis and Case Studies (6 Dec - 15 Dec)
- Identify outliers in the model.
- Conduct in-depth case studies on outliers to understand the reasons behind their unexpected performance.


#### Milestone 4: Outlier Analysis and Case Studies (15 Dec - 20 Dec)
- Create visual representations of the analysis, including graphs and charts.
- Document the entire process, findings, and key insights.
- Finalize and submit the datastory.


By following this timeline and organizational structure, we aim to provide a comprehensive analysis of movies that could have experienced different levels of success.
