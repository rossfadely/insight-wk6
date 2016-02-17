#!/usr/bin/env python
import os

class SortList(object):
    """

    """
    def __init__(self, filepath):
        pass

def check_args(args):
    """
    Check command line arguments specify valid paths.
    """
    # check that correct number of args are given
    m = '\n\nPlease specify a path for both the input and results file. \nCall '
    m += 'should look like:\n ./listSorting.py <path-to-input-file>/list.txt'
    m += '<path-to-output-file>/result.txt'
    assert len(args) == 3, m

    # check that input text file exists
    assert os.path.isfile(args[1]), 'Input file not found.'

    # check output text path is valid
    m = 'Please specify a valid path for output file in the form:\n'
    m += '<path-to-output-file>/result.txt'
    try:
        output_path = ''.join(args[2].split('/')[:-1])
        assert os.path.exists(output_path)
        assert args[2].split('/')[-1] == 'result.txt'
    except:
        assert False, m

    return args[1], args[2]

if __name__ == '__main__':
    # read command line
    import sys
    input_path, output_path = check_args(sys.argv)
