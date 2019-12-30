from subprocess import check_output

@then('it passes {test_name}')
def step_impl(context, test_name):
    assert ('All Sanity Checks Passed'
            in str(check_output('python sanity_check.py 1e', shell=True)))
