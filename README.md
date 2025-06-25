# Introduction
This is Schreddit, a Reddit clone. This work was made as a class assignment in collaboration with 4 other collaborators. 
The commit history was removed. Be aware, that some integral api-keys/ -urls had to be removed. This means for execution of the code you will have to use your own values.

# Project tour
### Home page
![alt text](https://github.com/Erbond12/Reddit-Klon/blob/main/project-preview/Home%20page%20with%20working%20videos.png?raw=true)

### Posts
When you click on a post, a modal window appears. This displayed the post itself, along with its comments and the option to comment on it. Voting on comments and posts was also possible.
![alt text](https://github.com/Erbond12/Reddit-Klon/blob/main/project-preview/Pop%20up%20when%20opening%20a%20post%20from%20home%20page.png?raw=true)

### Comment tree
The comments did appear similar to Reddit in a tree-like structure.
![alt text](https://github.com/Erbond12/Reddit-Klon/blob/main/project-preview/Nested%20comment%20tree%20with%20working%20voting.png?raw=true)

### Post creation
Posts could be assigned to a subreddit and different tags.
![alt text](https://github.com/Erbond12/Reddit-Klon/blob/main/project-preview/Post%20creation.png?raw=true)

### Subreddits
On the home page, you can also go directly to the subreddits you already follow.
![alt text](https://github.com/Erbond12/Reddit-Klon/blob/main/project-preview/Followed%20subreddits%20and%20home%20screen%20with%20recommendations.png?raw=true)

### User creation/ login
Creation of a new user/ login of existing users.
![alt text](https://github.com/Erbond12/Reddit-Klon/blob/main/project-preview/Register%20user%20or%20login.png?raw=true)

### Settings
A user could change his password and email.
![alt text](https://github.com/Erbond12/Reddit-Klon/blob/main/project-preview/User%20settings.png?raw=true)

# Run
### Backend
Install [Neo4j](https://neo4j.com/download/), the [Neo4j APOC Core library](https://neo4j.com/labs/apoc/4.3/installation/), [MongoDB](https://www.mongodb.com/try/download/community) and [Redis](https://redis.io/download).

Install [poetry](https://python-poetry.org/docs/#installation) and run `poetry install` from the `backend` directory (where the `pyproject.toml` file is located) to install the required dependencies.

Copy the contents of the `dot_env_example` to a new file called `.env` in the same directory and adjust credentials for production DB.

To run, execute `poetry run app/main.py` from the `backend` directory.
The API documentation will be available via http://localhost:8000/docs.

From the `backend` directory, run `poetry run scripts/dummy_data.py` with the `fill` argument to fill the databases with dummy data, with the `clear` argument to clear all data, or with `-h` for more information on configuration parameters.

### Frontend
Install [Node.js](https://nodejs.org/en/download/) and run `npm install` from the `frontend/schreddit-ui` directory (where the `package.json` file is located) to install the required dependencies.

To run, execute `npm start` from the `frontend/schreddit-ui` directory.
The app will be available via http://localhost:3000.

# Test
### Backend
Adjust credentials for testing DB in `.env`. 

Run `scripts/test.sh` to run all tests, including a coverage report.

# Develop
### Backend
To resolve the modules correctly in your IDE, the `backend` directory needs to be in your `PYTHONPATH` (e.g. [instructions for PyCharm](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-reloading-interpreter-paths.html)).

For logging Cypher queries, set the environment variable `NEOMODEL_CYPHER_DEBUG=1`.

For code linting, run `scripts/lint.sh` from the `backend` directory.

Before committing, run `scripts/format.sh` from the `backend` directory.
It performs automatic code formatting, import sorting and removes unused imports.
