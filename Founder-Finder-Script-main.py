import requests
from bs4 import BeautifulSoup
import urllib.parse
import csv

def find_wikipedia_founder(business_name):
    """
    Searches Wikipedia for the given business name and returns the founder's name if available.

    Parameters:
    business_name (str): The name of the business to search for.

    Returns:
    str: The name of the founder(s) or an error message if the information cannot be retrieved.
    """
    # Wikipedia API search endpoint
    wiki_api_url = "https://en.wikipedia.org/w/api.php"
    search_params = {
        'action': 'query',
        'format': 'json',
        'list': 'search',
        'srsearch': business_name,  # The search term (business name)
        'utf8': 1
    }

    # Send a GET request to the Wikipedia API
    wiki_response = requests.get(wiki_api_url, params=search_params)

    # Check if the API request was successful
    if wiki_response.status_code != 200:
        return "Unable to fetch search results"

    # Parse the JSON response from the Wikipedia API
    search_data = wiki_response.json()
    search_entries = search_data.get('query', {}).get('search', [])

    # If no search results were found, return a message
    if not search_entries:
        return "No relevant search results found"

    # Get the title of the top search result
    top_result_title = search_entries[0]['title']
    page_link = f"https://en.wikipedia.org/wiki/{urllib.parse.quote(top_result_title)}"

    # Request the Wikipedia page of the business
    page_response = requests.get(page_link)

    # Check if the page request was successful
    if page_response.status_code != 200:
        return f"Failed to load the page: {page_link}"

    # Parse the HTML content using BeautifulSoup
    page_content = BeautifulSoup(page_response.text, 'html.parser')

    # Find the infobox containing company details
    infobox_table = page_content.find('table', {'class': 'infobox'})
    if infobox_table:
        infobox_rows = infobox_table.find_all('tr')
        founder_names = []
        for row in infobox_rows:
            header_cell = row.find('th')
            # Look for the 'Founder' in the header cell
            if header_cell and 'Founder' in header_cell.get_text():
                founder_cell = row.find('td')
                if founder_cell:
                    founder_names.append(founder_cell.get_text(strip=True))
        # Return the founders as a comma-separated string if found
        if founder_names:
            return ', '.join(founder_names)
    return "Founder information not available"

def read_csv_and_find_founders(csv_file_path):
    """
    Reads a CSV file containing business names and searches for the founder of each business.

    Parameters:
    csv_file_path (str): The file path to the CSV file containing business names.
    """
    try:
        # Open the CSV file
        with open(csv_file_path, mode='r') as csvfile:
            csv_reader = csv.reader(csvfile)
            # Skip the header row if present
            next(csv_reader, None)

            # Process each business name in the CSV file
            for row in csv_reader:
                business_name = row[0].strip()  # Get the business name from the row
                if business_name:  # Ensure the business name is not empty
                    print(f"\nSearching for {business_name}...")
                    founder_name = find_wikipedia_founder(business_name)
                    print(f"Founder of {business_name}: {founder_name}")
    except Exception as ex:
        print(f"An error occurred while processing the CSV file: {ex}")

def initiate_script():
    """
    The main function that starts the script.
    """
    print("Welcome to the Business Founder Search Tool!")

    # Hardcoded path to the CSV file with business names
    csv_file_path = "/content/Company_Names_Dataset.csv"

    # Read the CSV file and find the founders
    read_csv_and_find_founders(csv_file_path)

if __name__ == "__main__":
    initiate_script()
