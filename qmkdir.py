import os
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Create a directory with a random name.")
    parser.add_argument("-d", default=os.getcwd(), help="base directory path (default: current directory)")
    parser.add_argument("-n", type=int, default=3, help="number of random bytes (default: 3, i.e. 6-char hex)")
    parser.add_argument("--full-path", action="store_true", help="print full path instead of name only")
    args = parser.parse_args()

    base = os.path.abspath(os.path.expanduser(args.d))

    if not os.path.isdir(base):
        print(f"error: '{base}' is not a directory or does not exist.", file=sys.stderr)
        sys.exit(1)

    name = os.urandom(args.n).hex()
    full = os.path.join(base, name)

    try:
        os.mkdir(full)
    except PermissionError:
        print(f"error: no write permission for '{base}'.", file=sys.stderr)
        sys.exit(1)

    print(full if args.full_path else name)

if __name__ == "__main__":
    main()
