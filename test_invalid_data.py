from main import *


def test_incorrect_name(page: Page):
    test_page = TestPage(page)

    test_page.open()
    time.sleep(5)

    test_page.click_checkbox()
    time.sleep(2)

    test_page.input_incorrect_name()
    test_page.input_correct_email()
    test_page.input_correct_password()
    time.sleep(2)

    test_page.click_next()

    test_page.except_visible_error_message_name()
    test_page.close()


def test_incorrect_email(page: Page):
    test_page = TestPage(page)

    test_page.open()
    time.sleep(5)

    test_page.click_checkbox()
    time.sleep(2)

    test_page.input_correct_name()
    test_page.input_incorrect_email()
    test_page.input_correct_password()
    time.sleep(2)

    test_page.click_next()

    test_page.except_visible_error_message_email()
    test_page.close()


def test_incorrect_password(page: Page):
    test_page = TestPage(page)

    test_page.open()
    time.sleep(5)

    test_page.click_checkbox()
    time.sleep(2)

    test_page.input_correct_name()
    test_page.input_correct_email()
    test_page.input_incorrect_password()
    time.sleep(2)

    test_page.click_next()

    test_page.except_visible_error_message_password()
    test_page.close()


def test_incorrect_referral(page: Page):
    test_page = TestPage(page)

    test_page.open()
    time.sleep(5)

    test_page.click_checkbox()
    time.sleep(2)

    test_page.input_correct_name()
    test_page.input_correct_email()
    test_page.input_correct_password()
    test_page.input_incorrect_referral()
    time.sleep(2)

    test_page.except_visible_error_message_referral()
    test_page.close()