# Homework 6: Weather Log Cleaning

## Project Description
This project cleans corrupted environmental weather station data using Python.

The script reads raw weather data, skips corrupted records and records from inactive sensors, converts temperatures from Fahrenheit to Celsius, and saves the cleaned data to a CSV file.

## Files
- `clean_logs.py` — Python script for cleaning the weather data.
- `environment.yml` — Conda environment configuration.
- `.gitignore` — Excludes the raw input and generated output files from Git.

## How to Run
1. Activate the Conda environment.
2. Place `environmental_raw.txt` in the project folder.
3. Run the script:

   ```bash
   python clean_logs.py
   ```

4. The cleaned data will be saved as `clean_weather.csv`.

## Output
The script prints the number of valid records written and the number of corrupted records skipped.