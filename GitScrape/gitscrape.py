'''This module is the main module of the program and handles its input and entry point.'''

import argparse
from collector import Collector
from requests_client import Requests


class GitScrape:
    '''Class to receive and process input for the program and then execute main components.'''

    @staticmethod
    def run():
        '''Main entry point for the program.'''

        # Argument definition and entry
        parser = argparse.ArgumentParser()
        parser.add_argument('-u', '--user', type=str, required=True,
                            help='Your GitHub account username.', action='store')
        parser.add_argument('-cd', '--clone-dir',
                            help=('Clones scraped repositories to the target directory '
                                  'when specified.'),
                            action='store')
        parser.add_argument('-q', '--query', type=str, required=True,
                            help=('The query to search for repositories with. Needs to be wrapped '
                                  'in quotation marks. Information on building GitHub queries '
                                  'can be found here: '
                                  'https://docs.github.com/en/github/searching-for-information-on-github/searching-for-repositories'),
                            action='store')
        parser.add_argument('-s', '--sort', type=str,
                            help=('Sorts the results of your query. Can be sorted by stars, forks, '
                                  'help-wanted-issues, updated. Leaving this empty '
                                  'defaults to best match.'),
                            action='store')
        parser.add_argument('-pp', '--per-page', type=int, help=('The number of results per API '
                                                                 'page request. Default is 10. '
                                                                 'Max is 100.'),
                            action='store')
        parser.add_argument('-p', '--pages', type=int, help=('The number of pages to query through.'
                                                             ' Default is 1.'),
                            action='store')
        parser.add_argument('-o', '--output', help='Outputs scraped data to the console.',
                            action='store_true')

        args = parser.parse_args()

        # Initializing repository scraping
        Requests.username = (args.user, '')
        repositories = Collector.scrape_repositories(args.query, args.sort, args.per_page,
                                                     args.pages)
        # Process action arguments
        if args.output:
            GitScrape.print_output(repositories)

    @staticmethod
    def print_output(repositories: list):
        '''Prints summarized output for all scraped repositories.'''

        print('Scraped Repository Data: \n')

        for repo in repositories:
            print('Name: ' + repo.name)
            print('Owner: ' + repo.owner)
            print('Full Name: ' + repo.full_name)
            print('Description: ' + repo.description)
            print('Language: ' + repo.language)
            print('Created At: ' + repo.created_at)
            print('Stars: ' + str(repo.stars))
            print('Forks: ' + str(repo.forks))
            print('Contributors: ' + str(repo.contributors))
            print('Commits: ' + str(repo.commits))
            print('Issues: ' + str(repo.issues))
            print('URL: ' + repo.url)
            print('-----------------------\n')

if __name__ == "__main__":
    GitScrape.run()
