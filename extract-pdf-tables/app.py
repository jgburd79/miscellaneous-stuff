"""
Copyright 2021 Joshua G. Burdeshaw

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the
Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the
Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR
IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""

"""
Instructions for Packaging as .exe executable file using Pyinstaller

Single file exe:

> pyinstaller -F --add-data "templates;templates" --add-data "drag_n_drop;drag_n_drop" app.py

"""


import sys
import os
from flask import Flask
from flask_dropzone import Dropzone

from pyfladesk import init_gui

from drag_n_drop.views import bp as drag_n_drop_bp

"""
This part is critical when packaging with Pyinstaller so that the template files
can be found after compiling.
"""
################################################################################
if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    app = Flask(__name__, template_folder=template_folder)
else:
    app = Flask(__name__)
################################################################################


app.config['UPLOAD_FOLDER'] = './UPLOAD_FOLDER'
# app.config['MAX_CONTENT_PATH']

dropzone = Dropzone(app)

app.register_blueprint(drag_n_drop_bp, url_prefix="/")

if __name__ == '__main__':
    # app.run(debug=True)
    init_gui(app, width=300, height=700, window_title="PDF Table Coverter", icon="csalogo.png", argv=None)