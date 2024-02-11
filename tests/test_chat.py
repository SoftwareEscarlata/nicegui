from selenium.webdriver.common.by import By

from nicegui import ui
from nicegui.testing import SeleniumScreen


def test_no_html(screen: SeleniumScreen):
    ui.chat_message('<strong>HTML</strong>')

    screen.open('/')
    screen.should_contain('<strong>HTML</strong>')


def test_html(screen: SeleniumScreen):
    ui.chat_message('<strong>HTML</strong>', text_html=True)

    screen.open('/')
    screen.should_contain('HTML')
    screen.should_not_contain('<strong>HTML</strong>')


def test_newline(screen: SeleniumScreen):
    ui.chat_message('Hello\nNiceGUI!')

    screen.open('/')
    assert screen.find('Hello').find_element(By.TAG_NAME, 'br')


def test_slot(screen: SeleniumScreen):
    with ui.chat_message():
        ui.label('slot')

    screen.open('/')
    screen.should_contain('slot')
