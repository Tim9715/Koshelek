from main import *


def test_empty_name(page: Page):
    test_page = TestPage(page)

    test_page.open()
    time.sleep(5)

    test_page.click_checkbox()
    time.sleep(2)

    test_page.input_correct_email()
    test_page.input_correct_password()

    test_page.click_next()
    time.sleep(3)

    test_page.expect_error_message_empty()
    test_page.close()


def test_empty_email(page: Page):
    test_page = TestPage(page)

    test_page.open()
    time.sleep(5)

    test_page.click_checkbox()
    time.sleep(2)

    test_page.input_correct_name()
    test_page.input_incorrect_password()

    test_page.click_next()
    time.sleep(2)

    test_page.expect_error_message_empty()
    test_page.close()


def test_empty_password(page: Page):
    test_page = TestPage(page)

    test_page.open()
    time.sleep(5)

    test_page.click_checkbox()
    time.sleep(2)

    test_page.input_correct_name()
    test_page.input_correct_email()

    test_page.click_next()
    time.sleep(3)

    test_page.expect_error_message_empty()
    test_page.close()