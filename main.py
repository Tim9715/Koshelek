import time
from base import *
from data import *
from playwright.sync_api import Page, sync_playwright, expect


class TestPage(Config):

    def click_checkbox(self):
        self.page.get_by_role(ElementsPage.button_checkbox).click()

    def click_next(self):
        self.page.get_by_role('button', name='Далее').click()


    def input_correct_name(self):
        self.page.get_by_label(ElementsPage.field_name).fill(InputData.correct_name)

    def input_correct_email(self):
        self.page.get_by_label(ElementsPage.field_email).fill(InputData.correct_email)

    def input_correct_password(self):
        self.page.get_by_label(ElementsPage.field_password).fill(InputData.correct_password)


    def input_incorrect_name(self):
        self.page.get_by_label(ElementsPage.field_name).fill(InputData.incorrect_name)

    def input_incorrect_email(self):
        self.page.get_by_label(ElementsPage.field_email).fill(InputData.incorrect_email)

    def input_incorrect_password(self):
        self.page.get_by_label(ElementsPage.field_password).fill(InputData.incorrect_password)

    def input_incorrect_referral(self):
        self.page.get_by_label(ElementsPage.field_referral).fill(InputData.incorrect_referral)


    def input_big_name(self):
        self.page.get_by_label(ElementsPage.field_name).fill(InputData.big_name)

    def input_big_email(self):
        self.page.get_by_label(ElementsPage.field_email).fill(InputData.big_email)

    def input_big_password(self):
        self.page.get_by_label(ElementsPage.field_password).fill(InputData.big_password)


    def input_min_name(self):
        self.page.get_by_label(ElementsPage.field_name).fill(InputData.min_name)

    def input_min_email(self):
        self.page.get_by_label(ElementsPage.field_email).fill(InputData.min_email)

    def input_min_password(self):
        self.page.get_by_label(ElementsPage.field_password).fill(InputData.min_password)


    def expect_error_message_empty(self):
        expect(self.page.get_by_text(ElementsPage.error_message_empty).first).to_be_visible()

    def except_visible_error_message_name(self):
        expect(self.page.get_by_text(ElementsPage.error_message_name).first).to_be_visible()

    def except_visible_error_message_email(self):
        expect(self.page.get_by_text(ElementsPage.error_message_email).first).to_be_visible()

    def except_visible_error_message_password(self):
        expect(self.page.get_by_text(ElementsPage.error_message_password).first).to_be_visible()

    def except_visible_error_message_password_min(self):
        expect(self.page.get_by_text(ElementsPage.error_message_password_min).first).to_be_visible()

    def except_visible_error_message_referral(self):
        expect(self.page.get_by_text(ElementsPage.error_message_referral)).to_be_visible()