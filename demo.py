# author: Son Chau
# date: 2021-11-19

"""This script prints out docopt args.
Usage: demo.py <arg1> --arg2=<arg2> [--arg3=<arg3>] [--arg4=<arg4>]

Options:
<arg>             Takes any value (this is a required positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)
[--arg4=<arg4>]   Takes any value (this is an optional option)
"""

from docopt import docopt


# define main function
def main():
    opt = docopt(__doc__)
    print(opt)
    print(type(opt))
    # print out arg4
    print(opt['--arg4'])

    # call main function
if __name__ == "__main__":
    main()
