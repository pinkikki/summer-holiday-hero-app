import argparse

from tools.diff import diff


def main():
  set_no_option = (lambda p, n: p.add_argument(
    n,
    action='store'
  ))
  parser = argparse.ArgumentParser(usage='file diff', description='how to use', add_help=True)
  set_no_option(parser, 'file_path_1')
  set_no_option(parser, 'file_path_2')

  args = parser.parse_args()

  diff(args.file_path_1, args.file_path_2)


if __name__ == '__main__':
  main()
