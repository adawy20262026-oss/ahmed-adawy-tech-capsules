---
author: Ahmed Adawy
description: A practical mathematical introduction to probability,
  information theory, sampling, and language-model generation using
  Python and NumPy.
edition: 1st Edition
keywords:
- Generative AI
- Large Language Models
- Probability
- Information Theory
- Python
- NumPy
- Language Models
- Machine Learning
language: en
title: "The Mathematics of Generative AI: From Probability to Language
  Models"
year: 2026
---

# The Mathematics of Generative AI

## From Probability to Language Models

### Ahmed Adawy

------------------------------------------------------------------------

## Copyright

Copyright آ© 2026 Ahmed Adawy.

All rights reserved.

No part of this publication may be reproduced, distributed, or
transmitted in any form without prior written permission from the
author, except for brief quotations used in reviews or scholarly
discussion.

This book is provided for educational purposes.

------------------------------------------------------------------------

# Preface

Generative AI often looks mysterious from the outside.

A language model receives a sequence of tokens and produces another
token. It can complete a paragraph, answer a question, write code,
summarize an article, or generate an explanation.

But underneath all of these impressive behaviors is a mathematical idea
that is much simpler than it first appears:

> A language model learns probabilities.

The model estimates which tokens are likely to appear given the tokens
that came before them.

That single idea connects language modeling to probability theory,
statistics, information theory, optimization, and numerical computation.

This book explores that connection.

The goal is not to hide the mathematics behind a framework or an API.
Instead, we will build the concepts from first principles and use Python
and NumPy to make them concrete.

You do not need advanced mathematics to begin.

You need curiosity, basic algebra, and a willingness to follow the
equations.

By the end of the book, you should understand not only what a language
model does, but why probability is at the center of generative AI.

------------------------------------------------------------------------

# Table of Contents

1.  [The Probabilistic View of
    AI](#chapter-1-the-probabilistic-view-of-ai)
2.  [Random Variables and Probability
    Distributions](#chapter-2-random-variables-and-probability-distributions)
3.  [Conditional Probability and Bayes'
    Theorem](#chapter-3-conditional-probability-and-bayes-theorem)
4.  [Maximum Likelihood and Learning from
    Data](#chapter-4-maximum-likelihood-and-learning-from-data)
5.  [Information Theory](#chapter-5-information-theory)
6.  [Cross-Entropy and Language
    Models](#chapter-6-cross-entropy-and-language-models)
7.  [Softmax, Temperature, and
    Sampling](#chapter-7-softmax-temperature-and-sampling)
8.  [From Probability to Text
    Generation](#chapter-8-from-probability-to-text-generation)
9.  [Perplexity and Measuring Language
    Models](#chapter-9-perplexity-and-measuring-language-models)
10. [Building a Tiny Probabilistic Language
    Model](#chapter-10-building-a-tiny-probabilistic-language-model)
11. [Putting Everything
    Together](#chapter-11-putting-everything-together)
12. [Final Project](#chapter-12-final-project)
13. [Practical Probability Labs](#chapter-13-practical-probability-labs)
14. [Numerical Stability in Generative
    AI](#chapter-14-numerical-stability-in-generative-ai)
15. [From Bigram Models to Neural Language
    Models](#chapter-15-from-bigram-models-to-neural-language-models)
16. [Designing a Small Text
    Generator](#chapter-16-designing-a-small-text-generator)

------------------------------------------------------------------------

# Chapter 1: The Probabilistic View of AI

## 1.1 What Does a Language Model Actually Predict?

Consider the sentence:

> The cat sat on the

What comes next?

A language model might assign probabilities such as:

``` text
mat       0.42
floor     0.18
chair     0.07
table     0.05
street    0.01
...
```

The model does not necessarily "know" that the answer is `mat`.

Instead, it estimates a probability distribution over possible next
tokens.

Mathematically:

> **Formula:** P(x_t+1 mid x_1,x_2,ldots,x_t)

This means:

> The probability of the next token given all previous tokens.

That is the fundamental prediction problem of an autoregressive language
model.

------------------------------------------------------------------------

## 1.2 Probability as a Language of Uncertainty

Probability gives us a way to describe uncertainty.

If we say:

> **Formula:** P(A)=1

then event (A) is certain.

If:

> **Formula:** P(A)=0

then event (A) is impossible.

For any event:

> **Formula:** 0 leq P(A) leq 1

A language model typically produces many probabilities whose sum is one:

> **Formula:** sum_i P(x_i)=1

For example:

``` text
P("cat") = 0.50
P("dog") = 0.30
P("bird") = 0.20
```

Then:

> **Formula:** 0.50+0.30+0.20=1

------------------------------------------------------------------------

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

``` text
cat     0.70
dog     0.20
bird    0.10
```

Greedy generation always chooses:

``` text
cat
```

Sampling can sometimes choose:

``` text
dog
```

or:

``` text
bird
```

The probability distribution therefore becomes the bridge between
prediction and generation.

------------------------------------------------------------------------

## 1.4 Tokens Instead of Words

Modern language models usually do not operate directly on words.

They operate on tokens.

A token may represent:

-   a complete word
-   part of a word
-   punctuation
-   whitespace
-   a symbol

For example:

``` text
"mathematics"
```

might be represented conceptually as:

``` text
["math", "ematics"]
```

The exact tokenization depends on the tokenizer.

The model ultimately predicts a probability distribution over the
vocabulary.

If the vocabulary has size (V), the model produces:

> **Formula:** P(x_1),P(x_2),ldots,P(x_V)

with:

> **Formula:** sum_i=1\^VP(x_i)=1

------------------------------------------------------------------------

## 1.5 A Simple Python Example

``` python
import numpy as np

tokens = ["cat", "dog", "bird"]

probabilities = np.array([0.5, 0.3, 0.2])

print(probabilities.sum())
```

Output:

``` text
1.0
```

We can sample from this distribution:

``` python
choice = np.random.choice(
    tokens,
    p=probabilities
)

print(choice)
```

The result is random, but not equally random.

`cat` is more likely than `bird`.

------------------------------------------------------------------------

## 1.6 The Central Idea

A language model can be viewed as a function:

> **Formula:** f(context) arrow probability distribution

For example:

``` text
"The cat sat on the"
```

becomes:

``` text
mat       0.42
floor     0.18
chair     0.07
...
```

The rest of generative text generation is built on top of this idea.

------------------------------------------------------------------------

# Chapter 2: Random Variables and Probability Distributions

## 2.1 Random Variables

A random variable is a mathematical representation of an uncertain
outcome.

Suppose:

> **Formula:** X = next token

If our vocabulary is:

``` text
["cat", "dog", "bird"]
```

then (X) can take one of those values.

We can assign probabilities:

> **Formula:** P(X=cat)=0.5

> **Formula:** P(X=dog)=0.3

> **Formula:** P(X=bird)=0.2

------------------------------------------------------------------------

## 2.2 Discrete Probability Distributions

Language-model tokens are discrete outcomes.

A discrete distribution can be represented as:

> **Formula:** P(X=x_i)

for every possible token (x_i).

The probabilities must satisfy:

> **Formula:** P(X=x_i)geq0

and:

> **Formula:** sum_i P(X=x_i)=1

------------------------------------------------------------------------

## 2.3 Expected Value

The expected value represents the weighted average outcome.

For a discrete variable:

> **Formula:** E\[X\]=sum_x xP(X=x)

For language tokens, numerical interpretation of the token itself is
usually not meaningful.

However, expected values become extremely useful when we work with
numerical quantities such as losses, rewards, and model scores.

------------------------------------------------------------------------

## 2.4 Variance

Variance measures how spread out a random variable is.

> **Formula:** Var(X)=E\[(X-E\[X\])\^2\]

Standard deviation is:

> **Formula:** sigma=sqrtVar(X)

Although language generation does not require us to manually calculate
token variance at every step, the idea of uncertainty remains
fundamental.

------------------------------------------------------------------------

## 2.5 Probability Vectors

A probability distribution over a vocabulary can be stored as a vector.

``` python
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

------------------------------------------------------------------------

## 2.6 From Scores to Probabilities

Neural networks usually do not directly output probabilities.

They output scores called logits.

Suppose:

``` python
logits = np.array([
    2.0,
    1.0,
    0.1
])
```

These values are not probabilities.

They can be converted into probabilities using softmax.

> **Formula:** softmax(z_i)= frace\^z_i sum_j e\^z_j

Python:

``` python
def softmax(x):
    exp_x = np.exp(x - np.max(x))
    return exp_x / exp_x.sum()

logits = np.array([2.0, 1.0, 0.1])

probabilities = softmax(logits)

print(probabilities)
print(probabilities.sum())
```

The subtraction of the maximum value improves numerical stability.

------------------------------------------------------------------------

## 2.7 Why Exponentials?

The exponential function has useful properties:

> **Formula:** e\^x\>0

for every real number (x).

Therefore all softmax outputs are positive.

Normalization then forces the total to equal one.

Softmax therefore transforms arbitrary real-valued scores into a valid
probability distribution.

------------------------------------------------------------------------

# Chapter 3: Conditional Probability and Bayes' Theorem

## 3.1 Probability Depends on Context

Consider:

> The bank is near the

Possible next tokens might include:

``` text
river
road
station
```

But now consider:

> I deposited money at the

The context changes the prediction.

This is conditional probability.

------------------------------------------------------------------------

## 3.2 Conditional Probability

The probability of (A) given (B) is:

> **Formula:** P(A\|B)=(P(Acap B)) / (P(B))

provided:

> **Formula:** P(B)\>0

In language modeling:

> **Formula:** P(next token\|context)

is the central quantity.

------------------------------------------------------------------------

## 3.3 Joint Probability

Joint probability describes two events occurring together:

> **Formula:** P(A,B)

The relationship between joint and conditional probability is:

> **Formula:** P(A,B)=P(A\|B)P(B)

This equation is extremely important.

------------------------------------------------------------------------

## 3.4 The Chain Rule

For a sequence:

> **Formula:** x_1,x_2,ldots,x_n

the probability of the entire sequence can be decomposed as:

> **Formula:** P(x_1,ldots,x_n)

P(x_1) P(x_2\|x_1) P(x_3\|x_1,x_2) `\cdots`{=tex}
P(x_n\|x_1,`\ldots`{=tex},x\_{n-1}) \]

This is the mathematical foundation of autoregressive language modeling.

------------------------------------------------------------------------

## 3.5 Language Models and the Chain Rule

Suppose:

``` text
The cat sat
```

A language model can estimate:

> **Formula:** P(The cat sat)

as:

> **Formula:** P(The) P(cat\|The) P(sat\|The cat)

For a longer sentence, we continue the process.

This means that generating a sentence can be understood as repeatedly
predicting the next token.

------------------------------------------------------------------------

## 3.6 Bayes' Theorem

Bayes' theorem is:

> **Formula:** P(A\|B)= fracP(B\|A)P(A) P(B)

It allows us to reverse conditional relationships.

Although modern neural language models are not simply "Bayesian
systems," Bayes' theorem is an essential part of probabilistic thinking.

------------------------------------------------------------------------

## 3.7 Example

Suppose a test detects a condition.

Let:

> **Formula:** P(D)=0.01

and:

> **Formula:** P(+\|D)=0.95

Suppose:

> **Formula:** P(+\|neg D)=0.05

Then:

> **Formula:** P(+)=P(+\|D)P(D)+P(+\|neg D)P(neg D)

Therefore:

> **Formula:** P(+)=0.95(0.01)+0.05(0.99)

> **Formula:** P(+)=0.059

Bayes gives:

> **Formula:** P(D\|+)= frac0.95(0.01) 0.059

approximately:

> **Formula:** 0.161

The lesson is important:

> A highly accurate positive test does not automatically mean a positive
> result has a high posterior probability.

The prior probability matters.

------------------------------------------------------------------------

# Chapter 4: Maximum Likelihood and Learning from Data

## 4.1 Where Do Probabilities Come From?

A language model cannot simply invent its probability distribution.

It must learn parameters from data.

Suppose a model has parameters:

> **Formula:** theta

The model represents:

> **Formula:** P_theta(x)

The goal is to find parameters that make observed training data
probable.

------------------------------------------------------------------------

## 4.2 Likelihood

Suppose our dataset contains:

> **Formula:** D=x_1,x_2,ldots,x_n

The likelihood is:

> **Formula:** L(theta)= prod_i=1\^n P_theta(x_i)

We want parameters that maximize this likelihood:

> **Formula:** theta\^\*

`\arg`{=tex}`\max`{=tex}\_`\theta `{=tex}L(`\theta`{=tex}) \]

This is Maximum Likelihood Estimation.

------------------------------------------------------------------------

## 4.3 Why Products Become Difficult

If the dataset contains thousands or millions of examples, multiplying
probabilities can produce extremely small numbers.

For example:

> **Formula:** 0.1\^1000

is tiny.

Instead, we use logarithms.

Because:

> **Formula:** log(ab)=log(a)+log(b)

we get:

> **Formula:** log L(theta)

`\sum`{=tex}\_i `\log `{=tex}P\_`\theta`{=tex}(x_i) \]

Maximizing likelihood is equivalent to maximizing log-likelihood.

------------------------------------------------------------------------

## 4.4 Negative Log-Likelihood

Machine learning systems usually minimize a loss.

Therefore we define:

> **Formula:** NLL

\-`\sum`{=tex}\_i `\log `{=tex}P\_`\theta`{=tex}(x_i) \]

Minimizing NLL is equivalent to maximizing likelihood.

This is one of the most important connections between probability and
machine learning optimization.

------------------------------------------------------------------------

## 4.5 A Tiny Example

Suppose the correct token has predicted probability:

``` text
0.8
```

Its negative log-likelihood is:

> **Formula:** -log(0.8)

Using Python:

``` python
import numpy as np

p = 0.8

loss = -np.log(p)

print(loss)
```

If the model predicts:

``` text
0.01
```

the loss is much larger.

``` python
p = 0.01

loss = -np.log(p)

print(loss)
```

The model is strongly penalized for assigning very low probability to
the correct answer.

------------------------------------------------------------------------

## 4.6 Learning Means Adjusting Probability

This gives us a powerful interpretation:

Training a language model means adjusting its parameters so that correct
tokens receive higher probability.

The model repeatedly observes:

``` text
context -> correct next token
```

and modifies its parameters.

Over time:

``` text
P(correct token | context)
```

should increase.

------------------------------------------------------------------------

# Chapter 5: Information Theory

## 5.1 What Is Information?

Information theory gives us mathematical tools for measuring uncertainty
and surprise.

One of the most famous quantities is information content.

For an event with probability (p):

> **Formula:** I(x)=-log_2 p(x)

A rare event contains more information.

A common event contains less information.

------------------------------------------------------------------------

## 5.2 Example

If:

> **Formula:** p=0.5

then:

> **Formula:** I=-log_2(0.5)=1

If:

> **Formula:** p=0.01

then:

> **Formula:** I=-log_2(0.01)

which is much larger.

The less expected an event is, the more surprising it is.

------------------------------------------------------------------------

## 5.3 Entropy

Entropy measures the average uncertainty of a probability distribution.

For a discrete distribution:

> **Formula:** H(X)

\-`\sum`{=tex}\_x P(x)`\log `{=tex}P(x) \]

Using base 2 gives entropy in bits.

------------------------------------------------------------------------

## 5.4 Maximum Entropy

Suppose we have three equally likely outcomes:

``` text
0.333
0.333
0.333
```

There is significant uncertainty.

But suppose:

``` text
0.98
0.01
0.01
```

The outcome is much more predictable.

Therefore entropy is high when probability is spread out and low when
one outcome dominates.

------------------------------------------------------------------------

## 5.5 Python Implementation

``` python
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

------------------------------------------------------------------------

## 5.6 Why Entropy Matters for Language

Consider two contexts.

Context A:

``` text
The capital of France is
```

The next token is highly predictable.

Entropy is relatively low.

Context B:

``` text
I wonder what will happen tomorrow when
```

Many continuations are possible.

Entropy can be higher.

A language model must learn these differences in uncertainty.

------------------------------------------------------------------------

## 5.7 Cross-Entropy

Cross-entropy measures how well one probability distribution represents
another.

For distributions (p) and (q):

> **Formula:** H(p,q)

\-`\sum`{=tex}\_x p(x)`\log `{=tex}q(x) \]

In supervised language modeling, the target distribution is often
represented as a one-hot vector.

If the correct token is (k):

> **Formula:** p_k=1

and every other target probability is zero.

Then cross-entropy becomes:

> **Formula:** H(p,q)=-log q_k

This is exactly the negative log-likelihood of the correct token.

------------------------------------------------------------------------

# Chapter 6: Cross-Entropy and Language Models

## 6.1 The Training Objective

Suppose the vocabulary contains:

``` text
["cat", "dog", "bird"]
```

The correct token is:

``` text
cat
```

The target distribution is:

``` text
[1, 0, 0]
```

Suppose the model predicts:

``` text
[0.7, 0.2, 0.1]
```

Cross-entropy is:

> **Formula:** -( 1log(0.7) + 0log(0.2) + 0log(0.1) )

Therefore:

> **Formula:** Loss=-log(0.7)

------------------------------------------------------------------------

## 6.2 Python

``` python
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

------------------------------------------------------------------------

## 6.3 What Happens When the Model Is Wrong?

Suppose:

``` text
prediction = [0.01, 0.49, 0.50]
```

The model gives the correct token only 1% probability.

The loss becomes:

> **Formula:** -log(0.01)

which is large.

This creates a strong learning signal.

------------------------------------------------------------------------

## 6.4 Cross-Entropy and Softmax

In a neural language model, we usually have:

``` text
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

This pipeline is one of the central computational patterns in modern
language models.

------------------------------------------------------------------------

## 6.5 Stable Softmax

Naively calculating:

``` python
np.exp(logits)
```

can overflow for very large logits.

Instead:

``` python
def stable_softmax(logits):
    shifted = logits - np.max(logits)
    exp_values = np.exp(shifted)
    return exp_values / np.sum(exp_values)
```

Subtracting the maximum does not change the resulting probabilities
because softmax is invariant to adding or subtracting the same constant
from every logit.

------------------------------------------------------------------------

## 6.6 Stable Cross-Entropy

A numerically stable implementation can operate directly on logits.

``` python
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

------------------------------------------------------------------------

# Chapter 7: Softmax, Temperature, and Sampling

## 7.1 Why Sampling Matters

Suppose a model predicts:

``` text
mat       0.60
floor     0.25
chair     0.10
street    0.05
```

Greedy decoding always selects:

``` text
mat
```

But generative AI often needs diversity.

Sampling allows the model to choose according to probability.

------------------------------------------------------------------------

## 7.2 Categorical Sampling

``` python
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

------------------------------------------------------------------------

## 7.3 Temperature

Temperature modifies the sharpness of the distribution.

Given logits (z_i):

> **Formula:** P_i= ( e\^z_i/T ) / ( sum_j e\^z_j/T )

where (T) is temperature.

------------------------------------------------------------------------

## 7.4 Low Temperature

If:

> **Formula:** T\<1

the distribution becomes sharper.

The highest-probability tokens become more dominant.

This usually produces more predictable output.

------------------------------------------------------------------------

## 7.5 High Temperature

If:

> **Formula:** T\>1

the distribution becomes flatter.

Lower-probability tokens become more likely.

This can increase variety but also increase randomness.

------------------------------------------------------------------------

## 7.6 Python Implementation

``` python
def temperature_softmax(logits, temperature=1.0):
    scaled = logits / temperature

    shifted = scaled - np.max(scaled)

    exp_values = np.exp(shifted)

    return exp_values / exp_values.sum()
```

Example:

``` python
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

------------------------------------------------------------------------

## 7.7 Top-k Sampling

Another strategy is top-k sampling.

Suppose the model has thousands of possible tokens.

We keep only the (k) highest-probability tokens.

For example:

``` text
top 5 tokens
```

Then we renormalize their probabilities.

Conceptually:

``` python
def top_k_filter(probabilities, k):
    indices = np.argsort(probabilities)[-k:]

    filtered = np.zeros_like(probabilities)

    filtered[indices] = probabilities[indices]

    filtered /= filtered.sum()

    return filtered
```

------------------------------------------------------------------------

## 7.8 Why Sampling Is Not the Same as Random Guessing

Random guessing treats all outcomes equally.

Sampling from a language model does not.

The model's learned distribution determines the probability of each
token.

Therefore:

> Sampling is controlled randomness.

------------------------------------------------------------------------

# Chapter 8: From Probability to Text Generation

## 8.1 Autoregressive Generation

The basic generation loop is simple.

Start with a prompt:

``` text
The future of AI
```

Predict the next token.

Append it.

Predict again.

Continue.

Mathematically:

> **Formula:** x_t+1 sim P(x\|x_1,ldots,x_t)

------------------------------------------------------------------------

## 8.2 Conceptual Algorithm

``` text
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

------------------------------------------------------------------------

## 8.3 A Tiny Bigram Model

We can build a simple language model without a neural network.

Consider:

``` text
the cat sat
the cat slept
the dog sat
the dog ran
```

We count transitions.

For example:

``` text
the -> cat: 2
the -> dog: 2
cat -> sat: 1
cat -> slept: 1
dog -> sat: 1
dog -> ran: 1
```

Then:

> **Formula:** P(cat\|the)=0.5

and:

> **Formula:** P(dog\|the)=0.5

------------------------------------------------------------------------

## 8.4 Building Counts

``` python
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

------------------------------------------------------------------------

## 8.5 Converting Counts to Probabilities

``` python
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

------------------------------------------------------------------------

## 8.6 Generating Text

``` python
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

``` python
current = "the"

generated = [current]

for _ in range(10):
    current = next_token(current)
    generated.append(current)

print(" ".join(generated))
```

------------------------------------------------------------------------

## 8.7 What Does This Teach Us?

Our tiny model has no Transformer.

It has no embeddings.

It has no attention.

Yet it already demonstrates the central idea:

> **Formula:** context arrow probability distribution arrow sample

Modern language models make this process dramatically more powerful by
learning sophisticated representations of context.

------------------------------------------------------------------------

# Chapter 9: Perplexity and Measuring Language Models

## 9.1 Why Accuracy Is Not Enough

Suppose a model predicts:

``` text
cat: 0.51
dog: 0.49
```

Another model predicts:

``` text
cat: 0.99
dog: 0.01
```

If the correct answer is `cat`, both models are correct under simple
classification accuracy.

But clearly the second model is much more confident.

We need a metric that considers probabilities.

Cross-entropy provides one.

Perplexity provides another interpretation.

------------------------------------------------------------------------

## 9.2 Definition

For a sequence of (N) tokens:

> **Formula:** PP= exp ( -(1) / (N) sum_i=1\^N log P(x_i) )

If logarithms are base 2:

> **Formula:** PP= 2\^H

where (H) is average cross-entropy in bits.

------------------------------------------------------------------------

## 9.3 Interpretation

Lower perplexity generally means the model assigns higher probability to
the observed sequence.

If:

> **Formula:** PP=10

we can loosely interpret the model as having uncertainty comparable to
choosing among about ten equally likely possibilities at each prediction
step.

This is an intuition, not a literal description of the vocabulary size.

------------------------------------------------------------------------

## 9.4 Python

``` python
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

------------------------------------------------------------------------

## 9.5 Perplexity and Model Comparison

If two models are evaluated on the same dataset and under comparable
conditions, the model with lower perplexity generally assigns greater
probability to the observed tokens.

However, perplexity should not be interpreted without considering:

-   tokenizer
-   vocabulary
-   dataset
-   preprocessing
-   evaluation setup

Different tokenization schemes can make raw perplexity comparisons
misleading.

------------------------------------------------------------------------

# Chapter 10: Building a Tiny Probabilistic Language Model

## 10.1 The Goal

We will now combine the concepts into a small model.

The model will:

1.  tokenize text
2.  count transitions
3.  calculate probabilities
4.  generate text
5.  evaluate likelihood

This is not a neural language model.

It is a mathematical laboratory.

------------------------------------------------------------------------

## 10.2 Training Data

``` python
corpus = [
    "the cat sat on the mat",
    "the cat slept on the mat",
    "the dog sat on the floor",
    "the dog slept on the floor",
    "the bird sat on the tree"
]
```

------------------------------------------------------------------------

## 10.3 Tokenization

``` python
sentences = [
    sentence.split()
    for sentence in corpus
]

print(sentences)
```

------------------------------------------------------------------------

## 10.4 Bigram Counts

``` python
from collections import defaultdict, Counter

bigram_counts = defaultdict(Counter)

for sentence in sentences:
    for a, b in zip(sentence, sentence[1:]):
        bigram_counts[a][b] += 1
```

------------------------------------------------------------------------

## 10.5 Probability Table

``` python
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

``` python
print(
    probabilities_for("the")
)
```

------------------------------------------------------------------------

## 10.6 Generation

``` python
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

``` python
print(generate("the"))
```

------------------------------------------------------------------------

## 10.7 The Problem with Raw Counts

Our model only remembers one previous token.

Therefore:

``` text
the cat
```

and:

``` text
the dog
```

both begin with the same context:

``` text
the
```

A larger context would allow better predictions.

This motivates higher-order language models and eventually neural
architectures.

------------------------------------------------------------------------

## 10.8 Smoothing

A problem occurs when a transition never appeared in the training data.

Suppose:

``` text
cat -> ran
```

never appeared.

Our model assigns:

> **Formula:** P(ran\|cat)=0

This can cause problems because:

> **Formula:** log(0)

is undefined.

One classical solution is Laplace smoothing.

------------------------------------------------------------------------

## 10.9 Laplace Smoothing

If:

> **Formula:** count(x,y)

is the observed count, we can use:

> **Formula:** P(y\|x)

```{=tex}
\frac{
count(x,y)+\alpha
}{
count(x)+\alpha V
}
```
\]

where:

-   (`\alpha`{=tex}) is the smoothing parameter
-   (V) is vocabulary size

For Laplace smoothing:

> **Formula:** alpha=1

------------------------------------------------------------------------

## 10.10 Python

``` python
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

------------------------------------------------------------------------

# Chapter 11: Putting Everything Together

## 11.1 The Full Mathematical Pipeline

We can now see the complete picture.

A language model receives context:

> **Formula:** x_1,ldots,x_t

and computes scores:

> **Formula:** z_1,ldots,z_V

These scores become probabilities:

> **Formula:** P(x_i\|context)

using softmax.

The probability of the correct token produces a loss:

> **Formula:** L=-log P(correct\|context)

The training algorithm modifies model parameters to reduce the average
loss.

During generation, the model converts the learned distribution into a
token using a decoding strategy.

------------------------------------------------------------------------

## 11.2 The Complete Flow

``` text
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

``` text
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

------------------------------------------------------------------------

## 11.3 Why the Same Mathematics Appears Everywhere

Probability appears in:

-   prediction
-   training
-   evaluation
-   sampling
-   uncertainty
-   generation

Information theory appears in:

-   entropy
-   cross-entropy
-   compression
-   loss functions
-   model evaluation

Optimization appears in:

-   parameter learning
-   minimizing loss
-   improving predictions

These subjects are not isolated.

They form one mathematical system.

------------------------------------------------------------------------

## 11.4 From Bigram Models to Transformers

Our bigram model uses:

> **Formula:** P(x_t\|x_t-1)

A more powerful model might use:

> **Formula:** P(x_t\|x_1,ldots,x_t-1)

A Transformer uses learned representations and attention to model
relationships across the context.

The architecture becomes much more complex.

The probabilistic objective remains surprisingly familiar.

The model still ultimately produces:

> **Formula:** P(next token\|context)

That is one of the most important ideas to remember.

------------------------------------------------------------------------

# Chapter 12: Final Project

## Build a Mini Language Generation Engine

The final project combines everything in this book.

The goal is to build a small probabilistic text-generation engine using
Python and NumPy.

------------------------------------------------------------------------

## 12.1 Project Requirements

Your engine should:

1.  accept a training corpus
2.  tokenize the corpus
3.  construct token transition counts
4.  convert counts into probabilities
5.  calculate entropy
6.  calculate negative log-likelihood
7.  calculate perplexity
8.  apply temperature
9.  sample the next token
10. generate a sequence

------------------------------------------------------------------------

## 12.2 Complete Implementation

``` python
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

------------------------------------------------------------------------

## 12.3 Training the Model

``` python
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

------------------------------------------------------------------------

## 12.4 Inspecting Probability

``` python
print(
    model.probabilities("the")
)
```

You may see something conceptually similar to:

``` text
{
    "cat": ...,
    "dog": ...,
    "bird": ...
}
```

The exact values depend on the corpus.

------------------------------------------------------------------------

## 12.5 Measuring Entropy

``` python
print(
    model.entropy("the")
)
```

If the next token is evenly distributed among several possibilities,
entropy will be relatively high.

If one token dominates, entropy will be lower.

------------------------------------------------------------------------

## 12.6 Generating Text

``` python
print(
    model.generate(
        "the",
        length=15,
        temperature=1.0
    )
)
```

Try:

``` python
temperature=0.5
```

Then:

``` python
temperature=2.0
```

Compare the generated sequences.

------------------------------------------------------------------------

## 12.7 What You Should Observe

At lower temperature, generation tends to become more concentrated
around high-probability transitions.

At higher temperature, probability becomes flatter and generation
becomes more exploratory.

This demonstrates an important principle:

> Generation is not separate from probability. Generation is probability
> being used operationally.

------------------------------------------------------------------------

# Conclusion

Generative AI can appear enormously complicated.

Modern language models contain billions of parameters, sophisticated
architectures, large datasets, and powerful optimization systems.

But beneath that complexity is a mathematical structure that can be
understood step by step.

The model observes data.

It learns statistical relationships.

It produces scores.

Scores become probabilities.

Probabilities define uncertainty.

Uncertainty can be measured with information theory.

The probability assigned to the correct token becomes a learning signal
through negative log-likelihood and cross-entropy.

During generation, the probability distribution becomes a mechanism for
selecting the next token.

The loop then repeats.

> **Formula:** context arrow prediction arrow probability arrow sampling
> arrow token arrow new context

This is the mathematical heart of autoregressive generation.

------------------------------------------------------------------------

# Appendix A: Essential Equations

## Probability

> **Formula:** 0leq P(A)leq1

## Conditional Probability

> **Formula:** P(A\|B)

```{=tex}
\frac{P(A\cap B)}
```
{P(B)} \]

## Joint Probability

> **Formula:** P(A,B)

P(A\|B)P(B) \]

## Bayes' Theorem

> **Formula:** P(A\|B)

```{=tex}
\frac{
P(B|A)P(A)
}{
P(B)
}
```
\]

## Chain Rule

> **Formula:** P(x_1,ldots,x_n)

`\prod`{=tex}\_{i=1}\^{n} P(x_i\|x_1,`\ldots`{=tex},x\_{i-1}) \]

## Information

> **Formula:** I(x)=-log p(x)

## Entropy

> **Formula:** H(X)

\-`\sum`{=tex}\_x P(x)`\log `{=tex}P(x) \]

## Cross-Entropy

> **Formula:** H(p,q)

\-`\sum`{=tex}\_x p(x)`\log `{=tex}q(x) \]

## Negative Log-Likelihood

> **Formula:** NLL

\-`\sum`{=tex}\_i`\log `{=tex}P(x_i) \]

## Softmax

> **Formula:** P_i

```{=tex}
\frac{e^{z\_i}}
```
{`\sum`{=tex}\_j e\^{z_j}} \]

## Temperature Softmax

> **Formula:** P_i

```{=tex}
\frac{e^{z\_i/T}}
```
{`\sum`{=tex}\_j e\^{z_j/T}} \]

## Perplexity

> **Formula:** PP

```{=tex}
\exp
```
`\left`{=tex}( -`\frac{1}{N}`{=tex} `\sum`{=tex}\_i `\log `{=tex}P(x_i)
`\right`{=tex}) \]

------------------------------------------------------------------------

# Appendix B: Python Mathematical Toolkit

``` python
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

------------------------------------------------------------------------

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

-   greedy decoding
-   sampling
-   temperature sampling
-   top-k sampling
-   top-p sampling

Once these five questions become intuitive, much of language-model
generation becomes easier to reason about.

------------------------------------------------------------------------

# Final Perspective

The mathematics of generative AI is not a collection of unrelated
equations.

It is a connected system.

Probability describes what may happen.

Conditional probability describes what may happen given context.

The chain rule describes the probability of sequences.

Maximum likelihood explains how models can learn from observed data.

Information theory measures uncertainty.

Cross-entropy measures how well predicted probabilities match observed
outcomes.

Softmax transforms model scores into probabilities.

Sampling transforms probabilities into generated tokens.

And autoregressive generation repeats the entire process.

The result is a simple mathematical loop hidden inside extremely
sophisticated systems:

> **Formula:** Context arrow Probability arrow Token arrow Context

Understanding this loop is one of the clearest ways to begin
understanding Generative AI.

------------------------------------------------------------------------

# Chapter 13: Practical Probability Labs

Chapter 13 turns the mathematical ideas of this book into short
experiments. Each lab is deliberately small. The objective is not to
build a production language model, but to make probability visible and
testable.

## 13.1 Lab 1: Verify a Probability Distribution

Start with three possible next tokens.

``` python
import numpy as np

tokens = ["cat", "dog", "bird"]
probabilities = np.array([0.50, 0.30, 0.20])

print("sum =", probabilities.sum())
print("minimum =", probabilities.min())
```

A valid discrete probability distribution must have non-negative entries
and a total of one. These two checks are simple, but they are useful
whenever probabilities are produced by custom code.

A good engineering habit is to validate assumptions early. If a vector
that is supposed to represent probabilities sums to 1.4, the problem
should be found before sampling begins.

## 13.2 Lab 2: Compare Two Distributions

Consider two models that predict the same vocabulary.

``` python
p = np.array([0.80, 0.10, 0.10])
q = np.array([0.34, 0.33, 0.33])

print(-np.sum(p * np.log2(p)))
print(-np.sum(q * np.log2(q)))
```

The first distribution is concentrated around one outcome. The second is
much flatter.

Entropy makes this difference measurable. The flatter distribution has
greater uncertainty because probability mass is spread across more
alternatives.

This is a useful mental model for language generation. Some contexts
strongly constrain the next token. Other contexts permit many plausible
continuations.

## 13.3 Lab 3: Surprise

Information content can be computed directly.

``` python
def information(probability):
    return -np.log2(probability)

for p in [0.5, 0.1, 0.01]:
    print(p, information(p))
```

As probability decreases, surprise increases.

The logarithm is important because it turns multiplication of
probabilities into addition of information. A sequence of several
moderately unlikely events can therefore be analyzed as the sum of their
individual information values.

## 13.4 Lab 4: Conditional Probability from Counts

Suppose a tiny corpus contains:

``` text
the cat
the dog
the cat
the bird
the dog
```

After the token `the`, the observed counts are:

``` text
cat   2
dog   2
bird  1
```

The conditional probabilities are therefore:

``` text
P(cat | the)  = 2 / 5
P(dog | the)  = 2 / 5
P(bird | the) = 1 / 5
```

Python can calculate the same values.

``` python
counts = {
    "cat": 2,
    "dog": 2,
    "bird": 1,
}

total = sum(counts.values())

probabilities = {
    token: count / total
    for token, count in counts.items()
}

print(probabilities)
```

The important point is that conditional probability can emerge directly
from observed frequencies. Neural language models use vastly more
sophisticated representations, but the probabilistic interpretation
remains.

## 13.5 Lab 5: Sampling Repeatedly

One sample can be misleading. Repeated sampling makes the underlying
distribution easier to see.

``` python
rng = np.random.default_rng(7)

tokens = np.array(["A", "B", "C"])
p = np.array([0.70, 0.20, 0.10])

samples = rng.choice(
    tokens,
    size=1000,
    p=p
)

for token in tokens:
    frequency = np.mean(samples == token)
    print(token, frequency)
```

The observed frequencies will not be exactly 0.70, 0.20, and 0.10.
Randomness creates variation.

As the number of samples grows, however, the observed frequencies tend
to move closer to the underlying probabilities.

This distinction matters in generative AI. A generated sentence is one
sample, not a direct display of the entire probability distribution.

## 13.6 Lab 6: Temperature as a Controlled Transformation

Temperature does not create new information. It changes how strongly the
existing logits influence the resulting distribution.

``` python
def temperature_softmax(logits, temperature):
    scaled = logits / temperature
    scaled = scaled - np.max(scaled)
    exp_values = np.exp(scaled)
    return exp_values / exp_values.sum()

logits = np.array([3.0, 2.0, 1.0])

for temperature in [0.5, 1.0, 2.0]:
    print(
        temperature,
        temperature_softmax(logits, temperature)
    )
```

At lower temperature, the largest logit receives more of the probability
mass.

At higher temperature, the distribution becomes flatter.

Temperature therefore acts as a decoding control. It does not retrain
the model and does not change the underlying learned parameters.

## 13.7 Lab 7: Greedy Decoding Versus Sampling

Suppose:

``` text
cat    0.55
dog    0.30
bird   0.15
```

Greedy decoding always chooses `cat`.

Sampling can choose all three outcomes, but not equally often.

This produces an important distinction:

``` text
greedy decoding = deterministic choice
sampling        = probabilistic choice
```

Neither strategy is universally best. The appropriate method depends on
the task.

A deterministic extraction task may benefit from predictable decoding.
Creative generation may benefit from controlled sampling.

## 13.8 Lab 8: Why Seed Values Matter

Random experiments are easier to debug when they can be reproduced.

``` python
rng1 = np.random.default_rng(42)
rng2 = np.random.default_rng(42)

a = rng1.choice(["A", "B", "C"], size=10)
b = rng2.choice(["A", "B", "C"], size=10)

print(np.array_equal(a, b))
```

The result is `True`.

A random seed does not remove randomness from the algorithm. It makes
the pseudo-random sequence repeatable.

For educational experiments, reproducibility is extremely valuable
because it lets us compare code changes without changing the random
sequence at the same time.

## 13.9 Lab 9: A Small Numerical Sanity Checklist

Before trusting a probability-based program, check:

1.  Are probabilities non-negative?
2.  Do they sum to approximately one?
3.  Are logarithms protected from zero when necessary?
4.  Is the temperature positive?
5.  Does sampling use the intended distribution?
6.  Can the experiment be reproduced with a fixed seed?
7.  Are evaluation data and training data clearly separated?

These checks are simple, but they reflect a broader principle of machine
learning engineering:

> Mathematical assumptions should become explicit software checks
> whenever possible.

------------------------------------------------------------------------

# Chapter 14: Numerical Stability in Generative AI

Probability formulas are elegant on paper. Computers, however, work with
finite-precision numbers. A mathematically correct expression can still
produce an unreliable numerical result if it is implemented carelessly.

## 14.1 The Overflow Problem

Consider:

``` python
import numpy as np

x = np.array([1000.0, 1001.0])

print(np.exp(x))
```

The exponential grows extremely quickly. Values of this size cannot be
represented safely in ordinary floating-point arithmetic.

Softmax appears to require exponentials, so a naive implementation can
fail.

## 14.2 Stable Softmax

The standard solution is to subtract the largest logit.

``` python
def stable_softmax(x):
    x = np.asarray(x, dtype=float)
    shifted = x - np.max(x)
    exp_values = np.exp(shifted)
    return exp_values / exp_values.sum()
```

Why is this valid?

For any constant `c`:

``` text
exp(z_i - c) / sum_j exp(z_j - c)
```

is equal to:

``` text
exp(z_i) / sum_j exp(z_j)
```

because the common factor `exp(-c)` cancels.

Choosing:

``` text
c = max(z)
```

makes the largest shifted value equal to zero. Every other shifted value
is therefore less than or equal to zero, keeping the exponentials in a
much safer numerical range.

## 14.3 Log-Sum-Exp

A related operation is:

``` text
log(sum_i exp(z_i))
```

This expression appears throughout probabilistic machine learning.

The stable form is based on:

``` text
m = max(z)
log(sum_i exp(z_i))
=
m + log(sum_i exp(z_i - m))
```

Python:

``` python
def logsumexp(z):
    z = np.asarray(z, dtype=float)
    m = np.max(z)
    return m + np.log(np.sum(np.exp(z - m)))
```

The same idea appears again and again: shift values before
exponentiating.

## 14.4 Why log Probabilities Are Useful

Suppose a sequence has token probabilities:

``` text
0.2
0.1
0.05
0.4
0.3
```

Its joint probability is their product.

``` python
probabilities = np.array([
    0.2, 0.1, 0.05, 0.4, 0.3
])

joint = np.prod(probabilities)
```

For long sequences, the product can become extremely small.

Instead, compute:

``` python
log_probability = np.sum(
    np.log(probabilities)
)
```

The log representation is easier to handle numerically and is also
convenient mathematically because products become sums.

## 14.5 Underflow and Zero Probabilities

A model that assigns probability exactly zero to an observed event
creates a problem:

``` text
log(0)
```

is not finite.

This is one reason smoothing is useful in count-based models.

Another common technique is clipping:

``` python
safe_probabilities = np.clip(
    probabilities,
    1e-12,
    1.0
)
```

Clipping is not a replacement for a sound probabilistic model, but it
can protect numerical code from invalid logarithms.

## 14.6 Floating-Point Equality

Computer arithmetic is approximate.

Instead of checking:

``` python
probabilities.sum() == 1.0
```

prefer:

``` python
np.isclose(
    probabilities.sum(),
    1.0
)
```

This distinction becomes important when probabilities are produced by
many floating-point operations.

A tiny difference such as:

``` text
0.9999999998
```

does not normally mean that the probability distribution is invalid.

## 14.7 Numerical Stability Is Part of the Mathematics

It is tempting to think of numerical stability as a programming detail
separate from theory.

In practice, the two are connected.

A formula that is mathematically correct but numerically unstable is not
a reliable computational implementation.

Generative AI systems perform enormous numbers of matrix operations,
exponentials, logarithms, and probability calculations. Stable
formulations are therefore essential.

## 14.8 A Stable Probability Pipeline

A useful implementation pattern is:

``` text
raw scores
    |
    v
shift / normalize
    |
    v
stable exponentials
    |
    v
probabilities
    |
    v
log probability or sampling
```

At each stage, the goal is to keep values in a numerically manageable
range.

## 14.9 Practical Rules

When implementing probability calculations:

-   subtract the maximum before exponentiating logits;
-   use logarithms for long products;
-   avoid taking `log(0)`;
-   use `np.isclose` for floating-point comparisons;
-   validate probability sums;
-   test extreme inputs, not only ordinary inputs.

These habits scale from a tiny educational model to large
machine-learning systems.

------------------------------------------------------------------------

# Chapter 15: From Bigram Models to Neural Language Models

The bigram model in this book is intentionally simple. It remembers one
previous token. Modern language models need to use much richer context.

## 15.1 The Limitation of One-Token Context

A bigram model estimates:

``` text
P(x_t | x_(t-1))
```

Suppose the text is:

``` text
the cat sat
the dog sat
the bird flew
```

After seeing `the`, the model cannot distinguish which animal the
sentence is discussing.

Its context is only one token.

A larger n-gram model can remember more tokens, but the number of
possible contexts grows quickly.

## 15.2 The Data Sparsity Problem

Suppose a model remembers five previous tokens.

The number of possible sequences becomes enormous as vocabulary size
grows.

If the vocabulary has size `V`, then the number of possible contexts of
length `k` can be on the order of:

``` text
V^k
```

Even moderate values of `V` and `k` produce huge spaces.

Many possible sequences will never appear in the training corpus.

This is the classic sparsity problem.

## 15.3 Neural Representations

Neural language models avoid storing every possible context as a
separate table.

Instead, tokens are represented numerically.

A simplified pipeline is:

``` text
tokens
   |
   v
embeddings
   |
   v
context representation
   |
   v
neural network
   |
   v
logits
   |
   v
softmax
   |
   v
probabilities
```

The representation of context is learned rather than manually
enumerated.

## 15.4 Why Vectors Help

A token can be represented by a vector:

``` text
[0.12, -0.44, 0.73, ...]
```

The vector is not the word itself. It is a numerical representation
learned by the model.

This allows a neural system to work with continuous representations
instead of treating every possible sequence as a completely unrelated
category.

## 15.5 From Local Counts to Learned Functions

The bigram model can be viewed as a lookup table:

``` text
previous token -> distribution
```

A neural language model instead learns a function:

``` text
context representation -> distribution
```

The second approach can generalize across related contexts.

That is one of the major conceptual transitions from classical
count-based language models to neural language models.

## 15.6 The Objective Does Not Disappear

Despite the architectural change, the training objective still has a
familiar form.

For a target token `x_t`, the model wants to increase:

``` text
P(x_t | x_1, ..., x_(t-1))
```

Equivalently, it wants to reduce a loss such as:

``` text
-log P(x_t | context)
```

The architecture becomes more powerful, but the probabilistic objective
remains recognizable.

## 15.7 Why Transformers Matter

Transformers provide a way to process relationships among many positions
in a sequence.

The attention mechanism allows the model to construct context-dependent
representations by weighting information from other positions.

Conceptually:

``` text
sequence
   |
   v
representations
   |
   v
attention
   |
   v
updated representations
   |
   v
logits
   |
   v
probabilities
```

The details are beyond the main scope of this book, but the final
probabilistic interface remains the same: predict the next token.

## 15.8 Causal Direction

For autoregressive generation, a token should not use future target
tokens that would not be available at generation time.

This is why causal masking is important in Transformer language models.

The conceptual restriction is:

``` text
position t
can use positions <= t
cannot use positions > t
```

The restriction preserves the direction of prediction.

## 15.9 Training and Generation Are Different Modes

During training, the model can process many known target positions
efficiently.

During generation, the model must repeatedly select a next token and
feed it back as part of the new context.

This creates the familiar loop:

``` text
prompt
  |
  v
model
  |
  v
probabilities
  |
  v
decoder
  |
  v
new token
  |
  +----> updated context
```

The same probability machinery therefore appears in both learning and
generation, but the operational workflow is different.

## 15.10 The Big Picture

The progression can be summarized as:

``` text
frequency counts
      |
      v
n-gram probabilities
      |
      v
neural representations
      |
      v
attention and deep networks
      |
      v
large-scale language models
```

The mathematics becomes richer, but the basic probabilistic question
remains:

> Given the context, what should the model believe about the next token?

------------------------------------------------------------------------

# Chapter 16: Designing a Small Text Generator

This final chapter converts the ideas of the book into a compact design
exercise. The goal is not maximum performance. The goal is to practice
turning mathematical assumptions into explicit software components.

## 16.1 Define the Contract

Our generator will accept:

``` text
training corpus
start token
generation length
temperature
```

It will return:

``` text
generated sequence
```

Internally it will maintain:

``` text
token vocabulary
transition counts
conditional probabilities
```

## 16.2 Separate the Components

A clean design separates four responsibilities:

``` text
Tokenizer
   |
   v
Trainer
   |
   v
Probability Model
   |
   v
Decoder
```

The tokenizer decides what the tokens are.

The trainer collects statistics.

The probability model converts statistics into conditional
distributions.

The decoder turns those distributions into generated tokens.

Separating these responsibilities makes the program easier to test and
extend.

## 16.3 A Compact Implementation

``` python
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

        return {
            item: count / total
            for item, count in counter.items()
        }

    def next_token(self, token, temperature=1.0):
        probs = self.probabilities(token)

        if not probs:
            return None

        tokens = list(probs.keys())
        values = np.array(
            list(probs.values()),
            dtype=float
        )

        if temperature <= 0:
            raise ValueError(
                "temperature must be positive"
            )

        logits = np.log(
            np.clip(values, 1e-12, 1.0)
        )

        logits = logits / temperature
        logits = logits - np.max(logits)

        weights = np.exp(logits)
        weights = weights / weights.sum()

        return self.rng.choice(
            tokens,
            p=weights
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
            token = self.next_token(
                current,
                temperature
            )

            if token is None:
                break

            output.append(token)
            current = token

        return " ".join(output)
```

## 16.4 Training the Generator

Use a small corpus:

``` python
corpus = [
    "the cat sat on the mat",
    "the cat slept on the mat",
    "the dog sat on the floor",
    "the dog slept on the floor",
    "the bird sat on the tree",
    "the bird flew over the tree",
]
```

Then:

``` python
model = SmallTextGenerator(seed=42)
model.train(corpus)

print(
    model.probabilities("the")
)
```

The result is a conditional distribution derived entirely from observed
transitions.

## 16.5 Generating at Different Temperatures

``` python
print(
    model.generate(
        "the",
        length=15,
        temperature=0.5
    )
)

print(
    model.generate(
        "the",
        length=15,
        temperature=1.0
    )
)

print(
    model.generate(
        "the",
        length=15,
        temperature=2.0
    )
)
```

Because the generator uses a fixed seed, the experiment is reproducible.

Changing the temperature changes the distribution used by the decoder.

## 16.6 Testing the Model

A small model still deserves tests.

``` python
p = model.probabilities("the")

assert p
assert np.isclose(
    sum(p.values()),
    1.0
)

for value in p.values():
    assert value >= 0
```

Test invalid temperatures too:

``` python
try:
    model.next_token(
        "the",
        temperature=0
    )
except ValueError:
    print("invalid temperature rejected")
```

These tests connect the mathematics directly to software behavior.

## 16.7 Measuring a Generated Sequence

Suppose the model generates:

``` text
the cat slept on the mat
```

For each observed transition, retrieve the corresponding conditional
probability.

Then compute the sequence log probability:

``` text
log P(x_1, ..., x_n)
=
sum_t log P(x_t | context)
```

This provides a bridge between generation and evaluation.

A generator should not only produce text. We can also ask how probable
that text was under the model.

## 16.8 What the Tiny Model Cannot Do

The model does not understand meaning in the human sense.

It does not possess world knowledge.

It does not model long-range dependencies effectively.

It does not learn semantic representations.

Its purpose is educational: it exposes the probabilistic machinery in a
form that can be inspected line by line.

That is precisely why such a model is valuable.

## 16.9 Extension: Add Unseen-Transition Handling

A practical extension is to handle a token with no outgoing transitions.

One simple policy is:

``` text
stop generation
```

Another is:

``` text
choose a new starting token
```

A more sophisticated model can use smoothing or back off to a
lower-order distribution.

The choice depends on the intended behavior.

## 16.10 Extension: Top-k Decoding

A top-k decoder keeps only the k most probable tokens before sampling.

``` python
def top_k_sample(tokens, probabilities, k, rng):
    k = min(k, len(tokens))

    indices = np.argsort(probabilities)[-k:]

    selected_tokens = tokens[indices]
    selected_probs = probabilities[indices]

    selected_probs = (
        selected_probs
        / selected_probs.sum()
    )

    return rng.choice(
        selected_tokens,
        p=selected_probs
    )
```

Top-k decoding is useful when the tail of a distribution contains many
extremely unlikely choices.

## 16.11 Extension: Record the Probability Trace

A useful educational improvement is to record every decision:

``` text
step
context
candidate token
probability
selected token
temperature
```

The trace makes generation observable.

Instead of seeing only the final sentence, we can inspect the
probability process that produced it.

This is a powerful debugging technique for probabilistic systems.

## 16.12 Final Engineering Checklist

Before calling the project complete, verify:

``` text
[ ] corpus loads correctly
[ ] tokens are counted
[ ] probabilities sum to one
[ ] zero-probability logs are protected
[ ] temperature is validated
[ ] sampling is reproducible when seeded
[ ] generation stops safely
[ ] tests cover normal and edge cases
```

The checklist is deliberately simple.

The deeper lesson is that mathematical definitions should become
explicit software invariants.

------------------------------------------------------------------------

# Appendix D: Worked Problems and Review Exercises

## D.1 Probability Normalization

A model predicts:

``` text
A = 0.25
B = 0.50
C = 0.25
```

Question:

Does this define a valid probability distribution?

Answer:

``` text
0.25 + 0.50 + 0.25 = 1.00
```

All values are non-negative, so the distribution is valid.

## D.2 Conditional Probability

Suppose:

``` text
P(A and B) = 0.18
P(B) = 0.60
```

Compute `P(A | B)`.

Use:

``` text
P(A | B) = P(A and B) / P(B)
```

Therefore:

``` text
P(A | B) = 0.18 / 0.60 = 0.30
```

## D.3 Information Content

If an event has probability:

``` text
p = 0.125
```

then with base-2 logarithms:

``` text
I = -log2(0.125)
```

Since `0.125 = 1/8`:

``` text
I = 3 bits
```

## D.4 Cross-Entropy

A correct token receives probability:

``` text
0.25
```

For a one-hot target, the cross-entropy is:

``` text
L = -log(0.25)
```

The exact numerical value depends on the logarithm base.

The important relationship is that assigning a smaller probability to
the correct token produces a larger loss.

## D.5 Perplexity

If the average negative log-likelihood is:

``` text
L = 1
```

using natural logarithms, then:

``` text
PP = exp(1)
```

which is approximately:

``` text
2.718
```

Perplexity therefore converts average log loss into a more intuitive
multiplicative scale.

## D.6 Temperature Reasoning

A distribution is produced from logits:

``` text
[4, 2, 0]
```

Ask:

1.  What happens when `T < 1`?
2.  What happens when `T = 1`?
3.  What happens when `T > 1`?

Answer:

-   `T < 1` makes the distribution sharper.
-   `T = 1` leaves the logits at their original scale.
-   `T > 1` makes the distribution flatter.

## D.7 Conceptual Question

Why does a language model need probability at generation time?

Because several next tokens can be plausible. Probability provides a
structured way to represent those alternatives and to select among them
according to a chosen decoding strategy.

## D.8 Design Question

Why is a bigram model useful even though modern language models are much
more complex?

Because it isolates the core probabilistic idea.

It shows:

``` text
context
  ->
conditional distribution
  ->
next token
```

Once that loop is understood, more sophisticated architectures can be
viewed as increasingly powerful ways of constructing the distribution.

## D.9 Coding Exercise

Modify the small text generator so that it returns both:

``` text
selected token
selected probability
```

For example:

``` text
token = "cat"
probability = 0.50
```

Then print the probability trace for a generated sequence.

## D.10 Reflection

After completing the exercises, explain in your own words:

1.  What is a probability distribution?
2.  What does conditional probability add?
3.  Why is the chain rule important?
4.  Why do language models use cross-entropy?
5.  What does softmax do?
6.  Why does temperature affect sampling?
7.  Why is perplexity useful?
8.  Why is numerical stability important?
9.  What does a bigram model teach us about larger language models?

If these questions can be answered clearly, the central mathematical
loop of generative language modeling is no longer a black box.

------------------------------------------------------------------------

# Final Review: The Mathematical Loop

The complete story of this book can be compressed into one sequence:

``` text
data
  |
  v
context
  |
  v
scores / logits
  |
  v
softmax
  |
  v
probability distribution
  |
  +----> entropy / uncertainty
  |
  +----> cross-entropy / loss
  |
  +----> temperature / filtering
  |
  v
sampling or greedy decoding
  |
  v
next token
  |
  +----> new context
```

Training and generation are different operations, but they meet at the
same probabilistic interface.

During training, the model learns parameters that make observed tokens
more probable.

During generation, those learned probabilities are used to choose new
tokens.

The architecture may be a tiny table, a neural network, or a Transformer
with billions of parameters. The scale changes dramatically. The central
question does not:

``` text
Given the context,
what probability should be assigned
to each possible next token?
```

That question is one of the mathematical foundations of generative AI.

------------------------------------------------------------------------

# End

## The Mathematics of Generative AI

### From Probability to Language Models

**Ahmed Adawy**

2026
