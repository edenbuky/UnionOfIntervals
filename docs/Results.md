# Results & Analysis 📊

## Union of Intervals – Results and Discussion

### 1. Union Of Intervals
In this question, we will study the hypothesis class of a finite union of disjoint intervals and the properties of the ERM algorithm for this class.

To review, let the sample space be \( \mathcal{X} = [0,1] \) and consider a binary classification problem, i.e., \( \mathcal{Y} = \{0,1\} \). We will try to learn using a hypothesis class that consists of \( k \) intervals. More explicitly, let \( I = \{ [l_1, u_1], \dots, [l_k, u_k] \} \) be \( k \) disjoint intervals such that \( 0 \leq l_1 \leq u_1 \leq l_2 \leq \dots \leq u_k \leq 1 \). For each such \( k \) disjoint intervals, define the corresponding hypothesis as:

\[ h_I(x) = \begin{cases} 
1 & \text{if } x \in [l_1, u_1] \cup \dots \cup [l_k, u_k] \\
0 & \text{otherwise} 
\end{cases} \]

Finally, define \( \mathcal{H}_k \) as the hypothesis class that consists of all hypotheses that correspond to \( k \) disjoint intervals:

\[ \mathcal{H}_k = \{ h_I | I = \{ [l_1, u_1], \dots, [l_k, u_k] \}, 0 \leq l_1 \leq u_1 \leq l_2 \leq \dots \leq u_k \leq 1 \} \]

We are given a sample of size \( n \): \( (x_1, y_1), \dots, (x_n, y_n) \). Assume that the points are sorted, so that \( 0 \leq x_1 \leq x_2 \leq \dots \leq x_n \leq 1 \).

---

### **(a) (8 points)**
Assume that the true distribution \( P[x,y] = P[y|x] \cdot P[x] \) is as follows:

\[ P[y=1|x] = \begin{cases} 
0.8 & \text{if } x \in [0,0.2] \cup [0.4, 0.6] \cup [0.8, 1] \\
0.1 & \text{if } x \in (0.2, 0.4) \cup (0.6, 0.8) 
\end{cases} \]

And \( P[y=0|x] = 1 - P[y=1|x] \). Since we know the true distribution \( P \), we can calculate \( e_P(h) \) precisely for any hypothesis \( h \in \mathcal{H}_k \). What is the hypothesis in \( \mathcal{H}_{10} \) with the smallest error (i.e., \( \text{argmin}_{h \in \mathcal{H}_{10}} e_P(h) \))?

### **Answer:**
{Explanation provided earlier for part (a)}

---

### **(b) (8 points)**
Write a function that, given a list of intervals \( I \), calculates the true error \( e_P(h_I) \). Then, for \( k = 3, n = 10, 15, 20, \dots, 100 \), perform the following experiment \( T = 100 \) times:

1. Draw a sample of size \( n \) and run the ERM algorithm on it.
2. Calculate the empirical error for the returned hypothesis.
3. Calculate the true error for the returned hypothesis.
4. Plot the empirical and true errors, averaged across the \( T \) runs, as a function of \( n \).
5. Discuss the results. Do the empirical and true errors decrease or increase with \( n \)? Why?

### **Answer:**
{Explanation provided earlier for part (b)}

---

### **(c) (8 points)**
Plot the empirical and true errors as a function of \( k \) for \( k = 1, \dots, 10 \). Discuss the results. What is the best \( k \)?

### **Answer:**
{Explanation provided earlier for part (c)}

---

### **Graphs and Visualizations:**
![Empirical and True Error as a Function of k](k_vs_error.png)

![Empirical vs. True Error as a Function of Sample Size](docs/graphs/n_vs_error.png)

---

### **Summary and Conclusions:**
1. **Empirical Error** increases with sample size but stabilizes as it converges to the true error.
2. **True Error** remains stable, indicating its intrinsic connection to the hypothesis and the true distribution.
3. **Overfitting** can be identified when the empirical error is significantly lower than the true error.
4. **Optimal k** balances accuracy and generalization.

For detailed explanations, refer to `docs/Results.md`.

