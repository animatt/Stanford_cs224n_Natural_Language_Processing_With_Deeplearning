Feature: Test PartialParse Implementation


Scenario Outline: parse_step
    Given PartialParse has stack <stack>, buffer <buffer>, dependencies <dependencies>
	When it is called with <transition>
	Then it mutates <attr> to <next_state>

Examples: state
    |stack                   |buffer                                           |dependencies |transition |next_state                                  |attr         |
	|['Root']                |['I', 'parsed', 'this', 'sentence', 'correctly'] |[]           |'S'        |['Root', 'I']                               |stack        |
	|['Root']                |['I', 'parsed', 'this', 'sentence', 'correctly'] |[]           |'S'        |[]                                          |dependencies |
	|['Root']                |['I', 'parsed', 'this', 'sentence', 'correctly'] |[]           |'S'        |['parsed', 'this', 'sentence', 'correctly'] |buffer       |
	|['Root', 'I', 'parsed'] |['this', 'sentence', 'correctly']                |[]           |'LA'       |['Root', 'parsed']                          |stack        |
	|['Root', 'I', 'parsed'] |['this', 'sentence', 'correctly']                |[]           |'LA'       |[('parsed', 'I')]                           |dependencies |
	|['Root', 'I', 'parsed'] |['this', 'sentence', 'correctly']                |[]           |'LA'       |['this', 'sentence', 'correctly']           |buffer       |

Scenario Outline: done
    Given PartialParse has stack <stack>, buffer <buffer>, dependencies <dependencies>
	When called
	Then it returns <finished>

Examples: state
    |stack           |buffer        |dependencies |finished |
    |['ROOT', 'bob'] |['something'] |[]           |False    |
	|['ROOT']        |[]            |[]           |True     |

Scenario Outline: minibatch_parse
    Given a class implementing object.predict(partial_parses) which returns <prediction>
	When it is called with sentences <sentences>, a model object, and batch_size <batch_size>
	Then it returns dependencies <dependencies>

Examples: sentences
    |sentences                         |prediction                                           |batch_size |dependencies                                                            |
	|[['I', 'am'], ['Hello', 'there']] |[['S', 'S'], ['S', 'S'], ['RA', 'RA'], ['RA', 'RA']] |2          |[[('I', 'am'), ('ROOT', 'I')], [('Hello', 'there'), ('ROOT', 'Hello')]] |
