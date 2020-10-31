import symengine
h1='x9'
h2='x10'
h3='x11'
h4='x12'
h5='x13'
h6='x14'
h7='x15'
h8='x16'
h9='x17'
h10='x9*x12*sin(-x3)/z14'
h11='x11*x14*sin(x2-x5)/z36'
h13='x12*x13*sin(x3-x4)/z45'
h12='x10*x16*sin(x1-x7)/z28'
h14='x12*x17*sin(x3-x8)/z49'
h15='x14*x15*sin(x5-x6)/z67'
h16='x14*x13*sin(x5-x4)/z65'
h17='x16*x15*sin(x7-x6)/z87'
h18='x16*x17*sin(x7-x8)/z89'
h19='(x12*x13*sin(x3-x4)/z45)+(x12*x17*sin(x7-x8)/z49)'
h20='(x16*x15*sin(x7-x6)/z87)+(x16*x17*sin(x7-x8)/z89)'
h21='(x14*x15*sin(x5-x6)/z67)+(x14*x12*sin(x5-x4)/z65)'

var = symengine.symbols('x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15 x16 x17')
f = symengine.sympify([h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14,h15,h16,h17,h18,h19,h20,h21])
J = symengine.zeros(len(f),len(var))
for i, fi in enumerate(f):
    for j, s in enumerate(var):        
        J[i,j] = symengine.diff(fi, s)
print(J)