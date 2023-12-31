"""Module for defining custom web fields to use on the API interface.
"""
import marshmallow
from webargs import ValidationError, fields, validate

from . import config, responses, utils


class ModelName(fields.String):
    """Field that takes a string and validates against current available
    models at config.MODELS_URI.
    """

    def _deserialize(self, value, attr, data, **kwargs):
        if value not in list(utils.ls_models()):
            raise ValidationError(f"Checkpoint `{value}` not found.")
        return value


class Dataset(fields.String):
    """Field that takes a string and validates against current available
    data files at config.DATA_URI.
    """

    def _deserialize(self, value, attr, data, **kwargs):
        if value not in list(utils.ls_datasets()):
            raise ValidationError(f"Dataset `{value}` not found.")
        return f"{config.DATA_URI}/processed/{value}"


class PredArgsSchema(marshmallow.Schema):
    """Prediction arguments schema for api.predict function."""

    class Meta:  # Keep order of the parameters as they are defined.
        # pylint: disable=missing-class-docstring
        # pylint: disable=too-few-public-methods
        ordered = True

    model_name = ModelName(
        metadata={
            "description": "String identification for models.",
        },
        required=True,
    )

    input_file = fields.Field(
        metadata={
            "description": "NPY file with np.arrays for predictions.",
            "type": "file",
            "location": "form",
        },
        required=True,
    )

    batch_size = fields.Integer(
        metadata={
            "description": "Number of samples per batch.",
        },
        required=False,
        validate=validate.Range(min=1),
    )

    steps = fields.Integer(
        metadata={
            "description": "Steps before prediction round is finished.",
        },
        required=False,
        validate=validate.Range(min=1),
    )

    accept = fields.String(
        metadata={
            "description": "Return format for method response.",
            "location": "headers",
        },
        required=True,
        validate=validate.OneOf(list(responses.content_types)),
    )


class TrainArgsSchema(marshmallow.Schema):
    """Training arguments schema for api.train function."""

    class Meta:  # Keep order of the parameters as they are defined.
        # pylint: disable=missing-class-docstring
        # pylint: disable=too-few-public-methods
        ordered = True

    model_name = ModelName(
        metadata={
            "description": "String identification for models.",
        },
        required=True,
    )

    input_file = Dataset(
        metadata={
            "description": "Dataset name from metadata for training input.",
        },
        required=True,
    )

    epochs = fields.Integer(
        metadata={
            "description": "Number of epochs to train the model.",
        },
        required=False,
        load_default=1,
        validate=validate.Range(min=1),
    )

    initial_epoch = fields.Integer(
        metadata={
            "description": "Epoch at which to start training.",
        },
        required=False,
        load_default=0,
        validate=validate.Range(min=0),
    )

    shuffle = fields.Boolean(
        metadata={
            "description": "Shuffle the training data before each epoch.",
        },
        required=False,
        load_default=True,
    )

    validation_split = fields.Float(
        metadata={
            "description": "Fraction of the data to be used as validation.",
        },
        required=False,
        load_default=0.0,
        validate=validate.Range(min=0.0, max=1.0),
    )

    accept = fields.String(
        metadata={
            "description": "Return format for method response.",
            "location": "headers",
        },
        required=True,
        validate=validate.OneOf(list(responses.content_types)),
    )
