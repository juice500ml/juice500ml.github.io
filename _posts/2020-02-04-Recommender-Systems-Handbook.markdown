---
layout: post
title:  "Recommender Systems Handbook"
date:   2020-02-04 02:50:19
author: Kwanghee Choi
categories: datascience
---

# Disclaimer
This is a partial summary of [Recommender Systems Handbook, 1st ed](https://books.google.co.kr/books/about/Recommender_Systems_Handbook.html?id=2hFG21Cp2qcC).

## Chapter 1. Introduction to Recommender Systems Handbook

### 1.1 Introduction

- Definition of Recommender Systems
- Recommender Systems (RSs) are software tools and techniques providing suggestions for items to be of use to a user.
- In their simplest form, personalized recommendations are offered as ranked lists of items.
- Information Overload Problem
- The availability of choices, instead of producing a benefit, started to decrease users’ well-being.
- Notable Conferences
    - ACM SIGIR (Special Interest Group on Information Retrieval)
    - ACM UMAP (User Modeling, Adaptation and Personalization)
    - ACM SIGMOD (Special Interest Group on Management Of Data)
- Sections of this book
    - Techniques most popularly used today
    - Evaluation of the quality of recommendations
    - How recommendations interact with users
    - Recommendations by User Generated Content (UGC)
    - Various advanced topics


### 1.3 Data and Knowledge Sources

- Knowledge poor (user ratings/evaluations of items) vs. Knowledge dependent (ontological descriptions of users/items)
- When a user is acquiring an item, it will always incur a cost
    - Cognitive cost of searching for the item
    - Monetary cost of paying for the item


### 1.4 Recommendation Techniques

- Recommendation computation = Prediction of the utility of an item for a user
- Degree of utility R(u, i) of the user u for item i
- R(u, i) may depend on other variables, which we generically call “contextual”
- Various techniques
    - Content-based: recommend items that are similar to the ones that the user liked in the past (user-to-item)
    - Collaborative filtering: recommends to the active user the items that other users with similar tastes liked in the past (user-to-user)
    - Demographic profile of the user
    - Knowledge-based: domain knowledge about how certain item features meet users needs and preferences
    - Community-based: based on the preferences of the users' friends
    - Hybrid recommender systems


### 1.6 Recommender Systems and Human Computer Interaction

- Effectiveness should not be evaluated only in terms of the accuracy of the prediction
- Trust about other users vs. Trust about the system
- Conversational Systems
- Interactive process where both user and system may query or provide info


# Part I: Basic Techniques

## Chapter 2. Data Mining Methods for Recommender Systems

### 2.2 Data Preprocessing

- Similarity Measures
    - Minkowski distance with degree of distance r
        - r=1: Manhattan distance
        - r=2: Euclidean distance
        - r=INF: Supremum distance
    - Mahalanobis distance
        - Distance measure between point-to-distribution or point-to-point using covariance matrix
    - Cosine distance (L2 norm)
        - Angle between two points
    - Pearson Correlation
        - Correlation which measures the linear relationship between objects
    - Distance for binary attributes
        - Simple Matching Coefficient
        - Jaccard Coefficient
        - Extended Jaccard (Tanimoto) Coefficient: Jaccard Coefficient with weights
- Sampling
    - Random sampling
    - Stratified sampling: Split into several partitions based on a particular feature, followed by random sampling on each partition independently.
    - Sampling with/without replacement: When an item is selected, it stays/is removed from the population.
    - It is common practice to use standard random sampling without replacement with an 80/20 proportion when separating training/testing data sets.
    - n-fold cross-validation: One is used for testing and the remaining n−1 folds are used for training. Average of N learned models is reported.
    - Leave-one-out (LOO): Extreme case of n-Fold, n = # of items.
- Reducing Dimensionality
    - Curse of Dimensionality
    - The notions of density and distance between points become less meaningful in highly dimensional spaces.
    - Principal Component Analysis (PCA)
        - PCA allows to obtain an ordered list of components that account for the largest amount of the variance from the data.
        - Length of the new coordinates is relative to the energy contained in their eigenvectors.
        - The rule of thumb is to choose dimensionality so that the cumulative energy is above a certain threshold, typically 90%.
        - PCA limitations
            - PCA relies on the empirical data set to be a linear combination of a certain basis.
            - Original data set has been drawn from a Gaussian distribution
    - Singular Value Decomposition (SVD)
        - SVD finds a lower dimensional feature space where the new features represent “concepts".
        - Strength of each "concept" in the context of the collection is computable.
        - n×m matrix data A (n items, m features)
        - = n×r matrix U (n items, r concepts) * r×r diagonal matrix λ (strength of each concept) * m×r matrix V (m features, r concepts)
        - Ak = Closest rank-k matrix to A
            - A can be approximated by simply truncating the eigenvalues at a given k.
            - Ak minimizes the sum of the squares of the differences of the elements of A and Ak.
        - SVD can be used to uncover latent relations between customers and products.
        - Low-dimensional space resulting from the SVD to improve neighborhood formation for later use in a kNN approach.
        - Online SVD Model: There are incremental algorithms to compute an approximated decomposition for SVD.
        - Matrix Factorization (MF) Methods
            - Non-negative Matrix Factorization (NNMF)
            - Regularized Kernel Matrix Factorization
    - Denoising
        - Remove noises (missing values or outliers) with domain knowledge.
        - Have to distinguish between natural and malicious noise.
        - accuracy improvements by investing in denoising could be larger than the ones obtained by complex algorithm optimizations.


### 2.3 Classification

- Nearest Neighbors
    - kNN classifier finds the k closest points (nearest neighbors) from the training records.
    - De facto standard for CF recommendation
- Decision Trees
    - Classifiers on a target attribute (or class) in the form of a tree structure, splits made by maximizing the information gain.
    - Decision tree induction algorithms: Hunts Algorithm, CART, ID3, C4.5, SLIQ, SPRINT
    - Inexpensive to construct
    - Extremely fast at classifying unknown instances
    - Easy to interpret
- Rule-based Classifiers
    - Rule-based classifiers classify data by using a collection of “if ... then ...” rules.
    - Extract rules directly from data with RIPPER or CN2
    - Extremely expressive since they are symbolic and operate with the attributes of the data without any transformation
    - Similar advantages compared to decision trees
    - It is very difficult to build a complete recommender model based on rules.
    - Rule-based system can be used to improve the performance of a RS by injecting partial domain knowledge or business rules.
- Bayesian Classifiers
    - Naive Bayes Classifier
        - Assumes the probabilistic independence of the attributes
        - Robust to isolated noise points and irrelevant attributes
        - Handle missing values by ignoring the instance during probability estimate calculations
    - Bayesian Belief Networks
        - Acyclic graph encode the dependence between attributes and a probability table that associates each node to its immediate parents.
        - Similar advantages compared to Naive Bayes Classifier
- Artificial Neural Networks
    - Can perform non-linear classification tasks
    - Black-box approach: provide no semantics for inferring knowledge
    - Some conclude that there does not seem to be a need for nonlinear classifiers such as the ANN.
- Support Vector Machines
    - Finds a linear hyperplane (decision boundary) that separates the data in such a way that the margin is maximized
    - If the items are not linearly separable we can decide to turn the SVM into a soft margin classifier by introducing a slack variable.
    - Kernel trick transforms data into a higher dimensional space.

- Ensembles of Classifiers

    - Will produce results that are in the worst case as bad as the worst classifier in the ensemble 
    - Bagging
        - Sampling with replacement, building the classifier on each bootstrap sample.
        - Aggregate results(voting or averaging) from each classifier
        - RandomForest
    - Boosting
        - Iterative procedure to adaptively change distribution of training data by focusing more on previously misclassified records
        - AdaBoost, XGBoost, GradientBoost
    - Stacking
        - Meta-learning which chooses results between models 
        - StackNet
- Evaluating Classifiers
    - Only introduce complexity if the performance gain obtained justifies it.
    - Mean Average Error
    - Root Mean Squared Error
    - Accuracy, Precision, Recall
    - ROC Curve


### 2.4 Cluster Analysis

- Clustering is sure to improve efficiency because the number of operations is reduced, but it is unlikely that it can help improve accuracy.
- k-Means
    - Partitions the data set of N items into k disjoint subsets with k centroids.
    - Assumes prior knowledge of the data in order to choose the appropriate k
- Density-based clustering
    - Density: Number of points within a specified radius
    - DBSCAN
- Message-passing clustering
    - Initially consider all points as centers (exemplars), propagate affinity until convergence
- Hierarchical clustering
    - Produces a set of nested clusters organized as a hierarchical tree (Dendogram)


### 2.5 Association Rule Mining

- Focuses on finding rules that will predict the occurrence of an item based on the occurrences of other items.
- Co-occurrence but not causality
- Apriori algorithm


## Chapter 3. Content-based Recommender Systems: State of the Art and Trends

### 3.2 Basics of Content-based Recommender Systems

- Content-based recommendation systems try to recommend items similar to those a given user has liked in the past.
- High Level Architecture of Content-based Systems
    - Content Analyzer: Make unstructured information structured with some kind of pre-processing step.
    - Profile Learner: Collects data representative of the user preferences and tries to generalize this data, in order to construct the user profile.
    - Filtering Component: Match the profile representation against that of items to be recommended.
- Advantages
    - User independence: Only needs ratings provided by the user to recommend to that user
    - Transparency: Explainable by explicitly listing content features or descriptions that caused an item to be recommended
    - Capable of recommending items not yet rated
- Disadvantages
    - Limited content analysis: Domain knowledge and ontologies are needed
    - Over-specialization: No way for finding something unexpected
    - Not capable of recommending to new users


### 3.3 State of the Art of Content-based Recommender Systems

- Item Representation
    - Adopt knowledge bases to obtain a “semantic” interpretation
    - Keyword-based Vector Space Model with TF-IDF weighting
        - IDF assumption: rare terms are not less relevant than frequent terms
        - TF assumption: multiple occurrences of a term in a document are not less relevant than single occurrences
        - Normalization assumption: long documents are not preferred to short documents
    - Keyword-based Systems
        - Represents profiles in the form of a weighted semantic network
        - Temporal decay of user feedback
        - Spreading activation technique
        - Relevance feedback mechanism
    - Semantic Analysis by using Ontologies
- User Profiles
    - The problem of learning user profiles can be cast as a binary categorization task: each item has to be classified as interesting or not.
    - Naive Bayes with multivariate Poisson model
    - Relevance feedback: Incrementally refine queries based on previous search results, ex) Rocchio’s formula


### 3.4 Trends and Future Research

- Social Tagging Recommender Systems
- Serendipity: introduction of some randomness
    - Filter out items if they are too similar to something the user has seen before
    - A serendipitous recommendation helps the user to find a surprisingly interesting item
    - it is reasonable to assume that if classification scores are close to zero, items are not known by the user, since the system was not able to clearly classify them as relevant or not. It might result to be the most serendipitous.


## Chapter 4. A Comprehensive Survey of Neighborhood-based Recommendation Methods

### 4.1 Introduction

- Type of responses: Scalar, Binary, Unary
- Type of problems: Best item, Top-N recommended items
- Type of metrics
    - Mean Absolute Error (MAE), Root Mean Squared Error (RMSE)
    - Precision, Recall
    - Average Reciprocal Hit-Rank (ARHR): Metrics used for ordered lists
- Type of approaches
    - Content-based approaches
        - Identify the common characteristics of items from one user, and then recommend to that user new items that share these characteristics.
        - User as a linear combination of item vectors
        - Cosine similarity, Minimum Description Length
        - Problems of limited content analysis, over-specialization
    - Collaborative filtering approaches
        - The rating of u for a new item i is likely to be similar to rating of i from user v, if u and v have rated other items in a similar way.
            - Neighbor-based: item-based or user-based
                - Excellent on terms of serendipity
                - Excellent at capturing local associations in the data
                - Only one parameter required for tuning, no training phase, so very simple, efficient, and stable
                - Justification can be presented to the user
            - Model-based: predict ratings of user for item
                - Excellent on terms of accuracy
                - Excellent at characterizing the preferences of a user with latent factors


### 4.2 Neighborhood-based Recommendation

- Automate the common principle of "word-of-mouth" (where one relies on the opinion of like-minded people)
- User-based Rating Prediction/Classification
    - Average/Voting of normalized ratings, weighted with user similarity
    - Classification is more riskier than prediction
    - Taking risk may be be desirable if it leads to serendipitous recommendations
- Item-based Recommendation
    - Average of normalized ratings, weighted with item similarity
- User-based vs. Item-based
    - Accuracy and efficiency depends mostly on the ratio between the number of users and items
        - A small number of high-confidence neighbors is by far preferable to a large number of untrustworthy neighbors
    - Stability depends on which side is more static
    - User-based are more likely to make serendipitous recommendations


### 4.3 Components of Neighborhood Methods

- Rating Normalization
    - Mean-centering: Removes the offsets caused by the different perceptions of an average rating
    - Z-score: Also considers the spread in the individual rating scales, more often blow up.
    - Preference-based filtering: Focuses on predicting the relative preferences of users (By ordering of items)
- Similarity Weight Computation
    - Selection of trusted neighbors, importance factor for those neighbors
    - Correlation-based similarity
        - Cosine Vector: Does not consider the differences in the mean and variance of the ratings made by each user
        - Pearson Correlation:  Normalization only on common items
        - Cosine Vector on Z-score normalization: Normalization on entire set of items
        - Adjusted Cosine Similarity: Normalization only on common items by user-mean-centered ratings
    - Mean Squared Difference: Does not capture negative correlations between user preferences or the appreciation of different items
    - Spearman Rank Correlation: Considers the ranking of these ratings, avoids the problem of rating normalization.
    - Significance Weighting: Similarity weight penalized by a factor proportional to the number of commonly rated items
        - To reduce the magnitude of a similarity weight when this weight is computed using only a few ratings
        - Concept of shrinkage: Weak or biased estimator can be improved if it is “shrunk” toward a null-value
    - Frequency-Weighted Pearson Correlation: Weighted with Inverse User Frequency (Scarce the rating, more important the score is)
- Neighborhood Selection
    - To achieve computational efficiency
    - Top-N Filtering: N nearest-neighbor
        - As N increases, more neighbors contribute, so the variance of individual neighbors is averaged out. → Higher accuracy
        - But if N is too big, few strong local relations are diluted by many weak relations. → Lower accuracy
    - Threshold filtering: Similarity weight thresholding
    - Negative filtering: Negative rating correlations are less reliable than positive ones


### 4.4 Advanced Techniques

- Important flaws of neighborhood approaches
    - Limited coverage: Bad on sparse data. Users can be neighbors only if they have rated common items.
    - Cold-start problem: Users or items newly added to the system may have no ratings at all.
- Dimensionality Reduction Method
    - Solves limited coverage and sparsity by projecting users and items into a reduced latent space that captures their most salient features
    - Decomposition of a user-item rating matrix
        - Latent Semantic Indexing (Equivalent to Singular Value Decomposition)
        - May use SVD with only the known ratings with regularization 
    - Decomposition of a sparse similarity matrix
        - Users are projected in the new plane
        - The users of the system are clustered in the plane using a recursive subdivision technique
- Graph-based methods
    - Bipartite graph between items and users
    - Use propagation or transitive association to influence other nodes
    - Path-based similarity
        - Shortest path
            - Horting: Asymmetric relation between two users that is satisfied if these users have rated similar items
            - Predictability: Stronger property than horting, additionally requiring the normalized ratings to be similar
            - Prediction of rating is computed as the average of predictions for the all shortest paths
        - Katz measure
            - Number of paths whose length is no more than given maximum length, attenuated by length of path
            - Closely related to Von Neumann Diffusion Kernel, Exponential Diffusion Kernel
        - Random walk similarity
            - Describe as first-order Markov process to obtain stable distribution vector
        - ItemRank
            - Random walk with probability of "teleport" to any node
        - Average first-passage time
            - Average number of steps needed by a random walker to reach a node for the first time
        - Average commute time
            - Symmetric version of average first-passage time
            - Sum of average first-passage time i → j and j → i


## Chapter 5. Advances in Collaborative Filtering

### 5.1 Introduction

- CF produce user specific recommendations without need of exogenous information about either items or users.
- Two main techniques of CF
    - Neighborhood Approach: Relationshops between items or users
    - Latent Factor Models: Transform both items and users into same latent factor space. ex) SVD
- Accuracy significantly improves by utilizing other sources
    - Temporal effects: Reflects dynamic, time-drifting nature of user-item interactions
    - Hidden feedback: ex) which items are chosen to be rated


### 5.2 Preliminaries

- Baseline predictors
    - Much of the observations (user ratings) are due to effects associated with either users or items, independently of their interaction
        - b(u): Bias of users ex) Some users may give higher ratings
        - b(i): Bias of items ex) Some items may receive higher ratings
        - E: Overall average rating
    - Bias b(u, i) = E + b(u) + b(i)
        - Biases can be calculated by transforming into least squares problem with SGD, or heuristic way with regularization parameters.
- Quality of the results is usually measured by the root mean squared error of ratings.
    - On Netflix competition, RMSE values of the top competitors lie in a quite compressed range.
    - But small difference on RMSE can significantly impact on the quality nonetheless.


### 5.3 Matrix factorization models

- Latent factor models approach CF with the holistic goal to uncover latent features that explain observed ratings.
- However, applying SVD to explicit ratings raises difficulties due to sparseness.
    - Highly prone to overfitting.
    - Some earlier works handles missing values with imputation, which considerably distorts data and can be computationally expensive.
- Therefore, regularization via modeling is needed for explicit ratings
- SVD
    - Both users and items associates with joint latent factor space of dimensionality f
        - q(i): Item vectors measure the extent to which the item possesses item features.
        - p(u): User vector measure the extent of interest the user has in items that are high on the corresponding factors
        - q(i) * p(u): Dot product between Item and User vectors captures the interaction between Item and User.
        - R(u, i) = E + b(u) + b(i) + q(i) * p(u)
            - b(u), b(i), q(i), p(u) can be calculated by transforming the problem into least squares problem with SGD
- SVD++
    - R(u): Set of items rated by user u
    - y(i): Item factors
    - Replace p(u) with p(u) + sum( y(i) where i is in R(u) ) / sqrt(R(u))
        - Normalization with 1/sqrt(R(u)
        - sum( y(i) where i is in R(u) ) used to characterize users based on the items that they rated
        - y(i) can also be calculated with SGD
- Time-aware factor model
    - Decomposing ratings into distinct terms
        - User-item bias at time t: `b(u, i, t) = E + b(u, t) + b(i, t)`
        - Item bias b(i, t)
            - `b(i, t) = b(i) + b(i, Bin(t))`
            - Binning time slices with Bin(t)
        - User bias b(u, t)
            - Parameterization by linear function
                - User bias at time ti: `b(u, t) = b(u) + a(u) * sign(t - t(u)) * |t - t(u)| ^ b`
                - t(u): Mean date of rating 
                - b: Normalization constant
                - `|t - t(u)|`: Number of dates
                - a(u): New parameter, learnable by SGD
            - More flexible parameterization is offered by splines
                - `b(u, t) = b(u) + sum(b(u, i) * e^(-sigma * |t - t(u, i)|) / sum(e^(-sigma * |t - t(u, i)|))`
                - sigma: normalization constant
                - Normalization by `1 / sum(e^(-sigma * |t - t(u, i)|))`
                - User bias is formed as a time-weighted Gaussian combination of multiple parameters
            - Gradual concept drift vs. Sudden drifts
                - Sudden drifts may reflect the mood of the user, impact of ratings given in a single day, or multi-person accounts
                - Single day effect modelling by b(u, t(u, i))
        - Preference bias p(u, t)
            - Each element in p(u) of dimension f can be parameterized
                - p1(u), p2(u), ... , pf(u)
                - Each pk(u) modeled by linear function
- Pros of gradient based SVD
    - Integrate multiple forms of user feedback
    - Captures evolving taste of user


### 5.4 Neighborhood models

- Latent factor models vs. Neighborhood models
    - Latent factor models offer high expressive ability, hence more accurate results
    - Neighborhood models are relatively simple and provide intuitive explanations
        - Allows identifying which of the past user actions are most influential on the computed prediction
    - Neighborhood models can make immediate recommendation
        - No need to train and estimate new parameters for the new user
- Components of neighborhood-based interpolation
    - Data normalization with baseline predictors
    - Neighbor selection with shrinking unreliable similarities
    - Choice of interpolation weights
- Similarity measures
    - Frequently, it is based on Pearson correlation constant p(i, j), which measures the tendency of users to rate i and j similarly.
        - Replace average with baseline predictors b(u, i) and b(u, j)
    - Shrunk correlation coefficient s(i, j) = p(i, j) * (n(i, j) - 1) / (n(i, j) - 1 + N)
        - n(i, j): Number of users that rated both i, j
        - N: Normalization constant
        - Shrinkage can be motivated from a Bayesian perspective
- Similarity-based interpolation
    - `S(k, i | u)`: Set of k neighbor items of i given user u
    - `r(u, i) = b(u, i) + E( r(u, j) - b(u, j) | j in S(k, i | u), probability s(i, j) )`
        - Dual use of the similarity s(i, j) for both identification of S(k, i | u) and interpolation weights.
    - Problems
        - s(i, j) is arbitrary.
        - It does not account for interactions among item neighbors.
            - ex) Lord of the Rings 1, 2, 3
        - Interpolation weights are normalized. Not useful neighbors are not ignored.
        - Variability of ratings may differ substantially, hence may not work too well.
- Jointly derived interpolation weights
    - Change s(i, j) into t(i, j), which is a learnable parameter by SGD.
    - t(i, j) is derived directly from the rating, without using any similarity measure.
    - t(i, j) explicitly accounts for relationship among neighbors.
    - Estimated weights may vary depending on the usefulness of the neighbors.
    - Automatically adjusts for variations.


### 5.5 Enriching neighborhood models

- Global neighborhood model
    - `r(u, i) = E + b(u) + b(i) + |R(u)| ^ b * Sum( (r(u, j) - b(u, j)) * t(i, j) + c(i, j) for j in R(u))`
    - Nearly the same with jointly derived interpolation weights, but with learnable bias c(i, j) and not using `S(k, i | u)`
    - `|R(u)| ^ b`: Normalization, with parameter b
- Factorized neighborhood model
    - Change t(i, j) into q(i) * x(j), c(i, j) into q(i) * y(j)
        - x(i), y(j) is two kind of item vectors
    - Add `|R(i)| ^ b * Sum( (r(v, i) - b(v, i)  * p(u) * z(v) for v in R(i) )`
        - p(u), z(v) is two kind of user vectors
- Temporal dynamics at neighborhood models
    - Change b(i, t), b(u, t) to time-aware factor model


### 5.6 Between neighborhood and factorization

- Best results for neighborhood models are achieved when neighborhood size is maximal.
    - Past user ratings are all considered.
- SVD, item-item, user-user are all analogous.


## Chapter 6. Developing Constraint-based Recommenders

### 6.1 Introduction

- Pros and Cons for Knowledge-based recommender technologies
    - Pros: Handles sparsity well
        - Works well on the case for items which are not bought very frequently (rather infeasible to collect numerous ratings for one specific item)
    - Cons: Knowledge acquisition bottleneck

        - Have to convert the knowledge possessed by domain experts into formal, executable representations
- Two types of Knowledge-based recommender technologies
    - Case-based: Recommendations on the basis of similarity metrics
    - Constraint-based: Exploit predefined recommender knowledge bases that contain explicit rules about how to relate customer requirements with item features
- Recommender knowledge base
    - Variables
        - Customer Properties
        - Product Properties
    - Constraints
        - Constraints: Systematically restricting the possible instantiations of customer properties
        - Filter Conditions: Relationship between potential customer requirements and the given product assortment
        - Products: Instantiations of product properties
- Recommendation task can be defined as a constraint satisfaction problem.
- Consistent recommendation: An assignment of the variable iff it does not violate any of the constraints.
- Examples of user interfaces
    - Dialogs can be modeled explicitly in the form of finite state models.
    - Users themselves are enabled to select interesting properties they would like to specify.


### 6.2 Development of Recommender Knowledge Bases

- We have to actively support knowledge engineers and domain experts in the development recommender applications. (Limit knowledge acquisition bottlenecks as much as possible)
- Rapid prototyping processes support the principle of concreteness where the user can immediately inspect the effects of introduced changes.
- Changes to all the information units should be performed on a graphical level.
- Integrated testing and debugging environment supports the principle of immediate feedback.


### 6.3 User Guidance in Recommendation Processes

- Critiquing: Recommend-review-revise cycle is repeated until the desired item is found.
    - Present individual items to the user who can then interactively give feedback in terms of critiques on individual features.
- Tweaking: User interactively exploring the item space.
- Personalized preference elicitation dialogs: Explicitly modeled and adaptive preference elicitation dialogs.
- Dealing with unfulfillable or too loose user requirements
    - “No matching product found” is highly undesirable.
    - Query relaxation: Finding a maximal subquery of the original query that returns at least one item.
- Suggesting alternatives for unfulfillable requirements
    - ex) Instead of only proposing the user to relax the constraints, recommend repairs (alternative constraints) on queries and size of result set for each repairs.
- Query tightening
    - Beside having no item in the result set, having too many items in the result set is also not desirable in an interactive recommender.


### 6.4 Calculating Recommendations

- Constraint satisfaction algorithms
    - Backtracking: If all the possible values of the current variable are inconsistent with the existing assignments and the constraints, the constraint solver backtracks.
    - Constraint Propagation: Try to modify an existing constraint satisfaction problem such that the search space can be reduced significantly.
        - State of local consistency: Guarantees consistent instantiations among groups of variables.
        - Turn an existing constraint satisfaction problem into an equivalent one.
        - Arc consistency
- Conjunctive queries with probabilistic databases
    - Fulfill the criteria in the WHERE clause and orders the result conform to a similarity metric.
- Ranking Items
    - Utility-based item ranking scheme
        - Soft constraints where the importance (preference) for each combination of variable values is determined on the basis of a corresponding utility function (weight).
    - Multi-attribute utility theory (MAUT)
        - (Wikipedia) Used to represent the preferences of an agent over bundles of goods either under conditions of certainty about the results of any potential choice, or under conditions of uncertainty.


### 6.5 Experiences from Projects and Case Studies

- Algorithm evaluations
    - Knowledge-based systems are hard to compare, because they require different types of algorithm input.
    - Evaluation always measures both the quality of the encoded knowledge base and the inferencing itself.
    - Knowledge-based recommenders did not perform worse in terms of serendipity measured by the catalog coverage metric than collaborative filtering.


## Chapter 7. Context-Aware Recommender Systems

### 7.2 Context in Recommender Systems

- We should consider contextual information, such as time, place, company of other people, etc.
    - Three dimensions of the contextual information
        - Temporal, Spatial, Technological (how to deliver)
- The ability to reach out and touch customers anywhere at anytime means that companies must deliver not just competitive products but also unique, real-time customer experiences shaped by customer context.
- Context: Events which characterize the life stages of a customer and that can determine a change in his/her preferences, status, and value for a company.
- "Intent of a purchase made by a customer"
- Context-aware recommender systems (CARS)
    - Rating function R : User × Item × Context → Rating
    - Context: A set of contextual dimensions K
    - Contextual Dimension: A set of attributes having a hierarchical structure and capturing a particular type of context.
- Obtaining contextual information
    - Explicitly by directly approaching relevant people
    - Implicitly from the data or the environment. ex) a change in location of the user detected by a mobile telephone company.
    - Inferring the context using statistical or data mining methods.
    - May initially identified by the domain experts.
    - Should apply various types of statistical tests identifying which of the chosen contextual attributes are truly significant.


### 7.3 Paradigms for Incorporating Context in Recommender Systems

- Paradigms
    - Recommendation via context-driven querying and search (Rule-based)
        - Recommender systems use the current context information and specified current user’s interest as queries to search for the most appropriate content 
    - Recommendation via contextual preference elicitation and estimation (Model-based)
        - Attempt to model and learn user preferences by observing the interactions or by obtaining preference feedback from the user.
- Components
    - Contextual pre-filtering
        - Contextual information drives data selection or data construction for that specific context
        - Allows deployment of any of the numerous traditional recommendation techniques previously proposed
        - May filter the training data itself for separate training for each case of contextual information.
            - Sparsity problem: Exact context may not have enough data for accurate rating prediction
            - But it has more relevant data
        - May generalize the data filtering query obtained based on a specified context
            - Use superset (Contextual segment) of each context
                - May define superset manually, with expert-driven approach
            - Have to aggregate each different context using some aggregation function
            - Evaluate the performance for each possible generalized pre-filter-generated recommender, and then would automatically choose the pre-filter with best performance
    - Contextual post-filtering
        - Resulting set of recommendations is adjusted (contextualized) for each user
            - Filtering out recommendations that are irrelevant in a given context
                - Heuristic: Thresholding number of common item characteristics for a given user in a given context
                - Model-based: Probability of relevance
            - Adjusting the ranking of recommendations on the list based on a given context
                - Heuristic: Sort with number of common item characteristics 
                - Model-based: Weighting the predicted rating
    - Contextual modeling
        - Contextual information is used directly in the modeling technique as part of rating estimation
        - Truly multidimensional recommendation functions, which essentially represent predictive models


### 7.4 Combining Multiple Approaches

- May combine several models of the same type, learned from several different contextual pre-filters
    - Find the ones which result in contextual segments having a significantly large amount of data
    - Find the ones with high predictive performance
    - Remove less general and less accurate pre-filters
    - If no such pre-filter exists, then the standard non-filtered algorithm is used for rating prediction


### 7.5 Additional Issues in Context-Aware Recommender Systems

- Properties of Context-Aware Recommender Systems
    - Complexity due to various types of contextual information
    - Interactivity: Contextual information usually needs to be elicited from the user


## Chapter 8. Evaluating Recommender Systems

### 8.1 Introduction

- How to compare recommenders based on a set of properties that are relevant for the application (property-directed evaluation)
- Three types of evaluation
    - Offline setting: Recommendation approaches are compared without user interaction
    - User studies: Small group of subjects experiment with the system and report on the experience
    - Online experiments: Large scale, real user populations interact with the system


### 8.2 Experimental Settings

- Guidelines for basic experiments
    - Hypothesis: Have to be concise and restrictive. ex) algorithm A better predicts user ratings than algorithm B
    - Controlling variables: All variables that are not tested must stay fixed
    - Generalization power: We want our conclusions to hold beyond the scope of the specific application or data set that we experimented with.
- Offline experiments
    - Using the pre-collected dataset, we can try to simulate the behavior of users
        - May be tempted to pre-filter the data by excluding items or users with low counts, in order to reduce the costs of experimentation, but introduces a systematic bias in the data (trade-off)
        - Should simulate the target application as closely as possible
        - User random sampling, hide all items after the sampled test time for each test user
        - Using fixed number of known items or a fixed number of hidden items per test user also introduces biases
    - To make reliable decisions before conducting user studies or online experiments (Compares a wide range of candidate algorithms at a low cost)
    - Typically questions about the prediction power of an algorithm
- User studies
    - Recruiting a set of test subjects, and asking them to perform several tasks requiring an interaction with the recommendation system to observe and record their behavior
    - Can test the behavior of users and influence of recommendation on user behavior
        - Checking out the assumptions we made on offline experiments
        - Can collect qualitative data that is often crucial for interpreting the quantitative results
    - But very expensive to conduct, have to do in small-scale
        - High possibility of population bias
        - Fundamental bias of awareness that they are participating in an experiment
    - Candidate approaches
        - Between subjects: Each subject is assigned to a candidate method and experiments
            - "All Between" (AB) Testing\
            - Can test how the user becomes accustomed to the system, and estimate a learning curve
        - Within subjects: Where each subject tests a set of candidates on different tasks
            - More bias, more information than between subjects
    - Variable Counter Balance
        - Choices may displayed either sequentially, or together, and both are biased
        - Latin square procedure: Randomizes the order or location of the various results each time, thus canceling out biases due to these untested variables
- Online evaluation
    - Effect of the recommendation system depends on a variety of factors
        - User's intent: How specific their information needs are, how much novelty vs. how much risk they are seeking
        - User's context: What items they are already familiar with, how much they trust the system
        - Online evaluation is the most trustworthy way
    - Important to sample users randomly, so that the comparisons between alternatives are fair
    - Important to single out the different aspects of the recommender
        - ex) if we care about algorithmic accuracy, keep the user interface fixed
        - ex) if we care about a better user interface, keep the algorithm fixed
    - Best to run an online evaluation last to reduce the risk
        - After an extensive offline study provides evidence
        - After a user study that measures the user’s attitude towards the system
- Drawing Reliable Conclusions
    - Confidence intervals and p-values
        - Rejecting results due to luck
        - Compute the distribution of the quantity of interest with a non-parametric method such as a histogram and finding upper and lower bounds such that include the quantity of interest with the desired probability
    - Paired Results
        - Sign test
            - Most simple
            - Lack of assumptions over the distribution of cases
            - nA out of nA + nB fair coin-flips coming up “heads”
            - When nA + nB is big, use normal distribution (Central limit theorem)
            - Test only examines the probability of one system outperforming the other, without regard to the magnitude of the difference
            - McNemar's test: Use chi-squared approximation
        - Paired Student’s t-test
            - Average difference between the performance scores of algorithms A and B, normalized by the standard deviation of the score difference
            - Wilcoxon signed rank test: Same with paired student's t-test, but do not make distributional assumptions on the differences
    - Unpaired results
        - Mann-Whitney test
            - Extension of Wilcoxon test
            - Probability of the null hypothesis that nA randomly chosen results from the total nA + nB have at least as good an average rank as the nA results that came from algorithm A
            - Can also use Gaussian approximation
    - Multiple tests
        - ex) At least one of the ten trials passes the sign test mistakenly of confidence 95% is 100% − (95%)^10 = 40%
        - "Tuning to the test set"
        - ANOVA or the Friedman test for ranking
            - Statistical Comparisons of Classifiers over Multiple Data Sets (Janez Demsar)


### 8.3 Recommendation System Properties

- Designer of the system must decide on the important properties to measure for the concrete application at hand
- Some of the properties can be traded-off
- User Preference
    - Assumption that all users are equal is wrong
    - Weight the vote by the importance of the user
    - User preference of different systems itself
    - It is important to know why people favor one system over the other
- Prediction Accuracy
    - Measuring accuracy
        - Root Mean Squared Error (RMSE) or Mean Absolute Error (MAE) of ratings
        - Normalized RMSE (NMRSE) and Normalized MAE (NMAE) are normalized with range of ratings (max-min)
        - Average RMSE and Average MAE adjust for unbalanced test sets
            - MAE or RMSE separately for each item and then take the average over all item
        - Magnitude of errors matter: suitable distortion measure needed (ex. stars: 4 vs 5, 1 vs 2)
    - Measuring prediction
        - Precision, True Positive Rate (Recall), False Positive Rate (1-Specificity) at N recommendations
        - Precision-recall curves (comparing precision to recall) or ROC curves (true positive rate to false positive rate)
        - F-measure or Area Under the ROC Curve (AUC) measures ROC curves
        - May compute precision-recall curve (or ROC curve) for each user and then average the resulting curves over users
    - Ranking Measures
        - Ranking with reference (true value) 
            - Cu: number of pairs of items for which the reference ranking asserts an ordering (i.e. not tied)
            - C+/C−: number of pairs that the system ranking asserts the correct order/incorrect order
            - Cu0: number of pairs where the reference ranking does not tie but the system ranking ties, Cu0 = Cu - (C+ + C-)
            - Normalized Distance-based Performance Measure (NDPM) = (C- + 0.5Cu0) / Cu
                - Perfect score of 0, worst score of 1
                - Not predicting a reference preference relation is penalized only half as much as contradicting it
                - Predicting preferences that the reference does not order (i.e. when we do not know the user’s true preference) is not penalized
            - Spearman’s ρ
            - Kendall’s τ
        - Ranking without reference (Utility-based ranking)
            - R-Score metric
                - Assumes that the value of recommendations decline exponentially down the ranked list
            - Normalized Cumulative Discounted Gain (NDCG)
                - Assuming each user u has a “gain” from being recommended an item i
                - Normalized by ideal DCG
            - Average Reciprocal Hit Rank (ARHR)
                - Assigns a utility 1/k to a successful recommendation at position k.
                - ARHR decays more slowly than R score but faster than NDCG
    - Online evaluation of ranking
        - Note that there is a possibility of multiple correct rankings
        - In offline evaluations, we have a single reference ranking which is assumed to be correct
        - Division of the interesting items, the uninteresting items, and the unknown items
- Coverage
    - Catalog coverage: Proportion of items that the recommendation system can recommend
    - Sales diversity: How unequally different items are chosen by users when a particular recommender system is used
        - Calculated with Gini Index or Shannon Entropy
    - User space coverage: Richness of the user profile required to make a recommendation
        - May consider the “coldness” of an item to credit the system more for properly predicting colder items, and less for the hot items that are predicted
- Confidence
    - Can be desirable to choose the one that can provide valid confidence estimates
- Trust
    - Can be beneficial to recommend a few items that the user already knows and likes
    - Trust in the system is correlated with repeated users, but not separated well other factors of user satisfaction
- Novelty
    - Recommendations for items that the user did not know about 
    - May assume that popular items are less likely to be novel
    - We must carefully model the hiding process such that it would resemble the true preference discovery process that occurs in the real system
- Serendipity
    - Random recommendations may be very surprising, and we therefore need to balance serendipity with accuracy
    - May reward the system for successful recommendations that are far from the user profile
- Diversity
    - Diversity of a list based on the sum, average, min, or max distance between item pairs
    - May compute both precision score and diversity score
- Utility
    - Utility can be measured cleanly from the perspective of the recommender system owner
    - But difficult to capture and model user utility
    - May assign negative utilities to unsuccessful recommendations
- Robustness
    - Stability of the recommendation in the presence of fake (intended) or wrong (unintended) information
    - Creating a system that is immune to any type of attack is unrealistic
    - Measured by the amount of injected malicious information
- Privacy
    - No third party should use the recommendation system to learn something about the preferences of a specific user
- Adaptivity
    - Item collection may change rapidly, or trends in interest over items may shift
    - Can evaluate offline by analyzing the amount of information needed before an item is recommended

