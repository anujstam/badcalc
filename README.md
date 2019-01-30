# badcalc
Multifunction Calculator with graphing and function storage

Intended to be used as a tool for personal convenience when studying calculus, with 0 emphasis on UI.
Supports single variable integration and Differentiation of functions, along with the ability to save and graph them.

Only permitted variable in a function is 'x'. Any multiplication should specify the '*' operator. Use '**' for powers and exp(f(x)), sin(f(x)),cos(f(x)) etc

Uses the sympy module's sympify and lambdify functions, which inturn use eval() so be cautious of the input you use
