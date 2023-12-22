# Movies that could have met a different success

## Abstract:
Imagine having a special tool that predicts if your movie will be a hit before you even start filming. If your movie is missing some key ingredients, don't worry! This tool also teaches you from the success stories of movies that defied the odds. Armed with this wisdom, you enter the filmmaking adventure with confidence, turning challenges into opportunities. The project aims to explore the intriguing cases of movies  that should've been hits but missed the mark, and those surprising successes that defy the odds.  It consists of making a formula for a films’ success where the primary focus, lies in the outliers movies that diverge from conventional formula of success. We will then analyse case by case these outliers and try to find  global parameters and relationships explaining why films that should have made it, failed instead. By studying these cases, we're not simply telling stories, we're hunting for the universal reasons behind the reasons why success isn't always what it seems.

## Research Questions:

1. What are the key components that contribute to a movie's financial success  and how do these components interact within our predictive model ?
2. How do outliers in our model differ from the general trends in successful movies ?
3. How can revenue be effectively standardized in accordance with inflation rates to ensure accurate and meaningful comparisons over time?"
4. Is there a universal parameter or relationship that elucidates the unexpected success of movies that defy conventional expectations, providing insights into their distinctive trajectories ?

## Proposed Additional Datasets:
- Inflation dataset : Since we want to compare the revenue of movies over time, we need to take into account the inflation. The CPI-U (Consumer Price Index for All Urban Consumers) is a common measure to do so, and we will use a table of it's annual values since 1913 to accordingly equalize the revenue of movies over time. 
The dataset is available on the U.S. BUREAU OF LABOR STATISTICS website. [Download the Inflation dataset](https://data.bls.gov/timeseries/CUUR0000SA0?years_option=all_years)


## Methods:
1. **Preprocessing** Preprocess raw data by handdling missing and inconsistent data for regression analysis. Perform discretization of features to use them as categorical features in our final prediction formula.
2. **Feature selection and data analysis:** Analyze each feature individually and identiy the significant factors influencing a movie's success. Use various plots for understanding the data. Perform regression analysis to identify factors that are most correlated with the box office revenue, as well as to disentangle data. For the final formula, select only features that have a significant impact on the box office revenue.
3. **Machine Learning Model:** Develop a predictive model using machine learning techniques to assess the impact of various features on box office revenue.
4. **Outlier Analysis:** Examine outliers from the model to understand why certain movies, despite non favorable characteristics, did succeed and why  films that should have made it, failed instead.

##  Internal milestones up until project Milestone P3 (19 Nov to 21 Dec):
#### Milestone 1: Data Collection and Preprocessing (19 Nov - 25 Nov)
- Gather relevant datasets, including information on movie characteristics and box office revenue.
- Preprocess the data, addressing missing values, standardizing revenue with inflation, and performing feature discretization.

#### Milestone 2: Feature selection & data analysis (26 Nov - 5 Dec)
- Come up with graphs illustrating the effects of different features on movies success.
- Perform regression analysis to identify key components of a successful movie.
- Only keep features that are most correlated with the box office revenues in the final formula.

#### Milestone 3: Predictive model, formula creation (6 Dec - 15 Dec)
- Develop a machine learning model to predict box office revenue based on movie features
- Identify outliers in the model.


#### Milestone 4: Outlier Analysis and creation of data story (15 Dec - 22 Dec)
- Conduct in-depth case studies on outliers to understand the reasons behind their unexpected performance.
- Create visual representations of the analysis, including graphs and charts
- Document the entire process, findings, and key insights.
- Work the datastory.


By following this timeline and organizational structure, we aim to provide a comprehensive analysis of movies that could have experienced different levels of success.

## Organization within the team

- [Rami Atassi](https://github.com/RamiATASSI): Preprocessing / Data analysis & feature selection / Machine learning model
- [Oussama Gabouj](https://github.com/Ousso11): Data analysis & Feature selection / Machine learning model / Website & data story writing
- [Garik Sahakyan](https://github.com/garikSahakayan): Preprocessing / Data analysis & feature selection / Machine learning model
- [Aziz Ben Haj Hmida](https://github.com/azizbenhaj): Data analysis & feature selection / Machine learning model / Website & data story writing
- [Jiewei Li](https://github.com/lijw0418): Data analysis & feature selection / Machine learning model