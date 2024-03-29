import os

import requests

# Your GitHub username
USERNAME = os.getenv('GITHUB_USERNAME', 'default_username')

# The organization to which you want to transfer repositories
ORGANIZATION = os.getenv('GITHUB_ORGANIZATION', 'default_organization')

# Your personal access token
TOKEN = os.getenv('GITHUB_TOKEN', 'default_token')

# GitHub API headers
headers = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
}

def list_forked_repos():
    """List all forked repositories."""
    repos = []
    page = 1
    while True:
        response = requests.get(
            f'https://api.github.com/users/{USERNAME}/repos?type=forks&page={page}&per_page=100',
            headers=headers
        )
        response.raise_for_status()
        data = response.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos

def transfer_repo(repo_name):
    """Transfer a repository to the specified organization."""
    response = requests.post(
        f'https://api.github.com/repos/{USERNAME}/{repo_name}/transfer',
        headers=headers,
        json={'new_owner': ORGANIZATION}
    )
    if response.status_code == 202:
        print(f'Successfully started transfer of {repo_name}')
    else:
        print(f'Failed to transfer {repo_name}: {response.content}')


def print_forked_repos():
    """
    Prints a list of names of forked repositories for the configured user.
    """
    forked_repos = list_forked_repos()  # Call the existing function to get forked repos
    if not forked_repos:
        print("No forked repositories found.")
        return
    print("Forked Repositories:")
    for repo in forked_repos:
        print(repo['name'])

def main():
    repos = list_forked_repos()
    for repo in repos:
        transfer_repo(repo['name'])

if __name__ == '__main__':
    main()
