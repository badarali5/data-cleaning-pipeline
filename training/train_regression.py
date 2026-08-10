from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor


def train_regression(X_train, X_test, y_train, y_test):

    models = {
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(random_state=42),
        "Random Forest": RandomForestRegressor(random_state=42)
    }

    results = {}

    for name, model in models.items():

        model.fit(X_train, y_train)
        predictions = model.predict(X_test)

        results[name] = (model, predictions)

    return results