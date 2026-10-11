# Writing two custom functions first

import csv

def celsius_converter(f_temp):
    """Converts Fahrenheit to Celsius and rounds to two decimal points"""
    fahrenheit = float(f_temp)
    celsius = (fahrenheit - 32) * 5 / 9
    return round(celsius, 2) # round() is used to round the value

def parse_and_clean(line):
    """Returns cleaned fields or None if the line is not valid"""
    fields = [field.strip() for field in line.split("|")] # splits the string by | delimiter

    # Checking if the line has 5 fields (columns)
    if len(fields) != 5:
        return None

    timestamp, station_id, temperature, humidity, status = fields

    # Checking whether no field is empty
    if not all(fields): # non-empty string is considered true
        return None

    # The sensors might be not active (e.g. "warning")
    if status != "ACTIVE": # means if status is not equal to
        return None

    # Now we need to make sure that temp and humidity are numbers

    try: # checks whether the values can be converted into floats
        float(temperature)
        float(humidity)
    except ValueError: # if data might contain words instead of numbers
        return None

    return fields # returns cleaned fields if the line is valid


# Now we'll be running the functions

def main():
    corrupted_count = 0
    valid_count = 0 # Kepping count for both valid and corrupted counts

    # opening input file for reading and output file for writing
    with open("environmental_raw.txt", "r", encoding="utf-8") as infile, \
         open("clean_weather.csv", "w", newline="", encoding="utf-8") as outfile:

        writer = csv.writer(outfile) # writing fields to the output file

        # Adding a header
        writer.writerow(["Timestamp", "StationID", "Temp(C)", "Humidity(%)", "Sensor_Status"])

        # Reading the input file - one line at a time
        for line_number, line in enumerate(infile):
            if line_number == 0: # skipping the header row (0)
                continue

            # Counting and skipping blank lines
            if not line.strip():
                corrupted_count += 1 # adding one every time such line occurs
                continue

            # Also checking if the current line is valid or not
            cleaned = parse_and_clean(line)

            if cleaned is None:
                corrupted_count += 1 # adding one if it occurs
                continue

            # We need to separate the fields from the valid record
            timestamp, station_id, temperature, humidity, status = cleaned

            # Converting Fahrenheit to C:
            celsius = celsius_converter(temperature) # using the function defined above

            # Now writing the cleaned record to the output csv
            writer.writerow([timestamp, station_id, celsius, humidity, status])

            valid_count += 1 # adding one each time a valid line occurs

    # And finally, printing a summary
    print(f"Valid records written: {valid_count}")
    print(f"Corrupted records that were skipped: {corrupted_count}")

if __name__ == "__main__": # makes the program run main() when script is executed directly
    main()