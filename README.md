# Company Founder Finder Script
## Project Overview
This script is designed to find the founders of companies using their names as input. It searches for each company's Wikipedia page, extracts the founder's information from the infobox, and displays it directly on the screen. The script processes a CSV file containing a list of company names, making it an efficient tool for retrieving founder information for multiple companies.

## Script Usage Instructions
### Environment Setup:

Ensure that Python is installed on your system.
Install the required Python libraries by running the following command:

pip install requests beautifulsoup4
### Input File:

The script expects a CSV file containing company names in the first column. The file path is hardcoded in the script (csv_file_path), so ensure the file is correctly placed, or update the path in the script as needed.
### Running the Script:
To run the script, simply execute the following command in your terminal:
script_name.py
The script will display the founder(s) of each company directly on the screen as it processes the CSV file.

## Resources Used
- **Wikipedia API**: To search for relevant Wikipedia pages based on company names.
- **BeautifulSoup**: To parse and extract founder information from the HTML content of Wikipedia pages.
- **CSV Module**: To handle and process the input CSV file containing company names.

## Challenges Faced
- Inconsistent Wikipedia Page Structure: One of the primary challenges was handling the variability in Wikipedia pages. Not all pages have a uniform structure, making it difficult to extract founder information consistently. This was managed by focusing on the infobox section, which generally contains key company details.
- Handling Edge Cases: Some companies may not have readily available Wikipedia pages, or their pages may not include founder information. The script includes error handling and informative messages to address these situations.

## Future Improvements
- Enhancing Data Sources: Expanding the script to use multiple data sources, such as Crunchbase or LinkedIn, to improve the accuracy and coverage of founder information.
- Machine Learning Integration: Incorporating machine learning models to predict and identify founder information when direct extraction from a webpage is not possible.
- GUI Development: Creating a graphical user interface (GUI) to make the script more user-friendly and accessible to non-technical users.
- Improved Error Handling: Implementing more sophisticated error handling to deal with various network issues, API limitations, or unexpected HTML structures.
