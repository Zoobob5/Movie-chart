# Movie Recommendation System

## Overview

This project is a simple movie recommendation system built in Python. It uses a movie dataset to create a graph of related movies and allows users to explore recommendations based on a starting movie. The user can choose between two different search algorithms: Breadth-First Search (BFS) and Depth-First Search (DFS).

## Features

- **Movie Dataset**: Contains a list of movies with information on genres, directors, and actors.
- **Graph Construction**: A graph is built connecting movies based on shared genres, directors, or actors.
- **BFS & DFS Search Algorithms**: Users can explore movie recommendations using either BFS or DFS.
- **Robust User Input**: The program handles invalid inputs by prompting the user to try again until a valid movie or search method is provided.

## Project Structure

- **bfs.py**: Contains the BFS algorithm for movie recommendations
- **dfs.py**: Contains the DFS algorithm for movie recommendations
- **graph.py**: Function to build the movie graph
- **main.py**: Main script to run the program
- **movies.py**: Contains the movie dataset
- **README.md**: Project documentation




## Ex: Output:
Enter a movie title to get related recommendations: Inception
Choose a search method (BFS or DFS): BFS

Movies related to Inception:
- Inception
- The Dark Knight
- Men in Black
- Pulp Fiction
- Toy Story
