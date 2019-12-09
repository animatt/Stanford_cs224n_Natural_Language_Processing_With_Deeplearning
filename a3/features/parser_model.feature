Feature: Test ParserModel Implementation

Scenario Outline: embedding_lookup
    Given a ParserModel object with embeddings shape <input_shape> and <n_features> features
	When it is sent embedding_lookup with <indices>
	Then it receives a tensor with shape <output_shape>

Examples: shapes
    |input_shape |n_features |indices          |output_shape |
	|[5, 2]      |3          |[[0, 1, 2]]      |[1, 6]       |
	|[5, 2]      |4          |[[0, 1], [2, 3]] |[2, 4]       |

Scenario Outline: forward
    Given a ParserModel object with embeddings shape <input_shape> and <n_features> features
	When it is sent forward with <indices>
	Then it receives a tensor with shape <output_shape>

Examples: arrays
    |input_shape |n_features |indices     |output_shape |
	|[5, 2]      |3          |[[0, 1, 2]] |[1, 3]       |
	