---
layout: post
title:  "What is a Manifold?"
date:   2022-12-25 15:35:00
author: Kwanghee Choi
categories: math
---

# What is a Manifold?
This is the summary of the lecture, [What is a Manifold?](https://youtube.com/playlist?list=PLRlVmXqzHjUQHEx63ZFxV-0Ortgf-rpJo), by [Dr. Bijan Haney](https://www.bijanhaney.com/index.html), also known as [XylyXylyX](https://youtube.com/@XylyXylyX). The lecture primarily focuses on constructing a mathematical basis for understanding general relativity, but I was more interested in the deep learning aspect of it. So, do keep in mind that some of the content is missing.

# [Lecture 1. Point Set Topology and Topological Spaces](https://www.youtube.com/watch?v=CEXSSz0gZI4)

## Motivation
- Consider two sets: $X = \mathbb{R}^2$ and $Y = (0, 1)$.
	- Even though we are talking about set of points, we are implying its structure. Topology gives structure to a set of points.
- Example structure: Metric $d(p_1, p_2)$ ($\neq$ vector space’s metric).
	- $p_1$, $p_2$ might contain coordinates such as (x, y), but we don’t care about that. We are just defining a function $d$ that is well-defined within $\lbrace(p_1, p_2): p_1 \in S$ and $p_2 \in S \rbrace$ where $S$ is the point set.

## Topology?
- Topology $T_X$ for the point set $X$: Also a set!
	- We denote $T_X$ = {Subsets of $X$ (i.e., open set)}
	- Open set of X = Element of the topology for the point set X
	- $(X, T_X)$: Topological space
- Given any sets $u_1, u_2, u_3 \in T_X$,
	1. $u_1 \cup u2 \in T_X$ (i.e., arbitrary union, possibly infinite)
	2. $u_1 \cap u_2 \in T_X$ (i.e., finite intersections)
	3. Null set $\in T_X$ (i.e., smallest set)
	4. $X \in T_X$ (i.e., biggest set)

## Example of Topological Spaces
- Consider open sets of $\mathbb{R}^2$.

### _Usual_ Topology
- Consider the base **open ball** $ \{ x: \vert x-p\vert < r \} $. For any point p, any radius r, they are all open sets!
- But using only the current defn. Violates (1) and (2) $\to$ We need to include intersections/unions of open balls
- Any shape can be built by correctly union-ing open balls.
	- Example. Rectangle (because we allow infinite union-ing)
	- Example. Intersection of two open ball which can be built by both (1) (obviously...) and (2) (by carefully constructing sets to intersect by unions)
	- Example. Disjoint union (it’s not "connected", but still an open set)
- Individual point is NOT an open set, because we cannot arrange it without infinite intersection. We only allow finite intersections.

### Other Topologies
- Let the defn. of open set = point p. Then,  $T_X$ becomes the power set of X $\to$ **Discrete Topology**
- Let the defn. of open set = {Null, X} $\to$ **Trivial Topology**
- Open sets of (0, 1)
	- Let the def. of open set: (0, 1-1/N) where N: 2, 3, 4, ...
	- We also include the null set to avoid violating (3).
	- For N $\to \infty$, it becomes (0, 1). Hence, it doesn’t violate (4).
	- Their union/intersection will always be the bigger/smaller one, so it doesn’t violate (1) and (2)
	- The size of the base set = size of the open set (i.e., don't need further intersections/unions to describe the open set. Very rare case, strange topology!)

### TL;DR: Definition of topology is arbitrary. If it satisfies the four rules, they are all topologies.


# [Lecture 2. Elementary Definitions](https://www.youtube.com/watch?v=EsF_5LoaL_8)

### Defn. Neighborhoods
- For point p in X, we call S the neighborhood of p, when:
	1. S is the subset of X
	2. $p \in S$
	3. For bigger subset $N \supset S$, N is also the neighborhood of p.
	4. For the neighborhoods of p, S and R, $S \cap R$ is also the neighborhood of p.
	5. For the subset $T_p \subset S_p$ where both are neighborhoods of p, and for all point $r \in T_p$, $S_p$ contains the neighborhoods of $r$.

### Defn. Closed set
- Closed set is the complement of an open set.
- For any closed set C, $X-C = U$: open set, and $X-U = C$: closed set.

### Defn. Limit point
- Thm. Open set that contains p = Open neighborhood of p
	- Remark. For all point in the open set, open set is the open neighborhood for each of the points.
- For a subset $S \subset X$, p is the limit point of S if:
	- "every open neighborhood of p" $\cup S$ is not null.
- Note. S doesn't need to be the open set.
- Remark. For any boundary point p of open set S (p is not inside S but at the "boundary"), p is the limit point of S. In other words, limit point p do not need to be inside S.

### Defn. Closure
-  Given the topological space $(X, T_X)$ and the subset $S \subset X$,
	- $\bar{S}$ (Closure of S) $ = S \cup$ "all of its limit points"

### Defn. Interior
- Point $p \in S^0$ (the interior of the set S) if:
	- I can find a subset $u_p \subset S$ that is the open set containing p.
- Remark. For the usual topology, the boundary point is not inside the interior, even in the case when S is the closed set.
- Remark. $S^0$ is always open.
- Remark. $S^0$ is the union of all the open sets inside S.
- Remark. S is open if and only if $S = S^0$.
- Remark. $S^0 = {\bar{S^c}}^c$. In other words, S^0 is the complement of the closure of the complement of S.
	- Complement of S = Outside S
	- Closure of the complement of S: Outside S including the boundaries
	- Complement of the closure of the complement of S: S except the boundaries
- Remark. "Missing loner point (only a single point excluded inside the S's boundary)" inside S is also not included in $S^0$ (i.e., it is not the interior)

### Defn. Exterior
- Complement of its closure
	- Idea. Boundary is not the exterior because it’s "too close" to the set.

### Defn. Boundary
- Neither the exterior nor the interior

### Defn. Dense
- For a subset $S \subset X$, S is dense in X when:
	- For all point $p \in X$,
	- $p \in S$ **or** p is the limit point of S.
	- In other words, $p \in \bar{S}$.
- Example. Consider the set of points with rational coordinates $S = \lbrace(q_1, q_2) \vert q_1 \in \mathbb{Q} \text{ and } q_2 \in \mathbb{Q}\rbrace$.
	- S is dense in the usual topology of $\mathbb{R}^2$, because we can find an infinitely close rational number (neighborhood) for any irrational number.
	- However, S is not dense in the discrete topology.

# [Lecture 3. Alternative Topologies and Separation](https://youtu.be/yd28dGdR7Tg)

## Alternative Topologies for Intervals
- We introduce various example topologies to understand different concepts more clearly.
- Recall. Topologies for open interval (0, 1)
	- Usual topology: Open interval (Euclidean topology $T_E$)
	- "Nested interval" topology: (0, 1-1/N) where N: 2, 3, ... ($T_{NI}$)

### Closed Interval Topology $T_{CI}$

- Consider the topology $T_{CI}$ for the closed interval [-1, 1].
	- Let's set the bases as half-open intervals [-1, a) and (b, 1] where $a>0, b<0$.
		- Let's denote the former "lower base" and the latter "upper base."
	- Union/Intersection within the lower/upper base is just the bigger/smaller member (same with the "Nested interval" topology).
	- Union of the any member of the lower & upper base is always the entire set.
	- Intersection of the upper & lower element: open interval (b, a) which always includes "0."  Hence, it's not a "general" open interval.

### Cofinite Topology $T_{CF}$
- For the open interval $X$ (0, 1) with the usual topology $T_X$:
	- Choose the finite number of points. Its complement can be constructed by the following:
		- Example. Points = {0.2, 0.4}. Then, the complement of the points = (0, 0.2) $\cup$ (0.2, 0.4) $\cup$ (0.4, 1.0) $\in T_X$.
	- We can exclude the finite number of points.
		- Example. $\{0.2, 0.4\}^C \cap \{0.3, 0.4\}^C = \{0.2, 0.3, 0.4\}^C$

## Separability
### $T_0$ Separability (Kolmogorov)
- To satisfy the $T_0$ Separability:
	- For any two points $p_1, p_2 \in X$, there has to exist an open set $S \in T_X$ such that $p_1 \in S$ but $p_2 \notin S$.
	- In other words, there has to exist the open set that _distinguishes_ two points.
- Remark. $T_E$ satisfies it.
- Remark. $T_{NI}$ does not satisfy it.
	- Consider $p_1=0.1, p_2=0.2$.
	- The bases are (0, 0.5), (0, 0.67), (0, 0.75)...
	- Hence, $p_1$ and $p_2$ is always within the base (0, 0.5). $\to$ Violation!
- Remark. $T_{CI}$ satisfies it.
	- For the case where $p_1>0, p_2<0$, $T_{CI}$ can be separated by using either lower or upper base.
		- This is somewhat _stronger_ than $T_0$, because we can find separate open set for both points.
	- For the asymmetric case where $p_1 * p_2 > 0$, it can be separated by using lower/upper base only.

### $T_1$ Separability (Frechet)
- To satisfy the $T_1$ Separability:
	- For any two points $p_1, p_2 \in X$, there has to exist open sets $\mathbf{S_1, S_2} \in T_X$ such that $p_1 \in S_1, p_2 \notin S_1$ and $\mathbf{p_1 \notin S_2, p_2 \in S_2}$.
	- In other words, each has to have a neighborhood not containing the other point.
- Remark. $T_{CF}$ satisfies it.

### $T_2$ Separability (Hausdorff)
- To satisfy the $T_2$ Separability:
	- For any two points $p_1, p_2 \in X$, there has to exist **disjoint** open sets $S_1, S_2 \in T_X$ and $\mathbf{S_1 \cap S_2 = \emptyset}$,
	- such that $p_1 \in S_1, p_2 \notin S_1$ and $p_1 \notin S_2, p_2 \in S_2$.
- Remark. $T_{CF}$ does not satisfy it, but $T_E$ satisfy it.
- The most common one! Also, if you want, you can get more stronger separability than this.

### Interesting properties
- Consider the usual topological space $(\mathbb{R}^2, J)$ and the real line $L \subset \mathbb{R}^2$ on the space.
	- Subset L induces a new usual topological space $(L, T_L)$ as all the open sets in $T_L \subset J$ (i.e., the neighbors of the boundary L) acts as an open interval.
- Consider the topological space $(T, T_T), (S, T_S)$.
	- The cartesian product $T \times S$ has the topology $T_T \times T_S$.

# [Lecture 4. Countability and Continuity](https://youtu.be/L1MC5GvlxPI)

## Countability
### Motivation
- Consider the topological space $(X, J)$ and a point $p \in X$ inside the open set $S \in J$.
- Let's define a more smaller open set $S_1 \subset S$ that is the neighbor of $p$.
- Let's keep defining the smaller open set such that $S_{n+1} \subset S_n$.
- The nested collection could terminate (ex. Discrete Topology), but for the open ball topology, there will be an infinite number of open sets.

### Defn. First-Countability
- The topological space $(X, J)$ is first-countable when:
	- **For every point** $p \in X$, there exist a countable open nested neighborhoods.
- Remark. If we use rational coordinates on the usual topological space, we can build a countable nested collection such as a ball with radius 1/N, i.e., usual topological space is first-countable.

### Defn. Second-Countability
- The topological space $(X, J)$ is second-countable when the topology has a countable base, i.e.,
	- **For every open set** $S \in J$ can be written as $S = \cup_i b_i$ of the bases $b_i$.
- Remark. If we use rational coordinates on the usual topological space, we can define a "rational" neigborhood for every point $p \in X$, i.e., usual topological space is second-countable.

### Remarks
- If the space is second countable, it is always first-countable. However, the converse is not true.
- Manifolds that "behave well" is second-countable.
- Nested interval topology $T_{NI}$ and closed interval topology $T_{CI}$ are second-countable.
- Cofinite topology $T_{CF}$ is not first-countable. (Approach: Start with a basis, check whether one can build a smaller basis based on the initial one.)

### Example. Lower-limit Topology $T_{LL}$

- Consider a lower-limit topology with the basis set $[b, a) \in T_{LL}$.
	- Note that $(l, m) \in T_{LL}$ by the following construction:
	- Consider a sequence $b_n \to l^+$. Then, the infinite union $\cup_n^\infty [b_i, m) = (l, m)$.
- Remark. Euclidean topology $T_E \subset T_{LL}$. In other words, $T_LL$ is _finer_ to $T_E$ and $T_E$ is _coarser_ to $T_{LL}$.
- Remark. It is clearly first-countable. However, it is not second-countable.
	- Assume that there exists a countable basis $[b_n, a_m)$ where $n, m \in \mathbb{I}$.
	- One can only construct a basis that is _customized_ to a specific $(l, m)$. If we change $l$, we have to redefine $b_n$, which violates the assumption of a fixed countable basis.
- "There is always this weird counterexamples."

### TL; DR: This is why we want the manifolds to be Hausdorff & Second-countable, because, if not, weird things happen.

## Continuity
### Motivation
- Consider a function $f: X \to Y$ where $X, Y$ is endowed to each topologies $T_X, T_Y$.
- We want to define continuity of the function $f$.
- Recall. epsilon-delta definition of a limit assumes lots of information such as the existence of a distance function. We aim to define continuity without these.

### Defn. Continuity
- Consider the inverse mapping $f^{-1}$ and the arbitrary open set $S_Y \in T_Y$.
- A function $f$ is continuous if the pre-image $f^{-1}(S_Y)$ is an open set in $T_X$.
- Remark. Relation with the epsilon-delta
	- [epsilon-side] For any $S_Y \in T_Y$,
	- [delta-side] we need to find the tight-enough open neighborhood $S_X \in T_X$ such that $f(S_X) \subset S_Y$.

### Examples
- Consider the function $f(x)=x$ and the topologies $T_E, T_{NI}, T_{CI}, T_{CF}, T_{LL}$.
	- Recall. Euclidian, Nested Intervals, Closed Intervals, Cofinite, Lower Limit
	- Each bases: (a, b), (0, 1-1/N), [-1, a) and (b, 1], Point exclusion, [b, a)
- $T_E \to T_{NI}$: Inverse of the nested interval (0, 1-1/N) directly maps to (a, b), i.e., for all the open set of $S_Y \in T_Y$, $f^{-1}(S_Y) \in T_X$. Hence, $f$ is cont.
- $T_E \to T_{CI}$: Open intervals are okay, But, it fails on the form of [0, a) or (b, 1] due to the point 0, 1. Hence, $f$ is not cont.
- $T_E \to T_{CF}$: N open intervals' union ($\in T_{CF}$) maps fine to  $T_E$. Hence, $f$ is cont.
- $T_E \to T_{LL}$: Half-closed interval [a, b) is not a closed set in $T_E$. Hence, $f$ is not cont.
- $T_{NI}, T_{CI}, T_{CF} \to T_E$: Consider (0.1, 0.2). It fails on everything.
- $T_{LL} \to T_E$: $f$ is cont. Recall that $T_{LL}$ is _finer_ to $T_E$.
- Everything else to $T_{Distinct}$: $f$ _has_ to be cont. because $T_{Distinct}$ is the finest topology.
- $T_{Distinct} \to T_{LL}$: Consider [0.1, 0.2]. Due to the upper limit, it fails. Hence, $f$ is not cont.

# [Lecture 5. Compactness, Connectedness, and Topological Properties](https://youtu.be/4wnLQdKZ4RU)

## Defn. Homeomorphism
- Defn. $f$ is homeomorphic when:
	- $f$ and $f^{-1}$ is both the cont. function, 1-to-1, and onto.
- Recall. 1-to-1 (injection): if $f(a) = f(b)$, $a=b$. Onto (surjection): Image is equal to its codomain.
- Remark. This is important because various topological properties are preserved for homeomorphisms, such as separability, connectedness, or compactness.
- Remark. There is no sense of shape, metric, and geometry here. It is very abstract.

## Defn. Compactness
- Defn. Open cover of a set X = A collection of open sets (subcovers) whose union covers X, i.e., $X \subset \cup_i s_i$.
- Case 1. Consider the case where the number of subset needs to be infinite to cover the open set X.
	- For example, next subcover only half of the remaining X that is not covered by the sum of previous subcovers.
	- Excluding the boundary, the subsets will _eventually_ cover all the elements in open set X, approaching the boundary as close as possible.
- Case 2. Compare it with the case where there are infinite number of subcovers, but only need finite subset of them to actually cover X.
- Defn. If I find any cover that needs infinite number of subcovers to cover X (Case 1), we call X **not compact**.
- Case 3. Same with Case 1, but with the closed set X.
	- Because of the boundary, the subcovers will get infinitely close to the boundary, but never include the boundary.
	- To include the boundary, we need to come up with a subcover that includes the boundary. It will *touch* the progressing subcovers, hence making the total number of subcovers finite.
	- Remark. One cannot found that is infinite. This case is compact.

## Defn. Connectedness
- For the topological space $(X, T_X)$, if there exists open sets $G, H \in T_X$ such that $G \cap H = \emptyset$ and $G \cup H = X$, we call that X is **not connected**.
	- Remark. If there are two or more *disconnected* subset, we call X not connected.
- Remark. Homeomorphism $f$ preserves connectedness.
	- For the topological space $(Y, T_Y)$ and function $f: X \to Y$, $f(G), f(H) \in T_Y$, $f(G) \cap f(H) = \emptyset$, and $f(G) \cup f(H) = Y$.

### Path-connectedness
- Defn. Given the arbitrary point $x, y \in X$, if I can *draw a line* between $x, y$, we call $x, y$ **path-connected**.
	- *Draw a line* means that I can define a continuous function $f: [0, 1] \to X$ where $f(0) = x, f(1) = y$.
- Defn. If I can path-connect arbitrary two points of X, we call X **path-connected**.
- Remark. If X is path-connected, X is connected. Its converse is not true.
- Remark. If one path can be "continuously deformed" into the other, such a deformation is called a homotopy.
	- On the sphere, any path can be deformed into another path (Simply connected).
	- However, on the donut, if it circles around the hole, it cannot be deformed into the straight path.

# Lecture 6. Topological Manifolds
### Definition of the Topological Manifold
- We consider the topological space $(X, T_X)$ (Set with its topology)
- with the topological properties:
	- Hausdorff (two points separable with two disjoint open set)
	- Second-countable (has a countable basis)
	- Paracompact (a form of compactness; we're skipping the details)
-  which makes the space metrizable.
	-  Metrizable = We can invent a metric $d$ that measure the space
	-  $d: X \times X \to \mathbb{R}^{+}$ (Sometimes it's $\mathbb{R}$ such as the Riemannian metric)
	-  Hausdorff (to istinguish points in a very aggressive way), Second-countable & Compact (to control the space to make it useful)
-  We denote the space **Topological Manifold**.

### Motivation for the Locally Euclidean
- $\mathbb{R}^N$ is simply a tuple of  N real numbers. So, let’s endow it with the usual topology (i.e., open ball topology), i.e., consider the topological space $(\mathbb{R}^N, T_{\mathbb{R}^N})$, which is quite rich!
- We need to build a homeomorphism from the topological manifold to $\mathbb{R}^N$, i.e., $f: X \to \mathbb{R}^N$, to enjoy its richness.
- Let’s enjoy the simplicity of $\mathbb{R}^N$, yet avoid requiring the extreme requirement of homeomorphism across the whole space by incorporating the idea **Locally Euclidean**!

### Exploiting the locality
- Let’s consider a space $(X, T_X)$ and its open set $U_p$, which is the neighborhood of the point $p$.
- Note that $(U_p, T_X \vert_{U_p})$ is also a topological space: all the elements’ unions and intersections are inside $U_p$, and the total union is equal to $U_p$. We can call that it *inherited* the topology from the original space.
- Now, consider the open set of $\mathbb{R}^N$, $S, T_{\mathbb{R}^N} \vert_S$. Now, let’s consider the homeomorphism $f: U_p \to S$, which is much easier to construct!
- Let’s extend this further. Consider any point $p \in X$ and its corresponding point $f(p) \in \mathbb{R}^N$. It’ll be awesome if we get to design $f$ for every open neighborhood of $p$ and $f(p)$, i.e., for every subcover of the open cover of $X$.
- If we manage to do so, we get to obtain the **coordinates**, i.e., $X$ is **locally Euclidean**.
	- Be careful that each subcover maps to a different *copy* of $\mathbb{R}^N$, so comparing the coordinates across different subcovers won’t make any sense.

### Motivating example: Earth map
- Consider the surface of the sphere $(X, T_{\mathbb{R}^3}\vert_X)$ which inherits from the 3-dimensional space.
	- We can easily construct $X$ by starting from the open ball $S$. The closure $\bar{S}$ will include the surface, hence let’s subtract the interior: $X=\bar{S} - S^0$.
- Sphere is compact *but* the plane is not.
	- Hence, we can determine that there will be no homeomorphism from $X \to \mathbb{R}^2$ (because it’ll preserve the topological properties).
	- However, if we remove a single point from $X$, it becomes non-compact! (Consider the continuously halving subcovers example towards the *south pole*)
- Consider any open neighborhood of the point $p$ on the sphere and its corresponding circle (open neighborhood of $f(p)$) on the plane $\mathbb{R}^2$.
