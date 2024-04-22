import pandas as pd

movies = pd.read_csv('dataset/movies_metadata.csv', low_memory=False)
movies.shape

