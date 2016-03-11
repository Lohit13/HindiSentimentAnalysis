# -*- coding: utf-8 -*-
from splinter import Browser

def transliterate(input_data):
    with Browser() as browser:
        url = "https://translate.google.co.in/#en/hi/" + input_data
        browser.visit(url)
        button = browser.find_by_id('gt-submit')
        button.click()
        text_div = browser.find_by_id('res-translit')
        return text_div.text

print transliterate('जीवन जीवन')

