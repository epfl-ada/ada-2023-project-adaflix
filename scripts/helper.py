import numpy as np
import pandas as pd
import nltk

#function used to tokenize into dataframe columns into single words
def tokenize(column):
    """Tokenizes a Pandas dataframe column and returns a list of tokens.

    Args:
        column: Pandas dataframe column.

    Returns:
        tokens (list): Tokenized list.
    """

    tokens = nltk.word_tokenize(column)
    return [w for w in tokens if w.isalpha()] 


#Function to split data between train and test
def split_set(data_to_split, ratio=0.8):
    """split data between train and test.

    Args:
        data_to_split: Pandas dataframe.
        ratio: ratio train/test data (default value: 0.8)

    Returns:
        train and test dataframes.
    """
    mask = np.random.rand(len(data_to_split)) < ratio
    return [data_to_split[mask].reset_index(drop=True), data_to_split[~mask].reset_index(drop=True)]

def outliers_removal(
    x_train_normalized, y_train, threshold=3, max_false_percentage=0.1
):
    """
    Remove outliers from the training data based on z-scores and a false percentage threshold.

    Parameters:
    - x_train_normalized (numpy.ndarray): Normalized training feature matrix.
    - y_train (numpy.ndarray): Training target labels.
    - threshold (float): Z-score threshold for defining outliers (default is 3).
    - max_false_percentage (float): Maximum acceptable percentage of False values in a row (default is 0.3).

    Returns:
    - x_train_cleaned (numpy.ndarray): Training feature matrix with outliers removed.
    - y_train_cleaned (numpy.ndarray): Training target labels with corresponding outliers removed.
    """

    z_scores = np.abs(x_train_normalized)

    # Create a mask of non-outliers
    outlier_mask = z_scores < threshold

    # Calculate the percentage of False values in each row of the mask
    false_percentages = 1 - np.mean(outlier_mask, axis=1)

    # Check if the false percentage is less than the threshold (10%)
    non_outlier_rows = false_percentages < max_false_percentage

    return x_train_normalized[non_outlier_rows], y_train[non_outlier_rows]

def standerdize(train_features, test_features):

    #standerdize train and test features
    means = train_features.mean()
    stddevs = train_features.std()

    train_features_std = pd.DataFrame()
    for c in train_features.columns:
        train_features_std[c] = (train_features[c]-means[c])/stddevs[c]

    # Use the mean and stddev of the training set
    test_features_std = pd.DataFrame()
    for c in test_features.columns:
        test_features_std[c] = (test_features[c]-means[c])/stddevs[c]

    return train_features_std, test_features_std