import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

def train_model(params):
    # Load data
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = iris.target

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    # Train model
    model = RandomForestClassifier(**params)
    model.fit(X_train, y_train)

    # Predict and calculate accuracy
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    return model, accuracy

if __name__ == "__main__":
    MLFLOW_TRACKING_URI = "http://127.0.0.1:5000"  # Adjust as per your MLflow server
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    mlflow.set_experiment('iris_rf_experiment')

    params = {'n_estimators': 100, 'max_depth': 4}

    with mlflow.start_run():
        model, accuracy = train_model(params)

        # Log parameters and metrics
        mlflow.log_params(params)
        mlflow.log_metric('accuracy', accuracy)

        # Log model
        mlflow.sklearn.log_model(model, "model")
