# Rank-biased Overlap (RBO)
[![CircleCI](https://circleci.com/gh/changyaochen/rbo/tree/master.svg?style=svg)](https://circleci.com/gh/changyaochen/rbo/tree/master)

This project contains a Python implementation of Rank-Biased Overlap (RBO) from: Webber, William, Alistair Moffat, and Justin Zobel. "A similarity measure for indefinite rankings." ACM Transactions on Information Systems (TOIS) 28.4 (2010): 20." ([Download][paper]).


## Introduction

RBO compares two ranked lists, and returns a numeric value between zero and one to quantify their similarity.
A RBO value of zero indicates the lists are completely different, and a RBO of one means completely identical. The terms 'different' and 'identical' require a little more clarification. 

Given two ranked lists:

    A = [a, b, c, d, e]
    B = [e, d, c, b, a]

We can see that both of them rank 5 items (a, b, c, d and e), but with completely opposite order. In this case the similarity between `A` and `B` should (and will) be 0. But here we are ranking the 5 same items, hence they are conjoint. If there is third ranked list

    C = [f, g, h, i, j]

which ranks 5 totally different items, then if we ask for the similarity between `A` and `C`, we should expect a value of 0 as well. In such non-conjoint case, we need to be able to calculate a similarity as well.

The RBO measure can handle ranked lists with different lengths as well, with proper extrapolation. For example, the RBO between the list `A` and list 

    D = [a, b, c, d, e, f, g]

will be 1. 


## Usage

### Installation using Pip

To install the RBO module to the current interpreter with Pip:

    pip install -e git+https://github.com/changyaochen/rbo.git@master#egg=rbo

To add the RBO module as managed dependency with Pipenv:

    pipenv install -e git+https://github.com/changyaochen/rbo.git@master#egg=rbo

### Computing RBO

The `RankingSimilarity` class contains the calculation for the different flavours of RBO, with clear reference to the corresponding equations in the paper.
Below shows how to compute the similarity of two ranked lists S and T:

```python
In [1]: import rbo

In [2]: S = [1, 2, 3]; T = [1, 3, 2]

In [3]: rbo.RankingSimilarity(S, T).rbo()
Out[3]: 0.8333333333333334
```

Accepted datatypes are Python lists and Numpy arrays.
Using Pandas series is possible using the underlying Numpy array as shown below. This restriction is necessary, because using `[]` on a Pandas series queries the index, which might not number items contiguously, or might even be non-numeric.

```python
In [4]: import pandas as pd

In [5]: U = pd.Series([1, 3, 2, 4, 5, 6])

In [6]: rbo.RankingSimilarity(T, U.values).rbo()
Out[6]: 1.0
```


# Development

Refer to the Makefile for supplementary tasks to development, e.g., executing unit tests, or checking for proper packaging.
Please let [me][contact] know if there is any issue.

[contact]: mailto:changyao.chen@gmail.com
[paper]: http://w.codalism.com/research/papers/wmz10_tois.pdf
