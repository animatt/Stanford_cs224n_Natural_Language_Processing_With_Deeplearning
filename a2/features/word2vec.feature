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

Scenario Outline: negSamplingLossAndGradient
    Given a negSamplingLossAndGradient function
	When it is applied to a center_word_vec=<center_word_vec>, outside_word_idx=<outside_word_idx>, K=<K>, outside_vectors=<outside_vectors>, and samples the indices <neg_sample_word_indices>
	Then it returns loss=<loss>, grad_center_vec=<grad_center_vec>, grad_outside_vecs=<grad_outside_vecs>

Examples: float and ndarrays
    |center_word_vec |outside_word_idx |outside_vectors                   |K |neg_sample_word_indices | loss              |grad_center_vec                                        |grad_outside_vecs                                                                                                                                                                         |
	|[0.4, 0.1, 0.4] |1                |[[1, 4, 7], [2, 5, 8], [3, 6, 9]] |2 |[0, 2]                  | 9.164771662626496 |[1.81345513574330, 1.80246819311271, 1.79148125048212] |[[0.343259574039805, 0.00439477705223728, 0.399701588466465], [0.0858148935099512, 0.00109869426305932, 0.0999253971166163], [0.343259574039805, 0.00439477705223728, 0.399701588466465]] |
	|[0.4, 0.1, 0.4] |1                |[[1, 4, 7], [2, 5, 8], [3, 6, 9]] |2 |[0, 0]                  | 3.917002965900743 |[1.67235009967665, 1.66136315704606, 1.65037621441547] |[[0.686519148079610, 0.00439477705223728, 0],[0.171629787019902, 0.00109869426305932, 0],[0.686519148079610, 0.00439477705223728, 0]]                                                     |

Scenario Outline: skipgram
    Given a skipgram function
	When it is applied to a current_center_word=<current_center_word>, window_size=<window_size>, outside_words=<outside_words>, word_2_ind=<word_2_ind>, center_word_vectors=<center_word_vectors>, outside_vectors=<outside_vectors>, and word_2_vec_loss_and_gradient=<word_2_vec_loss_and_gradient>
	Then it returns loss=<loss>, grad_center_vec=<grad_center_vec>, grad_outside_vecs=<grad_outside_vecs>

Examples: float and ndarrays
    | current_center_word | window_size | outside_words                                      | word_2_ind                               | center_word_vectors                                                                                                                                                                                      | outside_vectors                                                                                                                                                                                          | word_2_vec_loss_and_gradient  | loss | grad_center_vec | grad_outside_vecs |
    | c                   | 5           | ['d', 'a', 'e', 'e', 'd', 'b', 'c', 'd', 'b', 'd'] | {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4} | [[-0.96735714, -0.02182641, 0.25247529], [0.73663029, -0.48088687, -0.47552459], [-0.27323645, 0.12538062, 0.95374082], [-0.56713774, -0.27178229, -0.77748902], [-0.59609459, 0.7795666, 0.19221644]]   | [[-0.6831809, -0.04200519, 0.72904007], [0.18289107, 0.76098587, -0.62245591], [-0.61517874, 0.5147624, -0.59713884], [-0.33867074, -0.80966534, -0.47931635], [-0.52629529, -0.78190408, 0.33412466]]   | naiveSoftmaxLossAndGradient   |      |                 |                   |