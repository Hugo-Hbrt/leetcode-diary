# Space Repetition Training System

## Overview

This system is a small space repetition training system, that will ask the user to train leetcode problem frequently, and depending on 
how the problem is easy to solve for the user.

## Features

- Automatic synchronisation of available problems, by parsing the root README file.
- Automatic generation/saving of the training data.
- Training session generation, simple prompt for problem training success or not.

## Usage

To use the system, you just need to run the python script from project root folder.

```shell
python3 training/cli.py
```

Example output :

```shell
 Cards due today (Use ↑ ↓ to navigate, Enter to select, q to quit):

  Contains Duplicate
  Two Sum
  Group anagrams
  Encode and Decode Strings
  Top k frequent elements
  Valid Palindrome
  Valid Sudoku
  Valid Parentheses
  Longest Consecutive Sequence
  Length of Last Word
  Binary Search
  Min Stack
  Evaluate Reverse Polish Notation
  Two Sum II - Input Array Is Sorted
  Search a 2D Matrix
↓ More cards below
```
