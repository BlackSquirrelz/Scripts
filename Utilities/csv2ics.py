import csv
import sys
from datetime import datetime
from icalendar import Event, Calendar

def convert_csv_to_ics(input_csv, output_ics):
    cal = Calendar()

    # Read and process the CSV file
    with open(input_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            #print(row)
            event_title = row['eventTitle']
            start_date = row['startDate']
            start_time = row['startTime']
            end_date = row['endDate']
            end_time = row['endTime']
            location = row['location']
            description = row['description']
            # Combine date and time strings
            start_datetime = datetime.strptime(f"{start_date}T{start_time}:00", "%Y-%m-%dT%H:%M:%S")
            end_datetime = datetime.strptime(f"{end_date}T{end_time}:00", "%Y-%m-%dT%H:%M:%S")

            #print(f"{start_datetime} - {end_datetime}")

            # Create a new iCalendar event
            event = Event()
            event.add('summary', event_title)
            event.add('dtstart', start_datetime)
            event.add('dtend', end_datetime)
            event.add('location', location)
            event.add('description', description)

            # Add the event to the calendar
            cal.add_component(event)
            print(event)

    # Write the iCalendar data to the output file
    with open(output_ics, 'wb') as f:
        f.write(cal.to_ical())

    print(f'CSV data from {input_csv} has been converted to {output_ics}')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input.csv output.ics")
        sys.exit(1)

    input_csv = sys.argv[1]
    output_ics = sys.argv[2]

    convert_csv_to_ics(input_csv, output_ics)
