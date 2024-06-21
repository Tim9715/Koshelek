from main import *


def test_big(page: Page):
    test_page = TestPage(page)

    test_page.open()
    time.sleep(5)

    test_page.click_checkbox()
    time.sleep(2)

    test_page.input_big_name()
    test_page.input_big_email()
    test_page.input_big_password()
    time.sleep(2)

    test_page.click_next()
    time.sleep(3)

    test_page.except_visible_error_message_name()
    test_page.except_visible_error_message_password()
    test_page.close()


def test_min(page: Page):
    test_page = TestPage(page)

    test_page.open()
    time.sleep(5)

    test_page.click_checkbox()
    time.sleep(2)

    test_page.input_min_name()
    test_page.input_min_email()
    test_page.input_min_password()
    time.sleep(2)

    test_page.click_next()
    time.sleep(2)

    test_page.except_visible_error_message_name()
    test_page.except_visible_error_message_email()
    test_page.except_visible_error_message_password_min()
    test_page.close()