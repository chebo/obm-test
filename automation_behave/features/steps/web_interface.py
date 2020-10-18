import time

from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from behave import *
from automation_behave.utilites.env import Env

use_step_matcher("re")


@given("I open (?P<link>.+) using (?P<browser>.+)")
def step_impl(context, link, browser):
    """
    :type context: behave.runner.Context
    :type link: str
    :type browser: str
    """

    client = getattr(context, browser)
    client.get(link)


@when("I have (?P<expected_count>.+) links within school menu items using (?P<browser>.+)")
def step_impl(context, expected_count, browser):
    """
    :type context: behave.runner.Context
    :type expected_count: int
    :type browser: str
    """
    count = 0
    client = getattr(context, browser)

    menu_list = client.find_element_by_xpath('//li[contains(@id,"school")]/ul')
    options = [x for x in menu_list.find_elements_by_tag_name("li")]
    for x in options:
        if x.find_elements_by_tag_name("a"):
            count += 1
    assert count == int(expected_count)
    time.sleep(Env.vars['wait_time'])


@then("I take screenshot using (?P<browser>.+)")
def step_impl(context, browser):
    """
    :type context: behave.runner.Context
    """
    client = getattr(context, browser)
    client.save_screenshot("screenshot.png")