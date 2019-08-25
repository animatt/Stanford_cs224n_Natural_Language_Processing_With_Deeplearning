from math import isclose
from behave import *
import numpy as np
from word2vec import sigmoid, naiveSoftmaxLossAndGradient

@given('a sigmoid function')
def step_impl(context):
    pass

@when('it is applied to {inp:f}')
def step_impl(context, inp):
    context.result = sigmoid(inp)

@then('{out:f} is returned')
def step_impl(context, out):
    assert isclose(context.result, out), \
        f'Expected {out}, got {context.result}'

@when('it is applied to {inp:NdArray}')
def step_imp(context, inp):
    context.result = sigmoid(inp)

@then('{out:NdArray} is returned')
def step_imp(context, out):
    np.testing.assert_allclose(context.result, out)


@given('a naiveSoftmaxLossAndGradient function')
def step_imp(context):
    pass

@when('it is applied to center_word_vec: {center_word_vec:NdArray}, outside_word_idx: {outside_word_idx:d}, outside_vectors: {outside_vectors:NdArray}')
def step_imp(context,
             center_word_vec,
             outside_word_idx,
             outside_vectors):
    context.result = naiveSoftmaxLossAndGradient(
        center_word_vec,
        outside_word_idx,
        outside_vectors,
        None
    )

@then('it returns loss: {loss:f}, grad_center_vec: {grad_center_vec:NdArray}, grad_outside_vecs: {grad_outside_vecs:NdArray}')
def step_imp(context,
             loss,
             grad_center_vec,
             grad_outside_vecs):
    for i, out in enumerate([loss, grad_center_vec, grad_outside_vecs]):
        np.testing.assert_allclose(context.result[i], out)
