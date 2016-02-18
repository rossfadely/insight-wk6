#!/usr/bin/env python
import os
import string


class SortList(object):
    """Class to solve week 6 code challenge.

    Attributes:
        result (str): sorted string
    """
    def __init__(self, input_path=None, output_path=None):
        """Take in string to input file, read it in, and sort if length > 0.
        Write the result to text file.

        Args:
            input_path (str): Path to ascii text file to be read.
            output_path (str): Path to ascii text file where result is written.
        """
        # if any of the paths are None, initialize for testing else run.
        if (input_path is not None) & (output_path is not None):
            # open the file, get the line.
            line = self._open(input_path)

            # if line is empty write to file, else sort.
            if len(line) == 0:
                self.result = ''
            else:
                self.sort_line(line)

            # write to file.
            self._write(output_path)

    def sort_line(self, line):
        """Sort the line.  First remove unwanted characters, then parse the
        string, finally gather up the results.

        Args:
            line (str): String read in from text file.
        """
        line = self.clean_string(line)
        parsed = self.parse_line(line)
        self.result = self.gather_sorted(*parsed)

    def clean_string(self, line):
        """Remove all unwanted characters except dashes.

        Args:
            line (str): String read in from text file.
        """
        all_ascii = ''.join([chr(i) for i in range(256)])
        bad_ascii = all_ascii.translate(None, ''.join([string.ascii_letters,
                                        string.digits, '-', ' ']))
        return line.translate(None, bad_ascii)

    def parse_line(self, line):
        """Split the line, go through it and create int and str arrays.  Return
        these (sorted) arrays as well as a dict pointing to type.

        Args:
            line (str): String read in from text file.

        Returns:
            line (list): A list formed from splitting the original string on
                         spaces.
            int_arr (list): Sorted integer values in list.
            str_arr (list): Sorted string values in list.
            type_ind (dict): Indicator key pair for type at index in list.
        """
        # convert to list
        line = line.split()

        # characters that define integer entries
        int_chrs = string.digits + '-'

        # go through line and record indicies and values
        str_arr = []
        int_arr = []
        type_ind = {}
        for i, l in enumerate(line):
            # handle dashes, save a leading dash for ints
            first = l[0]
            l = l.translate(None, '-')

            # check if int or word like
            if l[0] in int_chrs:
                if first == '-':
                    l = '-' + l
                int_arr.append(int(l))
                type_ind[i] = 'int'
            else:
                str_arr.append(l)
                type_ind[i] = 'str'

        return (line, sorted(int_arr), sorted(str_arr key=str.lower), type_ind)

    def gather_sorted(self, line, int_arr, str_arr, type_ind):
        """Take the results and place sorted arrays in correct order, return the
        sorted line.

        Args:
            line (list): A list formed from splitting the original string on
                         spaces.
            int_arr (list): Sorted integer values in list.
            str_arr (list): Sorted string values in list.
            type_ind (dict): Indicator key pair for type at index in list.

        Returns:
            (str): The sorted string.
        """
        s, i = 0, 0
        for j in range(len(line)):
            if type_ind[j] == 'str':
                line[j] = str_arr[s]
                s += 1
            else:
                line[j] = str(int_arr[i])
                i += 1

        return ' '.join(line)

    def _open(self, filepath):
        """Read in the text line from file.

        Args:
            filepath (str): Path to text file to be read.
        """
        return open(filepath).read()

    def _write(self, filepath):
        """
        Write the text resulting line to file.

        Args:
            filepath (str): Path to where result is written.
        """
        f = open(filepath, 'w')
        f.write(self.result)
        f.close()


def check_args(args):
    """Check command line arguments specify valid paths.

    Args:
        args (list): Command line arguments to be checked.

    Returns:
        (str): Check path to file.
        (str): Checked path for output.
    """
    # check that correct number of args are given
    m = '\nPlease specify a path for both the input and results file. \nCall '
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
    import sys
    # read command line
    input_path, output_path = check_args(sys.argv)

    # run sorter
    sorter = SortList(input_path, output_path)
