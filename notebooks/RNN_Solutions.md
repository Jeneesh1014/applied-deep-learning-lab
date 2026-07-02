# RNN Exercises — Solutions

---

## Task 2: Determining the Number of Trainable Parameters

**Question:** Calculate the number of trainable parameters given the information about the dimensions of the input, the output and/or the hidden states.

For a standard Elman RNN, the trainable parameters are:

| Parameter | Shape | Count |
|---|---|---|
| $W_{xh}$ | $n \times m$ | $n \cdot m$ |
| $W_{hh}$ | $n \times n$ | $n \cdot n$ |
| $b_h$ | $n$ | $n$ |
| $W_{hy}$ | $o \times n$ | $o \cdot n$ |
| $b_y$ | $o$ | $o$ |

$$\text{Total} = (n \cdot m) + (n \cdot n) + n + (o \cdot n) + o$$

where $m$ = input size, $n$ = hidden size, $o$ = output size.

---

### a) $m = 5,\ n = 32,\ o = 10$

| Parameter | Calculation | Count |
|---|---|---|
| $W_{xh}$ | $32 \times 5$ | $160$ |
| $W_{hh}$ | $32 \times 32$ | $1024$ |
| $b_h$ | $32$ | $32$ |
| $W_{hy}$ | $10 \times 32$ | $320$ |
| $b_y$ | $10$ | $10$ |

$$\text{Total} = 160 + 1024 + 32 + 320 + 10 = \boxed{1546}$$

---

### b) $n = 10$, weights in $W_{xh} = 40$, $o = 3$

Here the number of weights in $W_{xh}$ is given directly (40), so we don't need $m$ separately.

| Parameter | Calculation | Count |
|---|---|---|
| $W_{xh}$ | given | $40$ |
| $W_{hh}$ | $10 \times 10$ | $100$ |
| $b_h$ | $10$ | $10$ |
| $W_{hy}$ | $3 \times 10$ | $30$ |
| $b_y$ | $3$ | $3$ |

$$\text{Total} = 40 + 100 + 10 + 30 + 3 = \boxed{183}$$

---

### c) $W_{hh}$ given as a $5\times5$ matrix, $m = 8,\ o = 2$

Since $W_{hh}$ is $5 \times 5$, the hidden size is $n = 5$.

| Parameter | Calculation | Count |
|---|---|---|
| $W_{xh}$ | $5 \times 8$ | $40$ |
| $W_{hh}$ | $5 \times 5$ (as given) | $25$ |
| $b_h$ | $5$ | $5$ |
| $W_{hy}$ | $2 \times 5$ | $10$ |
| $b_y$ | $2$ | $2$ |

$$\text{Total} = 40 + 25 + 5 + 10 + 2 = \boxed{82}$$

---

## Task 3: Calculating the Results of RNNs

**Question:** Calculate the results $y$ for each time step of the forward pass of the given Elman net, using $f(z) = \text{ReLU}(z) = \max(0, z)$ as the hidden-state activation function.

**Given:**

$$
x_1 = \begin{bmatrix}1\\2\\0\\-1\end{bmatrix}, \quad
x_2 = \begin{bmatrix}0\\-2\\4\\1\end{bmatrix}, \quad
h_0 = \begin{bmatrix}0\\0\end{bmatrix}
$$

$$
W_{xh} = \begin{bmatrix}2 & -1 & 3 & 1\\0 & 2 & -1 & -2\end{bmatrix}, \quad
W_{hh} = \begin{bmatrix}1 & 2\\-1 & 3\end{bmatrix}, \quad
b_h = \begin{bmatrix}1\\-2\end{bmatrix}
$$

$$
W_{hy} = \begin{bmatrix}2 & -1\\1 & 1\end{bmatrix}, \quad
b_y = \begin{bmatrix}0\\3\end{bmatrix}
$$

**Formulas:**
$$h_t = f(W_{xh}x_t + W_{hh}h_{t-1} + b_h), \qquad y_t = W_{hy}h_t + b_y$$

---

### Time step 1 ($t=1$)

**Step 1 — $W_{xh}x_1$:**
$$
\begin{bmatrix}2 & -1 & 3 & 1\\0 & 2 & -1 & -2\end{bmatrix}
\begin{bmatrix}1\\2\\0\\-1\end{bmatrix} =
\begin{bmatrix}(2)(1)+(-1)(2)+(3)(0)+(1)(-1)\\(0)(1)+(2)(2)+(-1)(0)+(-2)(-1)\end{bmatrix} =
\begin{bmatrix}-1\\6\end{bmatrix}
$$

**Step 2 — $W_{hh}h_0$:** since $h_0 = [0,0]^T$, this is $[0,0]^T$.

**Step 3 — add $b_h$:**
$$
\begin{bmatrix}-1\\6\end{bmatrix} + \begin{bmatrix}0\\0\end{bmatrix} + \begin{bmatrix}1\\-2\end{bmatrix} = \begin{bmatrix}0\\4\end{bmatrix}
$$

**Step 4 — apply ReLU:**
$$
h_1 = \text{ReLU}\left(\begin{bmatrix}0\\4\end{bmatrix}\right) = \begin{bmatrix}0\\4\end{bmatrix}
$$

**Step 5 — compute $y_1 = W_{hy}h_1 + b_y$:**
$$
\begin{bmatrix}2 & -1\\1 & 1\end{bmatrix}\begin{bmatrix}0\\4\end{bmatrix} + \begin{bmatrix}0\\3\end{bmatrix} =
\begin{bmatrix}-4\\4\end{bmatrix} + \begin{bmatrix}0\\3\end{bmatrix} =
\begin{bmatrix}-4\\7\end{bmatrix}
$$

$$\boxed{y_1 = \begin{bmatrix}-4\\7\end{bmatrix}}$$

---

### Time step 2 ($t=2$)

**Step 1 — $W_{xh}x_2$:**
$$
\begin{bmatrix}2 & -1 & 3 & 1\\0 & 2 & -1 & -2\end{bmatrix}
\begin{bmatrix}0\\-2\\4\\1\end{bmatrix} =
\begin{bmatrix}(2)(0)+(-1)(-2)+(3)(4)+(1)(1)\\(0)(0)+(2)(-2)+(-1)(4)+(-2)(1)\end{bmatrix} =
\begin{bmatrix}15\\-10\end{bmatrix}
$$

**Step 2 — $W_{hh}h_1$:**
$$
\begin{bmatrix}1 & 2\\-1 & 3\end{bmatrix}\begin{bmatrix}0\\4\end{bmatrix} =
\begin{bmatrix}(1)(0)+(2)(4)\\(-1)(0)+(3)(4)\end{bmatrix} =
\begin{bmatrix}8\\12\end{bmatrix}
$$

**Step 3 — add $b_h$:**
$$
\begin{bmatrix}15\\-10\end{bmatrix} + \begin{bmatrix}8\\12\end{bmatrix} + \begin{bmatrix}1\\-2\end{bmatrix} = \begin{bmatrix}24\\0\end{bmatrix}
$$

**Step 4 — apply ReLU:**
$$
h_2 = \text{ReLU}\left(\begin{bmatrix}24\\0\end{bmatrix}\right) = \begin{bmatrix}24\\0\end{bmatrix}
$$

**Step 5 — compute $y_2 = W_{hy}h_2 + b_y$:**
$$
\begin{bmatrix}2 & -1\\1 & 1\end{bmatrix}\begin{bmatrix}24\\0\end{bmatrix} + \begin{bmatrix}0\\3\end{bmatrix} =
\begin{bmatrix}48\\24\end{bmatrix} + \begin{bmatrix}0\\3\end{bmatrix} =
\begin{bmatrix}48\\27\end{bmatrix}
$$

$$\boxed{y_2 = \begin{bmatrix}48\\27\end{bmatrix}}$$

---

## Summary of Results

| Time step | $h_t$ | $y_t$ |
|---|---|---|
| $t=1$ | $[0,\ 4]^T$ | $[-4,\ 7]^T$ |
| $t=2$ | $[24,\ 0]^T$ | $[48,\ 27]^T$ |
