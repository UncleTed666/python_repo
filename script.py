import argparse

x = 10
print(x**2)

def main():
  parser = argparse.ArgumentParser(prog='Script to run')
  parser.add_argument('--param', nargs='?', help='"X" param')

  args = parser.parse_args()
  run(**vars(args))

def run(param=None):
  if param:
    return param**2
  
main()
