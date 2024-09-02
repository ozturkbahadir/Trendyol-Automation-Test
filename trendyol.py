from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def setup_driver(executable_path):
    """Sets up the Chrome WebDriver."""
    service = Service(executable_path=executable_path)
    driver = webdriver.Chrome(service=service)
    return driver

def close_popup(driver, timeout=10):
    """Closes the initial pop-up on the Trendyol website."""
    try:
        pop_up_close_button = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.modal-close"))
        )
        pop_up_close_button.click()
    except Exception as e:
        print(f"Failed to close pop-up: {e}")

def click_best_seller_link(driver, timeout=10):
    """Clicks on the 'Best Sellers' link."""
    try:
        best_seller_link = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/cok-satanlar?type=bestSeller&webGenderId=1']"))
        )
        best_seller_link.click()
    except Exception as e:
        print(f"Failed to click on the 'Best Sellers' link: {e}")

def get_products(driver, timeout=10):
    """Retrieves all product elements from the product listing page."""
    try:
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "product-listing-container"))
        )
        products = driver.find_elements(By.CSS_SELECTOR, ".product-card a")
        return products
    except Exception as e:
        print(f"Failed to get products: {e}")
        return []

def get_product_info(driver, timeout=10):
    """Retrieves the product title and price information."""
    try:
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        )
        product_title = driver.find_element(By.TAG_NAME, "h1").text

        try:
            discount_price = driver.find_element(By.CSS_SELECTOR, ".featured-prices .prc-dsc").text
            return product_title, discount_price, True
        except:
            regular_price = driver.find_element(By.CSS_SELECTOR, ".prc-dsc").text
            return product_title, regular_price, False
    except Exception as e:
        print(f"Failed to get product info: {e}")
        return None, None, False

def add_to_cart(driver, timeout=10):
    """Adds the current product to the cart."""
    try:
        add_to_cart_button = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.add-to-basket"))
        )
        add_to_cart_button.click()
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.add-to-basket-button-text-success"))
        )
        print("Product has been added to the cart.")
        return True
    except Exception as e:
        print(f"Failed to add product to cart: {e}")
        return False

def select_size_and_add_to_cart(driver, timeout=10):
    """Selects the size and adds the product to the cart."""
    try:
        wait = WebDriverWait(driver, timeout)
        select_size = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='sliderList']//div[@class='sp-itm' and @title='Beden seçmek için tıklayınız']"))
        )
        select_size.click()
        
        # Try adding to cart again after selecting size
        add_to_cart_button = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.add-to-basket"))
        )
        add_to_cart_button.click()
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.add-to-basket-button-text-success"))
        )
        print("Product has been added to the cart after selecting size.")
        return True
    except Exception as e:
        print(f"Failed to select size and add product to cart: {e}")
        return False

def open_cart(driver, timeout=10):
    """Opens the shopping cart page."""
    try:
        # Scroll to the top of the page
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)
        
        cart_link = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/sepet']"))
        )
        cart_link.click()
        time.sleep(5)  # Time for inspecting the cart
    except Exception as e:
        print(f"Failed to open cart: {e}")

def main():
    driver = setup_driver("chromedriver.exe")
    driver.get("https://www.trendyol.com/")

    close_popup(driver)
    click_best_seller_link(driver)

    products = get_products(driver)
    if not products:
        print("No products found.")
        driver.quit()
        return

    try:
        for i in range(len(products)):
            products = get_products(driver)  # Re-fetch to avoid stale element reference
            if not products:
                break

            products[i].click()
            product_title, product_price, is_discounted = get_product_info(driver)

            if product_title and product_price:
                if is_discounted:
                    print(f"Product {i + 1} title: {product_title}, Discounted Price: {product_price}")
                    if not add_to_cart(driver):
                        select_size_and_add_to_cart(driver)
                else:
                    print(f"Product {i + 1} title: {product_title}, {product_price}")
            
            driver.back()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "product-listing-container"))
            )

        open_cart(driver)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
