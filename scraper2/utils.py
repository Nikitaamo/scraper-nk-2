import requests
from bs4 import BeautifulSoup
import logging

def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        logging.error(f"Request failed for {url}: {e}")
        return None

def parse_html(html, selector):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        return soup.select(selector)
    except Exception as e:
        logging.error(f"HTML parsing failed: {e}")
        return []

def get_job_details(url, config):
    html = get_html(url)
    if html:
        try:
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.select_one(config['job_title_selector']).text.strip()
            location_company = soup.select_one(config['job_location_selector']).text.strip()
            views = soup.select_one(config['job_views_selector']).text.strip()
            try:
                applied = soup.select(config['job_apply_selector'])[1].text.strip()
            except IndexError:
                applied = "nenurodyta"
            return title, location_company, views, applied
        except Exception as e:
            logging.error(f"Error getting job details from {url}: {e}")
            return None
    else:
        return None
