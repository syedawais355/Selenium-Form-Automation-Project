This project is a demonstration of web automation using Python and the Selenium library. 
The script navigates to a practice form webpage and automatically fills in various fields, 
including text inputs, radio buttons, checkboxes, and dropdown menus, before submitting the form.

Features:

-   Automated Data Entry: Fills out a complete web form with predefined data.
-   Handles Diverse Form Elements: Interacts with a variety of HTML form elements.
-   Alert Handling: Includes a try-except block to manage and accept JavaScript alerts.
-   Modular Code: A reusable `fill` function is used for interacting with web elements.

Getting Started:
Follow these instructions to get a copy of the project up and running on your local machine.

Prerequisites:

You'll need to have the following installed:
*   Python 3.x
*   Google Chrome (or another web browser of your choice, but the script is currently set up for Chrome)
*   The corresponding WebDriver for your browser. For Chrome, you can download it from the [ChromeDriver website](https://chromedriver.chromium.org/downloads).

Installation:

1.  Clone the repository:
    git clone https://github.com/syedawais355/Selenium-Form-Automation-Project.git
    cd Selenium-Form-Automation-Project
 

2.  It's highly recommended to use a virtual environment:
    python -m venv venv
    source venv/bin/activate
    make sure ( On Windows, use venv\Scripts\activate )
    

3.  Install the necessary packages:
    pip install -r requirements.txt
    

Usage:
To run the script, execute the `main.py` file from your terminal:

python main.py

The script will launch a new browser window, perform the automated form filling, and then close the browser after a short delay.

Output  :



https://github.com/user-attachments/assets/dc448979-2bb9-473c-bfd3-471689d57a55



Contributing:


Contributions are welcome! If you have any suggestions or improvements, feel free to fork the repository and open a pull request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
