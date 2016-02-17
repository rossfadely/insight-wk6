#!/usr/bin/env python
import os

class SortList(object):
    """
    Class to solve week 6 code challenge.
    """
    def __init__(self, input_path, output_path):
        """
        Take in string to input file, read it in, and sort if needed.
        """
        # open the file, get the line.
        line = self._open(input_path)

        # if line is empty write to file, else sort.
        if len(line) == 0:
            self.result = ''
        else:
            self.sort_list(line)

        self._write(output_path)

    def sort_list(self, line):
        """
        Sort the line.
        """
        pass

    def _open(self, filepath):
        """
        Read in the text line from file.
        """
        return open(filepath).readlines()

    def _write(self, filepath):
        """
        Write the text resulting line to file.
        """
        f = open(filepath, 'w')
        f.write(self.result)
        f.close()

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
    assert args[2].split('/')[-1] == 'result.txt'
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

    sorter = SortList(input_path, output_path)
