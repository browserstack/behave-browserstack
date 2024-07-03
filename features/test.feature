Feature: BStack Sample Testing
    Scenario: Add product to cart
        When visit url "https://bstackdemo.com/"
        When item with xpath '//*[@id="1"]/p' is present to be added to cart
        When add to cart button '//*[@id="1"]/div[4]' for above item is clicked
        Then item in cart '//*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div/div[3]/p[1]' is same as the one which was added
