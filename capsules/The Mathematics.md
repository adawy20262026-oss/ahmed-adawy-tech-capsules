# The Mathematics of Generative AI: From Probability to Language Models

**Author:** Ahmed Adawy  
**Category:** General / Professional Technical Capsule  
**Difficulty:** Beginner  
**Language:** English  
**Version:** 1.0  
**Release:** 2026  

---

## Table of Contents

- [Preface](#preface)
- [Chapter 1: The Probabilistic View of AI](#chapter-1-the-probabilistic-view-of-ai)
- [Chapter 2: Random Variables and Probability Distributions](#chapter-2-random-variables-and-probability-distributions)
- [Chapter 3: Conditional Probability and Bayes' Theorem](#chapter-3-conditional-probability-and-bayes-theorem)
- [Chapter 4: Maximum Likelihood and Learning from Data](#chapter-4-maximum-likelihood-and-learning-from-data)
- [Chapter 5: Information Theory](#chapter-5-information-theory)
- [Chapter 6: Cross-Entropy and Language Models](#chapter-6-cross-entropy-and-language-models)
- [Chapter 7: Softmax, Temperature, and Sampling](#chapter-7-softmax-temperature-and-sampling)
- [Chapter 8: From Probability to Text Generation](#chapter-8-from-probability-to-text-generation)
- [Chapter 9: Perplexity and Measuring Language Models](#chapter-9-perplexity-and-measuring-language-models)
- [Chapter 10: Building a Tiny Probabilistic Language Model](#chapter-10-building-a-tiny-probabilistic-language-model)
- [Chapter 11: Putting Everything Together](#chapter-11-putting-everything-together)
- [Chapter 12: Final Project](#chapter-12-final-project)
- [Chapter 13: Practical Probability Labs](#chapter-13-practical-probability-labs)
- [Chapter 14: Numerical Stability in Generative AI](#chapter-14-numerical-stability-in-generative-ai)
- [Chapter 15: From Bigram Models to Neural Language Models](#chapter-15-from-bigram-models-to-neural-language-models)
- [Chapter 16: Designing a Small Text Generator](#chapter-16-designing-a-small-text-generator)
- [Conclusion](#conclusion)
- [Appendix A: Essential Equations](#appendix-a-essential-equations)
- [Appendix B: Python Mathematical Toolkit](#appendix-b-python-mathematical-toolkit)
- [Appendix C: A Mental Model for Language Models](#appendix-c-a-mental-model-for-language-models)
- [Appendix D: Worked Problems and Review Exercises](#appendix-d-worked-problems-and-review-exercises)
- [Final Review: The Mathematical Loop](#final-review-the-mathematical-loop)

---

## Preface

Generative AI often looks mysterious from the outside.

A language model receives a sequence of tokens and produces another token. It can complete a paragraph, answer a question, write code, summarize an article, or generate an explanation.

But underneath all of these impressive behaviors is a mathematical idea that is much simpler than it first appears:

> **The model estimates which tokens are likely to appear given the tokens that came before them.**

That single idea connects language modeling to probability theory, statistics, information theory, optimization, and numerical computation.

This book explores that connection. The goal is not to hide the mathematics behind a framework or an API. Instead, we will build the concepts from first principles and use Python and NumPy to make them concrete.

You do not need advanced mathematics to begin. You need curiosity, basic algebra, and a willingness to follow the equations. By the end of the book, you should understand not only what a language model does, but why probability is at the center of generative AI.

---

## Chapter 1: The Probabilistic View of AI

### 1.1 What Does a Language Model Actually Predict?

Consider the sentence:

> *"The cat sat on the ___"*

What comes next? A language model might assign probabilities such as:

| Token | Probability |
| :--- | :--- |
| `mat` | $0.42$ |
| `floor` | $0.18$ |
| `chair` | $0.07$ |
| `table` | $0.05$ |
| `street` | $0.01$ |

The model does not necessarily "know" that the answer is *mat*. Instead, it estimates a probability distribution over possible next tokens.

Mathematically:
$$P(x_t \mid x_1, x_2, \dots, x_{t-1})$$

This means:
$$P(	ext{"mat"} \mid 	ext{"The", "cat", "sat", "on", "the"})$$

That is the fundamental prediction problem of an autoregressive language model.

---

### 1.2 Probability as a Language of Uncertainty

Probability gives us a way to describe uncertainty.

If we say:
$$P(A) = 1.0$$
then event $A$ is certain.

If:
$$P(A) = 0.0$$
then event $A$ is impossible.

For any event:
$$0 \le P(A) \le 1$$

A language model typically produces many probabilities whose sum is one:
$$\sum_{x} P(x) = 1.0$$

For example:
- $P(	ext{"cat"}) = 0.50$
- $P(	ext{"dog"}) = 0.30$
- $P(	ext{"bird"}) = 0.20$

Then:
$$0.50 + 0.30 + 0.20 = 1.0$$

---

### 1.3 Why Probability Is Central to Generative AI

Generative AI is about producing new data. A model needs a mechanism for deciding what to generate. Probability provides exactly that mechanism.

Instead of saying: *"Always output the single word 'cat'"*, we can say: *"Output 'cat' with probability 0.70, 'dog' with probability 0.20, and 'bird' with probability 0.10."*

This creates variation. Suppose the model predicts:

```text
cat     0.70
dog     0.20
bird    0.10
```

- **Greedy generation** always chooses: `cat`
- **Sampling** can sometimes choose: `dog` or `bird`

The probability distribution therefore becomes the bridge between prediction and generation.

---

### 1.4 Tokens Instead of Words

Modern language models usually do not operate directly on words. They operate on tokens.

A token may represent:
- A complete word
- Part of a word
- Punctuation
- Whitespace
- A symbol

For example, `"mathematics"` might be represented conceptually as:
`["math", "ematics"]`

The exact tokenization depends on the tokenizer. The model ultimately predicts a probability distribution over the vocabulary. If the vocabulary has size $V$, the model produces:
$$P(x_1), P(x_2), \dots, P(x_V)$$
with:
$$\sum_{i=1}^{V} P(x_i) = 1.0$$

---

### 1.5 A Simple Python Example

```python
import numpy as np

tokens = ["cat", "dog", "bird"]
probabilities = np.array([0.5, 0.3, 0.2])

print(probabilities.sum())
# Output: 1.0

# We can sample from this distribution:
choice = np.random.choice(
    tokens,
    p=probabilities
)
print(choice)
```

The result is random, but not equally random. `cat` is more likely than `bird`.

---

### 1.6 The Central Idea

A language model can be viewed as a function:
$$	ext{Context} \longrightarrow 	ext{Probability Distribution over Next Token}$$

For example: `"The cat sat on the"` becomes:

```text
mat     0.42
floor   0.18
chair   0.07
```

The rest of generative text generation is built on top of this idea.

---

## Chapter 2: Random Variables and Probability Distributions

### 2.1 Random Variables

A random variable is a mathematical representation of an uncertain outcome. Suppose $X$ is the next token. If our vocabulary is `["cat", "dog", "bird"]`, then $X$ can take one of those values.

We can assign probabilities:
- $P(X = 	ext{"cat"}) = 0.50$
- $P(X = 	ext{"dog"}) = 0.30$
- $P(X = 	ext{"bird"}) = 0.20$

---

### 2.2 Discrete Probability Distributions

Language-model tokens are discrete outcomes. A discrete distribution can be represented as:
$$P(X = x_i) = p_i \quad 	ext{for every possible token } x_i$$

The probabilities must satisfy:
$$p_i \ge 0$$
and:
$$\sum_{i} p_i = 1.0$$

---

### 2.3 Expected Value

The expected value represents the weighted average outcome. For a discrete variable:
$$\mathbb{E}[X] = \sum_{i} x_i P(X = x_i)$$

For language tokens, numerical interpretation of the token itself is usually not meaningful. However, expected values become extremely useful when we work with numerical quantities such as losses, rewards, and model scores.

---

### 2.4 Variance

Variance measures how spread out a random variable is:
$$	ext{Var}(X) = \mathbb{E}\left[(X - \mathbb{E}[X])^2
ight]$$

Standard deviation is:
$$\sigma = \sqrt{	ext{Var}(X)}$$

Although language generation does not require us to manually calculate token variance at every step, the idea of uncertainty remains fundamental.

---

### 2.5 Probability Vectors

A probability distribution over a vocabulary can be stored as a vector.

```python
import numpy as np

p = np.array([
    0.50,
    0.30,
    0.20
])

print(p)
print(p.sum())
```

This vector is the model's belief about the next token.

---

### 2.6 From Scores to Probabilities

Neural networks usually do not directly output probabilities. They output scores called **logits**.

Suppose:
```python
logits = np.array([
    2.0,
    1.0,
    0.1
])
```

These values are not probabilities. They can be converted into probabilities using **softmax**:

$$	ext{softmax}(z)_i = rac{e^{z_i}}{\sum_{j} e^{z_j}}$$

```python
import numpy as np

def softmax(x):
    exp_x = np.exp(x - np.max(x))
    return exp_x / exp_x.sum()

logits = np.array([2.0, 1.0, 0.1])
probabilities = softmax(logits)

print(probabilities)
print(probabilities.sum())
```

The subtraction of the maximum value improves numerical stability.

---

### 2.7 Why Exponentials?

The exponential function $e^x$ has useful properties:
$$e^x > 0 \quad 	ext{for every real number } x$$

Therefore all softmax outputs are positive. Normalization then forces the total to equal one. Softmax therefore transforms arbitrary real-valued scores into a valid probability distribution.

---

## Chapter 3: Conditional Probability and Bayes' Theorem

### 3.1 Probability Depends on Context

Consider: `"The cat swam across the ___"`  
Possible next tokens might include: `river`, `lake`, `pool`.

But now consider: `"The train moved down the ___"`  
The context changes the prediction to: `track`, `rails`, `line`.

This is **conditional probability**.

---

### 3.2 Conditional Probability

The probability of $A$ given $B$ is:
$$P(A \mid B) = rac{P(A \cap B)}{P(B)} \quad 	ext{provided } P(B) > 0$$

In language modeling:
$$P(	ext{next token} \mid 	ext{context})$$
is the central quantity.

---

### 3.3 Joint Probability

Joint probability describes two events occurring together:
$$P(A \cap B) = P(A \mid B) P(B)$$

This equation is extremely important.

---

### 3.4 The Chain Rule

For a sequence $x_1, x_2, \dots, x_n$, the probability of the entire sequence can be decomposed as:
$$P(x_1, x_2, \dots, x_n) = P(x_1) P(x_2 \mid x_1) P(x_3 \mid x_1, x_2) \dots P(x_n \mid x_1, \dots, x_{n-1})$$

$$\prod_{i=1}^{n} P(x_i \mid x_1, \dots, x_{i-1})$$

This is the mathematical foundation of autoregressive language modeling.

---

### 3.5 Language Models and the Chain Rule

Suppose the sentence is: `"The cat sat"`

A language model can estimate $P(	ext{"The cat sat"})$ as:
$$P(	ext{"The"}) 	imes P(	ext{"cat"} \mid 	ext{"The"}) 	imes P(	ext{"sat"} \mid 	ext{"The cat"})$$

For a longer sentence, we continue the process. This means that generating a sentence can be understood as repeatedly predicting the next token.

---

### 3.6 Bayes' Theorem

Bayes' theorem is:
$$P(A \mid B) = rac{P(B \mid A) P(A)}{P(B)}$$

It allows us to reverse conditional relationships. Although modern neural language models are not simply "Bayesian systems," Bayes' theorem is an essential part of probabilistic thinking.

---

### 3.7 Example

Suppose a medical test detects a condition. Let:
- $D$: disease present
- $T$: test positive

Suppose:
- $P(D) = 0.01$ (prior probability)
- $P(T \mid D) = 0.95$ (sensitivity)
- $P(T \mid 
eg D) = 0.05$ (false positive rate)

Then:
$$P(T) = P(T \mid D)P(D) + P(T \mid 
eg D)P(
eg D)$$
$$P(T) = (0.95 	imes 0.01) + (0.05 	imes 0.99) = 0.0095 + 0.0495 = 0.0590$$

Bayes gives:
$$P(D \mid T) = rac{0.95 	imes 0.01}{0.0590} pprox 0.161 \quad (16.1\%)$$

The lesson is important: **The prior probability matters.**

---

## Chapter 4: Maximum Likelihood and Learning from Data

### 4.1 Where Do Probabilities Come From?

A language model cannot simply invent its probability distribution. It must learn parameters from data.

Suppose a model has parameters $	heta$. The model represents $P_	heta(x \mid 	ext{context})$. The goal is to find parameters $	heta$ that make observed training data probable.

---

### 4.2 Likelihood

Suppose our dataset contains independent observations $x_1, x_2, \dots, x_N$. The likelihood function is:
$$L(	heta) = \prod_{i=1}^{N} P_	heta(x_i)$$

We want parameters that maximize this likelihood:
$$rg\max_{	heta} L(	heta)$$

This is **Maximum Likelihood Estimation (MLE)**.

---

### 4.3 Why Products Become Difficult

If the dataset contains thousands or millions of examples, multiplying probabilities can produce extremely small numbers (underflow). For example:
$$0.1^{100} = 10^{-100}$$

Instead, we use logarithms. Because $\log(a 	imes b) = \log(a) + \log(b)$:
$$\log L(	heta) = \sum_{i=1}^{N} \log P_	heta(x_i)$$

Maximizing likelihood is equivalent to maximizing log-likelihood.

---

### 4.4 Negative Log-Likelihood

Machine learning systems usually minimize a loss function. Therefore we define **Negative Log-Likelihood (NLL)**:
$$	ext{NLL}(	heta) = -\sum_{i=1}^{N} \log P_	heta(x_i)$$

Minimizing NLL is equivalent to maximizing likelihood. This is one of the most important connections between probability and machine learning optimization.

---

### 4.5 A Tiny Example

Suppose the correct token has predicted probability $p = 0.8$. Its negative log-likelihood is:
$$	ext{Loss} = -\log(0.8) pprox 0.223$$

```python
import numpy as np

p = 0.8
loss = -np.log(p)
print(loss)  # 0.2231435513142097
```

If the model predicts $p = 0.01$:
```python
p = 0.01
loss = -np.log(p)
print(loss)  # 4.605170185988092
```

The model is strongly penalized for assigning very low probability to the correct answer.

---

### 4.6 Learning Means Adjusting Probability

This gives us a powerful interpretation:
> **Training a language model means adjusting its parameters so that correct tokens receive higher probability.**

The model repeatedly observes: `context -> correct next token` and modifies its parameters. Over time:
$$P(	ext{correct token} \mid 	ext{context}) \longrightarrow 1.0$$

---

## Chapter 5: Information Theory

### 5.1 What Is Information?

Information theory gives us mathematical tools for measuring uncertainty and surprise. One of the most famous quantities is **information content** (or self-information). For an event with probability $p$:
$$I(x) = -\log_2 P(x)$$

- A rare event contains **more information** (high surprise).
- A common event contains **less information** (low surprise).

---

### 5.2 Example

- If $P(x) = 0.5$, then $I(x) = -\log_2(0.5) = 1 	ext{ bit}$.
- If $P(x) = 0.01$, then $I(x) = -\log_2(0.01) pprox 6.64 	ext{ bits}$.

The less expected an event is, the more surprising it is.

---

### 5.3 Entropy

**Entropy** measures the average uncertainty of a probability distribution:
$$H(X) = -\sum_{x} P(x) \log_2 P(x)$$

Using base 2 gives entropy in **bits**.

---

### 5.4 Maximum Entropy

Suppose we have three equally likely outcomes: $p = [1/3, 1/3, 1/3]$. There is significant uncertainty.

But suppose $p = [0.98, 0.01, 0.01]$. The outcome is much more predictable.

Therefore **entropy is high when probability is spread out** and **low when one outcome dominates**.

---

### 5.5 Python Implementation

```python
import numpy as np

def entropy(probabilities):
    probabilities = np.asarray(probabilities)
    probabilities = probabilities[probabilities > 0]
    return -np.sum(probabilities * np.log2(probabilities))

p1 = np.array([1/3, 1/3, 1/3])
p2 = np.array([0.98, 0.01, 0.01])

print("Entropy p1:", entropy(p1))  # ~1.585 bits
print("Entropy p2:", entropy(p2))  # ~0.161 bits
```

---

### 5.6 Why Entropy Matters for Language

Consider two contexts:

- **Context A:** *"The capital of France is ___"*  
  The next token is highly predictable (`Paris`). Entropy is low.
- **Context B:** *"I wonder what will happen tomorrow when ___"*  
  Many continuations are possible. Entropy is higher.

A language model must learn these differences in uncertainty.

---

### 5.7 Cross-Entropy

**Cross-entropy** measures how well one probability distribution $q$ represents another true distribution $p$:
$$H(p, q) = -\sum_{x} p(x) \log q(x)$$

In supervised language modeling, the target distribution $p$ is represented as a one-hot vector. If the correct token is $k$:
$$p(k) = 1, \quad p(x 
eq k) = 0$$

Then cross-entropy becomes:
$$H(p, q) = -\log q(k)$$

This is exactly the **negative log-likelihood** of the correct token.

---

## Chapter 6: Cross-Entropy and Language Models

### 6.1 The Training Objective

Suppose the vocabulary contains `["cat", "dog", "bird"]`. The correct token is `cat`.

- Target distribution $p$: `[1, 0, 0]`
- Model prediction $q$: `[0.7, 0.2, 0.1]`

Cross-entropy is:
$$	ext{Loss} = -(1 \cdot \log(0.7) + 0 \cdot \log(0.2) + 0 \cdot \log(0.1)) = -\log(0.7) pprox 0.356$$

---

### 6.2 Python

```python
import numpy as np

target = np.array([1, 0, 0])
prediction = np.array([0.7, 0.2, 0.1])

loss = -np.sum(target * np.log(prediction))
print("Cross-entropy loss:", loss)
```

---

### 6.3 What Happens When the Model Is Wrong?

Suppose `prediction = [0.01, 0.49, 0.50]`. The model gives the correct token only 1% probability.

$$	ext{Loss} = -\log(0.01) pprox 4.605$$

This creates a strong learning signal for optimization.

---

### 6.4 Cross-Entropy and Softmax

In a neural language model, we have the following processing pipeline:

```text
hidden representation
         │
         ▼
 linear projection
         │
         ▼
      logits
         │
         ▼
      softmax
         │
         ▼
 probabilities
         │
         ▼
  cross-entropy
```

This pipeline is one of the central computational patterns in modern language models.

---

### 6.5 Stable Softmax

Naively calculating `np.exp(logits)` can overflow for large logits. Instead:

```python
def stable_softmax(logits):
    shifted = logits - np.max(logits)
    exp_values = np.exp(shifted)
    return exp_values / np.sum(exp_values)
```

Subtracting the maximum value does not change the resulting probabilities because softmax is invariant to adding or subtracting a constant from every logit:
$$rac{e^{z_i - c}}{\sum_j e^{z_j - c}} = rac{e^{-c} e^{z_i}}{e^{-c} \sum_j e^{z_j}} = rac{e^{z_i}}{\sum_j e^{z_j}}$$

---

### 6.6 Stable Cross-Entropy

A numerically stable implementation can operate directly on logits without explicitly computing full softmax probabilities first:

```python
import numpy as np

def cross_entropy_from_logits(logits, target_index):
    max_logit = np.max(logits)
    shifted = logits - max_logit
    log_sum_exp = max_logit + np.log(np.sum(np.exp(shifted)))
    return log_sum_exp - logits[target_index]
```

---

## Chapter 7: Softmax, Temperature, and Sampling

### 7.1 Why Sampling Matters

Suppose a model predicts:
- `mat`: $0.60$
- `floor`: $0.25$
- `chair`: $0.10$
- `street`: $0.05$

Greedy decoding always selects `mat`. But generative AI often needs diversity and creativity. Sampling allows the model to choose tokens according to their predicted probability distribution.

---

### 7.2 Categorical Sampling

```python
import numpy as np

tokens = ["mat", "floor", "chair", "street"]
probabilities = np.array([0.60, 0.25, 0.10, 0.05])

token = np.random.choice(tokens, p=probabilities)
print("Sampled token:", token)
```

---

### 7.3 Temperature

Temperature $T$ modifies the sharpness of the distribution:
$$P(x_i) = rac{e^{z_i / T}}{\sum_j e^{z_j / T}}$$

where $z_i$ are the logits and $T > 0$ is the temperature parameter.

---

### 7.4 Low Temperature ($T < 1.0$)

If $T = 0.5$, the logits are scaled up ($z_i / 0.5 = 2 z_i$), making differences between logits larger. The distribution becomes sharper, and high-probability tokens dominate. This produces more focused and predictable text.

---

### 7.5 High Temperature ($T > 1.0$)

If $T = 2.0$, the logits are scaled down ($z_i / 2.0 = 0.5 z_i$), smoothing out differences. The distribution becomes flatter, making lower-probability tokens more likely to be selected. This increases variety but can reduce coherence.

---

### 7.6 Python Implementation

```python
import numpy as np

def temperature_softmax(logits, temperature=1.0):
    scaled = logits / temperature
    shifted = scaled - np.max(scaled)
    exp_values = np.exp(shifted)
    return exp_values / exp_values.sum()

logits = np.array([3.0, 2.0, 1.0, 0.0])

print("T = 0.5:", temperature_softmax(logits, temperature=0.5))
print("T = 1.0:", temperature_softmax(logits, temperature=1.0))
print("T = 2.0:", temperature_softmax(logits, temperature=2.0))
```

---

### 7.7 Top-k Sampling

Top-k sampling restricts choices to the $k$ highest-probability tokens.

```python
import numpy as np

def top_k_filter(probabilities, k):
    indices = np.argsort(probabilities)[-k:]
    filtered = np.zeros_like(probabilities)
    filtered[indices] = probabilities[indices]
    filtered /= filtered.sum()
    return filtered
```

---

### 7.8 Why Sampling Is Not the Same as Random Guessing

Random guessing treats all tokens equally ($P(x_i) = 1/V$). Sampling from a language model samples according to learned probabilities. The distribution reflects rich linguistic patterns learned from training data.

---

## Chapter 8: From Probability to Text Generation

### 8.1 Autoregressive Generation

The basic generation loop is simple:

1. Start with a prompt: `"The future of AI"`
2. Predict the probability distribution for the next token.
3. Sample or select a token.
4. Append it to the context.
5. Repeat.

Mathematically:
$$x_t \sim P(x_t \mid x_1, x_2, \dots, x_{t-1})$$

---

### 8.2 Conceptual Algorithm

```text
       prompt
         │
         ▼
       model
         │
         ▼
   probabilities
         │
         ▼
     sampling
         │
         ▼
     new token
         │
         ▼
   append token
         │
         └────────► model again
```

---

### 8.3 A Tiny Bigram Model

Consider the training corpus:
```text
the cat sat
the cat slept
the dog sat
the dog ran
```

We count transition frequencies:
- `the -> cat`: 2
- `the -> dog`: 2
- `cat -> sat`: 1
- `cat -> slept`: 1
- `dog -> sat`: 1
- `dog -> ran`: 1

Then:
$$P(	ext{"cat"} \mid 	ext{"the"}) = rac{2}{4} = 0.50$$
$$P(	ext{"dog"} \mid 	ext{"the"}) = rac{2}{4} = 0.50$$

---

### 8.4 Building Counts

```python
from collections import defaultdict, Counter

text = "the cat sat the cat slept the dog sat the dog ran"
tokens = text.split()

counts = defaultdict(Counter)
for a, b in zip(tokens, tokens[1:]):
    counts[a][b] += 1

print(counts["the"])
```

---

### 8.5 Converting Counts to Probabilities

```python
def transition_probabilities(counter):
    total = sum(counter.values())
    return {token: count / total for token, count in counter.items()}

print(transition_probabilities(counts["the"]))
```

---

### 8.6 Generating Text

```python
import numpy as np

def next_token(current):
    counter = counts[current]
    if not counter:
        return None
    tokens_list = list(counter.keys())
    probs = np.array([counter[t] for t in tokens_list], dtype=float)
    probs /= probs.sum()
    return np.random.choice(tokens_list, p=probs)

current = "the"
generated = [current]
for _ in range(10):
    current = next_token(current)
    if not current:
        break
    generated.append(current)

print(" ".join(generated))
```

---

### 8.7 What Does This Teach Us?

Our tiny bigram model has no neural network, no embeddings, and no attention mechanism. Yet it demonstrates the central idea of generative text generation: **Predicting next-token probability distributions and sampling from them iteratively.**

---

## Chapter 9: Perplexity and Measuring Language Models

### 9.1 Why Accuracy Is Not Enough

Suppose Model 1 predicts: $P(	ext{"cat"}) = 0.51, P(	ext{"dog"}) = 0.49$.  
Suppose Model 2 predicts: $P(	ext{"cat"}) = 0.99, P(	ext{"dog"}) = 0.01$.

If the actual next token is `cat`, both models achieve 100% classification accuracy. But Model 2 is far more confident and accurate in its probability assignment. We need a probabilistic metric.

---

### 9.2 Definition

For a sequence of $N$ tokens $x_1, x_2, \dots, x_N$, the **perplexity (PP)** is:

$$	ext{PP} = \exp\left( -rac{1}{N} \sum_{i=1}^{N} \log P(x_i \mid 	ext{context}) 
ight)$$

If using base-2 logarithms:
$$	ext{PP} = 2^{H}$$
where $H$ is the average cross-entropy per token in bits.

---

### 9.3 Interpretation

Lower perplexity indicates better performance. A perplexity of $10$ means the model is as uncertain on average as if it were choosing uniformly among 10 equally likely options at each step.

---

### 9.4 Python Implementation

```python
import numpy as np

probabilities = np.array([0.8, 0.6, 0.5, 0.9])
average_nll = -np.mean(np.log(probabilities))
perplexity = np.exp(average_nll)

print("Perplexity:", perplexity)
```

---

### 9.5 Perplexity and Model Comparison

When comparing models using perplexity, ensure they share:
- The exact same vocabulary
- The exact same tokenizer
- The exact same evaluation dataset and preprocessing

---

## Chapter 10: Building a Tiny Probabilistic Language Model

### 10.1 The Goal

We build a complete count-based language model laboratory that tokenizes text, builds transition tables, computes probabilities, samples text, and measures sequence likelihood.

---

### 10.2 Training Data

```python
corpus = [
    "the cat sat on the mat",
    "the cat slept on the mat",
    "the dog sat on the floor",
    "the dog slept on the floor",
    "the bird sat on the tree"
]
```

---

### 10.3 Tokenization

```python
sentences = [sentence.split() for sentence in corpus]
```

---

### 10.4 Bigram Counts

```python
from collections import defaultdict, Counter

bigram_counts = defaultdict(Counter)
for sentence in sentences:
    for a, b in zip(sentence, sentence[1:]):
        bigram_counts[a][b] += 1
```

---

### 10.5 Probability Table

```python
def probabilities_for(token):
    counter = bigram_counts[token]
    total = sum(counter.values())
    if total == 0:
        return {}
    return {next_token: count / total for next_token, count in counter.items()}

print("P(* | 'the'):", probabilities_for("the"))
```

---

### 10.6 Generation

```python
import numpy as np

def generate(start_token, length=10):
    current = start_token
    output = [current]
    for _ in range(length - 1):
        counter = bigram_counts.get(current)
        if not counter:
            break
        tokens_list = list(counter.keys())
        probs = np.array([counter[t] for t in tokens_list], dtype=float)
        probs /= probs.sum()
        current = np.random.choice(tokens_list, p=probs)
        output.append(current)
    return " ".join(output)

print(generate("the"))
```

---

### 10.7 The Problem with Raw Counts

A bigram model only looks back one token. `the cat` and `the dog` both share the exact same context `the`. To handle longer context, we need higher-order n-grams or neural models.

---

### 10.8 Laplace Smoothing

If a transition never appeared in training data, raw counting assigns $P = 0$, causing $\log(0) 	o -\infty$. **Laplace (Add-1) Smoothing** solves this:

$$P_{	ext{Laplace}}(y \mid x) = rac{	ext{count}(x, y) + lpha}{	ext{count}(x) + lpha V}$$

where $lpha > 0$ (typically $lpha = 1.0$) and $V$ is vocabulary size.

```python
def smoothed_probability(count, total, vocabulary_size, alpha=1.0):
    return (count + alpha) / (total + alpha * vocabulary_size)
```

---

## Chapter 11: Putting Everything Together

### 11.1 The Full Mathematical Pipeline

We can now map the full architecture of probabilistic text processing:

```text
Training Data ──► Tokenization ──► Context/Target Pairs
                                            │
                                            ▼
                                      Neural Network
                                            │
                                            ▼
                                          Logits
                                            │
                                            ▼
                                         Softmax
                                            │
                                            ▼
                                  Probability Vector
                                            │
                                            ▼
                                      Cross-Entropy
                                            │
                                            ▼
                                      Optimization ──► Updated Parameters
```

During generation:

```text
Prompt ──► Model ──► Logits ──► Temp/Filtering ──► Sampling ──► New Token
  ▲                                                                 │
  └─────────────────────────────────────────────────────────────────┘
```

---

### 11.2 Why the Same Mathematics Appears Everywhere

- **Probability:** Prediction, training, evaluation, sampling, uncertainty, generation.
- **Information Theory:** Entropy, cross-entropy, perplexity, compression.
- **Optimization:** Gradient descent, parameter updates, loss minimization.

---

## Chapter 12: Final Project

### 12.1 Project Requirements

Build a self-contained `MiniLanguageModel` in Python that can:
- Train on a corpus
- Calculate transition probabilities
- Compute entropy and perplexity
- Support temperature-scaled generation

---

### 12.2 Complete Implementation

```python
import numpy as np
from collections import defaultdict, Counter

class MiniLanguageModel:
    def __init__(self):
        self.counts = defaultdict(Counter)
        self.vocabulary = set()

    def train(self, corpus):
        for sentence in corpus:
            tokens = sentence.split()
            self.vocabulary.update(tokens)
            for a, b in zip(tokens, tokens[1:]):
                self.counts[a][b] += 1

    def probabilities(self, token):
        counter = self.counts[token]
        if not counter:
            return {}
        total = sum(counter.values())
        return {t: count / total for t, count in counter.items()}

    def entropy(self, token):
        probs = self.probabilities(token)
        if not probs:
            return 0.0
        values = np.array(list(probs.values()))
        return -np.sum(values * np.log2(values))

    def next_token(self, token, temperature=1.0):
        probs = self.probabilities(token)
        if not probs:
            return None
        tokens_list = list(probs.keys())
        values = np.array(list(probs.values()), dtype=float)
        
        logits = np.log(values + 1e-12) / temperature
        logits -= np.max(logits)
        exp_values = np.exp(logits)
        values = exp_values / exp_values.sum()
        
        return np.random.choice(tokens_list, p=values)

    def generate(self, start, length=20, temperature=1.0):
        output = [start]
        current = start
        for _ in range(length - 1):
            next_val = self.next_token(current, temperature)
            if next_val is None:
                break
            output.append(next_val)
            current = next_val
        return " ".join(output)
```

---

### 12.3 Testing the Implementation

```python
corpus = [
    "the cat sat on the mat",
    "the cat slept on the mat",
    "the dog sat on the floor",
    "the dog slept on the floor",
    "the bird sat on the tree",
    "the bird flew over the tree"
]

model = MiniLanguageModel()
model.train(corpus)

print("P('the'):", model.probabilities("the"))
print("Entropy('the'):", model.entropy("the"))
print("Generated (T=0.5):", model.generate("the", length=10, temperature=0.5))
print("Generated (T=1.0):", model.generate("the", length=10, temperature=1.0))
print("Generated (T=2.0):", model.generate("the", length=10, temperature=2.0))
```

---

## Chapter 13: Practical Probability Labs

### 13.1 Lab 1: Verify a Probability Distribution

```python
import numpy as np

tokens = ["cat", "dog", "bird"]
probabilities = np.array([0.50, 0.30, 0.20])

print("Sum:", probabilities.sum())
print("Min entry:", probabilities.min())
assert np.isclose(probabilities.sum(), 1.0)
assert (probabilities >= 0).all()
```

---

### 13.2 Lab 2: Compare Two Distributions

```python
import numpy as np

p = np.array([0.80, 0.10, 0.10])
q = np.array([0.34, 0.33, 0.33])

hp = -np.sum(p * np.log2(p))
hq = -np.sum(q * np.log2(q))

print("Entropy P (focused):", hp)  # ~0.92 bits
print("Entropy Q (flat):   ", hq)  # ~1.58 bits
```

---

### 13.3 Lab 3: Surprise

```python
import numpy as np

def information(probability):
    return -np.log2(probability)

for p in [0.5, 0.1, 0.01]:
    print(f"P={p:<5} -> Surprise={information(p):.2f} bits")
```

---

### 13.4 Lab 4: Conditional Probability from Counts

```python
counts = {"cat": 2, "dog": 2, "bird": 1}
total = sum(counts.values())

probabilities = {token: count / total for token, count in counts.items()}
print("Conditional probabilities:", probabilities)
```

---

### 13.5 Lab 5: Sampling Repeatedly

```python
import numpy as np

rng = np.random.default_rng(7)
tokens = np.array(["A", "B", "C"])
p = np.array([0.70, 0.20, 0.10])

samples = rng.choice(tokens, size=1000, p=p)
for token in tokens:
    freq = np.mean(samples == token)
    print(f"Token {token}: Empirical={freq:.3f}, True={p[tokens==token][0]}")
```

---

### 13.6 Lab 6: Temperature as a Controlled Transformation

```python
import numpy as np

def temperature_softmax(logits, temperature):
    scaled = logits / temperature
    shifted = scaled - np.max(scaled)
    exp_values = np.exp(shifted)
    return exp_values / exp_values.sum()

logits = np.array([3.0, 2.0, 1.0])
for temp in [0.5, 1.0, 2.0]:
    print(f"T={temp}:", temperature_softmax(logits, temp))
```

---

### 13.7 Lab 7: Greedy Decoding Versus Sampling

- **Greedy Decoding:** Deterministic ($T 	o 0$). Always picks $rg\max_x P(x)$.
- **Sampling:** Probabilistic ($T > 0$). Draws samples according to $P(x)$.

---

### 13.8 Lab 8: Why Seed Values Matter

```python
import numpy as np

rng1 = np.random.default_rng(42)
rng2 = np.random.default_rng(42)

a = rng1.choice(["A", "B", "C"], size=10)
b = rng2.choice(["A", "B", "C"], size=10)

print("Identical sequences:", np.array_equal(a, b))
```

---

### 13.9 Lab 9: A Small Numerical Sanity Checklist

- Are probabilities non-negative?
- Do probabilities sum to 1.0?
- Are logarithms safe from $\log(0)$?
- Is temperature positive ($T > 0$)?
- Is sampling reproducible with a fixed random seed?

---

## Chapter 14: Numerical Stability in Generative AI

### 14.1 The Overflow Problem

```python
import numpy as np

x = np.array([1000.0, 1001.0])
# np.exp(x)  # Causes OverflowError / Inf!
```

---

### 14.2 Stable Softmax

Subtracting $m = \max_i(z_i)$ guarantees that all exponent arguments are $\le 0$:

```python
def stable_softmax(x):
    x = np.asarray(x, dtype=float)
    shifted = x - np.max(x)
    exp_values = np.exp(shifted)
    return exp_values / exp_values.sum()
```

---

### 14.3 Log-Sum-Exp

Computing $\log \sum_{i} e^{z_i}$ safely:

$$	ext{LogSumExp}(z) = m + \log \sum_i e^{z_i - m} \quad 	ext{where } m = \max_i(z_i)$$

```python
def logsumexp(z):
    z = np.asarray(z, dtype=float)
    m = np.max(z)
    return m + np.log(np.sum(np.exp(z - m)))
```

---

### 14.4 Why Log Probabilities Are Useful

Instead of multiplying probabilities:
$$\prod_{i=1}^{N} P(x_i) \longrightarrow 	ext{underflow to 0}$$

We sum log probabilities:
$$\sum_{i=1}^{N} \log P(x_i)$$

---

### 14.5 Underflow and Zero Probabilities

```python
safe_probabilities = np.clip(probabilities, 1e-12, 1.0)
```

---

### 14.6 Floating-Point Equality

Use `np.isclose` instead of `==`:

```python
import numpy as np

print(np.isclose(0.1 + 0.2, 0.3))  # True
```

---

## Chapter 15: From Bigram Models to Neural Language Models

### 15.1 The Limitation of One-Token Context

A bigram model estimates $P(x_t \mid x_{t-1})$. It cannot remember long-range dependencies.

---

### 15.2 The Data Sparsity Problem

For context length $k$ and vocabulary size $V$, an n-gram table requires storing up to $V^k$ entries. For $V = 50,000$ and $k = 5$, $V^k = 3.125 	imes 10^{23}$ entries, making table lookup impossible.

---

### 15.3 Neural Representations

Neural models map discrete tokens into continuous vector spaces (embeddings) and represent context with deep neural networks:

```text
tokens ──► embeddings ──► context representation ──► neural network ──► logits ──► softmax ──► probabilities
```

---

### 15.4 Why Vectors Help

Token embeddings allow semantic generalization:
$$	ext{vec("cat")} pprox 	ext{vec("dog")}$$

---

### 15.5 From Local Counts to Learned Functions

- **N-gram / Bigram:** Table lookup ($	ext{context} 	o 	ext{counts}$).
- **Neural Language Model:** Parameterized function $f_	heta(	ext{context}) 	o 	ext{logits}$.

---

### 15.6 The Objective Does Not Disappear

Regardless of whether the model is a simple n-gram or a 70-billion-parameter Transformer, the loss function remains the same: **Cross-Entropy / Negative Log-Likelihood**.

---

### 15.7 Why Transformers Matter

Transformers use self-attention mechanisms to allow every token in a context to dynamically attend to every other token.

---

### 15.8 Causal Direction

Autoregressive models use **causal masking** so that predicting token at position $t$ only depends on positions $\le t$.

---

## Chapter 16: Designing a Small Text Generator

### 16.1 Define the Contract

Inputs:
- Training corpus
- Start token
- Generation length
- Temperature

Outputs:
- Generated token sequence

---

### 16.2 Separate the Components

```text
Tokenizer ──► Trainer ──► Probability Model ──► Decoder
```

---

### 16.3 A Compact Implementation

```python
import numpy as np
from collections import defaultdict, Counter

class SmallTextGenerator:
    def __init__(self, seed=42):
        self.counts = defaultdict(Counter)
        self.rng = np.random.default_rng(seed)

    def train(self, corpus):
        for sentence in corpus:
            tokens = sentence.split()
            for token in tokens:
                self.counts.setdefault(token, Counter())
            for a, b in zip(tokens, tokens[1:]):
                self.counts[a][b] += 1

    def probabilities(self, token):
        counter = self.counts.get(token)
        if not counter:
            return {}
        total = sum(counter.values())
        return {item: count / total for item, count in counter.items()}

    def next_token(self, token, temperature=1.0):
        probs = self.probabilities(token)
        if not probs:
            return None
        tokens_list = list(probs.keys())
        values = np.array(list(probs.values()), dtype=float)

        if temperature <= 0:
            raise ValueError("Temperature must be positive")

        logits = np.log(np.clip(values, 1e-12, 1.0)) / temperature
        logits -= np.max(logits)
        weights = np.exp(logits)
        weights /= weights.sum()

        return self.rng.choice(tokens_list, p=weights)

    def generate(self, start, length=20, temperature=1.0):
        output = [start]
        current = start
        for _ in range(length - 1):
            token = self.next_token(current, temperature)
            if token is None:
                break
            output.append(token)
            current = token
        return " ".join(output)
```

---

### 16.4 Training and Testing

```python
corpus = [
    "the cat sat on the mat",
    "the cat slept on the mat",
    "the dog sat on the floor",
    "the dog slept on the floor",
    "the bird sat on the tree",
    "the bird flew over the tree"
]

model = SmallTextGenerator(seed=42)
model.train(corpus)

print("T=0.5:", model.generate("the", length=12, temperature=0.5))
print("T=1.0:", model.generate("the", length=12, temperature=1.0))
print("T=2.0:", model.generate("the", length=12, temperature=2.0))
```

---

## Conclusion

Generative AI can appear enormously complicated. Modern language models contain billions of parameters, sophisticated architectures, large datasets, and powerful optimization systems.

But beneath that complexity is a mathematical structure that can be understood step by step:

1. The model observes data.
2. It learns statistical relationships.
3. It produces scores (logits).
4. Scores become probabilities via Softmax.
5. Probabilities define uncertainty.
6. Uncertainty is measured with Information Theory.
7. The probability assigned to the correct token creates a loss via Cross-Entropy / NLL.
8. During generation, the probability distribution selects the next token.
9. The loop repeats.

This is the mathematical heart of autoregressive generation.

---

## Appendix A: Essential Equations

### Probability Theory
- **Conditional Probability:**  
  $$P(A \mid B) = rac{P(A \cap B)}{P(B)}$$

- **Joint Probability:**  
  $$P(A \cap B) = P(A \mid B) P(B)$$

- **Bayes' Theorem:**  
  $$P(A \mid B) = rac{P(B \mid A) P(A)}{P(B)}$$

- **Chain Rule of Probability:**  
  $$P(x_1, \dots, x_n) = \prod_{i=1}^{n} P(x_i \mid x_1, \dots, x_{i-1})$$

### Information Theory & Loss Functions
- **Entropy:**  
  $$H(X) = -\sum_{x} P(x) \log_2 P(x)$$

- **Cross-Entropy:**  
  $$H(p, q) = -\sum_{x} p(x) \log q(x)$$

- **Negative Log-Likelihood:**  
  $$	ext{NLL} = -\sum_{i=1}^{N} \log P(x_i)$$

- **Softmax:**  
  $$	ext{softmax}(z)_i = rac{e^{z_i}}{\sum_j e^{z_j}}$$

- **Temperature Softmax:**  
  $$	ext{softmax}(z, T)_i = rac{e^{z_i / T}}{\sum_j e^{z_j / T}}$$

- **Perplexity:**  
  $$	ext{PP} = \exp\left( -rac{1}{N} \sum_{i=1}^{N} \log P(x_i) 
ight)$$

---

## Appendix B: Python Mathematical Toolkit

```python
import numpy as np

def softmax(x):
    x = np.asarray(x, dtype=float)
    shifted = x - np.max(x)
    exp_values = np.exp(shifted)
    return exp_values / exp_values.sum()

def entropy(probabilities):
    p = np.asarray(probabilities, dtype=float)
    p = p[p > 0]
    return -np.sum(p * np.log2(p))

def cross_entropy(target, prediction):
    target = np.asarray(target, dtype=float)
    prediction = np.clip(np.asarray(prediction, dtype=float), 1e-12, 1.0)
    return -np.sum(target * np.log(prediction))

def negative_log_likelihood(probabilities):
    p = np.clip(np.asarray(probabilities, dtype=float), 1e-12, 1.0)
    return -np.sum(np.log(p))

def perplexity(probabilities):
    p = np.clip(np.asarray(probabilities, dtype=float), 1e-12, 1.0)
    return np.exp(-np.mean(np.log(p)))

def temperature_distribution(logits, temperature=1.0):
    logits = np.asarray(logits, dtype=float)
    return softmax(logits / temperature)
```

---

## Appendix C: A Mental Model for Language Models

When analyzing a language model, ask five key questions:

1. **What is the context?** (The preceding token sequence)
2. **What are the candidate next tokens?** (The vocabulary $V$)
3. **What raw scores does the model assign?** (The logits $z$)
4. **How are scores mapped to probabilities?** (Softmax / Temperature scaling)
5. **How is the next token selected?** (Greedy decoding, Top-$k$, Top-$p$, or Categorical Sampling)

---

## Appendix D: Worked Problems and Review Exercises

### D.1 Probability Normalization
**Question:** Given probabilities $A=0.25, B=0.50, C=0.25$, is this distribution valid?  
**Answer:** Yes, because $0.25 + 0.50 + 0.25 = 1.00$ and all entries are $\ge 0$.

### D.2 Conditional Probability
**Question:** Given $P(A \cap B) = 0.18$ and $P(B) = 0.60$, find $P(A \mid B)$.  
**Answer:** $P(A \mid B) = rac{0.18}{0.60} = 0.30$.

### D.3 Information Content
**Question:** Find self-information for $p = 0.125$.  
**Answer:** $I = -\log_2(0.125) = -\log_2(1/8) = 3 	ext{ bits}$.

### D.4 Temperature Reasoning
**Question:** How does temperature $T$ affect logits $[4, 2, 0]$?  
**Answer:**
- $T < 1.0$: Sharpens the distribution (dominant logit 4 gets almost $100\%$ mass).
- $T = 1.0$: Preserves standard softmax probabilities.
- $T > 1.0$: Flattens the distribution towards uniform randomness.

---

## Final Review: The Mathematical Loop

```text
       Data
        │
        ▼
     Context
        │
        ▼
   Scores / Logits
        │
        ▼
     Softmax
        │
        ▼
Probability Distribution ──► Entropy / Uncertainty
        │                ──► Cross-Entropy / Loss
        │                ──► Temperature / Filtering
        ▼
Sampling or Greedy Decoding
        │
        ▼
    Next Token
        │
        └────────► New Context
```

*End of Book.*
