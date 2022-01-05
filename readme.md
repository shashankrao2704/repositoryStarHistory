# Introduction

The project analyzes how the star count of a repository developed over its entire history. It takes the user and their
repository name as an input and outputs a dataset as a `.csv` file containing the timestamp of the starring and the user 
who starred the repository. 

## Requirements

`python >= 3.x`

`pandas == 1.3.x`

`pyGithub == 1.55`

## How to run?

Create a `.env` file and write your access token as :

`TOKEN=<github personal access token>`

Install the requirements :

```shell
pip install -r requirements.txt
```
Run the `gitStarHistory.py` :

```shell
$ python3 gitStarHistory.py
```
Enter the repository user and the repository name :
```jupyter
Enter user: <repository user>
Enter repository: <repository name> 
```
In the output, the dataframe with the star history will be printed and is saved as `<repository name>_star_history.csv`