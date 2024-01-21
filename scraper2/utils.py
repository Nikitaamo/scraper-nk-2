import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Request failed: {e}")

def parse_html(html, selector):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.select(selector)

def get_job_details(url, config):
    html = get_html(url)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select_one(config['job_title_selector']).text.strip()
        location_company = soup.select_one(config['job_location_selector']).text.strip()
        views = soup.select_one(config['job_views_selector']).text.strip()
        try:
            applied = soup.select(config['job_apply_selector'])[1].text.strip()
        except IndexError:
            applied = "nenurodyta"
        return title, location_company, views, applied
    return None
