import PyPDF2
import csv

from pathlib import Path
before_file  = Path("D:") / "Data Science" / "10.pdf"


# Open the PDF file
with open(before_file, 'rb') as f:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfFileReader(f)

    # Open a CSV file for writing
    with open('my_csv_file.csv', 'w') as csv_file:
        # Create a CSV writer object
        csv_writer = csv.writer(csv_file)

        # Get the number of pages in the PDF
        num_pages = pdf_reader.numPages

        # Loop through each page
        for i in range(num_pages):
            # Get the page object
            page = pdf_reader.getPage(i)

            # Extract the text from the page
            page_text = page.extractText()

            # Split the text into lines
            lines = page_text.split('\n')

            # Loop through each line
            for line in lines:
                # Strip leading and trailing whitespace from the line
                line = line.strip()

                # Find the position of the data you need
                data_position = line.index('my_data:')

                # Extract the data from the line
                my_data = line[data_position + len('my_data:'):]

                # Write the data to the CSV file
                csv_writer.writerow([my_data])
