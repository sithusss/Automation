# README: Selenium Login Automation Script

Prerequisites
1. Visual Studio Code (VS Code)
   Ensure you have VS Code installed on your system. You can use command prompt also

2. Python
   Install Python (version 3.8 or later is recommended).I used python 3.10.10

3. Google Chrome
   Make sure Google Chrome is installed on your system (I use ChromeDriver version 132 for compatibility).

4. ChromeDriver
   Download ChromeDriver version 132 from the official website:
     [https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/)
   Add the downloaded ChromeDriver executable to your system's PATH or specify its location in the script.I added this file to my executable file location

5. Selenium
   Install Selenium in a virtual environment as described in the setup instructions below.


Setting Up the Environment

Step 1: Create the Script
   Create the python script file (`automationtesting.py`) to your desired directory.

Step 2: Set Up a Virtual Environment
1. Open the terminal in VS Code.
2. Navigate to the folder where the script is located.
3. Create a virtual environment using the following command:
   ```
   python -m venv venv
   ```
4. Activate the virtual environment:
   
     ```
     venv\Scripts\activate
     ```
  

Step 3: Install Dependencies
1. Install Selenium in the virtual environment:
   ```
   pip install selenium
   ```

Step 4: Configure ChromeDriver
1. Ensure ChromeDriver version 132 is downloaded.
2. Add its executable to your system's PATH.
   - Alternatively, place ChromeDriver in the same directory as the script and specify its path in the script like:
     ```python
     driver = webdriver.Chrome(executable_path="path_to_chromedriver")
     ```

How to Execute the Script

1. Open the terminal in VS Code.
2. Navigate to the folder containing the script and activate the virtual environment (if not already activated).
3. Run the script using the following command:
   ```bash
   python automationtesting.py
   ```
4. The script will:
   Perform login tests for both valid and invalid credentials.
   Save screenshots of the results in a folder named `test_results` within the script's directory.


Notes
Replace `"validUsername"` and `"ValidPassword123"` in the script with actual valid credentials for `https://demoqa.com/login`. 
	actual credentials - username: testuser, password: Test@123
The script is configured to work with Google Chrome and ChromeDriver version 132. Ensure the browser and driver versions match.


