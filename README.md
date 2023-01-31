# Rank-biased Overlap (RBO)
[![CircleCI](https://circleci.com/gh/changyaochen/rbo/tree/master.svg?style=svg)](https://circleci.com/gh/changyaochen/rbo/tree/master)
[![PyPI version](https://badge.fury.io/py/rbo.svg)](https://badge.fury.io/py/rbo)

This project contains a Python implementation of Rank-Biased Overlap (RBO) from: Webber, William, Alistair Moffat, and Justin Zobel. "A similarity measure for indefinite rankings." ACM Transactions on Information Systems (TOIS) 28.4 (2010): 20." ([Download][paper]).

- [Rank-biased Overlap (RBO)](#rank-biased-overlap-rbo)
  - [Introduction](#introduction)
  - [Usage](#usage)
    - [Installation using pip](#installation-using-pip)
    - [Computing RBO](#computing-rbo)
    - [Computing extrapolated RBO](#computing-extrapolated-rbo)
- [Development](#development)

## Introduction

> For a more general introduction, please refer to this blog [post](https://changyaochen.github.io/Comparing-two-ranked-lists/).

RBO compares two ranked lists, and returns a numeric value between zero and one to quantify their similarity.
A RBO value of zero indicates the lists are completely different, and a RBO of one means completely identical. The terms 'different' and 'identical' require a little more clarification.

Given two ranked lists:

    A = ["a", "b", "c", "d", "e"]
    B = ["e", "d", "c", "b", "a"]

We can see that both of them rank 5 items ("a", "b", "c", "d" and "e"), but with completely opposite order. In this case the similarity between `A` and `B` should be larger than 0 (as they contain the same items, namely, conjoint), but smaller than 1 (as the order of the items are different). If there is third ranked list

    C = ["f", "g", "h", "i", "j"]

which ranks 5 totally different items, then if we ask for the similarity between `A` and `C`, we should expect a value of 0. In such a non-conjoint case, we need to be able to calculate a similarity as well.

The RBO measure can handle ranked lists with different lengths as well, with proper extrapolation. For example, the RBO between the list `A` and list

    D = ["a", "b", "c", "d", "e", "f", "g"]

will be 1.


## Usage

### Installation using pip

To install the RBO module to the current interpreter with Pip:

    pip install rbo


### Computing RBO

The `RankingSimilarity` class contains the calculation for the different flavours of RBO, with clear reference to the corresponding equations in the paper.
Below shows how to compute the similarity of two ranked lists S and T:

```python
In [1]: import rbo

In [2]: S = [1, 2, 3]

In [3]: T = [1, 3, 2]

In [4]: rbo.RankingSimilarity(S, T).rbo()
Out[4]: 0.8333333333333334
```

Accepted data types are Python lists and Numpy arrays.
Using Pandas series is possible using the underlying Numpy array as shown below. This restriction is necessary, because using `[]` on a Pandas series queries the index, which might not number items contiguously, or might even be non-numeric.

```python
In [1]: import pandas as pd

In [2]: import rbo

In [3]: S = [1, 2, 3]

In [4]: U = pd.Series([1, 3, 2])

In [5]: rbo.RankingSimilarity(S, U.values).rbo()
Out[5]: 0.8333333333333334
```

### Computing extrapolated RBO
There is an extension of the vanilla RBO implementation, in which we extrapolate from the visible lists, and assume that the degree of agreement seen up to depth $k$ is continued indefinitely.

This extrapolated version is implemented as the `RankingSimilarity.rbo_ext()` method.


# Development

Refer to the Makefile for supplementary tasks to development, e.g., executing unit tests, or checking for proper packaging.
Please let [me][contact] know if there is any issue.

[contact]: mailto:changyao.chen@gmail.com
[paper]: http://w.codalism.com/research/papers/wmz10_tois.pdf
