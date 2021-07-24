import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.title('Superquadrics')
st.subheader('Formulas')
st.latex(r'\left|\frac{x}{a}\right|^s + \left|\frac{y}{b}\right|^t + \left|\frac{z}{c}\right|^u = 1')
st.markdown('where $r$, $s$, and $t$ are positive real numbers that determine the main features of the superquadric, and $a$, $b$, and $c$ are scaling parameters.')
st.latex(r'\left(\left|\frac{x}{a}\right|^{n_2} + \left|\frac{y}{b}\right|^{n_2}\right)^\frac{n_1}{n_2} + \left|\frac{z}{c}\right|^{n_1} = 1')
st.markdown('where $n_1$ and $n_2$ are shape parameters, and $a$, $b$, and $c$ are scaling parameters.')
st.subheader('Formula python code')
with st.echo():
    import numpy as np
    def superquadrics(a,b,c,n1,n2,x,y,z):
        values = np.power(np.power(np.abs(x/a),n2) \
                        + np.power(np.abs(y/b),n2),n1/n2) \
               + np.power(np.abs(z/c),n1)
        return values
X, Y, Z = np.mgrid[-1:1:50j, -1:1:50j, -2:2:100j]
a  = 1.
b  = 1.
c  = st.slider('c (a=b=1)', .2, 2., 1., .2)
n1 = st.slider('n1', 1, 10, 10, 1)
n2 = st.slider('n2', 1, 10, 2, 1)
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
st.write(fig)
st.subheader('Code')
st.markdown('* https://github.com/ken2s/superquadrics/blob/main/st_superquadrics.py')
st.subheader('References')
st.markdown('* https://en.wikipedia.org/wiki/Superquadrics')
