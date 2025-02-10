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

## **Experimental Analysis and Results**

_(The following sections will include the experimental results and analysis from the implementation of the algorithm. Please provide the next question so I can continue adding the details!)_

