## Goal
We have some set of features and we want to model how our observations that are associated with these features change as we change the values of the features.

## Case Study
Predict house values.
* Features include: location, size of bedrooms, square feet etc.
* Observations: house value or house sale price

## Using regression to
* Classification
* Analyze the importance of the features

## Regression
* x - feature, covariate or predictor
* y - observation response

## Linear Regression
* Fit a line through the data
* Use Residual sum of squares (RSS) to determine which line is better
* Search through all w0, w1 (intersect, scope) and find the pair which minimize RSS cost

## How to choose model order/complexity
* Simulate predictions
* 1. Remove some houses
* 2. Fit model on the remaining (Training Set)
* 3. Predict heldout houses (Test Set)
* Training Error only consider training set

## Machine learning pipeline
Data -> ML Method -> Intelligence
Training Data (house id, house attributes, house prices table) -> Feature extraction(Sqft, # bathrooms) -> ML Model (regression) -> Predicted house prices (compared to the actual sale price)


