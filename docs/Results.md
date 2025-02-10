# Results & Analysis 📊

## **Union of Intervals - Problem Description**

In this assignment, we study the hypothesis class of a **finite union of disjoint intervals** and analyze the properties of the **Empirical Risk Minimization (ERM) algorithm** for this class.

Let the sample space be **\( \mathcal{X} = [0,1] \)** and consider a **binary classification problem**, where \( \mathcal{Y} = \{0,1\} \). We aim to learn using a hypothesis class consisting of **\( k \) disjoint intervals**.

### **Mathematical Formulation**
We define a hypothesis class of disjoint intervals as follows:

Let \( I \) be a set of \( k \) disjoint intervals:
\[ I = \{[l_1, u_1], [l_2, u_2], ..., [l_k, u_k]\} \]
where the intervals are ordered such that:
\[ 0 \leq l_1 \leq u_1 \leq l_2 \leq u_2 \leq ... \leq u_k \leq 1 \]

For each such set \( I \), define the corresponding hypothesis function:
\[ h_I(x) = \begin{cases} 1, & \text{if } x \in [l_1, u_1] \cup \dots \cup [l_k, u_k] \\ 0, & \text{otherwise} \end{cases} \]

The hypothesis class \( \mathcal{H}_k \) consists of all possible such hypotheses:
\[ \mathcal{H}_k = \{ h_I | I = \{[l_1, u_1], ..., [l_k, u_k]\}, 0 \leq l_1 \leq u_1 \leq l_2 \leq u_2 \leq ... \leq u_k \leq 1 \} \]

We are given a labeled sample of size \( n \):
\[ (x_1, y_1), ..., (x_n, y_n) \]
where the points \( x_i \) are sorted in increasing order: \( 0 \leq x_1 < x_2 < ... < x_n \leq 1 \).

---

## **(b) Empirical and True Error Analysis**

### **Problem Statement**
We implement a function that calculates the true error \( e_P(h_I) \) for a given list of intervals \( I \). Then, for \( k = 3 \) and various values of \( n \) (10, 15, 20, ..., 100), we conduct the following experiment \( T = 100 \) times:
1. Draw a sample of size \( n \) and run the **ERM algorithm**.
2. Calculate the **empirical error** for the returned hypothesis.
3. Calculate the **true error** for the returned hypothesis.
4. Plot the empirical and true errors, averaged across the \( T \) runs, as a function of \( n \).
5. Discuss the results: Do the empirical and true errors decrease or increase with \( n \)? Why?

### **Solution & Analysis**
- The **empirical error** increases as \( n \) grows, but its **rate of increase slows down**, which aligns with theoretical expectations. A **larger sample size provides more information about the true distribution**, allowing for a better hypothesis selection.
- The **true error remains relatively constant**, with slight fluctuations. This behavior is expected because the true error is an inherent property of the hypothesis and the true distribution \( P \), which do not change with sample size.
- Overall, we observe the expected trend where **as \( n \) increases, the empirical and true errors converge**, demonstrating the consistency of the ERM algorithm.

---


