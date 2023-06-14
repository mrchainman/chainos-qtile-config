from libqtile.log_utils import logger
from qtile_extras.popup.toolkit import (
    PopupText,
    PopupWidget,
    PopupGridLayout,
)
from libqtile.resources.utils.settings import colors

class Base():
    instances = [] 
    def __init__(self,qtile,x_index):
        self.qtile_instance = qtile
        self.x_index = x_index
        self.x_index_mod = - self.x_index * 44 + 15
        logger.warning(f"Instance count is: {len(self.__class__.instances)}")
        if len(self.__class__.instances) > 0:
            logger.warning("if clause triggered")
            for v in self.__class__.instances:
                try:
                    v.layout.kill()
                    logger.warning(f"Deleted {v}")
                except BaseException as e:
                    logger.warning(f"Error Occured: {e}")
                finally:
                    self.__class__.instances = []

        else:
            self.__class__.instances.append(self)
            self._init_params()
            self._startup()

    def _init_params(self):
        self.controls = []

    def _startup(self):
        pass

    def show_layout(self):
        self.layout.show(x=self.x_index_mod, y=0, relative_to = 3, relative_to_bar=True)

    def gen_layout(self,qtile,rows=3,cols=3,width=100,height=200):
        try:
            self.layout = PopupGridLayout(
                                qtile,
                                rows=rows,
                                cols=cols,
                                width=width,
                                height=height,
                                controls=self.controls,
                                background=colors["trans"],
                                initial_focus=None,
                                close_on_click=False,
                                )
        except BaseException as e:
            logger.warning(f"Could not construct layout, error: {e}")
