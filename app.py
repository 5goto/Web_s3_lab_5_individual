from flask import Flask, render_template, request
from unils.complex_funx import ComplexMod

app = Flask(__name__)


import controllers.index

if __name__ == '__main__':
    app.run()
