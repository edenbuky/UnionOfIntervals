# Results & Analysis 📊

## **Union of Intervals - Problem Description**

In this assignment, we study the hypothesis class of a **finite union of disjoint intervals** and analyze the properties of the **Empirical Risk Minimization (ERM) algorithm** for this class.

Let the sample space be 𝒳 = [0,1] and consider a **binary classification problem**, where 𝒴 = \{0,1\} . We aim to learn using a hypothesis class consisting of **𝒌 disjoint intervals**.

### **Mathematical Formulation**
We define a hypothesis class of disjoint intervals as follows:

Let 𝐼 be a set of  𝑘 disjoint intervals:
𝐼 = \{[𝓁₁, 𝓊₁], [𝓁₂, 𝓊₂], ..., [𝓁ₖ, 𝓊ₖ]\}
where the intervals are ordered such that:
0 ≤ 𝓁₁ ≤ 𝓊₁ ≤ 𝓁₂ ≤ 𝓊₂ ≤ ... ≤ 𝓊ₖ ≤ 1

For each such set 𝐼, define the corresponding hypothesis function:
\[ hₗ(x) = \begin{cases} 1, & \text{if } x \in [l_1, u_1] \cup \dots \cup [l_k, u_k] \\ 0, & \text{otherwise} \end{cases} \]
<img width="775" alt="Screenshot 2025-02-11 at 15 04 49" src="https://github.com/user-attachments/assets/38b17e99-462b-470d-beb7-5e0ccae55196" />

The hypothesis class \( \mathcal{H}_k \) consists of all possible such hypotheses:
ℋₖ = \{ hₗ | I = \{[𝓁₁, 𝓊₁], ..., [𝓁ₖ, 𝓊ₖ]\}, 0 ≤ 𝓁₁ ≤ 𝓊₁ ≤ 𝓁₂ ≤ 𝓊₂ ≤ ... ≤ 𝓊ₖ ≤ 1 \}

We are given a labeled sample of size \( n \):
\[ (x_1, y_1), ..., (x_n, y_n) \]
where the points \( x_i \) are sorted in increasing order: \( 0 \leq x_1 < x_2 < ... < x_n \leq 1 \).

---

## **(a) Hypothesis Selection with Minimum Error**

### **Problem Statement**
We assume the true distribution \( P[x, y] = P[y|x] \cdot P[x] \) is given as follows:
- \( x \) is uniformly distributed over \([0,1]\).
- The conditional probability \( P[y=1|x] \) is defined as:
  \[
  P[y=1|x] = \begin{cases} 
  0.8, & \text{if } x \in [0,0.2] \cup [0.4,0.6] \cup [0.8,1] \\
  0.1, & \text{if } x \in (0.2,0.4) \cup (0.6,0.8)
  \end{cases}
  \]
- Since \( P[y=0|x] = 1 - P[y=1|x] \), we can compute the exact error \( e_P(h) \) for any hypothesis \( h \in \mathcal{H}_k \).

### **Solution**
For \( h \in \mathcal{H}_{10} \), the error is computed as:
\[
  e_P(h) = \mathbb{E}_{(X,Y) \sim P} \left[ \Delta_{zo}(h(X),Y) \right] = \sum_{(X,Y) \in \mathcal{X} \times \mathcal{Y}} P(X,Y) \Delta_{zo}(h(X),Y)
\]
Since \( X \) is uniformly distributed over \([0,1]\), we use \( P(X,Y) = P(Y|X)P(X) \) to rewrite:
\[
  e_P(h) = \int_0^1 P[Y=1|x] \Delta_{zo}(h(X),1)dx + \int_0^1 P[Y=0|x] \Delta_{zo}(h(X),0)dx
\]
We focus only on cases where \( \Delta_{zo} \neq 0 \), meaning incorrect predictions:
- \( I_1 \): Intervals where \( h(X)=1 \) and \( P(Y=1|X) = 0.8 \) (no error, ignored)
- \( I_2 \): Intervals where \( h(X)=1 \) and \( P(Y=1|X) = 0.1 \) (error occurs)
- \( I_3 \): Intervals where \( h(X)=0 \) and \( P(Y=1|X) = 0.8 \) (error occurs)
- \( I_4 \): Intervals where \( h(X)=0 \) and \( P(Y=1|X) = 0.1 \) (no error, ignored)

Thus, the expected error simplifies to:
\[
  e_P(h) = \int_{I_2} 0.1dx + \int_{I_3} (1-0.8)dx = 0.1|I_2| + 0.2|I_3|
\]
To minimize error, we aim to keep \( I_2 \) and \( I_3 \) as small as possible. One approach is to introduce a small unit \( \varepsilon > 0 \) at the interval edges, ensuring exactly 10 disjoint segments:
\[
  \min_{n_1, n_2 \in \mathbb{N}} \{ 0.1 n_1 \cdot \varepsilon + 0.2 n_2 \cdot \varepsilon \}
\]
where:
- \( n_1 \) is the number of intervals added to the complement of \([0,0.2] \cup [0.4,0.6] \cup [0.8,1]\)
- \( n_2 \) is the number of intervals removed from \([0,0.2] \cup [0.4,0.6] \cup [0.8,1]\)

This ensures the best hypothesis \( h \in \mathcal{H}_{10} \) has the smallest possible classification error.

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
#### **Graph:**
![Empirial VS true Error](empiricalVStrueError.png)

---

## **(c) Error Behavior as a Function of \( k \)**

### **Problem Statement**
We draw a sample of size \( n = 1500 \) and find the best ERM hypothesis for \( k = 1, 2, ..., 10 \). We then plot the empirical and true errors as a function of \( k \) and analyze how the error behaves. We also define \( k^* \) to be the \( k \) with the smallest empirical error for ERM and discuss whether this makes \( k^* \) a good choice.

### **Solution & Analysis**
- In this experiment, we observed that \( k^* = 9 \) yielded the smallest empirical error.
- However, this does not necessarily mean that \( \mathcal{H}_{k^*} \) is the best hypothesis class. This is because it may lead to **overfitting**, where the selected hypothesis is overly complex and fits the training set too closely, capturing unnecessary noise.
- A hypothesis that generalizes well should have both **low true error** and **low empirical error**. While \( k^* \) minimizes the empirical error, it may not perform well on new data.
- A simpler model with a slightly higher empirical error but a lower true error could be a better choice for generalization.

#### **Graph:**
![Empirial and true Error](empiricalANDtrueError.png)

