## Goal

Classifier takes some input x, it pushes x through the model to output some value y that we are trying to predict.

## Simple threshold classifier
* Count negative/positive words

## Linear classifier
* Training a classifier = Learning the weights
* Score(x) = weighted count of words in sentence

## Decision boundary
* Decision boundary separates positive & negative predictions

## Classification error & accuracy
* error = (# of mistake)/(Total # of sentences)
* accuracy = (# of correct) /(Total # of sentences)   -- diagonal
* error + accuracy = 1

## Confusion matrix
True, Predicted
* +, + 		true positive
* +, - 		false negative
* -, +		false positive
* -, -		true negative
