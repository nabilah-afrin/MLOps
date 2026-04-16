import mlflow
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error
import numpy as np


mlflow.set_experiment("diabetes_experiment")

diabetes = load_diabetes()
X,y = diabetes.data, diabetes.target
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)


learning_rate = 0.01
n_iterations = 1000  # Increased for better convergence

with mlflow.start_run(run_name="SGDRegressor"):
    mlflow.log_param("learning_rate", learning_rate)
    mlflow.log_param("n_iterations", n_iterations)

    model = SGDRegressor(learning_rate='constant', eta0=learning_rate, max_iter=n_iterations, random_state=42, tol=1e-3)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    
    mlflow.log_metric("mse", mse)
    print(f"Mean Squared Error: {mse}")

    # log artifact (model coefficients)
    with open("model_coefficients.txt", "w") as f:
        f.write(f"Model: SGDRegressor\nMSE: {mse}\nLearning Rate: {learning_rate}\nIterations: {n_iterations}\n")
        f.write("Model Coefficients:\n")
        f.write(str(model.coef_))
    mlflow.log_artifact("model_coefficients.txt")