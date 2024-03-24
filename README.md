This script utilizes Selenium to automate web browsing and extract the price of a product on Amazon. It continuously checks the price of the specified product and compares it to the previous price. If the price drops, it sends an SMS notification using Twilio.

Selenium: Install Selenium using pip:

``pip install selenium``

Chrome WebDriver: Download the Chrome WebDriver and ensure it's in your PATH.

Twilio Setup:

- Create a Twilio account and obtain your Account SID, Auth Token, and Twilio phone number.
- Update the account_sid, auth_token, from_, and to variables in the script with your Twilio credentials and recipient's phone number.

Amazon Product URL:

- Update the get_driver function with the URL of the Amazon product you want to track.

Run the script:

``python amazon_price_tracker.py``
