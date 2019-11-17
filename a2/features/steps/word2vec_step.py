from math import isclose
from behave import *
from unittest import mock
import importlib

import numpy as np
import word2vec
from word2vec import (
    sigmoid, naiveSoftmaxLossAndGradient, negSamplingLossAndGradient,
    skipgram
)

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

@given('a negSamplingLossAndGradient function')
def step_imp(context):
    pass

@when('it is applied to a center_word_vec={center_word_vec:NdArray}, outside_word_idx={outside_word_idx:d}, K={K:d}, outside_vectors={outside_vectors:NdArray}, and samples the indices {neg_sample_word_indices:NdArray}')
def step_imp(context,
             center_word_vec,
             outside_word_idx,
             outside_vectors,
             K,
             neg_sample_word_indices):
    with mock.patch('word2vec.getNegativeSamples',
                    return_value=neg_sample_word_indices):
        context.result = negSamplingLossAndGradient(
            center_word_vec,
            outside_word_idx,
            outside_vectors,
            None,
            K
        )

@then('it returns loss={loss:f}, grad_center_vec={grad_center_vec:NdArray}, grad_outside_vecs={grad_outside_vecs:NdArray}')
def step_imp(context,
             loss,
             grad_center_vec,
             grad_outside_vecs):
    for i, expected in enumerate([loss, grad_center_vec, grad_outside_vecs]):
        np.testing.assert_allclose(context.result[i], expected)

@given('a skipgram function')
def step_impl(context):
    pass

@when('it is applied to a current_center_word={current_center_word:l}, window_size={window_size:d}, outside_words={outside_words:Array}, word_2_ind={word_2_ind:Dict}, center_word_vectors={center_word_vectors:NdArray}, outside_vectors={outside_vectors:NdArray}, and word_2_vec_loss_and_gradient={word_2_vec_loss_and_gradient:l}')
def step_impl(context, current_center_word, window_size, outside_words,
              word_2_ind, center_word_vectors, outside_vectors,
              word_2_vec_loss_and_gradient):
    context.result = skipgram(current_center_word, window_size, outside_words,
                              word_2_ind, center_word_vectors, outside_vectors,
                              None,
                              getattr(word2vec, word_2_vec_loss_and_gradient))

@then('it returns loss={loss:f}, grad_center_vec={grad_center_vec:NdArray}, grad_outside_vecs={grad_outside_vecs:NdArray')
def step_impl(context, loss, grad_center_vec, grad_outside_vecs):
    for i, out in enumerate([loss, grad_center_vec, grad_outside_vecs]):
        np.testing.assert_allclose(context.result[i], out)
