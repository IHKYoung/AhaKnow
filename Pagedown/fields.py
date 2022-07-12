# -*- coding: utf-8 -*-
"""
    @Author: Zeal Young
    @URL: https://ahaknow.com
    @Create: 2021/9/25 21:11
"""
from wtforms.fields import TextAreaField
from .widgets import PageDown


class PageDownField(TextAreaField):
    widget = PageDown()
