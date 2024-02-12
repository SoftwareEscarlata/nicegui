import time

import pytest

from nicegui.testing import SimulatedScreen

from .. import main


@pytest.mark.module_under_test(main)
def test_markdown_message(screen: SimulatedScreen) -> None:
    screen.open('/')
    screen.should_contain('Try running')


@pytest.mark.module_under_test(main)
def test_button_click(screen: SimulatedScreen) -> None:
    screen.open('/')
    screen.click('Click me')
    screen.should_contain('Button clicked!')


@pytest.mark.module_under_test(main)
def test_sub_page(screen: SimulatedScreen) -> None:
    screen.open('/subpage')
    screen.should_contain('This is a subpage')


@pytest.mark.module_under_test(main)
def test_with_connected(screen: SimulatedScreen) -> None:
    screen.open('/with_connected')
    screen.check_exceptions()
    screen.should_contain('This is a subpage')
    screen.check_exceptions()
    screen.should_contain('Connected!')
    screen.check_exceptions()
    time.sleep(1)
    screen.check_exceptions()
