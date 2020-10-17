import time

from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from behave import *
from automation_behave.utilites.env import Env

use_step_matcher("re")

@when("I open (?P<link>.+) using (?P<browser>.+)")
def step_impl(context, link, browser):
    """
    :type context: behave.runner.Context
    :type link: str
    :type browser: str
    """

    client = getattr(context, browser)

    client.get(link)
    time.sleep(Env.vars['wait_time'])
    attach(
        client.get_screenshot_as_png(),
        name="screenshot",
        attachment_type=AttachmentType.PNG
    )


@then("I take screenshot using (?P<browser>.+)")
def step_impl(context, browser):
    """
    :type context: behave.runner.Context
    """
    client = getattr(context, browser)
    client.save_screenshot("screenshot.png")