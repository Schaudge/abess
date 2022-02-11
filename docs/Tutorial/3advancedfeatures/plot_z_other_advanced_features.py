"""
Other Advanced Features
========================
"""
#%%
# Integrate SIS
# -------------------
# Ultra-high dimensional predictors increase computational cost but reduce estimation accuracy for any statistical procedure. To reduce dimensionality from high to a relatively acceptable level, a fairly general asymptotic framework, named feature screening (sure independence screening) is proposed to tackle even exponentially growing dimension. The feature screening can theoretically maintain all effective predictors with a high probability, which is called "the sure screening property".
# 
# In our program, to carrying out the Integrate SIS, user need to pass an integer smaller than the number of the predictors to the `screening_size`. Then the program will first calculate the marginal likelihood of each predictor and reserve those predictors with the `screening_size` largest marginal likelihood. Then, the ABESS algorithm is conducted only on this screened subset. 
# 
# Here is an example.
import numpy as np
from abess.datasets import make_glm_data
from abess.linear import LinearRegression

np.random.seed(0)

n = 100
p = 1000
k = 3
np.random.seed(2)

# gene data
dt = make_glm_data(n = n, p = p, k = k, family = 'gaussian')
print('real coefficients\' indexes:', np.nonzero(dt.coef_)[0])

# fit
model = LinearRegression(support_size = range(0, 5), screening_size = 100)
model.fit(dt.x, dt.y)
print('fitted coefficients\' indexes:', np.nonzero(model.coef_)[0])

########################################################
# User-specified cross validation division
# ---------------------------------------------
# Sometimes, especially when running a test, we would like to fix the train and valid data used in cross validation, instead of choosing them randomly.
# One simple method is to fix a random seed, such as `numpy.random.seed()`. But in some cases, we would also like to specify which samples would be in the same "fold", which has great flexibility.
# 
# In our program, an additional argument `cv_fold_id` is for this user-specified cross validation division. An integer array with the same size of input samples can be given, and those with same integer would be assigned to the same "fold" in K-fold CV.

n = 100
p = 1000
k = 3
np.random.seed(2)

dt = make_glm_data(n = n, p = p, k = k, family = 'gaussian')

# cv_fold_id has a size of `n`
# cv_fold_id has `cv` different integers
cv_fold_id = [1 for i in range(30)] + [2 for i in range(30)] + [3 for i in range(40)] 

model = LinearRegression(support_size = range(0, 5), cv = 3)
model.fit(dt.x, dt.y, cv_fold_id = cv_fold_id)
print('fitted coefficients\' indexes:', np.nonzero(model.coef_)[0])

########################################################
# User-specified initial active set
# -----------------------------------------
# We believe that it worth allowing given an initial active set so that the splicing process starts from this set for each sparsity. 
# It might come from prior analysis, whose result is not quite precise but better than random selection, so the algorithm can run more efficiently. Or you just want to give different initial sets to test the stability of the algorithm.
# 
# *Note that this is NOT equal to `always_select`, since they can be exchanged to inactive set when splicing.*
# 
# To specify initial active set, an additive argument `A_init` should be given in `fit()`.


n = 100
p = 10
k = 3
np.random.seed(2)

dt = make_glm_data(n = n, p = p, k = k, family = 'gaussian')

model = LinearRegression(support_size = range(0, 5))
model.fit(dt.x, dt.y, A_init = [0, 1, 2])

#%%
# Some strategies for initial active set are:
# 
# - If `sparsity = len(A_init)`, the splicing process would start from `A_init`.
# - If `sparsity > len(A_init)`, the initial set includes `A_init` and other variables `inital screening` chooses.
# - If `sparsity < len(A_init)`, the initial set includes part of `A_init`.
# - If both `A_init` and `always_select` are given, `always_select` first.
# - For warm-start, `A_init` will only affect splicing under the first sparsity in `support_size`.
# - For CV, `A_init` will affect each fold but not the re-fitting on full data.
#
# R tutorial
# -----------------------
# For R tutorial, please view [https://abess-team.github.io/abess/articles/v07-advancedFeatures.html](https://abess-team.github.io/abess/articles/v07-advancedFeatures.html).
