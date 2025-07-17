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
python3 training/spaced_repetition_training.py
```

Example output :

```shell
21 problems are due for review today:
- Valid Anagram
- Contains Duplicate
- Two Sum
- Group anagrams
- Encode and Decode Strings
- Top k frequent elements
- Valid Palindrome
- Valid Sudoku
- Valid Parentheses
- Longest Consecutive Sequence
- Length of Last Word
- Binary Search
- Min Stack
- Evaluate Reverse Polish Notation
- Two Sum II - Input Array Is Sorted
- Search a 2D Matrix
- Guess Number Higher or Lower
- First Bad Version
- Koko Eating Bananas
- Daily Temperatures
- Search in a Binary Search Tree

Reviewing: Valid Anagram
Was the training successful? (y/n/q to quit): y

Reviewing: Contains Duplicate
Was the training successful? (y/n/q to quit): q
Exiting training session. Progress will be saved.
```
