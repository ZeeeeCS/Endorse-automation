from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import random
webdriver_service = Service(ChromeDriverManager().install())

# Set up ChromeOptions
options = webdriver.ChromeOptions()

options.add_argument("--disable-gpu")
options.add_argument("--disable-software-rasterizer")
options.add_argument("--disable-features=WebRTC")
options.add_argument("--use-angle=gl")

# Initialize the WebDriver
driver = webdriver.Chrome(service=webdriver_service, options=options)


def random_delay():
    time.sleep(random.uniform(1, 3))  # Random delay between 1 and 3 seconds

def login_linkedin(email, password):
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)
    driver.find_element(By.ID, "username").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)

# Open LinkedIn login page
login_linkedin("habadtmam@gmail.com", "990990zx")

# Wait for user input (manually login)
time.sleep(5)  # Give enough time to manually log in or use automation to log in

# List of profiles to visit (replace with actual LinkedIn profile URLs)
profiles = [
    "https://www.linkedin.com/in/mahmoud-attia-ibrahime-6b5720247/details/skills/?detailScreenTabIndex=0",
    "https://www.linkedin.com/in/mohammedemad-9951m/details/skills/",
    "https://www.linkedin.com/in/sayed-salama-843492284/details/skills/"
]

def endorse_skill(profile):
    driver.get(profile)
    random_delay()
    
    try:
        # Wait for the "Endorse" button to be present
        endorse_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'artdeco-button') and contains(.//span, 'Endorse')]"))
        )
        
        # Scroll the button into view
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", endorse_button)
        random_delay()
        
        # Wait for the button to be clickable
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(endorse_button))
        
        # Click the button
        endorse_button.click()
        print("Skill endorsed!")
    except Exception as e:
        print("Could not find or click the endorse button:", e)

for profile in profiles:
    endorse_skill(profile)

# Close the browser
driver.quit()