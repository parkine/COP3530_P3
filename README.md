# Movie Recommender Application

## Overview

The **Movie Recommender System** is a Python-based web application that suggests movies based on user input. Users can enter two of their favorite movies, and the system recommends similar movies using graph-based algorithms like **BFS (Breadth-First Search)** and **DFS (Depth-First Search)**. The project used **Flask** for the web interface, **SQLite** for the database, and custom logic for finding movie relationships. 


---

## Features

- **Search Algorithms**:
  - Recommends movies using either BFS or DFS, based on the user's selection.
- **Dynamic Recommendations**:
  - Calculates movie similarity based on attributes such as genres, directors, writers, and ratings.
- **User-Friendly Interface**:
  - Includes labels, placeholders, and error messages to guide users.
- **Efficient Backend**:
  - Uses a graph-based data structure for traversing and finding similar movies.
- **Error Handling**:
  - Handles invalid inputs and provides feedback to users.

---

## Technologies Used

- **Python**: Core programming language for backend logic.
- **Flask**: Web framework for building the application.
- **SQLite**: Database for storing movie information.
- **HTML/CSS**: Frontend for the user interface.

---

## Prerequisites

- **Python 3**: Ensure Python 3 is installed on your system.
- **PIP** : Ensure pip is installed on your system for managing Python packages.

---

## Installation and Running

1. Clone or download the repository:
```
  git clone https://github.com/parkine/Movie_Recommender.git
```
2. Install Dependencies:
```
  pip install -r requirements.txt
```
3. Navigate to the project directory:
```
  cd Movie_Recommender/src
```
4. Run the application:
```
  python3 app.py
```
5. Open your browser and go to: http://localhost:5000

---

## How to Use
1. Launch the app in your browser.
2. Enter the names of two favorite movies in the provided fields.
3. Select the search algorithm (DFS or BFS).
4. Click the find button to view a list of similar movies.

## Homepage
![alt text](homepage.png)