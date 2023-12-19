import pandas as pd
import numpy as np
import os
import json
import statsmodels.api as sm

PATH_FOLDER = "MovieSummaries/"

def load_character_metadata():
    character_file_name = os.path.join(PATH_FOLDER, 'character.metadata.tsv')
    names_1 = ["Wikipedia_movie_ID",
                "Freebase movie ID", 
                "Movie_release_date",
                "Character_name",
                "Actor date of birth", 
                "Actor_gender",
                "Actor height (in meters)", 
                "Actor ethnicity (Freebase ID)",
                "Actor_name",
                "Actor age at movie release", 
                "Freebase character/actor map ID", 
                "Freebase character ID",
                "Freebase actor ID"]

    character_metadata = pd.read_csv(character_file_name,  sep="\t", names= names_1)
    return character_metadata


def load_movie_metadata():
    movie_file_name = os.path.join(PATH_FOLDER, 'movie.metadata.tsv')
    names_2 = ["Wikipedia_movie_ID",
                "Freebase movie ID", 
                "Movie_name",
                "Movie_release_date",
                "Movie_box_office_revenue",
                "Movie_runtime",
                "Movie languages (Freebase ID:name tuples)",
                "Movie countries (Freebase ID:name tuples)", 
                "Movie genres (Freebase ID:name tuples)"]

    movie_metadata = pd.read_csv(movie_file_name,  sep="\t", names = names_2)
    return movie_metadata

def load_plot_summaries():
    summary_file_name = os.path.join(PATH_FOLDER, 'plot_summaries.txt')
    summary_metadata = pd.read_csv(summary_file_name, sep="\t", names=["Movie ID", "Movie Summary"])

    summary_metadata["Movie Summary"] = summary_metadata["Movie Summary"].astype("string")
    return summary_metadata

def load_tvtropes():
    tvtropes_file_name = os.path.join(PATH_FOLDER, 'tvtropes.clusters.txt')
    tvtropes_metadata = pd.read_csv(tvtropes_file_name, sep="\t", names=['character', 'data'])

    # Convert the 'data' column to strings
    tvtropes_metadata['data'] = tvtropes_metadata['data'].apply(lambda x: str(x))

    # Extract and convert the JSON data to separate columns
    tvtropes_metadata = pd.DataFrame([(character_type, json.loads(data)) for character_type, data
                                      in zip(tvtropes_metadata['character'], tvtropes_metadata['data'])])

    # redefine columns lost from the previous operation
    tvtropes_metadata.columns = ['character', 'data']

    # Expand the 'data' column into separate columns
    tvtropes_metadata = pd.concat([tvtropes_metadata, tvtropes_metadata['data'].apply(pd.Series)], axis=1)

    # Drop the original 'data' column
    tvtropes_metadata.drop('data', axis=1, inplace=True)

    tvtropes_metadata.columns = [['Character_role',
                                  'Character_name',
                                  'Movie_name',
                                  'Freebase character/actor map ID',
                                  'Actor_name']]
    return tvtropes_metadata

def load_name_clusters():
    name_file_name = os.path.join(PATH_FOLDER, 'name.clusters.txt')
    name_metadata = pd.read_csv(name_file_name, sep="\t", names=["Character name", "Freebase character/actor map ID"])
    return name_metadata


def disagregate_list_feature(df, feature_name):
    #Create new df
    result_df = df.copy()
    # Step 1: Get the unique set of languages
    unique_features = set(feature for features in result_df[feature_name] for feature in features)

    # Step 2: Create binary columns for each language
    for feature in unique_features:
        result_df[feature] = result_df[feature_name].apply(lambda x: feature in x)

    # Step 3: Drop the original 'Languages' column
    result_df.drop(feature_name, axis=1, inplace=True)

    # Resulting DataFrame
    return result_df

def regression_analysis(df, revenue_string):
    X = df.drop([revenue_string], axis=1)
    y = df[revenue_string]

    X = X.astype(int)

    X = sm.add_constant(X)


    model = sm.OLS(y, X).fit()

    print(model.summary())
    return model

def display_regression_result(model):
    # Extract coefficients and corresponding character names
    coefficients = model.params[1:]  # Exclude the intercept
    feature = coefficients.index
    p_values = model.pvalues[1:]
    # Create a DataFrame to store coefficients and character names
    coefficients_df = pd.DataFrame({'Feature': feature, 'Coefficient': coefficients, 'p-value': p_values})
    #print lines of 10 best and worst coefficients
    print('Top 10 more successful features with coefficients and p-values:')
    print(coefficients_df.sort_values(by='Coefficient', ascending=False).head(10))
    print('Top 10 more successful features with coefficients and p-values:')
    print(coefficients_df.sort_values(by='Coefficient', ascending=False).tail(10))
