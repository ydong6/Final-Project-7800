#!/usr/bin/env python
# encoding: utf-8
'''
Created on May 3, 2016
Final Project: Designing and Examining Gibson Assemble Sequence
7800 Programming for Biologist.
@author: Yuankai Dong
'''

import argparse
from Bio import Restriction
from Bio import SeqIO
from Bio import pairwise2
import colorama
from colorama import Fore, Back, Style
from collections import Counter

colorama.init()


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--in1", type=str,
                        help="provide sequence1 with extension")
    parser.add_argument("--in2", type=str,
                        help="provide sequence2 with extension")
    parser.add_argument(
        "--out",
        required=True,
        help="Enter the name of the output file.",
        type=str
    )
    return parser.parse_args()


class gibson:

    def __init__(self, value1, value2, value3):
        self.outfile = value3
        with open(value1, 'r') as f:
            self.record = SeqIO.read(f, 'fasta')
            self.seq1 = self.record.seq
            self.pro_seq1 = self.seq1.translate()
        with open(value2, 'r') as e:
            self.record2 = SeqIO.read(e, 'fasta')
            self.seq2 = self.record2.seq
            self.pro_seq2 = self.seq2.translate()

    def restriction(self):
        with open(self.outfile, 'w')as result:
            result.write('{0}\n{1:<20}\n{2}\n'.format(
                'Final project output', 'Reading File:', self.record))

            NEB = Restriction.RestrictionBatch(first=[], suppliers='N')
            enzyme_cut = NEB.search(self.seq1, linear=False)
            counter = Counter()
            for key, value in enzyme_cut.items():
                if value != []:
                    counter[key] = len(value)
            single_cuts = min(counter.values())
            single_set = []
            for key, value in counter.items():
                if value == single_cuts:
                    single_set.append([key, value])
            # print(sorted(single_set))
            result.write('\n{0:<20}\n{1:<20}{2:<10}\n{3:<10}\n'.format(
                'Single cut:',
                'Cut sites',
                'Enzyme',
                '============================================================'
            )
            )
            for item in sorted(single_set):
                result.write(
                    '{0:<20}{1:<10}\n'.format(str(item[1]), str(item[0])))

    def align_search(self):
        with open(self.outfile, 'a+')as write:
            for a in pairwise2.align.localxd(self.seq1, self.seq2,
                                             -1, -1, -2, -1):
                usa = pairwise2.format_alignment(*a)
                print(Fore.BLUE + self.record.id, self.record2.id)
                print(Back.YELLOW + usa + Style.RESET_ALL)

                write.write('\n\n{0}{1:<10}\n{2:<10}\n{3:<10}'
                            .format('Sequence ID: ', self.record.id,
                                    'Sequence Alignment', usa))

            for b in pairwise2.align.localxs(self.pro_seq1, self.pro_seq2,
                                             -1, -1):
                uk = pairwise2.format_alignment(*b)
                print(Fore.BLUE + self.record.id, self.record2.id)
                print(Back.YELLOW + uk + Style.RESET_ALL)
                write.write('\n{0:<20}{1:<10}\n{2:<10}\n{3:<10}'
                            .format('Protein ID: ', self.record.id,
                                    'Protein Alignment',
                                    uk))


def main():
    arg = parser()
    seqa = arg.in1
    seqb = arg.in2
    search = gibson(seqa, seqb, arg.out)
    search.restriction()
    search.align_search()


if __name__ == '__main__':
    main()
