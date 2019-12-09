from parser_model import ParserModel
from unittest import mock
import numpy as np

@given('a ParserModel object with embeddings shape {input_shape:Array} and {n_features:d} features')
def step_impl(context, input_shape, n_features):
    np.random.seed(0)
    input_ar = np.random.uniform(0, high=5, size=input_shape).astype('float32')
    context.parser_model = ParserModel(input_ar, n_features=n_features)

@when('it is sent embedding_lookup with {indices:Tensor}')
def step_impl(context, indices):
    context.result = context.parser_model.embedding_lookup(indices)

@then('it receives a tensor with shape {output_shape:Array}')
def step_impl(context, output_shape):
    assert [x for x in context.result.shape] == output_shape

@when('it is sent forward with {indices:Tensor}')
def step_impl(context, indices):
    context.result = context.parser_model(indices)
