import os

from github import Github
from dotenv import load_dotenv
import pandas as pd

load_dotenv('.env')
AUTH_TOKEN = os.getenv('TOKEN')


# Fetches star count data and saves it in a .csv file
# Includes date of starring, user who starred and stars as index
def fetch_repo_stars(repository_data):
    stargazers = repository_data.get_stargazers_with_dates()
    data = [(stargazer.starred_at.strftime("%Y-%m-%dT%H:%S"), stargazer.user.login) for stargazer in stargazers]
    star_df = pd.DataFrame(data, columns=['Date', 'User'])
    star_df.index = star_df.index + 1
    star_df.index.names = ['Stars']
    star_df.to_csv(repository_data.name + '_star_history.csv')
    return star_df


# To fetch repository name
def fetch_repo_data():
    user = input("Enter user: ")
    repo = input("Enter repository: ")
    g = Github(AUTH_TOKEN)
    repository_data = g.get_repo(user + "/" + repo)
    return repository_data


if __name__ == '__main__':
    repo_data = fetch_repo_data()
    star_data = fetch_repo_stars(repo_data)
    # print star history collected
    print(star_data)
