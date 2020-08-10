'''This module handles the collection and scraping of repositories from GitHub.'''

import re
from bs4 import BeautifulSoup
from requests_client import Requests
from data.repository import Repository


class Collector:
    '''Class to collect and process retreived repository data from GitHub.'''

    @staticmethod
    def scrape_repositories(query: str, sort: str, max_results=10, pages=1) -> list:
        '''Begins collecting and scraping the specified number of repositories.'''

        repositories = list()

        for i in range(1, pages + 1):
            params = {'q': query, 'sort': sort, 'order': 'desc', 'per_page': max_results, 'page': i}
            data = Requests.get('/search/repositories', params)

            processed = [Collector.process_item(item) for item in data['items']]
            repositories.extend(processed)

        return repositories

    @staticmethod
    def process_item(item: dict) -> Repository:
        '''Finishes collecting and organizes the data into a dataclass.'''

        repository = Repository()

        repository.name = item['name']
        repository.owner = item['owner']['login']
        repository.full_name = item['full_name']
        repository.description = item['description']
        repository.language = item['language']
        repository.created_at = item['created_at']
        repository.stars = item['stargazers_count']
        repository.forks = item['forks_count']
        repository.url = item['svn_url']
        repository.clone_url = item['clone_url']

        repository.issues = Collector.get_repository_issues(repository.full_name)
        (contributors, commits) = Collector.get_scraped_data(repository.full_name)

        repository.contributors = contributors
        repository.commits = commits

        return repository

    @staticmethod
    def get_repository_issues(full_name: str) -> int:
        '''Gets the total number of issues for a repository.'''

        endpoint = f'/repos/{full_name}/issues'
        data = Requests.get(endpoint)

        # First element contains number for latest issue
        issues = data[0]['number']

        return issues

    @staticmethod
    def get_scraped_data(full_name: str) -> tuple:
        '''Collects additional data through scraping the repository page.'''

        page = Requests.get_html('https://github.com/' + full_name)
        soup = BeautifulSoup(page, 'html.parser')

        regex = re.compile('[a-zA-Z+,\n ]')

        contributors_tag = soup.find_all(href=f'/{full_name}/graphs/contributors')
        commits_tag = soup.find_all('span', 'd-none d-sm-inline')

        contributors = -1

        if len(contributors_tag) > 0:
            # Last found is the best available match
            contributors = int(regex.sub('', contributors_tag[-1].text))

        commits = int(regex.sub('', commits_tag[-1].text))

        return (contributors, commits)
