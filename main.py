import argparse
import migrator

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-s', '--source', dest='source_username', help='Source account')
  parser.add_argument('-d', '--dest', dest='dest_username', help='Destination account')
  args = parser.parse_args()

  migrator.migrate(source=args.source_username,dest=args.dest_username)

if __name__ == "__main__":
  main()