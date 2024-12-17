# EQUATION

```
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400
```

In example above we will use $x_a$ and $y_a$ for $button$ $A$ movement, $x_b$ and $y_b$ for $button$ $B$ movement, $X$ and $Y$ for $prize$ pozition. By this we get:

$$
    \begin{align}
    \overrightarrow{bttA} = [x_a,y_b] \\
    \overrightarrow{bttB} = [x_b,y_b] \\
    prize = (X,Y)
    \end{align}
$$

In this AoC task we need to calculate if it is possible to combine vectors $\overrightarrow{bttA}$ and $\overrightarrow{bttB}$ such that starting from point $(0,0)$ we end up in $(X,Y)$, and what are the number of each. We are going to represend each of this two numbers as $n$ and $m$ for $button$ $A$ clicks and $button$ $B$ accordingly. We can make two equations basing on informations above:

$$
    \begin{align}
    nx_a + mx_b = X  \\
    ny_a + my_b = Y 
    \end{align}
$$

We need to calculate $n$ and $m$ so after some transformations of equations above we get:

$$
    \begin{align}
    n = \frac{Yx_b-Xy_b}{y_ax_b-x_ay_b} \\
    m = \frac{X-nx_a}{x_b}
    \end{align}
$$

Now we can check if it works. We put into equation data from above.

$$
    \begin{align}
    n = \frac{5400  \cdot 22 - 8400 \cdot 67}{34 \cdot 22 - 94 \cdot 67} = 80 \\
    m = \frac{8400 - 80 \cdot 94}{22} = 40
    \end{align}
$$

We need to remember that $n,m \in N^+$ so if our solution does not belong to established domain it means that there is no combination of $\overrightarrow{bttA}$ and $\overrightarrow{bttB}$ that achives our initial goal.

