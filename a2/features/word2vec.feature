Feature: Test Word2Vec Implementation

Scenario Outline: sigmoid
    Given a sigmoid function
    When it is applied to <input>
    Then <output> is returned

Examples: float
    |input          |output       |
    |0.0            |0.5          |
    |1.0            |0.7310585786 |
    |-1.0           |0.2689414214 |

Examples: ndarray
    |input         |output                            |
    |[-1, 0, 1]    |[0.2689414214, 0.5, 0.7310585786] |


Scenario Outline: naiveSoftmaxLossAndGradient
    Given a naiveSoftmaxLossAndGradient function
    When it is applied to center_word_vec: <center_word_vec>, outside_word_idx: <outside_word_idx>, outside_vectors: <outside_vectors>
    Then it returns loss: <loss>, grad_center_vec: <grad_center_vec>, grad_outside_vecs: <grad_outside_vecs>

Examples: float and ndarrays
    |center_word_vec |outside_word_idx |outside_vectors                                     |loss                |grad_center_vec                                              |grad_outside_vecs                                                                                                                                                                                         |
	|[0.2, 1.0, 0.5] |1                |[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]] |1.895613488056148   |[0.7948861720921339, 0.7948861720921343, 0.7948861720921343] |[[0.005488768308294598, -0.16995477103501588,  0.1644660027267213], [0.027443841541472988,  -0.8497738551750793,  0.8223300136336065], [0.013721920770736494, -0.42488692758753965, 0.41116500681680324]] |
