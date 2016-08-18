#!/usr/bin/env python
# -*- coding: utf-8 -*-

import htmlPy
import os

app = htmlPy.AppGUI(title=u"تست افسردگی بک", maximized=True)

app.template_path = os.path.abspath(".")
app.static_path = os.path.abspath(".")

app.template = ("index.html", {"username": "htmlPy_user"})

app.start()
