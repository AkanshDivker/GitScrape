'''This module handles the utiltiy for creating web requests.'''

import requests


class Requests:
    '''Class tailored to creating web requests directed at the GitHub API.'''

    headers = {'User-Agent': 'gitscrape-app/1.0.0', 'Accept': 'application/vnd.github.v3+json'}
    api_url = 'https://api.github.com'
    username = tuple()

    @staticmethod
    def get(endpoint: str, params=None):
        '''Override for requests.get() tailored for GitHub API.'''
        response = requests.get(Requests.api_url + endpoint, auth=Requests.username,
                                headers=Requests.headers, params=params)
        data = response.json()

        return data

    @staticmethod
    def get_html(url: str) -> str:
        '''Gets the HTML content of the specified URL.'''
        response = requests.get(url)
        data = response.text

        return data
