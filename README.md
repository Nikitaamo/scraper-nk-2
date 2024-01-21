Based on the structure provided in the screenshot, here's an updated `README.md` that includes installation and setup instructions suitable for beginners:

```markdown
# Web Scraper for Job Listings

## Introduction

This project contains a Python-based web scraper that extracts job listings from websites. It's set up with a virtual environment, includes utility functions, and can be customized with a configuration file.

## Project Structure

- `scraper.py`: The main scraper script.
- `utils.py`: Utility functions used by the scraper.
- `config.json`: Configuration file to set up scraper parameters.
- `config.example.json`: An example configuration file.
- `scraper.py`: The entry point for running the scraper.
- `requirements.txt`: A list of Python packages required to run the scraper.
- `venv/`: A virtual environment directory for the project's dependencies.

## Getting Started

### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Installation

1. **Clone the Repository**

   If you have `git` installed, you can clone the repository using the following command:

   ```bash
   git clone https://github.com/Nikitaamo/scraper-nk-2.git
   ```

   Replace `https://github.com/Nikitaamo/scraper-nk-2.git` with the URL of the Git repository.

2. **Set Up the Virtual Environment**

   Navigate to the project directory and create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

   Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**

   With the virtual environment activated, install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. Make a copy of `config.example.json` and rename it to `config.json`.
2. Edit `config.json` with your desired parameters, such as `search_url`, `job_list_selector`, etc.

### Running the Scraper

1. With the virtual environment activated, run the scraper using:

   ```bash
   python scraper2/scraper.py
   ```

2. Check the `logs` directory for output and any errors encountered during the scraping process.

## Contributing

Feel free to fork the project, make changes, and submit a pull request if you have improvements or fixes.

## License

Specify your license or state that the project is in the public domain.

## Disclaimer

This scraper is for educational purposes only. 