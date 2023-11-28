from flask import Flask, render_template, request
from unils.complex_funx import ComplexMod

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    result = False
    form = ''
    base = ''
    r = ''

    if request.method == "GET":
        form = request.values.get('form')
        return render_template('index.html',
                               form=form, result=result)
    else:
        result = True

        form_result = ''
        img_result = ''
        arg_result = ''

        if 'r' in request.values:
            r = request.values.get('r')
            img = request.values.get('imagine')
            operations = request.values.getlist('operation[]')

            comp_mod = ComplexMod(float(r), float(img))

            if '0' in operations:
                form_result = comp_mod.get_alg_form()
            if '1' in operations:
                img_result = comp_mod.get_img()
            if '2' in operations:
                arg_result = comp_mod.get_arg()

        else:
            base = request.values.get('base')
            img = request.values.get('imagine')
            operations = request.values.getlist('operation[]')

            comp_mod = ComplexMod(float(base), float(img))

            if '0' in operations:
                form_result = comp_mod.get_exp_form()
            if '1' in operations:
                img_result = comp_mod.get_img()
            if '2' in operations:
                arg_result = comp_mod.get_arg()

        return render_template('index.html',
                               form='alg',
                               result=result,
                               form_result=form_result,
                               img_result=img_result,
                               arg_result=arg_result,
                               base=base,
                               r=r,
                               img=img,
                               operations=operations)


if __name__ == '__main__':
    app.run()
