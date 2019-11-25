from parser_transitions import PartialParse, minibatch_parse
from unittest.mock import MagicMock

@given('PartialParse has stack {stack:Array}, buffer {buffer:Array}, dependencies {dependencies:Array}')
def step_impl(context, stack, buffer, dependencies):
    __partial_parse = PartialParse(buffer)
    __partial_parse.stack = stack
    __partial_parse.buffer = buffer
    __partial_parse.dependencies = dependencies
    context.partial_parse = __partial_parse

@when('it is called with \'{transition:l}\'')
def step_impl(context, transition):
    # print('................')
    # print(context.partial_parse.stack)
    # print(context.partial_parse.buffer)
    # print(context.partial_parse.dependencies)
    # print('****************')
    context.result = context.partial_parse.parse_step(transition)

@then('it mutates {attr:l} to {next_state:Array}')
def step_impl(context, attr, next_state):
    assert getattr(context.partial_parse, attr) == next_state

@given('a class implementing object.predict(partial_parses) which returns {prediction:Array}')
def step_impl(context, prediction):
    class MockModel:
        def __init__(self):
            self.idx = 0
        def predict(self, partial_parses):
            idx = self.idx
            self.idx += 1
            return prediction[idx]
    context.model = MockModel()

@when('called')
def step_impl(context):
    context.result = context.partial_parse.done()

@then('it returns {finished:Bool}')
def step_impl(context, finished):
    assert context.result == finished

@when('it is called with sentences {sentences:Array}, a model object, and batch_size {batch_size:d}')
def step_impl(context, sentences, batch_size):
    context.result = minibatch_parse(sentences, context.model, batch_size)

@then('it returns dependencies {dependencies:Array}')
def step_impl(context, dependencies):
    print(context.result)
    assert context.result == dependencies
