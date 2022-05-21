# Superquadrics

### Formulas

$$
    \left|\frac{x}{a}\right|^s 
  + \left|\frac{y}{b}\right|^t 
  + \left|\frac{z}{c}\right|^u 
  = 1
$$

<!-- <img src="https://latex.codecogs.com/gif.latex?\large&space;{\color{Gray}&space;\begin{align*}&space;\left|\frac{x}{a}\right|^s&space;&plus;&space;\left|\frac{y}{b}\right|^t&space;&plus;&space;\left|\frac{z}{c}\right|^u&space;=&space;1&space;\end{align*}}" title="\large {\color{Gray} \begin{align*} \left|\frac{x}{a}\right|^s + \left|\frac{y}{b}\right|^t + \left|\frac{z}{c}\right|^u = 1 \end{align*}}" /> -->

where *s*, *t* and *u* are positive real numbers that determine the main features of the superquadric, and *a*, *b*, and *c* are scaling parameters.

$$
  \large{\left(
      \left|\frac{x}{a}\right|^{n_2}
    + \left|\frac{y}{b}\right|^{n_2}
      \right)^\frac{n_1}{n_2} 
    + \left|\frac{z}{c}\right|^{n_1} }
  = 1
$$

<!-- <img src="https://latex.codecogs.com/gif.latex?\large&space;{\color{Gray}&space;\begin{align*}&space;\left(\left|\frac{x}{a}\right|^{n_2}&space;&plus;&space;\left|\frac{y}{b}\right|^{n_2}\right)^\frac{n_1}{n_2}&space;&plus;&space;\left|\frac{z}{c}\right|^{n_1}&space;=&space;1&space;\end{align*}}" title="\large {\color{Gray} \begin{align*} \left(\left|\frac{x}{a}\right|^{n_2} + \left|\frac{y}{b}\right|^{n_2}\right)^\frac{n_1}{n_2} + \left|\frac{z}{c}\right|^{n_1} = 1 \end{align*}}" />  -->

where *n<sub>1</sub>* and *n<sub>2</sub>* are shape parameters, and *a*, *b*, and *c* are scaling parameters.

### Formula python code
```python
import numpy as np
@st.cache
def superquadrics(a,b,c,n1,n2,x,y,z):
    values = np.power(np.power(np.abs(x/a),n2) \
                    + np.power(np.abs(y/b),n2),n1/n2) \
            + np.power(np.abs(z/c),n1)
    return values
```

### Streamlit
[share.streamlit.io](https://share.streamlit.io/ken2s/superquadrics/main/st_superquadrics.py)
