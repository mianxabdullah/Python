import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("data/raw/movies.csv")
clustered = pd.read_csv("outputs/clustered_movies.csv")
df = movies.merge(clustered,on='movieId')
print(clustered.columns)
df.head()

def recommend(movie_name,n=5):

    movie = df[df['title'].str.contains(movie_name,case=False)] #case=False works with lowercase and uppercase also initcap
    if movie.empty:
        print("Movie not found")
        return
    
    movie_id = movie.iloc[0]['movieId'] #extracting the movieId of the first movie that matches the name
    cluster = movie.iloc[0]['group'] #extracting the cluster of the first movie that matches the name
    cluster_movies = df[df['group']==cluster] #selecting all movies in the same cluster
    features = df.columns.difference(['movieId', 'title', 'genres', 'group']) #selecting all columns except the ones specified
    similarity = cosine_similarity(cluster_movies[features]) #calculating cosine similarity between movies in the same cluster

    idx = cluster_movies.index.get_loc(movie.index[0]) #getting the index of the movie in the cluster_movies dataframe
    scores = list(enumerate(similarity[idx])) #enumerate returns a tuple of index and value, so we are creating a list of tuples of index and similarity score
    scores = sorted(scores,key=lambda x:x[1],reverse=True) #sorting the list of tuples based on the similarity score in descending order

    recommendations = []
    for i,_ in scores[1:n+1]: #skipping the first movie as it is the same movie and getting the next n movies cosine similarity scores with itself = 1.0
        recommendations.append(cluster_movies.iloc[i]['title']) #extracting the title of the movie that are most similar to the movie that was passed as an argument to the function
    return recommendations

