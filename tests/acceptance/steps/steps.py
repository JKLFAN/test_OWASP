from behave import *
from selenium import webdriver
from tests.acceptance.pages.home_page import Homepage
from tests.acceptance.pages.login_page import LoginPage
from tests.acceptance.pages.register_page import RegisterPage

use_step_matcher('re')


@given('I navigate to the OWASP homepage')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get(Homepage(context.driver).url)


@step('I remove all the popups')
def step_impl(context):
    Homepage(context.driver).click_dismiss_buttons()


@step('I click on the account link')
def step_impl(context):
    Homepage(context.driver).click_account_link()


@step('I click on the login link')
def step_impl(context):
    Homepage(context.driver).click_login_link()


@then('I will be on the login page')
def step_impl(context):
    LoginPage(context.driver).assert_header()
    LoginPage(context.driver).assert_url()


@step('I click on the new customer link')
def step_impl(context):
    LoginPage(context.driver).click_new_customer()


@then('I will be on the user registration page')
def step_impl(context):
    RegisterPage(context.driver).assert_header()
    RegisterPage(context.driver).assert_url()


@when('I input data into the mandatory field')
def step_impl(context):
    RegisterPage(context.driver).enter_details()