import sympy as sy

# Create some symbols that we can use as variables 
# in mathematical expressions
x, y, z = sy.symbols('x y z')

# Use sympy to determine and print the functional form 
# for the derivative of x^2 
dx2 = sy.diff( x**2, x )
print( "The derivative of x^2 is", dx2 )
# Use sympy to determine and print the functional form 
# for the derivative of cos(x) 
dcos= sy.diff( sy.cos(x), x )
print( "The derivative of cos(x) is", dcos )
# Use sympy to determine and print the functional form 
# for the derivative of sin(x)
dsin = sy.diff( sy.sin(x), x )
print( "The derivative of sin(x) is", dsin )
# Just in case you are curous
dtanh = sy.diff( sy.tanh(y), y)
print( "The derivative of tanh(y)", dtanh  )
# Use sympy to determine and print the functional form of a 
# function that would be a pain to differentiate by hand
# as we would need to use the both the chain rule and the 
# product rule
dmess = sy.diff( sy.exp(z**2)*sy.cos(sy.sin(z)) + (z**2)*sy.exp(z), z )
print( "The derivative of this hot mess of a function is", dmess )
