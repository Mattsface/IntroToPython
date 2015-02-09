#!/usr/bin/env python


def main():
    x = safe_input("This is a text ")
    print ""
    print x


def safe_input(text):
    try:
        return raw_input(text)
    except EOFError:
        return None
    except KeyboardInterrupt:
        return None


if __name__ == '__main__':
    main()