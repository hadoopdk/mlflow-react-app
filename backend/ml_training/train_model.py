import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# MLflow configuration
MLFLOW_TRACKING_URI = "http://mlflow:5000"  # Adjust as per your MLflow server
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

def run_training(params):
    # Load sample data
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3)

    # Start an MLflow experiment
    with mlflow.start_run():
        # Train model
        model = RandomForestClassifier(**params)
        model.fit(X_train, y_train)

        # Evaluate model
        accuracy = accuracy_score(y_test, model.predict(X_test))
        print(accuracy)

        # Log parameters, metrics, and model
        mlflow.log_params(params)
        mlflow.log_metric('accuracy', accuracy)
        mlflow.sklearn.log_model(model, "model")

        return {"accuracy": accuracy}

