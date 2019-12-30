Feature: Utils

Scenario Outline: pad_sents
    When passed <input> and pad_XX
	Then it returns <output>

Examples: json files
    |input               | output               |
	|in_pad_sents_1.json | out_pad_sents_1.json |
