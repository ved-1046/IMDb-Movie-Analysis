
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('IMDB-Movie-Data.csv')
print(df.info())
print(df.shape)
print(df.columns)
print(df.head(5))

print(df.isnull().sum())
df = df.dropna() #dropping null values
top_movies = df.sort_values(by = 'Rating',ascending = False)
print(top_movies[['Title', 'Rating']].head(10)) #Top 10 highest rated movies

#director that directed most movies
director_count = df['Director'].value_counts()
print(director_count.head(10))

#which genre has highest rating
genre_rating = df.groupby('Genre')['Rating'].mean().sort_values(ascending=False)
print(genre_rating.head(10))

#which year has higher no of movies 
year_releases = df['Year'].value_counts().sort_index() #sorts by years
print(year_releases.head(10))

#which director has highest average movie rating
director_rating = df.groupby('Director')['Rating'].mean().sort_values(ascending = False)
print(director_rating.head(10))

#movies with top revenue
top_revenue = df.sort_values(by = 'Revenue (Millions)',ascending = False)
print(top_revenue[['Title','Revenue (Millions)']].head(10))

#movies with higher votes
top_votes = df.sort_values(by='Votes',ascending = False)
print(top_votes[['Title','Votes']].head(10))

fig , axes = plt.subplots(2,2,figsize = (14,10))

axes[0,0].barh(
    top_movies['Title'].head(10),
    top_movies['Rating'].head(10),
    color = 'RoyalBlue'
)

axes[0,0].set_title('Top 10 highest rated movies')
axes[0,0].set_xlabel('Rating')
axes[0,0].set_ylabel('Movie Title')


axes[0,1].barh(
    director_rating.index[:10],
    director_rating.values[:10],
     color = 'Green'
)

axes[0,1].set_title('Directors with highest rating')
axes[0,1].set_xlabel('Rating')
axes[0,1].set_ylabel('Director')

axes[1,0].bar(
    genre_rating.index[:10],
    genre_rating.values[:10],
     color = 'Orange'
)

axes[1,0].set_title("Genres with higher rating")
axes[1,0].set_xlabel('Rating')
axes[1,0].set_ylabel('Genre')

axes[1,0].tick_params(axis = 'x',rotation = 90)

axes[1,1].plot(
    year_releases.index,
    year_releases.values,
    marker='o',
    color = 'purple',
    linestyle = '--'
)

axes[1,1].set_title('Movie releases',fontsize = 10 , fontweight = 'bold')
axes[1,1].set_xlabel('Year')
axes[1,1].set_ylabel('Number of Movies')
axes[1,1].grid(True)

plt.tight_layout()
plt.savefig("dashboard.png", dpi=300)
plt.show()