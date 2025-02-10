# Results & Analysis 📊

## 1. Union Of Intervals
In this question, we will study the hypothesis class of a finite union of disjoint intervals, and the properties of the ERM algorithm for this class.

To review, let the sample space be \( \mathcal{X} = [0,1] \) and consider a binary classification problem, i.e., \( \mathcal{Y} = \{0,1\} \). We will try to learn using a hypothesis class that consists of \( k \) intervals. More explicitly, let \( I = \{ [l_1, u_1], \dots, [l_k, u_k] \} \) be \( k \) disjoint intervals such that \( 0 \leq l_1 \leq u_1 \leq l_2 \leq \dots \leq u_k \leq 1 \). For each such \( k \) disjoint intervals, define the corresponding hypothesis as:

\[
h_I(x) = \begin{cases} 
1 & \text{if } x \in [l_1, u_1] \cup \dots \cup [l_k, u_k] \\
0 & \text{otherwise} 
\end{cases}
\]

Finally, define \( \mathcal{H}_k \) as the hypothesis class that consists of all hypotheses that correspond to \( k \) disjoint intervals:

\[
\mathcal{H}_k = \{ h_I | I = \{ [l_1, u_1], \dots, [l_k, u_k] \}, 0 \leq l_1 \leq u_1 \leq l_2 \leq \dots \leq u_k \leq 1 \}
\]

We are given a sample of size \( n \): \( (x_1, y_1), \dots, (x_n, y_n) \). Assume that the points are sorted, so that \( 0 \leq x_1 \leq x_2 \leq \dots \leq x_n \leq 1 \).

---

### (a) (8 points)
Assume that the true distribution \( P[x,y] = P[y|x] \cdot P[x] \) is as follows:

\[
P[y=1|x] = \begin{cases} 
0.8 & \text{if } x \in [0, 0.2] \cup [0.4, 0.6] \cup [0.8, 1] \\
0.1 & \text{if } x \in (0.2, 0.4) \cup (0.6, 0.8) 
\end{cases}
\]

And \( P[y=0|x] = 1 - P[y=1|x] \). Since we know the true distribution \( P \), we can calculate \( e_P(h) \) precisely for any hypothesis \( h \in \mathcal{H}_k \). What is the hypothesis in \( \mathcal{H}_{10} \) with the smallest error (i.e., \( \text{argmin}_{h \in \mathcal{H}_{10}} e_P(h) \))?

#### **Answer:**
עבור \( h \in H_{10} \) מתקיים כי:

\[
e_P(h) = \mathbb{E}_{(X,Y) \sim P}[\Delta_{zo}(h(X,Y))] = \sum_{(X,Y) \in \mathcal{X} \times \mathcal{Y}} P(X,Y) \Delta_{zo}(h(X),Y)
\]

כיוון ש-\( X \) מתפלג אחיד מעל [0,1], נשתמש ב-\( P(X,Y) = P(Y|X)P(X) \) ולכן:

\[
e_P(h) = \int_0^1 P[Y=1|x]\Delta_{zo}(h(X),1)dx + \int_0^1 P[Y=0|x]\Delta_{zo}(h(X),0)dx
\]

בעצם נרצה להתעלם מהמקרים בהם \( \Delta_{zo}(h(X),0)=0 \) או \( \Delta_{zo}(h(X),1)=1 \).

נגדיר את האינטרוולים הבאים:
- **\( I_1 \)** – אוסף האינטרוולים בהם \( h(X)=1 \) ו-\( P(Y=1|X)=0.8 \) → במקרה זה האינטגרל יתאפס בגלל \( \Delta_{zo} \).
- **\( I_2 \)** – אוסף האינטרוולים בהם \( h(X)=1 \) ו-\( P(Y=1|X)=0.1 \) → זו טעות של ההיפותזה ולכן \( \Delta_{zo} \) תחזיר 1.
- **\( I_3 \)** – אוסף האינטרוולים בהם \( h(X)=0 \) ו-\( P(Y=1|X)=0.8 \) → גם זו טעות של ההיפותזה ולכן \( \Delta_{zo} \) תחזיר 1.
- **\( I_4 \)** – אוסף האינטרוולים בהם \( h(X)=0 \) ו-\( P(Y=1|X)=0.1 \) → במקרה זה האינטגרל יתאפס.

מעניין אותנו רק אינטרוולים \( I_2 \) ו-\( I_3 \):

\[
e_P(h) = \int_{I_2} 0.1dx + \int_{I_3} (1-0.8)dx = 0.1|I_2| + 0.2|I_3|
\]

נרצה אינטרוולים כמה שיותר קטנים שמוכלים ב-\( I_2 \) ו-\( I_3 \).
דרך אחת היא לבחור יחידה \( \varepsilon > 0 \) מזערית מאוד ולהוסיף או להחסיר אותה בין האינטרוולים \( [0,0.2] \cup [0.4,0.6] \cup [0.8,1] \) כך שנקבל חלוקה ל-10 אינטרוולים.

נרצה:
\[
\min_{n_1 ,n_2 \in \mathbb{N}} \{0.1n_1 \cdot \varepsilon + 0.2n_2 \cdot \varepsilon\}
\]

כאשר \( n_1 \) הוא כמות האינטרוולים שהוספנו להם קטע \( \varepsilon \) מהמשלים של \( [0,0.2] \cup [0.4,0.6] \cup [0.8,1] \) ו-\( n_2 \) הוא מספר הקטעים שהסרנו להם \( \varepsilon \) מ-\( [0,0.2] \cup [0.4,0.6] \cup [0.8,1] \).

---
