import os
import json
import logging
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from utils import get_html, parse_html

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
logging.info("Logging is set up. Starting the scraper.")

# Get the HTML content of the search page
logging.info(f"Fetching search results from {config['search_url']}")
search_html = get_html(config['search_url'])

if search_html:
    logging.info("Search page fetched successfully.")
    job_elements = parse_html(search_html, config['job_list_selector'])
    logging.info(f"Found {len(job_elements)} job elements.")

    for job_element in job_elements:
        # Assuming the job link is within an 'a' tag directly within each job element.
        job_link_element = job_element.find('a', href=True)
        if job_link_element:
            job_url = urljoin(config['base_url'], job_link_element['href'])
            logging.info(f"Fetching job details from {job_url}")
            job_html = get_html(job_url)

            if job_html:
                job_soup = BeautifulSoup(job_html, 'html.parser')
                title_element = job_soup.select_one(config['job_title_selector'])
                location_element = job_soup.select_one(config['job_location_selector'])
                company_element = job_soup.select_one(config['job_company_selector'])
                views_element = job_soup.select_one(config['job_views_selector'])
                applied_element = job_soup.select_one(config['job_apply_selector'])

                title = title_element.get_text(strip=True) if title_element else 'Not provided'
                location = location_element.get_text(strip=True).split('-')[
                    0].strip() if location_element else 'Not provided'
                company = company_element.get_text(strip=True) if company_element else 'Not provided'
                views = views_element.get_text(strip=True) if views_element else 'Not provided'
                applied = applied_element.get_text(strip=True) if applied_element else 'Not provided'

                logging.info(
                    f"Job Title: {title}, Location: {location}, Company: {company}, Views: {views}, Applied: {applied}")
                print(f"Scraped: {title}")
            else:
                logging.error(f"Failed to fetch job details from {job_url}")

            time.sleep(config['delay'])  # Delay as per the configuration
        else:
            logging.warning(f"No job link found in job element. Element HTML: {job_element}")
else:
    logging.error("Failed to fetch the search page.")

logging.info("Scraper finished.")
