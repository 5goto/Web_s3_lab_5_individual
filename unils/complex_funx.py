import cmath


class ComplexMod:
    def __init__(self, base, img, exp=True):
        if not exp:
            self.complex_num = complex(base, img)
        else:
            self.complex_num = cmath.rect(base, img)

    def get_img(self):
        return self.complex_num.imag

    def get_arg(self):
        return cmath.phase(self.complex_num)

    def get_exp_form(self):
        r = abs(self.complex_num)
        theta = cmath.phase(self.complex_num)
        return f'{r} * (cos({theta}) + i * sin({theta}))'

    def get_alg_form(self):
        return self.complex_num
