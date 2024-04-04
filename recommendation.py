import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Read the CSV file into a pandas DataFrame
movies_df = pd.read_csv('movies.csv', encoding="utf8")

print(movies_df)


tf = TfidfVectorizer(analyzer='word', ngram_range=(1,2)) 
tfidf_matrix = tf.fit_transform(movies_df['genres'])
cosine_sim = cosine_similarity(tfidf_matrix) 
cosine_sim_df = pd.DataFrame(cosine_sim, index=movies_df['title'], columns=movies_df['title']) 

def get_recommendations(movie_id, similarity_df, movies_df, k=10):
    ix = similarity_df.loc[:,movie_id].to_numpy().argpartition(range(-1,-k,-1))
    closest = similarity_df.columns[ix[-1:-(k+2):-1]] 
    closest = closest.drop(movie_id, errors='ignore')    
    return pd.DataFrame(closest).merge(movies_df).head(k)

def checking_validation(movie:str):
    try:
        x = movie
        y = get_recommendations(x, cosine_sim_df, movies_df[['title', 'genres']])
        print("Here is your recommendations....")
        print(y)
        return 0

    except KeyError as e:
        print("No movies found with this name!!!")
        return 1
    
y=1

while y==1:
    movie = input('enter movie name from the above output or from the movies.csv file.. ')
    y = checking_validation(movie)
