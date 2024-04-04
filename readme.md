# Movie Recommendation System

This Python script implements a simple movie recommendation system based on content similarity. It reads movie data from a CSV file (`movies.csv`), computes the TF-IDF vectors for the movie genres, calculates cosine similarity between movies based on their genre descriptions, and provides movie recommendations based on similarity.

## Requirements

- Python 3.x
- pandas
- scikit-learn

## Usage

1. Ensure you have installed the required packages mentioned above.
    ```sh $ pip install -r requirnment.txt ```
2. Place the `movies.csv` file containing movie data in the same directory as the script.
3. Run the script `python3 recommendation.py`.
4. Enter the name of a movie when prompted.
5. The script will output recommendations based on the entered movie.

## File Descriptions

- `movie_recommendation.py`: The main Python script implementing the movie recommendation system.
- `movies.csv`: A CSV file containing movie data with columns: `movieId`, `title`, and `genres`.
- `README.md`: This file, providing instructions and information about the script.
