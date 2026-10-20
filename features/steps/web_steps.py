from behave import when, then
from selenium.webdriver.common.by import By


@when('I press the "{button}" button')
def step_press_button(context, button):
    element = context.browser.find_element(
        By.XPATH,
        f'//button[normalize-space()="{button}"]'
        f' | //input[@type="submit" and @value="{button}"]'
        f' | //input[@type="button" and @value="{button}"]'
    )
    element.click()


@then('I should see "{text}" in the results')
def step_text_in_results(context, text):
    results = context.browser.find_element(By.ID, "search_results")
    assert text in results.text, (
        f'Expected "{text}" in results, got: {results.text}'
    )


@then('I should not see "{text}" in the results')
def step_text_not_in_results(context, text):
    results = context.browser.find_element(By.ID, "search_results")
    assert text not in results.text, (
        f'Unexpected "{text}" found in results: {results.text}'
    )


@then('I should see the message "{message}"')
def step_message_present(context, message):
    page_text = context.browser.find_element(By.TAG_NAME, "body").text
    assert message in page_text, (
        f'Expected message "{message}" on the page'
    )