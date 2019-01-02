# Project Description
**Title:** 
Make My Playlist

**Group Members:**
Seher Khan, Sudeeksha Sanikommu and Shreyasi Chaudhary

**Goal:**
The aim of this project is to make it easier for a user to generate their playlist given a set of songs. 

# Project Structure
We employed a classification approach which creates the playlist based on predefined playlists and obtained satisfactory results. We also experimented with a clustering approach, taking into account the listening history of similar users and producing more personalized playlists.

**Approach 1:**
Number of rows (songs): 8980
Features: popularity, acousticness, energy, liveness, tempo, speechiness, instrumentalness, time_signature, danceability, key, duration_ms, loudness, valence, mode
Classes: Love, romantic, classical, edm,  dance, breakup, rock, jazz, sad, trance, hiphop, country, party,  new hits,  workout, old hits, happy
Source: Spotify

Classification models employed:  Decision Tree, SVM, Logistic Regression, Naive Bayes, LDA, QDA, Random Forest,  Gradient Boosting Classifier, One vs Rest Classification, Neural Networks, Ada boost, Voting Classifier, Class Hierarchy

**Approach 2:**
Data: 
* Listening history of 54,687 users was obtained from the Echo Nest.
* Users with fewer than 5 songs in their history were dropped.
* Features of each song was extracted for each remaining user and then averaged * out to produce features *for the user*.

Clustering model employed to cluster users: Mean Shift Clustering, K means, and Affinity propagation
