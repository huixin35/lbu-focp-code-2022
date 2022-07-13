# Student Marks Statistics

This program reads in five marks and prints out some possibly useful
statistics.

Points to note:
* `input` always gives a string, so we need to convert the value entered to a number.
* Brackets are needed in the average calculation to make sure
  addition happens before division.
* There are built-in functions to find the maximum and minimum - no
  need to work out how to code these!
* f-strings are a neat way to show results.

The program will obviously fail if a value is entered that is not a number. It
also does not check that the values are within some sensible bounds -
negative marks would be accepted and processed, for example.
