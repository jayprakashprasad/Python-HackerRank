# Python3 program to 
# swap two numbers without using temporary variable
x = 10
y = 5
# code to swap 
# 'x' and 'y'
# x now becomes 50
x = x * y

# y becomes 10
y = x // y; 

# x becomes 5
x = x // y; 

print("After Swapping: x =", 
			x, " y =", y)

"""Problems with above methods 
1) The multiplication and division based approach doesn’t work if one of the numbers is 0 as the product becomes 0 irrespective of the other number.
2) Both Arithmetic solutions may cause arithmetic overflow. If x and y are too large, addition and multiplication may go out of integer range.
3) When we use pointers to variable and make a function swap, all of the above methods fail when both pointers point to the same variable. Let’s take a look what will happen in this case if both are pointing to the same variable.
// Bitwise XOR based method 
x = x ^ x; // x becomes 0 
x = x ^ x; // x remains 0 
x = x ^ x; // x remains 0
// Arithmetic based method 
x = x + x; // x becomes 2x 
x = x – x; // x becomes 0 
x = x – x; // x remains 0
Let us see the following program. """
