from selenium import webdriver
from twilio.rest import Client
import time

def get_driver():
# Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("https://www.amazon.ca/Philips-Automatic-Espresso-EP3241-74/dp/B0B7P81K6S?ref_=Oct_DLandingS_D_fb5eba4e_0")
  return driver

def main():
  driver = get_driver()
  # xpath was taken in Chrome by right-clicking
  # over <span aria-hidden="true">$15.12</span>
  # and then Copy -> xpath
  element = driver.find_element(by="xpath", value='//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[1]/span[2]')
  # print('element', element.text)
  return element.text

def clean_price(raw):
  return float(raw.replace('$', ''))

account_sid = 'AC2c8f548726a631d1c284c6dbf2416af2'
auth_token = 'd0ec70ee1d61bb5cd610edf87567c35f'
client = Client(account_sid, auth_token)

raw_price = main()
price = clean_price(raw_price)

prices = [price]


while True:
  time.sleep(5)
  raw_price = main()
  price = clean_price(raw_price)
  prices.append(price)
  print(prices)

  if prices[-1] < prices[-2]:
    message = client.messages.create(
                  body=f"The price has just dropped to ${price}. Hurry up!",
                  from_='+00000',
                  to='+00000'
                  )
  del prices[-2]
  


