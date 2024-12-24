<h1 align="center" id="title">Website Downloader Project</h1>

<p id="description">This project allows users to download an entire website for offline viewing. It uses Python's requests library to fetch web pages and the BeautifulSoup library to parse HTML content. The downloaded website includes the main HTML page as well as associated CSS and JavaScript files.</p>

  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Download Full Website: The script downloads the website's HTML CSS and JavaScript resources saving them to a specified local directory.
*   Supports Relative URLs: It handles relative URLs for CSS JS and other resources ensuring that the website structure remains intact when downloaded.
*   Customizable Output Directory: Users can specify a directory where the website will be saved.
*   User-Agent Header: To bypass basic bot protection the script includes a custom User-Agent header that mimics a common web browser.

<h2>🛠️ Installation Steps:</h2>

<p>1. How to Run the Project</p>

```
To run the project easily follow these steps:
```

<p>2. Using</p>

```
setup.bat Purpose: This file installs the required Python libraries (requests and beautifulsoup4) for the project.
```

<p>3. Steps to Use:</p>

```
Download the project and ensure that you have Python 3.x installed. Double-click the setup.bat file to automatically install the required libraries.
```

  
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Save HTML: The HTML content is saved as an index.html file in the specified directory.
*   Resource Downloading: The script then downloads the necessary resources (CSS files JavaScript files) and saves them locally.
*   HTML Parsing: Using BeautifulSoup the HTML is parsed and relevant resources (CSS JS) are extracted.
*   Website Fetching: The script sends an HTTP request to the website and retrieves the HTML content.
*   User Input: The user provides the URL of the website they want to download.
