import random
import spotipy
import time
from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data4
import pandas as pd

client_id = ''
client_secret = ''
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False

#your uri list goes here
s_list = ['spotify:track:2d7LPtieXdIYzf7yHPooWd','spotify:track:0y4TKcc7p2H6P0GJlt01EI','spotify:track:6q4c1vPRZREh7nw3wG7Ixz','spotify:track:54KFQB6N4pn926IUUYZGzK','spotify:track:0NeJjNlprGfZpeX2LQuN6c']

#put uri to dataframe
df = pd.DataFrame(s_list)
df.columns = ['URI']

df['energy'] = ''*df.shape[0]
df['loudness'] = ''*df.shape[0]
df['speechiness'] = ''*df.shape[0]
df['valence'] = ''*df.shape[0]
df['liveness'] = ''*df.shape[0]
df['tempo'] = ''*df.shape[0]
df['danceability'] = ''*df.shape[0]

for i in range(0,df.shape[0]):
  time.sleep(random.uniform(3, 6))
  URI = df.URI[i]
  features = sp.audio_features(URI)
  df.loc[i,'energy'] = features[0]['energy']
  df.loc[i,'speechiness'] = features[0]['speechiness']
  df.loc[i,'liveness'] = features[0]['liveness']
  df.loc[i,'loudness'] = features[0]['loudness']
  df.loc[i,'danceability'] = features[0]['danceability']
  df.loc[i,'tempo'] = features[0]['tempo']
  df.loc[i,'valence'] = features[0]['valence']
  uri=0

print(df)