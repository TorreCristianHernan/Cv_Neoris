import requests
from bs4 import BeautifulSoup
from docx import Document
from tkinter import Tk, Label, Entry, Button, filedialog
import os

# Function to handle button click event
def download_word(url):
    """
    Downloads the visible text content from a given URL and saves it as a Word document.

    Args:
        url (str): The URL to download the content from.

    Returns:
        None

    Raises:
        None
    """
    # Make a GET request to the URL
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Use BeautifulSoup to parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        print("soup",soup)
        # Create a new Word document
        document = Document()
        #####
        ####
        for element in soup.find_all(string=True):
            # Check if the text is inside a script or style tag
            if element.parent.name not in ['script', 'style']:
                # Add the text to the Word document
                document.add_paragraph(str(element))

        ####
        #####

        # Save the Word document
        file_path = filedialog.asksaveasfilename(defaultextension=".docx")
        document.save(file_path)
        print("The Word document has been created successfully.")
    else:
        print("Error accessing the page: Status", response.status_code)

# Create the Tkinter window
window = Tk()
window.title("Download Web Page as Word Document")

# Create a label and entry for the URL input
url_label = Label(window, text="URL:")
url_label.pack()
url_entry = Entry(window)
url_entry.pack()

# Create a button to initiate the download
download_button = Button(window, text="Download as Word", command=lambda: download_word(url_entry.get()))
download_button.pack()

# Run the Tkinter event loop
window.mainloop()
