import pandas as pd
import matplotlib.pyplot as plt
# loading the data 
df =pd.read_csv('netflix_titles.csv')
# cleaning  
df= df.dropna(subset=['type','release_year','rating','country','duration'])

type_counts=df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index,type_counts.values,color=['skyblue','orange'])
plt.title('number of movies vs tv shows on netflix')
plt.xlabel('type')
plt.ylabel('count')
plt.tight_layout()
plt.savefig('movies_vs_tv.png')
plt.show()

movie_df=df[df['type'] == 'Movie'].copy()
movie_df['duration_int']= movie_df['duration'].str.replace('min','').astype(int)
plt.figure(figsize=(8,6))
plt.hist(movie_df['duration_int'],bins=30, color='blue',edgecolor='black')
plt.title('distribuation of movie ')
plt.tight_layout()
plt.savefig('movie_duration_histogram.png')
plt.show()

release_counts=df['release_year'].value_counts().sort_index()
plt.figure(figsize=(8,9))
plt.scatter(release_counts.index,release_counts.values,color='red')
plt.title('relase_year vs number of shows ')
plt.tight_layout()
plt.savefig('release_year_vs_number_of_shows.png')
plt.show()

country_conunt= df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_conunt.index,country_conunt.values,color='teal')
plt.title('top 10 country by the shows ')
plt.xlabel('number of shows')
plt.ylabel('name of country')
plt.tight_layout()
plt.savefig('top 10 country by shows.png')
plt.show()

content_by_year= df.groupby(['release_year','type']).size().unstack().fillna(0)
fig, ax=plt.subplots(1,2, figsize=(12,5))
#first subplot movies
ax[0].plot(content_by_year.index,content_by_year['Movie'],color='blue')
ax[0].set_title('movies released per year ')
plt.savefig('movies_content_by_year.png')
plt.show()