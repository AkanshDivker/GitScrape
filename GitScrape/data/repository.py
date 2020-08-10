'''This module contains the Repository dataclass for storing data.'''

from dataclasses import dataclass


@dataclass
class Repository:
    '''Dataclass containing data pertaining to repository information.'''
    name: str = ''
    owner: str = ''
    full_name: str = ''
    description: str = ''
    language: str = ''
    created_at: str = ''
    stars: int = 0
    forks: int = 0
    url: str = ''
    clone_url: str = ''

    contributors: int = 0
    commits: int = 0
    issues: int = 0
