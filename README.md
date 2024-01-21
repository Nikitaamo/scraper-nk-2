# Web Scraper for Job Listings

## Introduction

This project hosts a Python-based web scraper designed to extract job listings from various websites. Set within a virtual environment and bolstered by utility functions, the scraper can be easily customized through a configuration file.

## Project Structure

- `scraper2/scraper.py`: The main scraper script.
- `scraper2/utils.py`: Utility functions that assist the scraper.
- `config.json`: The configuration file that sets parameters for the scraper.
- `config.example.json`: An example that shows the setup for `config.json`.
- `venv/`: A virtual environment directory for the project's dependencies.
- `requirements.txt`: A list of necessary Python packages for running the scraper.
- `logs/`: Directory where the scraper's operation logs are saved.

## Getting Started

### Prerequisites

- Python 3.x
- Pip (Python package manager)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/scraper-nk-2.git
   ```

2. **Set Up the Virtual Environment**

   In the project directory, create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

   Then activate it:

   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`

3. **Install Dependencies**

   With the virtual environment active:

   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. Copy `config.example.json` to a new file named `config.json`.
2. Edit `config.json` to set the scraper parameters.

### Running the Scraper

Execute the scraper script with:

```bash
python scraper2/scraper.py
```

## Logging

The scraper is equipped with a comprehensive logging system that records two types of logs:

### General Operations (`main.log`)

- Initialization of the scraper and logging system.
- Fetching the search results page and success or failure of this action.
- Number of job listings found in the search results.
- Status messages as each job detail page is fetched.
- Errors and warnings, such as failure to fetch job details or missing job links.

### Job Details (`job_details.log`)

For every job listing processed, the following details are logged:

- Sequential number of the job listing.
- Job Title: Extracted text of the job title.
- Location: Cleaned text showing job location.
- Company: The company name associated with the job.
- Views: Number of views for the job listing.
- Applied: The count of applications submitted.
- Salary: Calculated net salary from the provided gross salary, if applicable.

An example log entry would be:

```text
1. Job Title: Senior Data Analyst, Location: Berlin, Company: DataCorp, Views: 1500, Applied: 120, Salary: 3000€-5000€/mon.Net
```

## Contributing

Feel free to fork the project, make changes, and submit a pull request if you have improvements or fixes.

## License

This project is in the public domain.

## Disclaimer

This scraper is for educational purposes only. 