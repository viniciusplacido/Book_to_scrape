# Web Scraping: Books to Scrape

-->Description:
These codes were created as part of project 2 of Python Developer course from Open Classroom. The goal was to create a code (Scrape_books.py) to extract information from the website https://books.toscrape.com/ in a web scraping process with Python.

Firstly, I wrote a code which visits this page and extracts the following information: product_page_url, universal_ product_code (upc), title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url.

Secondly, I imported all the information collected to a separate CSV for each book category.

Finally, as an extension of the work done, I wrote a new code (Scrape_Books_Images.py) to download and save all the images of the books available on the site.



-->Requirements:
beautifulsoup4==4.9.3
pandas2==0.0.0
requests==2.25.1
lxml==4.6.2



-->Installation:
Python:: You can download Python using the following link: https://www.python.org/downloads/

PIP:: Package management system used to install and manage software packages written in Python. It stands for “preferred installer program” or “Pip Installs Packages”. PIP is automatically installed with Python 2.7.9+ and Python 3.4+. Check if PIP is already installed before you install PIP on Windows, check if PIP is already installed. Type in the following command at the command prompt: pip help
If PIP responds, then PIP is installed. Otherwise, there will be an error saying the program could not be found. To install PIP (windows) type in the following: python get-pip.py

Requirements files:: Instead of installing packages individually, pip allows you to declare all dependencies in a Requirements File. To install all of the packages in this file using the -r flag: pip install -r requirements.txt



-->Virtual environment:
Before you can start installing or using packages in your virtual environment you’ll need to activate it. Activating a virtual environment will put the virtual environment-specific python and pip executables into your shell’s PATH.

On macOS and Linux: source env/bin/activate
On Windows: .\env\Scripts\activate

As long as your virtual environment is activated pip will install packages into that specific environment and you’ll be able to import and use packages in your Python application. If you want to switch projects or otherwise leave your virtual environment, simply run: deactivate







