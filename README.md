# Rank-Biased Overlap (rbo)
This is the implementation of Rank-Biased Overlap (rbo), from [this](http://www.williamwebber.com/research/papers/wmz10_tois.pdf) paper. 

The purpose of rbo is to compare 2 ranked lists, and return a numeric value between 0 and 1, to quantify their similarity, whereas 0 means completely different, and 1 means complete identical. Here the 'different' and 'identical' requires a little more clarification. 

If the two ranked lists are 

`A = [a,b,c,d,e]`, 

`B = [e,d,c,b,a]`, 

we can see that both of them rank 5 items (a, b, c, d and e), but with completely opposite order. In this case the similarity between `A` and `B` should (and will) be 0. But here we are ranking the 5 same items, hence they are conjoint. If there is third ranked list

`C = [f,g,h,i,j]`

which ranks 5 totally different items, then if we ask for the similarity between `A` and `C`, we should expect a value of 0 as well. In such non-conjoint case, we need to be able to calculate a similarity as well.

The rbo measure can handle ranked lists with different lengths as well, with proper extrapolation. For example, the rbo between the list `A` and list 

`D = [a,b,c,d,e,f,g]` 

will be 1. 

The main class is `RankingSimilarity` class, in which we calculate various implementation of rbo, with clear reference to the corresponding equations in the paper.

Please let [me](changyao.chen@gmail.com) know if there is any issue.
