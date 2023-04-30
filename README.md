# Text-Extraction
International Collaboration Fund PLUS (ICF PLUS) Application Form Text Extractor

## Table of Contents
#### Introduction
#### Features
#### Getting Started
#### Usage
#### Screenshots
#### License

## Introduction
Welcome to my Desktop Application, a tool designed to simplify the process of extracting information from PDF and DOCX files. With this application, you can quickly and easily upload files and extract important data, such as names, addresses, and phone numbers. The application is built with a user-friendly interface, making it easy to navigate for users of all technical backgrounds. It also includes a database management feature, allowing you to store and manage the extracted data with ease. Whether you're a business owner, researcher, or student, this application can save you time and effort by automating the tedious task of manual data extraction. Try it out today and experience the power of streamlined document processing!

This application is designed to make it easy for users to extract text content from Docx and PDF files and store the information in a PostgreSQL database. The program provides a graphical user interface for users to interact with and drag and drop files to extract data.

Once the data is extracted, users can perform CRUD operations on the data stored in the database. The application automatically validates user input to ensure it meets the required format and constraints. Users can also export data from the database to a CSV file for further analysis or sharing.

Overall, this application provides an easy and efficient way to manage text content from Docx and PDF files and store it in a centralized database for easy access and management.

## Features
1. Extracts text from Docx and PDF files: The application can read Docx and PDF files and extract their text content.
2. Stores data in a database: The extracted data is stored in a PostgreSQL database for easy access and management.
3. Performs CRUD operations: The application allows users to create, read, update, and delete data in the database.
4. GUI for user interaction: The application provides an easy-to-use graphical user interface for users to interact with the program.
5. Drag and drop files: Users can simply drag and drop files into the application to extract their text content and store the data in the database.
6. Automatic data validation: The application automatically validates the data entered by users to ensure it meets the required format and constraints.
7. Export data to CSV: Users can export the data in the database to a CSV file for further analysis or sharing.

## Getting Started
1.  Clone the repository to your local machine.
2.  Make sure you have Python 3.x installed on your system.
3.  Install the required packages mentioned in the requirements.txt file by running pip install -r requirements.txt command in your terminal.
4.  Open the database.ini file and configure it according to your database settings.
5.  Run the DatabaseManager.py file to create the necessary tables in your database.
6.  Run the DesktopApplication.py file to launch the application.
7.  Select the desired option from the menu bar to either read a docx/pdf file or to perform CRUD operations on the database.
8.  To read a docx/pdf file, click on the corresponding button, select the file, and the text or information from the file will be extracted and stored in the database.
9.  To perform CRUD operations on the database, select the appropriate option from the menu bar and enter the necessary details.
10. Enjoy using the application!
Note: Make sure to have a working internet connection, as the application uses various libraries that require an active internet connection to function properly.

## Usage
1. Make sure that Python 3.6 or higher is installed on your system. You can check your current Python version by running the command python --version in your terminal or command prompt.
2. Clone or download the repository to your local machine.
3. Open a terminal or command prompt and navigate to the root directory of the project.
4. Run the following command to install the required Python libraries:
    pip install -r requirements.txt
5. Next, you need to set up the database by creating the required tables. Run the following command to create the tables:
    python DatabaseManager.py
6. Once the database is set up, you can launch the GUI by running the following command:
    python DesktopApplication.py
7. The GUI should launch and you can use it to extract text or information from docx or pdf files, and store the data in the database. You can also perform CRUD operations on the data in the database using the GUI.
8. To exit the application, click on the "Exit" button in the main menu or press escape.

## Screenshots
![none](https://drive.google.com/file/d/1NreFOcLMlwZfp4wYdPUjOSEniphCl6eX/view?usp=sharing)

## License
Copyright 2023 mahd0x8

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
