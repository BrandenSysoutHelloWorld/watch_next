# Imports
import spacy

hulk_movie = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

def read_movies():
    # Movies dictionary
    movies = {}

    # Open movies.txt
    with open('movies.txt', 'r') as file_movies:
        
        # Read movies from text file
        movie_list = file_movies.readlines()

        for movie in movie_list:
            split_movie = movie.split(' :')

            # Add movie to Movies dictionary
            movies.update({split_movie[0]: split_movie[1]})

    # Returns Movies List
    return movies


def compare_movies(compare_desc):
    # Load Spacy model
    nlp = spacy.load('en_core_web_md')

    # Dictionary used to store similarity scores
    movie_scores = {}
    
    hulk_token = nlp(compare_desc)

    # Call Read Movies function
    movies = read_movies()

    # Comparing movie descriptions
    for title, desc in movies.items():
        # Tokenize movie descriptions
        tokenized_desc = nlp(desc)
        
        similarity_score = hulk_token.similarity(tokenized_desc)

        print(title, similarity_score)

        movie_scores.update({title: similarity_score})

    return movie_scores    

def suggest_movie():
    # Call Compare Movies function
    scores = compare_movies(hulk_movie)

    highest_score = 0
    suggest_movie = None

    for title, score in scores.items():
        if score > highest_score:
            highest_score = score
            suggest_movie = title
    
    return suggest_movie

print('SUGGESTED MOVIE: ', suggest_movie())
