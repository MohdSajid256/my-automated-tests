# Automated Login Tests  

This repository contains automated tests for the login functionality of an application, implemented using Python and Selenium. 
All test scenarios are included within a single Python file, managed directly on the main branch.  

## Test Scenarios Covered  

The automated tests cover the following scenarios:  

*   Successful login with correct credentials.  
*   Failed login with incorrect credentials.  
*   Login attempt with empty fields.  
*   Verification of error messages for invalid inputs.  
*   Confirmation that a successful login redirects to a dashboard page.  

## Setup and Running the Tests  

1.  **Clone the repository:**  

    ```bash  
    git clone <repository-url>  
    cd <repository-name>  
    ```  

2.  **Install dependencies:**  

    Make sure you have Python installed. Then, install the required libraries using pip:  

    ```bash  
    pip install selenium  
    ```  

    You will also need a web driver for the browser you want to use (e.g., ChromeDriver for Chrome, GeckoDriver for Firefox).
     Download the appropriate driver and ensure it's in your system's PATH or provide the path to the driver in your test script.  

4.  **Run the tests:**  

    To run all the tests in the single Python file, execute the following command in your terminal:  

    ```bash  
    python your_test_file_name.py  
    ```  

    Replace `your_test_file_name.py` with the actual name of your Python file containing the tests.  

## Version Control  

This project utilizes Git for version control. Development and implementation of all test scenarios were conducted directly within a single Python file on the main branch.  

*   The main branch serves as the primary branch for all development.  
*   Commits were made directly to the main branch as the tests were developed and updated.  

Meaningful commit messages were used throughout the development process to provide context and clarity for each change made to the test file.  

