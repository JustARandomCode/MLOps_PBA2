import time
import pytest
from train import load_data, train


@pytest.fixture(scope="module")
def trained():
    return train(load_data())


# Unit test: accuracy sanity check
def test_accuracy(trained):
    model, X_test, y_test = trained
    assert model.score(X_test, y_test) >= 0.80


# Unit test: latency limit check
def test_latency(trained):
    model, X_test, _ = trained
    start = time.time()
    model.predict(X_test.iloc[[0]])
    assert time.time() - start < 0.5


# Integration test: data -> train -> predict
def test_pipeline_integration(trained):
    model, X_test, _ = trained
    preds = model.predict(X_test)
    assert len(preds) == len(X_test)
    assert set(preds).issubset({0, 1})