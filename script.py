import argparse

def main():
  parser = argparse.ArgumentParser(prog='Script to run')
  parser.add_argument('--param', nargs='?', help='"X" param')

  args = parser.parse_args()
  run(**vars(args))

def run(param=None):
  try:
      param = int(param)
  except:
      raise ValueError('wrong type "param"')
  print(param**2)
  
main()
