import pytest
from playwright.sync_api import Page, expect

def test_product_page(sauce_page:Page):
    logo = sauce_page.locator("div.app_logo")
    expect(logo.get_by_text("Swag Labs")).to_be_visible()
    sauce_page.wait_for_timeout(2000)

#1. Count total number of cart items
    cart = sauce_page.locator("div[data-test='inventory-item']")
    expect(cart).to_have_count(6)
    
    cart_count = cart.count()
    print("Number of items:", cart_count)
    sauce_page.wait_for_timeout(2000)
    
#2 Get all titles of each items
    cart_title = sauce_page.locator("*[data-test='inventory-item-name']")
    sauce_page.wait_for_timeout(2000)
    # cart_title.all_inner_texts()
    print("Cart title items:", cart_title.all_text_contents())
    expect(cart_title).to_have_text(['Sauce Labs Backpack', 'Sauce Labs Bike Light',
                                     'Sauce Labs Bolt T-Shirt', 'Sauce Labs Fleece Jacket',
                                     'Sauce Labs Onesie', 'Test.allTheThings() T-Shirt (Red)'])
    
#3 Click Add to Cart of specific cart item
    item = sauce_page.locator("[data-test='inventory-item']").filter(
    has_text="Sauce Labs Backpack")
    item.get_by_role("button", name="Add to cart").click()
    sauce_page.wait_for_timeout(2000)
    
#4 Validate the button changed
    expect(item.get_by_role("button", name="Remove")).to_be_visible()

#5 Validate cart badge
    expect(sauce_page.locator("[data-test='shopping-cart-badge']")).to_have_text("1")
    sauce_page.wait_for_timeout(2000)
    
# 6. Validate added item is in "Your Cart" page
    # Go to Your Cart page
    your_cart = sauce_page.locator("#shopping_cart_container")
    your_cart.click()

    # Validate Your Cart title
    your_cart_title = sauce_page.locator("[data-test='title']")
    expect(your_cart_title).to_be_visible()
    expect(your_cart_title).to_have_text("Your Cart")

    # Check that Sauce Labs Backpack is in the cart
    cart_item = sauce_page.locator("[data-test='inventory-item']").filter(has_text="Sauce Labs Backpack")

    expect(cart_item).to_be_visible()
    expect(cart_item).to_contain_text("Sauce Labs Backpack")
    sauce_page.wait_for_timeout(2000)
    
    
    

    
    