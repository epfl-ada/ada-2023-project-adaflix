import pandas as pd
import numpy as np
import os
import json

PATH_FOLDER = "MovieSummaries/"

def load_character_metadata():
    character_file_name = os.path.join(PATH_FOLDER, 'character.metadata.tsv')
    names_1 = ["Wikipedia movie ID",
                "Freebase movie ID", 
                "Movie release date", 
                "Character name", 
                "Actor date of birth", 
                "Actor gender", 
                "Actor height (in meters)", 
                "Actor ethnicity (Freebase ID)",
                "Actor name", 
                "Actor age at movie release", 
                "Freebase character/actor map ID", 
                "Freebase character ID",
                "Freebase actor ID"]

    character_metadata = pd.read_csv(character_file_name,  sep="\t", names= names_1)
    return character_metadata


def load_movie_metadata():
    movie_file_name = os.path.join(PATH_FOLDER, 'movie.metadata.tsv')
    names_2 = ["Wikipedia movie ID", 
                "Freebase movie ID", 
                "Movie name", 
                "Movie release date", 
                "Movie box office revenue", 
                "Movie runtime", 
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

    tvtropes_metadata.columns = [['Character role',
                                  'Character name',
                                  'Movie name',
                                  'Freebase character/actor map ID',
                                  'Actor name']]
    return tvtropes_metadata

def load_name_clusters():
    name_file_name = os.path.join(PATH_FOLDER, 'name.clusters.txt')
    name_metadata = pd.read_csv(name_file_name, sep="\t", names=["Character name", "Freebase character/actor map ID"])
    return name_metadata

