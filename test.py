#!/usr/bin/env python
import unittest, string
import numpy as np
from listSorting import SortList

sorter = SortList()

def string_gen(N=100, frac_str=0.5, bad_tol=0., max_str_len=20, max_bad_len=2,
               seed=1234):
    """Generate string to test sorter.

    Args:
        N (int): Total number of strings/ints in clean string.
        frac_str (float): Decimal fraction of N that will be type string
        bad_tol (float): Tolerance for inserting bad ascii (decided randomly)

    Returns:
        test_string (str): Test string with bad ascii inserted
        targ_string (str): Target string (clean and sorted)
    """
    np.random.seed(seed)
    Nstr = np.int(np.round(N * frac_str))
    Nint = N - Nstr
    all_ascii = ''.join([chr(i) for i in range(256)])
    bad_ascii = all_ascii.translate(None, ''.join([string.ascii_letters,
                                    string.digits, '-', ' ']))
    bad_ascii = [b for b in bad_ascii]

    # generate random str, int arrays
    str_arr, int_arr = [], []
    str_chrs = np.array([s for s in string.ascii_letters])
    for i in range(Nstr):
        str_len = np.random.randint(1, max_str_len)
        s = ''.join(str_chrs[np.random.randint(str_chrs.size, size=str_len)])
        str_arr.append(s)
    int_arr = np.random.randint(-999999, 999999, Nint)

    # sort
    sorted_int = sorted(int_arr)
    sorted_str = sorted(str_arr)

    # make target and test strings
    target, test = [], []
    type_ind = {}
    int_count, str_count = 0, 0
    for i in range(N):
        if (((np.random.randint(1)) & (int_count < Nint)) |
            (str_count == Nstr)):
            targ_add = str(sorted_int[int_count])
            test_add = str(int_arr[int_count])
            type_ind[i] = 'int'
            int_count += 1
        else:
            targ_add = sorted_str[str_count]
            test_add = str_arr[str_count]
            type_ind[i] = 'str'
            str_count += 1

        # randomly add bad ascii to test_add
        if np.random.rand() < bad_tol:
            Nbad = np.random.randint(1, max_bad_len)
            locs = np.random.permutation(len(test_add))
            for l in locs:
                test_add = test_add[:l] + np.random.choice(bad_ascii) + \
                    test_add[l:]
        test.append(test_add)
        target.append(targ_add)
    return ' '.join(test), ' '.join(target), sorted_int, sorted_str, type_ind

class TestSorterMethods(unittest.TestCase):
    def test_clean_string(self):
        examples = ['-2\n2@1 -11*21 adAD:Sbiha? pojKKdfa -1121 a;a; sle 2^&%00 30\')']
        targets = ['-221 -1121 adADSbiha pojKKdfa -1121 aa sle 200 30']
        res = sorter.clean_string(examples[0])
        self.assertEqual(res, targets[0])

    def test_parse(self):
        test, targ, sorted_int, sorted_str, type_ind_targ = string_gen()
        line = sorter.clean_string(test)
        l, ints, strs, type_ind = sorter.parse_line(line)
        self.assertEqual(sorted_int, ints)
        self.assertEqual(sorted_str, strs)
        self.assertEqual(type_ind_targ, type_ind)

    def test_sort(self):
        test, targ, sorted_int, sorted_str, type_ind = string_gen()
        sorter.sort_line(test)
        self.assertEqual(targ, sorter.result)

    def test_end_to_end(self):
        test, targ, sorted_int, sorted_str, type_ind = string_gen()
        sorter.result = test
        sorter._write('./test_line.txt')
        sorter.__init__('./test_line.txt', './test_result.txt')
        result = sorter._open('./test_result.txt')
        self.assertEqual(targ, result)

if __name__ == '__main__':
    unittest.main()
