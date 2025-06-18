# Weather Data Aggregator

## Objectives

Build a Python-based CLI tool to fetch weather data from two different APIs, normalize it, and save it to CSV and JSON. Then, containerize the entire solution.

## Setup

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/dvela-pan/coding-test.git

cd coding-test
```

### 2. Create a `.env` File

Copy the `.env.example` file to `.env`:

```bash
cp .env.example .env
```

Edit the `.env` file and replace `your_openweather_api_key` and `your_weatherapi_api_key` with your actual API keys.

### 3. Install Dependencies

Ensure you have Python 3.8+ installed. Then, install the required dependencies:

```bash
# Create a virtual environment
python3 -m venv .venv

# Enable the virtual environment
source .venv/bin/activate

# Install dependencies in the virtual environment
pip install -r requirements.txt
```

## Code Structure

- **`main.py`**: The entry point of the application. It orchestrates fetching, normalizing, and saving weather data.
- **`weather_fetcher.py`**: Contains asynchronous functions to fetch weather data from OpenWeather and WeatherAPI.
- **`data_transformer.py`**: Normalizes the API responses into a common format.
- **`file_writer.py`**: Handles saving the normalized data to CSV and JSON files.
- **`config.py`**: Loads API keys from environment variables using `dotenv`.

## Notes

- Ensure your `.env` file is not committed to version control. It is already included in `.gitignore`.
- The application fetches weather data for the following cities by default: London, New York, Tokyo, São Paulo, and Johannesburg. You can modify the `CITIES` list in `main.py` to include other cities.


## GET started 


```bash
sudo docker build -t weather-app .
docker run --env-file .env  weather-app --json --csv
```