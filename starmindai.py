import pandas as pd
import Levenshtein as lev
import string

# read input data
dogs_df = pd.read_csv("./20210103_hundenamen.csv")


def remove_punctuation(text):
    no_punct = "".join([c for c in text if c not in string.punctuation])
    return no_punct


def make_lowercase(text):
    return text.lower()


# remove punctuations and make lower case
dogs_df['HUNDENAME'] = dogs_df['HUNDENAME']. \
    apply(lambda x: remove_punctuation(make_lowercase(x)))

# remove unbekants
dogs_df['HUNDENAME'] = \
    dogs_df['HUNDENAME'][dogs_df['HUNDENAME'] != 'unbekannt']


# levenshtein distance
result = [name for name in dogs_df['HUNDENAME'].unique()
          if (lev.distance("luca", name) == 1)]
