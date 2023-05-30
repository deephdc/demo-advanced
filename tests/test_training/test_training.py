"""Testing module for api train. This is a test file designed to use
pytest and prepared for some basic assertions and to add your own tests.

You can add new tests following the next structure:
```py
def test_{description for the test}(training):
    assert {statement with metadata that returns true or false}
```

The conftest.py module in the same directory includes the fixture to return
to your tests inside the argument variable `training` the value generated by
your function defined at `api.train`.
"""
# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument


def test_training_acc(training):
    """Test training result includes accuracy on the return."""
    assert "accuracy" in training
    assert isinstance(training["accuracy"], list)
    assert all(isinstance(x, float) for x in training["accuracy"])
    assert all(0.0 <= x <= 1.0 for x in training["accuracy"])


def test_training_loss(training):
    """Test training result includes loss on the return."""
    assert "loss" in training
    assert isinstance(training["loss"], list)
    assert all(isinstance(x, float) for x in training["loss"])
    assert all(0.0 <= x for x in training["loss"])


def test_training_checkpoint(training):
    """Test training result provides the new checkpoint name."""
    assert "new_checkpoint" in training
    assert isinstance(training["new_checkpoint"], str)
