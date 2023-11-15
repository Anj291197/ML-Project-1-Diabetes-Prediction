# ML-Project-1
The Diabetes prediction dataset is a collection of medical and demographic data from patients, along with their diabetes status (positive or negative).
This dataset can be used to build machine learning models to predict diabetes in patients based on their medical history and demographic information1.
One of the machine learning models that can be used for this task is the Support Vector Classifier (SVC) algorithm.
SVC is a type of supervised learning algorithm that can classify data into two or more classes by finding the optimal hyperplane that separates the data points. 
SVC can handle both linear and non-linear classification problems by using different kernel functions, such as linear, polynomial, radial basis function (RBF), or sigmoid2.
To use SVC for diabetes prediction, one needs to follow these steps:
Import the necessary libraries, such as pandas, numpy, sklearn, and matplotlib.
Load the dataset and perform some exploratory data analysis, such as checking the shape, data types, summary statistics, and missing values of the dataset.
Split the dataset into training and testing sets, using a suitable ratio, such as 80:20.
Create an SVC object and specify the kernel function and other hyperparameters, such as gamma.
Fit the SVC model on the training data and make predictions on the testing data.
Evaluate the performance of the model using appropriate metrics, such as accuracy, precision, recall, f1-score.
