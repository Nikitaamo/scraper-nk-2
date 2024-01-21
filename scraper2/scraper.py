import os
import json
import logging
import time
import re
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

# Set up main logger
main_log_file_path = os.path.join(log_directory, 'main.log')
main_logger = logging.getLogger('MainLogger')
main_logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(main_log_file_path)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler.setFormatter(formatter)
main_logger.addHandler(file_handler)

# Set up job details logger
job_details_log_file_path = os.path.join(log_directory, 'job_details.log')
job_details_logger = logging.getLogger('JobDetailsLogger')
job_details_logger.setLevel(logging.INFO)
details_file_handler = logging.FileHandler(job_details_log_file_path)
details_file_handler.setFormatter(formatter)
job_details_logger.addHandler(details_file_handler)

main_logger.info("Logging is set up. Starting the scraper.")

# Get the HTML content of the search page
main_logger.info(f"Fetching search results from {config['search_url']}")
search_html = get_html(config['search_url'])

if search_html:
    main_logger.info("Search page fetched successfully.")
    job_elements = parse_html(search_html, config['job_list_selector'])
    main_logger.info(f"Found {len(job_elements)} job elements.")
    job_details_logger.info(f"Found {len(job_elements)} job elements.")

    for i, job_element in enumerate(job_elements, start=1):
        job_link_element = job_element.find('a', href=True)
        if job_link_element:
            job_url = urljoin(config['base_url'], job_link_element['href'])
            main_logger.info(f"Fetching job details from {job_url}")
            job_html = get_html(job_url)

            if job_html:
                job_soup = BeautifulSoup(job_html, 'html.parser')
                title_element = job_soup.select_one(config['job_title_selector'])
                title = title_element.get_text(strip=True) if title_element else 'Title Not Found'

                location_element = job_soup.select_one(config['job_location_selector'])
                company_element = job_element.select_one(config['job_company_selector'])
                views_element = job_soup.select_one(config['job_views_selector'])
                applied_element = job_soup.select_one(config['job_apply_selector'])
                salary_element = job_soup.select_one(config['job_salary_selector'])

                location = location_element.get_text(strip=True).split('-')[0].strip() if location_element else 'Location Not Provided'
                company = company_element.get_text(strip=True) if company_element else 'Company Not Provided'
                views = views_element.get_text(strip=True) if views_element else 'Views Not Provided'
                applied = applied_element.get_text(strip=True) if applied_element else 'Applications Not Provided'
                salary_text = salary_element.get_text(strip=True) if salary_element else 'Salary Not Provided'

                salary = 'Salary Not Provided'
                if salary_text:
                    salary_numbers = re.findall(r'\b\d+\b', salary_text)
                    if salary_numbers and 'Gross' in salary_text:
                        salary_net = [str(int(round(int(num) * 0.6))) for num in salary_numbers]  # Calculate net salary
                        salary = '-'.join(salary_net) + '€/mon.Net'
                    elif salary_numbers and 'Net' in salary_text:
                        salary = '-'.join(salary_numbers) + '€/mon.Net'
                    else:
                        salary = salary_text

                job_details_log_message = f"{i}. Job Title: {title}, Location: {location}, Company: {company}, Views: {views}, Applied: {applied}, Salary: {salary}"
                job_details_logger.info(job_details_log_message)

            else:
                main_logger.error(f"Failed to fetch job details from {job_url}")
            time.sleep(config['delay'])
        else:
            main_logger.warning("No job link found in job element.")

main_logger.info("Scraper finished.")
