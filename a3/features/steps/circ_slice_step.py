from circ_slice import CircSlice

@when('initialized with start {start:d}, size {size:d} and data {data:Array}')
def step_impl(context, start, size, data):
    context.circ_slice = CircSlice(start, size, data)

@then('it returns {output:Array}')
def step_impl(context, output):
    assert context.circ_slice == output
