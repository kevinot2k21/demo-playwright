import pytest
from playwright.sync_api import Page, expect

def test_cart_page(sauce_page:Page):
    logo = sauce_page.locator("div.app_logo")
    expect(logo.get_by_text("Swag Labs")).to_be_visible()
    sauce_page.wait_for_timeout(2000)
    
#1 Add items to cart
    item1 = sauce_page.locator("[data-test='inventory-item']").filter(
    has_text="Sauce Labs Backpack")
    item1.get_by_role("button", name="Add to cart").click()
    sauce_page.wait_for_timeout(2000)
    item2 = sauce_page.locator("[data-test='inventory-item']").filter(
    has_text="Sauce Labs Bike Light")
    item2.get_by_role("button", name="Add to cart").click()
    sauce_page.wait_for_timeout(2000)
    
#2 Validate cart badge
    expect(sauce_page.locator("[data-test='shopping-cart-badge']")).to_have_text("2")
    sauce_page.wait_for_timeout(2000)
    
#3 Go to Your Cart page
    your_cart = sauce_page.locator("#shopping_cart_container")
    your_cart.click()

#4 Validate Your Cart title
    your_cart_title = sauce_page.locator("[data-test='title']")
    expect(your_cart_title).to_be_visible()
    expect(your_cart_title).to_have_text("Your Cart")

#5 Check that Sauce Labs Backpack is in the cart
    cart_items = sauce_page.locator("[data-test='inventory-item']").filter(has_text="Sauce Labs Backpack" and "Sauce Labs Bike Light")
    expect(cart_items).to_be_visible()
    expect(cart_items).to_contain_text("Sauce Labs Backpack" and "Sauce Labs Bike Light")
    #Verify the Quantity == 1
    expect(sauce_page.locator('[data-test="item-quantity"]').first).to_have_text("1")
    sauce_page.wait_for_timeout(2000)

#Click Remove Item
    remove_item = sauce_page.locator('[data-test="remove-sauce-labs-backpack"]').click()
    expect(sauce_page.locator('[data-test="remove-sauce-labs-backpack"]')).not_to_be_visible()
    

#6 Back into Product item
    continue_shopbtn = sauce_page.locator("[data-test='continue-shopping']")
    expect(continue_shopbtn).to_be_visible()
    continue_shopbtn.click()
    #Product page
    product_title = sauce_page.locator("[data-test='title']")
    expect(product_title).to_be_visible()
    expect(product_title).to_have_text("Products")
    sauce_page.wait_for_timeout(2000)
    
#Go to Checkout page
    your_cart = sauce_page.locator("#shopping_cart_container").click()
    your_cart_title = sauce_page.locator("[data-test='title']")
    expect(your_cart_title).to_be_visible()
    expect(your_cart_title).to_have_text("Your Cart")
    
    #Click Checkout Button
    checkout_btn = sauce_page.locator("[data-test='checkout']").click()
    checkout_info_title = sauce_page.locator("[data-test='title']")
    expect(your_cart_title).to_be_visible()
    expect(your_cart_title).to_have_text("Checkout: Your Information")
    sauce_page.wait_for_timeout(2000)
