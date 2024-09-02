# Trendyol Automation Script

## Overview

This Python script uses Selenium WebDriver to automate the browsing and interaction with the Trendyol website. It performs the following tasks:

1. **Setup WebDriver**: Configures the Chrome WebDriver for Selenium.
2. **Close Pop-Up**: Closes the initial pop-up that appears on the Trendyol homepage.
3. **Navigate to Best Sellers**: Clicks on the "Best Sellers" link to view popular products.
4. **Retrieve Products**: Extracts the list of products displayed on the Best Sellers page.
5. **Extract Product Information**: Retrieves the title and price of each product.
6. **Add to Cart**: Adds each product to the cart, including handling discount and size selection if applicable.
7. **Open Cart**: Navigates to the shopping cart page to review the added items.

## Features

- **Pop-Up Handling**: Automatically closes initial pop-ups for smoother browsing.
- **Dynamic Product Handling**: Retrieves product details and handles discount and size selection dynamically.
- **Cart Management**: Adds products to the cart and navigates to the cart page.

## Prerequisites

- Python 3.x
- Chrome WebDriver (compatible with your installed version of Google Chrome)
- Selenium library

## Output

Product 1 title: Trendyol Collection T-Shirt, Discounted Price: 29.99 TL
Product has been added to the cart.
Product 2 title: Trendyol Sports Shoes, Discounted Price: 79.99 TL
Product has been added to the cart.
Product 3 title: Trendyol Leather Jacket, 149.99 TL
Product has been added to the cart.
Product 4 title: Trendyol Sunglasses, Discounted Price: 19.99 TL
Product has been added to the cart.
Product 5 title: Trendyol Wrist Watch, Discounted Price: 89.99 TL
Product has been added to the cart.

The shopping cart has been opened.
