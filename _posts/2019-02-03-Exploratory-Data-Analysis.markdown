---
layout: post
title:  "Exploratory Data Analysis"
date:   2019-02-03 17:03:21
author: Kwanghee Choi
categories: datascience
---

# Overview
This is a summary of a book [Exploratory Data Analysis](https://www.amazon.com/Exploratory-Data-Analysis-John-Tukey/dp/0201076160) by [John W. Tukey](https://en.wikipedia.org/wiki/John_Tukey). When the book is written in the 70s, computing power (i.e. graph software, or data-related software) was not available for the public, let alone for researchers and analysts. Thus, the majority of the contents were dedicated to pen-and-paper methods, which I am going to omit throughout the whole summary. With that said, I believe the key concepts and ideas for analyzing and visualizing data haven’t change much since then, as visual perceptions of human beings should’ve not undergo dramatic changes. Therefore, it should be useful for this summary to concentrate more on the conceptual basis, rather than the specific techniques for analysis.

# Preface
- It is important to understand *what you can do* before you learn to measure *how well you seem to have done it*.
- This book is about *exploratory data analysis*, about looking at data to see what it seems to say. Its concern is with appearance, not with confirmation, to make it more easily handleable by human minds.
- The greatest value of a picture is when it *forces* us to notice what we never expected to see.

# 1. Scratching down numbers (stem-and-leaf)
- Exploratory data analysis (EDA) is detective work
	- Needs both tools and understanding
	- Different detailed understandings are needed for each case (Domain knowledge)
- Exploratory vs. Confirmatory
	- Uncovers indications vs. Proves indications to draw out conclusions
	- More flexible vs. More exact
	- We need both; first EDA (search, explore), then CDA (prove, confirm)
- A batch of numbers: a set of similar values
- Stem and leaf method
	- ![stem_and_leaf](https://juice500ml.github.io/assets/img/fe61569f-4964-4e07-9372-81ae8c259f55.jpeg)
	- Appearances of seperation into groups (clustering)
	- Where the values are centered for each cluster
	- How widely the values are spread for each cluseter
	- Apparent "breaks" (edge values of clusters)
	- Unexpectedly popular or unpopular values
- It is easy to understand numbers, but it is hard to find out what those numbers really imply.

# 2. Easy summaries — numerical and graphical
- Summarizing the most frequently occuring characteristics of the pattern of a batch
	- Median(Q2), Extremes (min, max), Hinges (quartiles, Q1, Q3)
	- Range: difference between extremes
	- H-spread: difference between hinges
- It would be wrong to expect a standard summary to reveal the unusual.
- There will be no substitute for having the full detail, set out in as easily managable way.
- 5-number summary
	- ![five_number_summary](https://juice500ml.github.io/assets/img/4b35fcfb-1741-4b4a-ba4b-59179809d698.jpeg)
- Dot plot and Box-and-whisker plot
	- ![dot_plot_and_box_and_whisker_plot](https://juice500ml.github.io/assets/img/4e5b81e0-3605-4db0-84cd-7fc9c875c1be.jpeg)

# 3. Easy re-expression
- If the way the numbers are collected does not ake them easy to grasp, we should change them, preserving as much information as we can use.
- Re-expressions preserving the ordering: log, sqrt, negative exponentials($-1/x, -1/x^2, -1/x^{1/2}, ...$)
- ![re_expression_on_x](https://juice500ml.github.io/assets/img/914f0d07-0039-4d73-8a4c-73e2f6e60ce2.jpeg)
- ![re_expression_on_logx](https://juice500ml.github.io/assets/img/384fbb92-45ad-4e52-a9b5-3979c5396150.jpeg)
- If one expression is straight, those above it are hollow upward, those below it are hollow downward.
- Can re-express not only the y-axis, but also the x-axis. Any axis can be re-expressed.

# 4. Effective comparison, including well-chosen expression
- Choose a good re-expression based on the following
	- Does it show symmetry within each batches well?
	- Does it show agreement among each batches well?
	- ![symmetry_and_agreement](https://juice500ml.github.io/assets/img/b73d3956-bae6-4c52-9ab4-16c280f9b692.jpeg)
- Residual = Given value - Summary value (ex. median)
- The meaning of logarithms
	- Reduces multiplications into additions.
	- log residuals are, in fact, ratios

# 5. Plots of relationship
- Given = Fit + Residual
	- Fit: An incomplete, approximate description. Part of the information. (ex. $y=ax+b$)
	- Residual: Deviation from the current description. Additional information for each point.
	- How it deviates from the description (model) = How it behaves out of the ordinary (generally)
- Using multiple linear models paired with re-expressions
	- ![linear_growth_model](https://juice500ml.github.io/assets/img/b92e7179-79a6-4113-b902-912756084dc1.jpeg)
	- ![exponential_growth_model](https://juice500ml.github.io/assets/img/4518056a-dcdf-49c9-8cc0-63a3c8d7fe24.jpeg)
	- The reason behind choosing these models to make a successful approximation, is that we already know these are population data, so we can apply demographic theory, or in other words, domain knowledge for that specific data.
- Indications for re-expressions
	- ![crowding](https://juice500ml.github.io/assets/img/1f0067ca-811c-4147-9d88-6e64954ce3b0.jpeg)

# 6. Straightening out plots
- Straightening by re-expressing x is not the same as re-expressing y.
- Just because re-expression makes things quite straight, it doesn’t say that it is a new law.

# 7. Smoothing sequences
- Given data = Smooth + Rough
	- Smooth: Smoothing models such as running medians or moving average. Connected points or smooth curve.
	- Rough: Seperate points.
- Any kind of smoothing methods (or predictive models) has some sort of judgement whatsoever. Eye-smoothing is the maximal amount of judgement, and minimal amount of arithmetic.
- Re-expression does alter the smoothness, but not very much.

# 8. Parallel and wandering schematic plots
- 
