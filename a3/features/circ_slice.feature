Feature: Test CircSlice Implementation

Scenario Outline: __init__
    When initialized with start <start>, size <size> and data <data>
	Then it returns <output>

Examples: array
    |start |size |data            |output    |
	|0     |3    |[1, 2, 3, 4, 5] |[1, 2, 3] |
	|3     |3    |[1, 2, 3, 4, 5] |[4, 5, 1] |
	