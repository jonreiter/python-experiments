import argparse

def test_arg_spec(args_list, expected_values):
    parser = argparse.ArgumentParser()
    parser.add_argument('--flag1', type=eval, choices=[True, False], default=True)
    parser.add_argument('--flag2', type=eval, choices=[True, False], default=False)
    args = parser.parse_args(args_list)
    assert(args.flag1 == expected_values[0])
    assert(args.flag2 == expected_values[1])


test_arg_spec(['--flag1=True', '--flag2=False'], [True, False])
test_arg_spec(['--flag1=True', '--flag2=True'], [True, True])
test_arg_spec(['--flag1=False', '--flag2=False'], [False, False])
test_arg_spec(['--flag1=False', '--flag2=True'], [False, True])
