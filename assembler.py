from assembly_parser import assembly_parser
from instruction_table import instruction_table
from register_table import register_table
from pseudoinstruction_table import pseudoinstruction_table

import sys
import argparse

parser = argparse.ArgumentParser(description='Help')
parser.add_argument('--verbose',action='store_true',help='verbose flag' )
parser.add_argument('--instruction', '-i', help='assembly instruction', required=False, type=str)
parser.add_argument('--file','-f' ,required=False,help='inputfile', type=str)
parser.add_argument('--output','-o' ,required=False,help='outputfile', type=str)
parser.add_argument('--start','-s' ,required=False,help='starting adress', type=int)
args = parser.parse_args()


def main(args):
    instruction=[args.instruction]
    assembly_file = args.file
    ouput_file = args.output
    start_addr = args.start
    if start_addr == None:
        start_addr = 0
    if assembly_file != None:
        asm           = open(assembly_file)
        lines = asm.readlines()
        if start_addr == None:
            start_addr =0x80001000
    else:
        lines = instruction

    parser = assembly_parser(start_addr, instruction_table, register_table, pseudoinstruction_table,4,output_file=ouput_file)
    parser.first_pass(lines)
    parser.second_pass(lines)



if __name__ == '__main__':
    main(args)

