from utils import pad_sents

@when('passed {input_list:json_file} and pad_XX')
def step_impl(context, input_list):
    context.result = pad_sents(input_list, 'pad_XX')

@then('it returns {output:json_file}')
def step_impl(context, output):
    print(context.result)
    print(output)
    assert context.result == output
