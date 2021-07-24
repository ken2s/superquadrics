# superquadrics.py

import plotly.graph_objects as go
import numpy as np

def superquadrics(a,b,c,n1,n2,x,y,z):
    values = np.power(np.power(np.abs(x/a),n2) \
                    + np.power(np.abs(y/b),n2),n1/n2) \
           + np.power(np.abs(z/c),n1)
    return values

X, Y, Z = np.mgrid[-1:1:50j, -1:1:50j, -1:1:50j]
a = 1.
b = 1.
c = 1.
n1= 10.
n2= 2.

fig = go.Figure(data=go.Isosurface(
    x = X.flatten(),
    y = Y.flatten(),
    z = Z.flatten(),
    value = superquadrics(a,b,c,n1,n2,X,Y,Z).flatten(),
    isomin = .5,
    isomax = 1,
    showscale = False,
))
fig.update_layout(
    scene = dict(
        xaxis_title='',
        yaxis_title='',
        zaxis_title='',
        xaxis = dict(
            showbackground = False,
            showline = False,
            showticklabels = False,
        ),
        yaxis = dict(
            showbackground = False,
            showline = False,
            showticklabels = False,
        ),
        zaxis = dict(
            showbackground = False,
            showline = False,
            showticklabels = False,
        ),
    )
)
fig.show()