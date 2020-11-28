# Sympy

The reason for doing the previous exercise is that it is tempting to think that:

* Variables hold the values of quantities that are stored in memory.  Variables thus play the role of nouns in a language.
* Functions change the values of the variables.  Functions thus play the role of verbs in a language. 

The point I wanted to make by getting you to do the previous exercise is that this distinction is misleading.  The set of instructions within a function are themself stored in memory.  We can thus change a function by writing something that changes the parts of memory where the function is stored.  In mathematics, functions are therefore objects in their own right.  Consequently, we can develop operations for transforming functions much as we have established operations like addition, subtraction and so on for transforming numbers.  

You have even encountered some of these operations that act on functions already.  Differentiation, for example, is an operation that transforms one function into a second different function.  You can thus write computer programs that calculate the analytical derivatives of functions for you.  How these functions work is well beyond the scope of this module. In this exercise I am going to show you how you can use Python to check the derivatives in your homework.

In the code in `main.py`, I have written a Python program to evaluate the analytic derivatives of some functions.  The first three are ![](https://render.githubusercontent.com/render/math?math=x^2), ![](https://render.githubusercontent.com/render/math?math=\cos(x)) and ![](https://render.githubusercontent.com/render/math?math=\sin(x)).  When you run the code, you should be able to see that Python outputs that these derivatives are ![](https://render.githubusercontent.com/render/math?math=2x), ![](https://render.githubusercontent.com/render/math?math=-\sin(x)) and ![](https://render.githubusercontent.com/render/math?math=\cos(x)) respectively.  You probably did not need Python to work these things out for you.  I have also got Python to output the derivative of the ![](https://render.githubusercontent.com/render/math?math=\tanh(x)) function that we encountered earlier as well as a beast of a function that would be a pain to differentiate by hand.

You can hopefully work out how to modify the code on the left to evaluate the derivatives in your homework.  You can thus use Python to check your working.  To see if you have understood the basic ideas modify the code on the left and get it to set the following variables:

1. `dx4` should  be set equal to the derivative of ![](https://render.githubusercontent.com/render/math?math=x^4)
2. `dtanx` should be set equal to the first derivative of ![](https://render.githubusercontent.com/render/math?math=\tan(x))
3. `dexpx` should be set equal to the first derivative of ![](https://render.githubusercontent.com/render/math?math=\exp(x))
4. `dex` should be set equal to the first derivative of ![](https://render.githubusercontent.com/render/math?math=\exp\left(\frac{x^2}{2}\right))

Use a modified version of the Python code that is shown in `main.py` to evaluate these derivatives.
 
