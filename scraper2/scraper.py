import os
import json
import logging
from urllib.parse import urljoin
from utils import get_html, parse_html, get_job_details

# Load configuration
with open('config.json') as config_file:
    config = json.load(config_file)

# Set up logging directory
log_directory = "logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

log_file_path = os.path.join(log_directory, 'main.log')

# Set up logging
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# Get the HTML content of the search page
search_html = get_html(config['search_url'])
job_elements = parse_html(search_html, config['job_list_selector'])

for job_element in job_elements:
    job_link = job_element.find('a', href=True)
    if job_link:
        job_url = urljoin(config['base_url'], job_link['href'])
        job_details = get_job_details(job_url, config)
        if job_details:
            title, location_company, views, applied = job_details
            logging.info(f"Job Title: {title}, Location and Company: {location_company}, Views: {views}, Applied: {applied}")
            print(f"Scraped: {title}")
