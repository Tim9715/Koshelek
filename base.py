from main import *


class Config:

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto('https://koshelek.ru/authorization/signup')

    def close(self):
        self.page.close()

