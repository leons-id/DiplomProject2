import View


class Contr:
    def __init__(self, inModel):
        self.model = inModel
        # self.view = Anom_View.View(self)
        self.view = View.View(self)
        self.model.addView(self.view.ui)
        self.view.show()