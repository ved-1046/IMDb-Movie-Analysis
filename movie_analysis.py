import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


sns.set_theme(style = 'whitegrid',palette = 'deep')

df = pd.read_csv('IMDB-Movie-Data.csv')
print(df.info())
print(df.describe())
print(df.duplicated().sum())
print(df.shape)
print(df.columns)
# print(df.head(5))

df['Revenue (Millions)'] = df['Revenue (Millions)'].fillna(df['Revenue (Millions)'].median())
df['Metascore'] = df['Metascore'].fillna(df['Metascore'].median())

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

#average rating of movies per year
yearly_rating = df.groupby('Year')['Rating'].mean().sort_index()
print(yearly_rating.head(10))

#average runtime by genre
runtime_avg = df.groupby('Genre')['Runtime (Minutes)'].mean().sort_values(ascending = False)
print(runtime_avg.head(10))

fig , axes = plt.subplots(2,2,figsize = (16,10))

sns.histplot(
    data = df,
    x = 'Rating',
    bins = 15,
    kde = True,
    color = 'royalblue',
    ax = axes[0,0]
    )

axes[0,0].set_title('Distribution of IMDb ratings',
                    fontsize = 13,
                    fontweight = 'bold')

axes[0,0].set_xlabel('IMDb Rating',fontsize = 11)

axes[0,0].set_ylabel('No of movies',fontsize = 11)

director_df = director_rating.head(10).reset_index()
director_df.columns = ['Director' , 'Rating']

sns.barplot(
    data = director_df,
    x='Rating',
    y='Director',
    ax = axes[0,1],
    color = 'darkorange'
)

axes[0,1].set_title('Directors with highest rating',fontsize = 13,
    fontweight = 'bold')
axes[0,1].set_xlabel('Rating',fontsize = 11)
axes[0,1].set_ylabel('Director',fontsize = 11)

genre_df = genre_rating.head(10).reset_index()
genre_df.columns = ['Genre' , 'Rating']

sns.barplot(
    data = genre_df,
    x = 'Rating',
    y = 'Genre',
    ax = axes[1,0],
    color = 'seagreen'
)

axes[1,0].set_title("Genres with higher rating",fontsize = 13,
    fontweight = 'bold')
axes[1,0].set_xlabel('Rating',fontsize = 11)
axes[1,0].set_ylabel('Genre',fontsize = 11)

axes[1,0].tick_params(axis = 'x',rotation = 90)

axes[1,1].plot(
    year_releases.index,
    year_releases.values,
    marker='o',linewidth = 2.5,
    markersize = 7,
    color = 'crimson',
    linestyle = '--',
)

axes[1,1].set_title('Movie releases',fontsize = 10 , fontweight = 'bold')
axes[1,1].set_xlabel('Year')
axes[1,1].set_ylabel('Number of Movies')
axes[1,1].grid(True)

plt.suptitle(
    'IMDb Movie Analysis Dashboard',
    fontsize = 20,
    fontweight = 'bold',
)

plt.tight_layout(rect=[0,0,1,0.96])
plt.savefig("dashboard.png", dpi=300,bbox_inches = 'tight')
plt.show()

#relationship between ratings and revenue
plt.figure(figsize=(8,5))

sns.scatterplot( #relationship between two numerical values
    data = df,
    x = 'Rating',
    y = 'Revenue (Millions)',
    color = 'darkorange',
    alpha = 0.6 ,#--> gives us the opacity of the scattered plots here,
   
)
corr = df[['Rating','Revenue (Millions)']].corr(numeric_only = True)
print(corr)
plt.title('IMDb Ratings vs Revenue')
plt.xlabel("IMDb Ratings")
plt.ylabel('Revenue (Millions)')
plt.savefig("Rating_vs_Revenue(Millions).png", dpi=300,bbox_inches = 'tight')
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(
    data = df,
    x = 'Rating',
    y = 'Votes',
    color = 'red',
)

corr = df[['Rating','Votes']].corr(numeric_only = True)
print(corr)
plt.title('IMDb Ratings vs Votes')
plt.xlabel("IMDb Ratings")
plt.ylabel('Votes')
plt.savefig("ratings_vs_votes.png", dpi=300,bbox_inches = 'tight')
plt.show()

corr_matrix = df[
    ['Rating',
     'Votes',
     'Revenue (Millions)',
     'Runtime (Minutes)',
     'Metascore',
     'Year']

].corr(numeric_only = True)
print(corr_matrix)

plt.figure(figsize=(8,6))

sns.heatmap(
    corr_matrix, #instead of plotting original data frame we r plotting correlation matrix
    annot = True,#displays correlation values inside each cell
    cmap = 'coolwarm',
    fmt = '.2f', #formats to 2 deicmal places
)

plt.title('Correlation Heatmap')
plt.savefig("correlation_heatmap.png", dpi=300,bbox_inches = 'tight')
plt.show()