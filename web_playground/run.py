import argparse

from web_playground.app import app


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', action='store', nargs='?', default=6565, type=int)
    return parser.parse_args()


def main():
    args = parse_args()
    app.run(debug=True, port=args.port)


if __name__ == '__main__':
    main()
