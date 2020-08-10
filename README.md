# GitScrape

GitScrape is a Python program which intends to help make data retrieval on GitHub simple and efficient. GitScrape is capable of querying for specified repository types and then collect relevent data and statistics on the repository, while also cloning the repositories if necessary. Particularly in software related research, large sets of data are required to perform studies. GitScrape hopes to make this process a little easier by automating the collection process, and making the collected repositories easy to use for analysis with additionally provided statsics included and ready to use.

#### TO-DO:
- Implement smart system for cloning and stats storage
- Improve performance

## Getting Started

You can get started by cloning the repository on your desktop. The code should be commented enough to follow along and understand. Please install the necessary Python requirements that are located inside of the `requirements.txt` file.

### Prerequisites

This project requires Python 3.7 to be installed. Please ensure the required modules in `requirements.txt` are installed. Should be compatible for all systems that have Python 3.7 properly installed.

### Usage
In order to use the module, cd into the `GitScrape` directory and simply start the script by calling `python gitscrape.py` in your terminal. A full list of commands and their details can be seen by running `python gitscrape.py -h` in your terminal. A lot of the commands are optional based on your needs, but the query and user commands are necessary to use GitScrape.

An example command to scrape the top 10 starred Python repositories on GitHub would be as follows.

```
python gitscrape.py -u username -q "language:python" -s stars -pp 10 -p 1 -o
```

For additional information on creating your own queries for the GitHub API, please read the documentation provided on the API website here: https://docs.github.com/en/github/searching-for-information-on-github/searching-for-repositories

### Final Notes

I created this to help me with collecting repositories for my own research. I'm always happy to learn, help out and, teach others. If you have any questions or comments, feel free to contact me!

## Authors

* **Akansh Divker** - *Author* - [AkanshDivker](https://github.com/AkanshDivker)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
