import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import pyautogui

def find_word_start(prev, new):    
    max_len = min(len(prev), len(new))
    
    for i in range(max_len, 0 , -1):
        if prev[-i:] == new[:i]:
            return new[i:]
        
    return new

def main():
    # Path to your Edge WebDriver executable
    PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe"
    service = Service(PATH)

    driver = webdriver.Edge(service=service)
    driver.get("https://monkeytype.com")

    # wait for website to load
    time.sleep(1)

    try:
        # Find and click the "Accept" button for cookies
        accept_button = driver.find_element(By.XPATH, "//button[contains(text(), 'accept all')]")
        accept_button.click()
        print("Cookies accepted.")
        time.sleep(1)  # Wait for the cookies acceptance to process
    except:
        print("No cookies notification found.")

    start_time = time.time()
    prev_word_string = " "

    while True:
        words = driver.find_elements(By.CLASS_NAME, "word")

        word_string = " ".join(word.text for word in words)
        word_string = find_word_start(prev_word_string, word_string)

        pyautogui.write(word_string, interval=0.01)
        
        prev_word_string = word_string
            
        # For 30 second type test
        if time.time() - start_time > 29:
            print("TYPING STOPPED")
            break
        
    time.sleep(1000)
    
if __name__ == "__main__":
    main()