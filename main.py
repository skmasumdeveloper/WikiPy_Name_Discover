##########################
# Please run and enter your Name #
##########################


import requests
from bs4 import BeautifulSoup

def search_wikipedia(name):
    # Format the search query for the Wikipedia API
    search_query = f"https://en.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch={name}&utf8=1"

    # Send a GET request to the Wikipedia API
    response = requests.get(search_query)
    data = response.json()

    # Extract relevant information from the API response
    search_results = data.get('query', {}).get('search', [])

    return search_results

def get_top_5_results(name):
    # Get search results for the given name
    results = search_wikipedia(name)

    # Extract the top 5 search results or all results if less than 5
    top_5_results = results[:5]

    return top_5_results

def get_plain_text_from_html(html):
    # Use BeautifulSoup to remove HTML tags and get plain text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text()

def print_wikipedia_results(results):
    # Print the names, Wikipedia URLs, and snippets with borders
    print("\nTop 5 Results:")
    for result in results:
        page_title = result.get('title', '')
        page_id = result.get('pageid', '')
        page_url = f"https://en.wikipedia.org/?curid={page_id}"
        snippet_html = result.get('snippet', '')
        
        # Convert HTML to plain text
        snippet_text = get_plain_text_from_html(snippet_html)

        # Print result with borders
        print('-' * 50)
        print(f"{page_title}\n")
        print(f"Details: {snippet_text}...\n")
        print(f"Link: {page_url}\n")
        print('-' * 50)

# Get user input for the name
user_name = input()

# Get and print the top 5 Wikipedia results for the given name
top_results = get_top_5_results(user_name)
print_wikipedia_results(top_results)
