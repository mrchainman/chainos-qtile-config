import pycurl
import certifi
from io import BytesIO
from libqtile.lazy import lazy
from libqtile.backend.x11.window import Window
from qtile_extras.popup.toolkit import (
    PopupGridLayout,
    PopupText
)
from libqtile.resources.utils.settings import colors

def get_weather(qtile):
    # Creating a buffer as the cURL is not allocating a buffer for the network response
    buffer = BytesIO()
    c = pycurl.Curl()
    #initializing the request URL
    c.setopt(c.URL, 'https://wttr.in')
    #setting options for cURL transfer
    c.setopt(c.WRITEDATA, buffer)
    #setting the file name holding the certificates
    c.setopt(c.CAINFO, certifi.where())
    # perform file transfer
    c.perform()
    #Ending the session and freeing the resources
    c.close()
    #retrieve the content BytesIO
    body = buffer.getvalue()
    #decoding the buffer
    data = (body.decode('iso-8859-1'))
    controls = []
    ri = 0
    ci = 0
    for i in data:
        controls.append(
                PopupText(
                    text=str(i),
                    row = ri,
                    col = ci,
                    width=0.1,
                    height=0.1,
                    h_align="center",
                    highlight=colors["accent"],
                    highlight_method="block",
                    background=colors["trans"],
            )
        )
        if ci < 6:
            ci += 1
        else:
            ri += 1
            ci = 0

    layout = PopupGridLayout(
        qtile,
        rows=5,
        cols=7,
        width=300,
        height=300,
        controls=controls,
        background=colors["trans"],
        initial_focus=None,
    )

    layout.show()
