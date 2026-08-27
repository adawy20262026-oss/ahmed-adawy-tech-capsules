title: "The Mathematics of Generative AI: From Probability to Language Models"
author: "Ahmed Adawy"
language: "en"
edition: "1st Edition"
year: "2026"
description: "A practical mathematical introduction to probability, information theory, sampling, and language-model generation using Python and NumPy."
keywords:
  - Generative AI
  - Large Language Models
  - Probability
  - Information Theory
  - Python
  - NumPy
  - Language Models
  - Machine Learning
---

# The Mathematics of Generative AI

## From Probability to Language Models

### Ahmed Adawy

---

## Copyright

Copyright آ© 2026 Ahmed Adawy.

All rights reserved.

No part of this publication may be reproduced, distributed, or transmitted in any form without prior written permission from the author, except for brief quotations used in reviews or scholarly discussion.

This book is provided for educational purposes.

---

# Preface

Generative AI often looks mysterious from the outside.

A language model receives a sequence of tokens and produces another token. It can complete a paragraph, answer a question, write code, summarize an article, or generate an explanation.

But underneath all of these impressive behaviors is a mathematical idea that is much simpler than it first appears:

> A language model learns probabilities.

The model estimates which tokens are likely to appear given the tokens that came before them.

That single idea connects language modeling to probability theory, statistics, information theory, optimization, and numerical computation.

This book explores that connection.

The goal is not to hide the mathematics behind a framework or an API. Instead, we will build the concepts from first principles and use Python and NumPy to make them concrete.

You do not need advanced mathematics to begin.

You need curiosity, basic algebra, and a willingness to follow the equations.

By the end of the book, you should understand not only what a language model does, but why probability is at the center of generative AI.

---

# Table of Contents

1. [The Probabilistic View of AI](#chapter-1-the-probabilistic-view-of-ai)
2. [Random Variables and Probability Distributions](#chapter-2-random-variables-and-probability-distributions)
3. [Conditional Probability and Bayes' Theorem](#chapter-3-conditional-probability-and-bayes-theorem)
4. [Maximum Likelihood and Learning from Data](#chapter-4-maximum-likelihood-and-learning-from-data)
5. [Information Theory](#chapter-5-information-theory)
6. [Cross-Entropy and Language Models](#chapter-6-cross-entropy-and-language-models)
7. [Softmax, Temperature, and Sampling](#chapter-7-softmax-temperature-and-sampling)
8. [From Probability to Text Generation](#chapter-8-from-probability-to-text-generation)
9. [Perplexity and Measuring Language Models](#chapter-9-perplexity-and-measuring-language-models)
10. [Building a Tiny Probabilistic Language Model](#chapter-10-building-a-tiny-probabilistic-language-model)
11. [Putting Everything Together](#chapter-11-putting-everything-together)
12. [Final Project](#chapter-12-final-project)

---

# Chapter 1: The Probabilistic View of AI

## 1.1 What Does a Language Model Actually Predict?

Consider the sentence:

> The cat sat on the

What comes next?

A language model might assign probabilities such as:

```text
mat       0.42
floor     0.18
chair     0.07
table     0.05
street    0.01
...
````

The model does not necessarily "know" that the answer is `mat`.

Instead, it estimates a probability distribution over possible next tokens.

Mathematically:

[
P(x\_{t+1} \mid x\_1,x\_2,\ldots,x\_t)
]

This means:

> The probability of the next token given all previous tokens.

That is the fundamental prediction problem of an autoregressive language model.

---

## 1.2 Probability as a Language of Uncertainty

Probability gives us a way to describe uncertainty.

If we say:

[
P(A)=1
]

then event (A) is certain.

If:

[
P(A)=0
]

then event (A) is impossible.

For any event:

[
0 \leq P(A) \leq 1
]

A language model typically produces many probabilities whose sum is one:

[
\sum\_i P(x\_i)=1
]

For example:

```text
P("cat") = 0.50
P("dog") = 0.30
P("bird") = 0.20
```

Then:

[
0.50+0.30+0.20=1
]

---

## 1.3 Why Probability Is Central to Generative AI

Generative AI is about producing new data.

A model needs a mechanism for deciding what to generate.

Probability provides exactly that mechanism.

Instead of saying:

> Always choose the most likely word.

we can say:

> Sample a word according to the learned probability distribution.

This creates variation.

Suppose the model predicts:

```text
cat     0.70
dog     0.20
bird    0.10
```

Greedy generation always chooses:

```text
cat
```

Sampling can sometimes choose:

```text
dog
```

or:

```text
bird
```

The probability distribution therefore becomes the bridge between prediction and generation.

---

## 1.4 Tokens Instead of Words

Modern language models usually do not operate directly on words.

They operate on tokens.

A token may represent:

- a complete word
- part of a word
- punctuation
- whitespace
- a symbol

For example:

```text
"mathematics"
```

might be represented conceptually as:

```text
["math", "ematics"]
```

The exact tokenization depends on the tokenizer.

The model ultimately predicts a probability distribution over the vocabulary.

If the vocabulary has size (V), the model produces:

[
P(x\_1),P(x\_2),\ldots,P(x\_V)
]

with:

[
\sum\_{i=1}^{V}P(x\_i)=1
]

---

## 1.5 A Simple Python Example

```python
import numpy as np

tokens = ["cat", "dog", "bird"]

probabilities = np.array([0.5, 0.3, 0.2])

print(probabilities.sum())
```

Output:

```text
1.0
```

We can sample from this distribution:

```python
choice = np.random.choice(
    tokens,
    p=probabilities
)

print(choice)
```

The result is random, but not equally random.

`cat` is more likely than `bird`.

---

## 1.6 The Central Idea

A language model can be viewed as a function:

[
f(\text{context}) \rightarrow \text{probability distribution}
]

For example:

```text
"The cat sat on the"
```

becomes:

```text
mat       0.42
floor     0.18
chair     0.07
...
```

The rest of generative text generation is built on top of this idea.

---

# Chapter 2: Random Variables and Probability Distributions

## 2.1 Random Variables

A random variable is a mathematical representation of an uncertain outcome.

Suppose:

[
X = \text{next token}
]

If our vocabulary is:

```text
["cat", "dog", "bird"]
```

then (X) can take one of those values.

We can assign probabilities:

[
P(X=\text{cat})=0.5
]

[
P(X=\text{dog})=0.3
]

[
P(X=\text{bird})=0.2
]

---

## 2.2 Discrete Probability Distributions

Language-model tokens are discrete outcomes.

A discrete distribution can be represented as:

[
P(X=x\_i)
]

for every possible token (x\_i).

The probabilities must satisfy:

[
P(X=x\_i)\geq0
]

and:

[
\sum\_i P(X=x\_i)=1
]

---

## 2.3 Expected Value

The expected value represents the weighted average outcome.

For a discrete variable:

[
E[X]=\sum\_x xP(X=x)
]

For language tokens, numerical interpretation of the token itself is usually not meaningful.

However, expected values become extremely useful when we work with numerical quantities such as losses, rewards, and model scores.

---

## 2.4 Variance

Variance measures how spread out a random variable is.

[
Var(X)=E[(X-E[X])^2]
]

Standard deviation is:

[
\sigma=\sqrt{Var(X)}
]

Although language generation does not require us to manually calculate token variance at every step, the idea of uncertainty remains fundamental.

---

## 2.5 Probability Vectors

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

## 2.6 From Scores to Probabilities

Neural networks usually do not directly output probabilities.

They output scores called logits.

Suppose:

```python
logits = np.array([
    2.0,
    1.0,
    0.1
])
```

These values are not probabilities.

They can be converted into probabilities using softmax.

[
softmax(z\_i)=
\frac{e^{z\_i}}
{\sum\_j e^{z\_j}}
]

Python:

```python
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

## 2.7 Why Exponentials?

The exponential function has useful properties:

[
e^x>0
]

for every real number (x).

Therefore all softmax outputs are positive.

Normalization then forces the total to equal one.

Softmax therefore transforms arbitrary real-valued scores into a valid probability distribution.

---

# Chapter 3: Conditional Probability and Bayes' Theorem

## 3.1 Probability Depends on Context

Consider:

> The bank is near the

Possible next tokens might include:

```text
river
road
station
```

But now consider:

> I deposited money at the

The context changes the prediction.

This is conditional probability.

---

## 3.2 Conditional Probability

The probability of (A) given (B) is:

[
P(A|B)=\frac{P(A\cap B)}{P(B)}
]

provided:

[
P(B)>0
]

In language modeling:

[
P(\text{next token}|\text{context})
]

is the central quantity.

---

## 3.3 Joint Probability

Joint probability describes two events occurring together:

[
P(A,B)
]

The relationship between joint and conditional probability is:

[
P(A,B)=P(A|B)P(B)
]

This equation is extremely important.

---

## 3.4 The Chain Rule

For a sequence:

[
x\_1,x\_2,\ldots,x\_n
]

the probability of the entire sequence can be decomposed as:

# [ P(x\_1,\ldots,x\_n)

P(x\_1)
P(x\_2|x\_1)
P(x\_3|x\_1,x\_2)
\cdots
P(x\_n|x\_1,\ldots,x\_{n-1})
]

This is the mathematical foundation of autoregressive language modeling.

---

## 3.5 Language Models and the Chain Rule

Suppose:

```text
The cat sat
```

A language model can estimate:

[
P(\text{The cat sat})
]

as:

[
P(\text{The})
P(\text{cat}|\text{The})
P(\text{sat}|\text{The cat})
]

For a longer sentence, we continue the process.

This means that generating a sentence can be understood as repeatedly predicting the next token.

---

## 3.6 Bayes' Theorem

Bayes' theorem is:

[
P(A|B)=
\frac{P(B|A)P(A)}
{P(B)}
]

It allows us to reverse conditional relationships.

Although modern neural language models are not simply "Bayesian systems," Bayes' theorem is an essential part of probabilistic thinking.

---

## 3.7 Example

Suppose a test detects a condition.

Let:

[
P(D)=0.01
]

and:

[
P(+|D)=0.95
]

Suppose:

[
P(+|\neg D)=0.05
]

Then:

[
P(+)=P(+|D)P(D)+P(+|\neg D)P(\neg D)
]

Therefore:

[
P(+)=0.95(0.01)+0.05(0.99)
]

[
P(+)=0.059
]

Bayes gives:

[
P(D|+)=
\frac{0.95(0.01)}
{0.059}
]

approximately:

[
0.161
]

The lesson is important:

> A highly accurate positive test does not automatically mean a positive result has a high posterior probability.

The prior probability matters.

---

# Chapter 4: Maximum Likelihood and Learning from Data

## 4.1 Where Do Probabilities Come From?

A language model cannot simply invent its probability distribution.

It must learn parameters from data.

Suppose a model has parameters:

[
\theta
]

The model represents:

[
P\_\theta(x)
]

The goal is to find parameters that make observed training data probable.

---

## 4.2 Likelihood

Suppose our dataset contains:

[
D={x\_1,x\_2,\ldots,x\_n}
]

The likelihood is:

[
L(\theta)=
\prod\_{i=1}^{n}
P\_\theta(x\_i)
]

We want parameters that maximize this likelihood:

# [ \theta^\*

\arg\max\_\theta L(\theta)
]

This is Maximum Likelihood Estimation.

---

## 4.3 Why Products Become Difficult

If the dataset contains thousands or millions of examples, multiplying probabilities can produce extremely small numbers.

For example:

[
0.1^{1000}
]

is tiny.

Instead, we use logarithms.

Because:

[
\log(ab)=\log(a)+\log(b)
]

we get:

# [ \log L(\theta)

\sum\_i \log P\_\theta(x\_i)
]

Maximizing likelihood is equivalent to maximizing log-likelihood.

---

## 4.4 Negative Log-Likelihood

Machine learning systems usually minimize a loss.

Therefore we define:

# [ NLL

-\sum\_i \log P\_\theta(x\_i)
]

Minimizing NLL is equivalent to maximizing likelihood.

This is one of the most important connections between probability and machine learning optimization.

---

## 4.5 A Tiny Example

Suppose the correct token has predicted probability:

```text
0.8
```

Its negative log-likelihood is:

[
-\log(0.8)
]

Using Python:

```python
import numpy as np

p = 0.8

loss = -np.log(p)

print(loss)
```

If the model predicts:

```text
0.01
```

the loss is much larger.

```python
p = 0.01

loss = -np.log(p)

print(loss)
```

The model is strongly penalized for assigning very low probability to the correct answer.

---

## 4.6 Learning Means Adjusting Probability

This gives us a powerful interpretation:

Training a language model means adjusting its parameters so that correct tokens receive higher probability.

The model repeatedly observes:

```text
context -> correct next token
```

and modifies its parameters.

Over time:

```text
P(correct token | context)
```

should increase.

---

# Chapter 5: Information Theory

## 5.1 What Is Information?

Information theory gives us mathematical tools for measuring uncertainty and surprise.

One of the most famous quantities is information content.

For an event with probability (p):

[
I(x)=-\log\_2 p(x)
]

A rare event contains more information.

A common event contains less information.

---

## 5.2 Example

If:

[
p=0.5
]

then:

[
I=-\log\_2(0.5)=1
]

If:

[
p=0.01
]

then:

[
I=-\log\_2(0.01)
]

which is much larger.

The less expected an event is, the more surprising it is.

---

## 5.3 Entropy

Entropy measures the average uncertainty of a probability distribution.

For a discrete distribution:

# [ H(X)

-\sum\_x P(x)\log P(x)
]

Using base 2 gives entropy in bits.

---

## 5.4 Maximum Entropy

Suppose we have three equally likely outcomes:

```text
0.333
0.333
0.333
```

There is significant uncertainty.

But suppose:

```text
0.98
0.01
0.01
```

The outcome is much more predictable.

Therefore entropy is high when probability is spread out and low when one outcome dominates.

---

## 5.5 Python Implementation

```python
import numpy as np

def entropy(probabilities):
    probabilities = np.asarray(probabilities)

    probabilities = probabilities[
        probabilities > 0
    ]

    return -np.sum(
        probabilities * np.log2(probabilities)
    )

p1 = np.array([1/3, 1/3, 1/3])
p2 = np.array([0.98, 0.01, 0.01])

print(entropy(p1))
print(entropy(p2))
```

---

## 5.6 Why Entropy Matters for Language

Consider two contexts.

Context A:

```text
The capital of France is
```

The next token is highly predictable.

Entropy is relatively low.

Context B:

```text
I wonder what will happen tomorrow when
```

Many continuations are possible.

Entropy can be higher.

A language model must learn these differences in uncertainty.

---

## 5.7 Cross-Entropy

Cross-entropy measures how well one probability distribution represents another.

For distributions (p) and (q):

# [ H(p,q)

-\sum\_x p(x)\log q(x)
]

In supervised language modeling, the target distribution is often represented as a one-hot vector.

If the correct token is (k):

[
p\_k=1
]

and every other target probability is zero.

Then cross-entropy becomes:

[
H(p,q)=-\log q\_k
]

This is exactly the negative log-likelihood of the correct token.

---

# Chapter 6: Cross-Entropy and Language Models

## 6.1 The Training Objective

Suppose the vocabulary contains:

```text
["cat", "dog", "bird"]
```

The correct token is:

```text
cat
```

The target distribution is:

```text
[1, 0, 0]
```

Suppose the model predicts:

```text
[0.7, 0.2, 0.1]
```

Cross-entropy is:

[
-\left(
1\log(0.7)
\+
0\log(0.2)
\+
0\log(0.1)
\right)
]

Therefore:

[
Loss=-\log(0.7)
]

---

## 6.2 Python

```python
import numpy as np

target = np.array([1, 0, 0])

prediction = np.array([
    0.7,
    0.2,
    0.1
])

loss = -np.sum(
    target * np.log(prediction)
)

print(loss)
```

---

## 6.3 What Happens When the Model Is Wrong?

Suppose:

```text
prediction = [0.01, 0.49, 0.50]
```

The model gives the correct token only 1% probability.

The loss becomes:

[
-\log(0.01)
]

which is large.

This creates a strong learning signal.

---

## 6.4 Cross-Entropy and Softmax

In a neural language model, we usually have:

```text
hidden representation
        |
        v
linear projection
        |
        v
logits
        |
        v
softmax
        |
        v
probabilities
        |
        v
cross-entropy
```

This pipeline is one of the central computational patterns in modern language models.

---

## 6.5 Stable Softmax

Naively calculating:

```python
np.exp(logits)
```

can overflow for very large logits.

Instead:

```python
def stable_softmax(logits):
    shifted = logits - np.max(logits)
    exp_values = np.exp(shifted)
    return exp_values / np.sum(exp_values)
```

Subtracting the maximum does not change the resulting probabilities because softmax is invariant to adding or subtracting the same constant from every logit.

---

## 6.6 Stable Cross-Entropy

A numerically stable implementation can operate directly on logits.

```python
def cross_entropy_from_logits(logits, target_index):
    max_logit = np.max(logits)

    shifted = logits - max_logit

    log_sum_exp = (
        max_logit
        + np.log(
            np.sum(np.exp(shifted))
        )
    )

    return log_sum_exp - logits[target_index]
```

This avoids unnecessary numerical instability.

---

# Chapter 7: Softmax, Temperature, and Sampling

## 7.1 Why Sampling Matters

Suppose a model predicts:

```text
mat       0.60
floor     0.25
chair     0.10
street    0.05
```

Greedy decoding always selects:

```text
mat
```

But generative AI often needs diversity.

Sampling allows the model to choose according to probability.

---

## 7.2 Categorical Sampling

```python
import numpy as np

tokens = [
    "mat",
    "floor",
    "chair",
    "street"
]

probabilities = np.array([
    0.60,
    0.25,
    0.10,
    0.05
])

token = np.random.choice(
    tokens,
    p=probabilities
)

print(token)
```

---

## 7.3 Temperature

Temperature modifies the sharpness of the distribution.

Given logits (z\_i):

[
P\_i=
\frac{
e^{z\_i/T}
}{
\sum\_j e^{z\_j/T}
}
]

where (T) is temperature.

---

## 7.4 Low Temperature

If:

[
T<1
]

the distribution becomes sharper.

The highest-probability tokens become more dominant.

This usually produces more predictable output.

---

## 7.5 High Temperature

If:

[
T>1
]

the distribution becomes flatter.

Lower-probability tokens become more likely.

This can increase variety but also increase randomness.

---

## 7.6 Python Implementation

```python
def temperature_softmax(logits, temperature=1.0):
    scaled = logits / temperature

    shifted = scaled - np.max(scaled)

    exp_values = np.exp(shifted)

    return exp_values / exp_values.sum()
```

Example:

```python
logits = np.array([
    3.0,
    2.0,
    1.0,
    0.0
])

print(
    temperature_softmax(
        logits,
        temperature=0.5
    )
)

print(
    temperature_softmax(
        logits,
        temperature=2.0
    )
)
```

---

## 7.7 Top-k Sampling

Another strategy is top-k sampling.

Suppose the model has thousands of possible tokens.

We keep only the (k) highest-probability tokens.

For example:

```text
top 5 tokens
```

Then we renormalize their probabilities.

Conceptually:

```python
def top_k_filter(probabilities, k):
    indices = np.argsort(probabilities)[-k:]

    filtered = np.zeros_like(probabilities)

    filtered[indices] = probabilities[indices]

    filtered /= filtered.sum()

    return filtered
```

---

## 7.8 Why Sampling Is Not the Same as Random Guessing

Random guessing treats all outcomes equally.

Sampling from a language model does not.

The model's learned distribution determines the probability of each token.

Therefore:

> Sampling is controlled randomness.

---

# Chapter 8: From Probability to Text Generation

## 8.1 Autoregressive Generation

The basic generation loop is simple.

Start with a prompt:

```text
The future of AI
```

Predict the next token.

Append it.

Predict again.

Continue.

Mathematically:

[
x\_{t+1}
\sim
P(x|x\_1,\ldots,x\_t)
]

---

## 8.2 Conceptual Algorithm

```text
prompt
  |
  v
model
  |
  v
probabilities
  |
  v
sampling
  |
  v
new token
  |
  v
append token
  |
  +-------> model again
```

This loop is the heart of autoregressive generation.

---

## 8.3 A Tiny Bigram Model

We can build a simple language model without a neural network.

Consider:

```text
the cat sat
the cat slept
the dog sat
the dog ran
```

We count transitions.

For example:

```text
the -> cat: 2
the -> dog: 2
cat -> sat: 1
cat -> slept: 1
dog -> sat: 1
dog -> ran: 1
```

Then:

[
P(cat|the)=0.5
]

and:

[
P(dog|the)=0.5
]

---

## 8.4 Building Counts

```python
from collections import defaultdict, Counter

text = """
the cat sat
the cat slept
the dog sat
the dog ran
"""

tokens = text.split()

counts = defaultdict(Counter)

for a, b in zip(tokens, tokens[1:]):
    counts[a][b] += 1

print(counts["the"])
```

---

## 8.5 Converting Counts to Probabilities

```python
def transition_probabilities(counter):
    total = sum(counter.values())

    return {
        token: count / total
        for token, count in counter.items()
    }

print(
    transition_probabilities(
        counts["the"]
    )
)
```

---

## 8.6 Generating Text

```python
import numpy as np

def next_token(current):
    counter = counts[current]

    tokens = list(counter.keys())

    probabilities = np.array([
        counter[token]
        for token in tokens
    ], dtype=float)

    probabilities /= probabilities.sum()

    return np.random.choice(
        tokens,
        p=probabilities
    )
```

Then:

```python
current = "the"

generated = [current]

for _ in range(10):
    current = next_token(current)
    generated.append(current)

print(" ".join(generated))
```

---

## 8.7 What Does This Teach Us?

Our tiny model has no Transformer.

It has no embeddings.

It has no attention.

Yet it already demonstrates the central idea:

[
context \rightarrow probability\ distribution \rightarrow sample
]

Modern language models make this process dramatically more powerful by learning sophisticated representations of context.

---

# Chapter 9: Perplexity and Measuring Language Models

## 9.1 Why Accuracy Is Not Enough

Suppose a model predicts:

```text
cat: 0.51
dog: 0.49
```

Another model predicts:

```text
cat: 0.99
dog: 0.01
```

If the correct answer is `cat`, both models are correct under simple classification accuracy.

But clearly the second model is much more confident.

We need a metric that considers probabilities.

Cross-entropy provides one.

Perplexity provides another interpretation.

---

## 9.2 Definition

For a sequence of (N) tokens:

[
PP=
\exp
\left(
-\frac{1}{N}
\sum\_{i=1}^{N}
\log P(x\_i)
\right)
]

If logarithms are base 2:

[
PP=
2^{H}
]

where (H) is average cross-entropy in bits.

---

## 9.3 Interpretation

Lower perplexity generally means the model assigns higher probability to the observed sequence.

If:

[
PP=10
]

we can loosely interpret the model as having uncertainty comparable to choosing among about ten equally likely possibilities at each prediction step.

This is an intuition, not a literal description of the vocabulary size.

---

## 9.4 Python

```python
import numpy as np

probabilities = np.array([
    0.8,
    0.6,
    0.5,
    0.9
])

average_nll = -np.mean(
    np.log(probabilities)
)

perplexity = np.exp(
    average_nll
)

print(perplexity)
```

---

## 9.5 Perplexity and Model Comparison

If two models are evaluated on the same dataset and under comparable conditions, the model with lower perplexity generally assigns greater probability to the observed tokens.

However, perplexity should not be interpreted without considering:

- tokenizer
- vocabulary
- dataset
- preprocessing
- evaluation setup

Different tokenization schemes can make raw perplexity comparisons misleading.

---

# Chapter 10: Building a Tiny Probabilistic Language Model

## 10.1 The Goal

We will now combine the concepts into a small model.

The model will:

1. tokenize text
2. count transitions
3. calculate probabilities
4. generate text
5. evaluate likelihood

This is not a neural language model.

It is a mathematical laboratory.

---

## 10.2 Training Data

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

## 10.3 Tokenization

```python
sentences = [
    sentence.split()
    for sentence in corpus
]

print(sentences)
```

---

## 10.4 Bigram Counts

```python
from collections import defaultdict, Counter

bigram_counts = defaultdict(Counter)

for sentence in sentences:
    for a, b in zip(sentence, sentence[1:]):
        bigram_counts[a][b] += 1
```

---

## 10.5 Probability Table

```python
def probabilities_for(token):
    counter = bigram_counts[token]

    total = sum(counter.values())

    return {
        next_token: count / total
        for next_token, count
        in counter.items()
    }
```

Example:

```python
print(
    probabilities_for("the")
)
```

---

## 10.6 Generation

```python
def generate(start_token, length=12):
    current = start_token
    output = [current]

    for _ in range(length - 1):
        counter = bigram_counts.get(current)

        if not counter:
            break

        tokens = list(counter.keys())

        probabilities = np.array([
            counter[token]
            for token in tokens
        ], dtype=float)

        probabilities /= probabilities.sum()

        current = np.random.choice(
            tokens,
            p=probabilities
        )

        output.append(current)

    return " ".join(output)
```

Run:

```python
print(generate("the"))
```

---

## 10.7 The Problem with Raw Counts

Our model only remembers one previous token.

Therefore:

```text
the cat
```

and:

```text
the dog
```

both begin with the same context:

```text
the
```

A larger context would allow better predictions.

This motivates higher-order language models and eventually neural architectures.

---

## 10.8 Smoothing

A problem occurs when a transition never appeared in the training data.

Suppose:

```text
cat -> ran
```

never appeared.

Our model assigns:

[
P(ran|cat)=0
]

This can cause problems because:

[
\log(0)
]

is undefined.

One classical solution is Laplace smoothing.

---

## 10.9 Laplace Smoothing

If:

[
count(x,y)
]

is the observed count, we can use:

# [ P(y|x)

\frac{
count(x,y)+\alpha
}{
count(x)+\alpha V
}
]

where:

- (\alpha) is the smoothing parameter
- (V) is vocabulary size

For Laplace smoothing:

[
\alpha=1
]

---

## 10.10 Python

```python
def smoothed_probability(
    count,
    total,
    vocabulary_size,
    alpha=1.0
):
    return (
        count + alpha
    ) / (
        total + alpha * vocabulary_size
    )
```

This guarantees non-zero probability for every vocabulary item.

---

# Chapter 11: Putting Everything Together

## 11.1 The Full Mathematical Pipeline

We can now see the complete picture.

A language model receives context:

[
x\_1,\ldots,x\_t
]

and computes scores:

[
z\_1,\ldots,z\_V
]

These scores become probabilities:

[
P(x\_i|context)
]

using softmax.

The probability of the correct token produces a loss:

[
L=-\log P(correct|context)
]

The training algorithm modifies model parameters to reduce the average loss.

During generation, the model converts the learned distribution into a token using a decoding strategy.

---

## 11.2 The Complete Flow

```text
Training Data
     |
     v
Tokenization
     |
     v
Context / Target Pairs
     |
     v
Neural Network
     |
     v
Logits
     |
     v
Softmax
     |
     v
Probability Distribution
     |
     v
Cross-Entropy
     |
     v
Optimization
     |
     +------> Updated Parameters
```

Then:

```text
Prompt
  |
  v
Trained Model
  |
  v
Logits
  |
  v
Temperature / Filtering
  |
  v
Sampling
  |
  v
New Token
  |
  +------> Repeat
```

---

## 11.3 Why the Same Mathematics Appears Everywhere

Probability appears in:

- prediction
- training
- evaluation
- sampling
- uncertainty
- generation

Information theory appears in:

- entropy
- cross-entropy
- compression
- loss functions
- model evaluation

Optimization appears in:

- parameter learning
- minimizing loss
- improving predictions

These subjects are not isolated.

They form one mathematical system.

---

## 11.4 From Bigram Models to Transformers

Our bigram model uses:

[
P(x\_t|x\_{t-1})
]

A more powerful model might use:

[
P(x\_t|x\_1,\ldots,x\_{t-1})
]

A Transformer uses learned representations and attention to model relationships across the context.

The architecture becomes much more complex.

The probabilistic objective remains surprisingly familiar.

The model still ultimately produces:

[
P(next\ token|context)
]

That is one of the most important ideas to remember.

---

# Chapter 12: Final Project

## Build a Mini Language Generation Engine

The final project combines everything in this book.

The goal is to build a small probabilistic text-generation engine using Python and NumPy.

---

## 12.1 Project Requirements

Your engine should:

1. accept a training corpus
2. tokenize the corpus
3. construct token transition counts
4. convert counts into probabilities
5. calculate entropy
6. calculate negative log-likelihood
7. calculate perplexity
8. apply temperature
9. sample the next token
10. generate a sequence

---

## 12.2 Complete Implementation

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

            for a, b in zip(
                tokens,
                tokens[1:]
            ):
                self.counts[a][b] += 1

    def probabilities(self, token):

        counter = self.counts[token]

        if not counter:
            return {}

        total = sum(counter.values())

        return {
            token: count / total
            for token, count
            in counter.items()
        }

    def entropy(self, token):

        probs = self.probabilities(token)

        if not probs:
            return 0.0

        values = np.array(
            list(probs.values())
        )

        return -np.sum(
            values * np.log2(values)
        )

    def next_token(
        self,
        token,
        temperature=1.0
    ):

        probs = self.probabilities(token)

        if not probs:
            return None

        tokens = list(probs.keys())

        values = np.array(
            list(probs.values()),
            dtype=float
        )

        logits = np.log(
            values + 1e-12
        )

        logits /= temperature

        logits -= np.max(logits)

        exp_values = np.exp(logits)

        values = (
            exp_values
            / exp_values.sum()
        )

        return np.random.choice(
            tokens,
            p=values
        )

    def generate(
        self,
        start,
        length=20,
        temperature=1.0
    ):

        output = [start]

        current = start

        for _ in range(length - 1):

            next_value = self.next_token(
                current,
                temperature
            )

            if next_value is None:
                break

            output.append(next_value)

            current = next_value

        return " ".join(output)
```

---

## 12.3 Training the Model

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
```

---

## 12.4 Inspecting Probability

```python
print(
    model.probabilities("the")
)
```

You may see something conceptually similar to:

```text
{
    "cat": ...,
    "dog": ...,
    "bird": ...
}
```

The exact values depend on the corpus.

---

## 12.5 Measuring Entropy

```python
print(
    model.entropy("the")
)
```

If the next token is evenly distributed among several possibilities, entropy will be relatively high.

If one token dominates, entropy will be lower.

---

## 12.6 Generating Text

```python
print(
    model.generate(
        "the",
        length=15,
        temperature=1.0
    )
)
```

Try:

```python
temperature=0.5
```

Then:

```python
temperature=2.0
```

Compare the generated sequences.

---

## 12.7 What You Should Observe

At lower temperature, generation tends to become more concentrated around high-probability transitions.

At higher temperature, probability becomes flatter and generation becomes more exploratory.

This demonstrates an important principle:

> Generation is not separate from probability. Generation is probability being used operationally.

---

# Conclusion

Generative AI can appear enormously complicated.

Modern language models contain billions of parameters, sophisticated architectures, large datasets, and powerful optimization systems.

But beneath that complexity is a mathematical structure that can be understood step by step.

The model observes data.

It learns statistical relationships.

It produces scores.

Scores become probabilities.

Probabilities define uncertainty.

Uncertainty can be measured with information theory.

The probability assigned to the correct token becomes a learning signal through negative log-likelihood and cross-entropy.

During generation, the probability distribution becomes a mechanism for selecting the next token.

The loop then repeats.

[
context
\rightarrow
prediction
\rightarrow
probability
\rightarrow
sampling
\rightarrow
token
\rightarrow
new\ context
]

This is the mathematical heart of autoregressive generation.

---

# Appendix A: Essential Equations

## Probability

[
0\leq P(A)\leq1
]

## Conditional Probability

# [ P(A|B)

\frac{P(A\cap B)}
{P(B)}
]

## Joint Probability

# [ P(A,B)

P(A|B)P(B)
]

## Bayes' Theorem

# [ P(A|B)

\frac{
P(B|A)P(A)
}{
P(B)
}
]

## Chain Rule

# [ P(x\_1,\ldots,x\_n)

\prod\_{i=1}^{n}
P(x\_i|x\_1,\ldots,x\_{i-1})
]

## Information

[
I(x)=-\log p(x)
]

## Entropy

# [ H(X)

-\sum\_x P(x)\log P(x)
]

## Cross-Entropy

# [ H(p,q)

-\sum\_x p(x)\log q(x)
]

## Negative Log-Likelihood

# [ NLL

-\sum\_i\log P(x\_i)
]

## Softmax

# [ P\_i

\frac{e^{z\_i}}
{\sum\_j e^{z\_j}}
]

## Temperature Softmax

# [ P\_i

\frac{e^{z\_i/T}}
{\sum\_j e^{z\_j/T}}
]

## Perplexity

# [ PP

\exp
\left(
-\frac{1}{N}
\sum\_i
\log P(x\_i)
\right)
]

---

# Appendix B: Python Mathematical Toolkit

```python
import numpy as np


def softmax(x):

    x = np.asarray(x)

    shifted = x - np.max(x)

    exp_values = np.exp(shifted)

    return (
        exp_values
        / exp_values.sum()
    )


def entropy(probabilities):

    p = np.asarray(
        probabilities,
        dtype=float
    )

    p = p[p > 0]

    return -np.sum(
        p * np.log2(p)
    )


def cross_entropy(
    target,
    prediction
):

    target = np.asarray(
        target,
        dtype=float
    )

    prediction = np.asarray(
        prediction,
        dtype=float
    )

    prediction = np.clip(
        prediction,
        1e-12,
        1.0
    )

    return -np.sum(
        target * np.log(prediction)
    )


def negative_log_likelihood(
    probabilities
):

    probabilities = np.asarray(
        probabilities,
        dtype=float
    )

    probabilities = np.clip(
        probabilities,
        1e-12,
        1.0
    )

    return -np.sum(
        np.log(probabilities)
    )


def perplexity(probabilities):

    probabilities = np.asarray(
        probabilities,
        dtype=float
    )

    probabilities = np.clip(
        probabilities,
        1e-12,
        1.0
    )

    loss = -np.mean(
        np.log(probabilities)
    )

    return np.exp(loss)


def temperature_distribution(
    logits,
    temperature=1.0
):

    logits = np.asarray(
        logits,
        dtype=float
    )

    scaled = logits / temperature

    return softmax(scaled)
```

---

# Appendix C: A Mental Model for Language Models

When looking at a language model, ask five questions:

### 1. What is the context?

What information does the model currently have?

### 2. What are the possible next tokens?

These form the vocabulary.

### 3. What scores does the model assign?

These are the logits.

### 4. How are scores converted to probabilities?

Usually through softmax.

### 5. How is the next token selected?

Possible strategies include:

- greedy decoding
- sampling
- temperature sampling
- top-k sampling
- top-p sampling

Once these five questions become intuitive, much of language-model generation becomes easier to reason about.

---

# Final Perspective

The mathematics of generative AI is not a collection of unrelated equations.

It is a connected system.

Probability describes what may happen.

Conditional probability describes what may happen given context.

The chain rule describes the probability of sequences.

Maximum likelihood explains how models can learn from observed data.

Information theory measures uncertainty.

Cross-entropy measures how well predicted probabilities match observed outcomes.

Softmax transforms model scores into probabilities.

Sampling transforms probabilities into generated tokens.

And autoregressive generation repeats the entire process.

The result is a simple mathematical loop hidden inside extremely sophisticated systems:

[
\boxed{
\text{Context}
\rightarrow
\text{Probability}
\rightarrow
\text{Token}
\rightarrow
\text{Context}
}
]

Understanding this loop is one of the clearest ways to begin understanding Generative AI.

---

# End

## The Mathematics of Generative AI

### From Probability to Language Models

**Ahmed Adawy**

2026
