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
