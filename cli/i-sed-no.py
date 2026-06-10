"""
##   i-sed-no   ##

This script, "I _sed_ no,", is a replacement for `sed` for me on the command-line

## One main use case:
- pick a file (or glob)
- accept a regex
- replace with another string
- write those replacements to the file
- print the results to the console

## Additional features:

### Dry runs available
- test which files are targeted, mostly for globs
- test regex validity
- test number and contents of matches
  - show all matches if there are less than twenty
  - bunch together identical matches with a count, e.g. "snth (3)" if there are three matches of "snth".
- test full command, without writing to file
  - output shows the files targeted and count
    - and full file list, if there are less than five
  - output shows the number of replacements to be made, and the new string to be written

### Help output
- `-h` shows usage information and brief program tagline
- `--help` shows a longer description of the program, describing the features in more detail

### Interactive CLI harness
- `--interactive` or `-i` activates an interactive CLI harness
  - so that the user can set file glob, regex, and replacement string interactively
    - and iteratively call the dry runs, modifying what needs changing, but keeping the options they've already chosen


"""

import argparse
import glob
import re
import sys
from collections import Counter
from pathlib import Path

TAGLINE = 'i-sed-no: a friendlier sed-style find/replace tool with dry runs and an interactive mode.'

USAGE = 'i-sed-no.py [options] REGEX REPLACEMENT FILE_OR_GLOB [FILE_OR_GLOB ...]'

SHORT_HELP = f"""{TAGLINE}

usage: {USAGE}

options:
  -h                 show this brief usage information
  --help             show a longer description of the program
  -n, --dry-run      run the full command without writing to any file
  --list-files       dry run: show which files are targeted by the glob(s)
  --check-regex      dry run: test that the regex is valid
  --show-matches     dry run: show count and contents of matches
  -i, --interactive  interactive harness for setting glob/regex/replacement
"""

LONG_HELP = SHORT_HELP + """
description:
  i-sed-no ("I sed no") performs regex find-and-replace across one or more
  files selected by path or glob. Replacements are written back to the files,
  and a summary of results is printed to the console.

dry runs:
  --list-files     Expands the file arguments / globs and prints the files
                   that would be targeted, without reading or writing them.
  --check-regex    Compiles the regex and reports whether it is valid,
                   along with any error message from the regex engine.
  --show-matches   Scans the targeted files and reports the number of
                   matches. If there are fewer than twenty matches in total,
                   each match is shown; identical matches are bunched
                   together with a count, e.g. 'snth (3)'.
  -n, --dry-run    Runs the full command without writing anything. Output
                   shows the targeted files and their count (the full file
                   list if there are fewer than five), the number of
                   replacements that would be made, and the replacement
                   string that would be written.

interactive mode:
  -i, --interactive starts a small CLI harness where you can set the file
  glob, regex, and replacement string one at a time, run any of the dry runs
  against the current settings, tweak whatever needs changing while keeping
  the rest, and finally apply the replacement for real.

note on globs:
  In non-interactive mode your shell expands globs before Python sees them,
  which works fine since all positional extras are treated as file args --
  but quote the glob (e.g. '**/*.py') if you want Python's recursive
  matching instead of the shell's.
"""


def expand_files(patterns):
    """Expand globs/paths into a sorted, de-duplicated list of existing files."""
    files = []
    for pattern in patterns:
        matched = glob.glob(pattern, recursive=True)
        if matched:
            files.extend(p for p in matched if Path(p).is_file())
        elif Path(pattern).is_file():
            files.append(pattern)
    return sorted(set(files))


def compile_regex(pattern):
    """Return (compiled_regex, error_message). Exactly one will be None."""
    try:
        return re.compile(pattern), None
    except re.error as e:
        return None, str(e)


def read_text(path):
    return Path(path).read_text(encoding='utf-8', errors='replace')


def collect_matches(regex, files):
    """Return a list of all match strings across the given files."""
    matches = []
    for f in files:
        matches.extend(m.group(0) for m in regex.finditer(read_text(f)))
    return matches


def print_file_list(files, full_list_limit=None):
    print(f'{len(files)} file(s) targeted')
    if full_list_limit is None or len(files) < full_list_limit:
        for f in files:
            print(f'  {f}')


def print_matches(matches, show_all_limit=20):
    print(f'{len(matches)} match(es) found')
    if 0 < len(matches) < show_all_limit:
        for text, count in Counter(matches).items():
            print(f'  {text} ({count})' if count > 1 else f'  {text}')


def do_list_files(patterns):
    files = expand_files(patterns)
    print_file_list(files)
    return 0


def do_check_regex(pattern):
    regex, error = compile_regex(pattern)
    if regex is None:
        print(f'invalid regex: {error}')
        return 1
    print(f'regex OK: {pattern!r}')
    return 0


def do_show_matches(pattern, patterns):
    regex, error = compile_regex(pattern)
    if regex is None:
        print(f'invalid regex: {error}')
        return 1
    files = expand_files(patterns)
    if not files:
        print('no files matched')
        return 1
    print_matches(collect_matches(regex, files))
    return 0


def do_replace(pattern, replacement, patterns, dry_run):
    regex, error = compile_regex(pattern)
    if regex is None:
        print(f'invalid regex: {error}')
        return 1
    files = expand_files(patterns)
    if not files:
        print('no files matched')
        return 1

    print_file_list(files, full_list_limit=5)

    total = 0
    for f in files:
        text = read_text(f)
        new_text, count = regex.subn(replacement, text)
        total += count
        if count and not dry_run:
            Path(f).write_text(new_text, encoding='utf-8')
            print(f'  {f}: {count} replacement(s) written')
        elif count:
            print(f'  {f}: {count} replacement(s) would be made')

    verb = 'would be made' if dry_run else 'made'
    print(f'{total} replacement(s) {verb}, replacing with: {replacement!r}')
    return 0


def prompt(label, current):
    shown = f' [{current}]' if current else ''
    value = input(f'{label}{shown}: ').strip()
    return value if value else current


def interactive(args):
    print(TAGLINE)
    
    cwd = Path.cwd()
    home = Path.home()
    try:
        rel_cwd = f'~/{cwd.relative_to(home)}'
    except ValueError:
        rel_cwd = str(cwd)
    print(f'Working directory: {rel_cwd}')
    
    print('Interactive mode. Press enter at a prompt to keep the current value.\n')

    pattern = args.regex or ''
    replacement = args.replacement or ''
    patterns = list(args.files)

    menu = """
commands:
  g  set file glob(s) (space-separated)
  r  set regex
  s  set replacement string
  f  dry run: list targeted files
  v  dry run: validate regex
  m  dry run: show matches
  d  dry run: full command, no writes
  w  WRITE replacements to files
  p  print current settings
  q  quit
"""
    print(menu)

    while True:
        try:
            choice = input('i-sed-no> ').strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return 0

        if choice == 'g':
            raw = prompt('file glob(s)', ' '.join(patterns))
            patterns = raw.split()
        elif choice == 'r':
            pattern = prompt('regex', pattern)
        elif choice == 's':
            replacement = prompt('replacement', replacement)
        elif choice == 'f':
            if patterns:
                do_list_files(patterns)
            else:
                print('set file glob(s) first (g)')
        elif choice == 'v':
            if pattern:
                do_check_regex(pattern)
            else:
                print('set regex first (r)')
        elif choice == 'm':
            if pattern and patterns:
                do_show_matches(pattern, patterns)
            else:
                print('set regex (r) and file glob(s) (g) first')
        elif choice in ('d', 'w'):
            if pattern and patterns:
                do_replace(pattern, replacement, patterns, dry_run=(choice == 'd'))
            else:
                print('set regex (r) and file glob(s) (g) first')
        elif choice == 'p':
            print(f'  glob(s):     {" ".join(patterns) or "(unset)"}')
            print(f'  regex:       {pattern or "(unset)"}')
            print(f'  replacement: {replacement or "(unset)"}')
        elif choice == 'q':
            return 0
        elif choice in ('h', '?', 'help'):
            print(menu)
        elif choice:
            print(f'unknown command: {choice!r} (h for help)')


def build_parser():
    parser = argparse.ArgumentParser(prog='i-sed-no.py', usage=USAGE, add_help=False)
    parser.add_argument('-h', dest='short_help', action='store_true')
    parser.add_argument('--help', dest='long_help', action='store_true')
    parser.add_argument('-n', '--dry-run', action='store_true')
    parser.add_argument('--list-files', action='store_true')
    parser.add_argument('--check-regex', action='store_true')
    parser.add_argument('--show-matches', action='store_true')
    parser.add_argument('-i', '--interactive', action='store_true')
    parser.add_argument('regex', nargs='?')
    parser.add_argument('replacement', nargs='?')
    parser.add_argument('files', nargs='*')
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)

    if args.short_help:
        print(SHORT_HELP)
        return 0
    if args.long_help:
        print(LONG_HELP)
        return 0
    if args.interactive:
        return interactive(args)

    if args.check_regex:
        if args.regex is None:
            print('error: --check-regex requires a REGEX argument')
            return 2
        return do_check_regex(args.regex)

    if args.list_files:
        patterns = [p for p in [args.regex, args.replacement, *args.files] if p]
        if not patterns:
            print('error: --list-files requires at least one FILE_OR_GLOB argument')
            return 2
        return do_list_files(patterns)

    if args.show_matches:
        if args.regex is None or args.replacement is None:
            print('error: --show-matches requires REGEX and FILE_OR_GLOB arguments')
            return 2
        return do_show_matches(args.regex, [args.replacement, *args.files])

    if args.regex is None or args.replacement is None or not args.files:
        print(SHORT_HELP)
        return 2

    return do_replace(args.regex, args.replacement, args.files, dry_run=args.dry_run)


if __name__ == '__main__':
    sys.exit(main())
