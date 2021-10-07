import numpy


def apply_thresholds(input, thresholds, choices):
    """
    Return one of the choices depending on the input position compared to thresholds, for each input.

    Examples:
        >>> input = numpy.array([4, 5, 6, 7, 8])
        >>> thresholds = [5, 7]
        >>> choices = [10, 15, 20]
        >>> apply_thresholds(input, thresholds, choices)
        array([10, 10, 15, 15, 20])

    """

    condlist = [input <= threshold for threshold in thresholds]
    if len(condlist) == len(choices) - 1:
        # If a choice is provided for input > highest threshold, last condition must be true to return it.
        condlist += [True]
    assert len(condlist) == len(choices), \
        "apply_thresholds must be called with the same number of thresholds than choices, or one more choice"
    return numpy.select(condlist, choices)


def concat(this, that):
    """

    Examples:
        >>> this = ["this", "that"]
        >>> that = numpy.array([1, 2.5])
        >>> concat(this, that)
        array(['this1.0', 'that2.5']...)

    """

    if isinstance(this, numpy.ndarray) and not numpy.issubdtype(this.dtype, numpy.str):
        this = this.astype('str')
    if isinstance(that, numpy.ndarray) and not numpy.issubdtype(that.dtype, numpy.str):
        that = that.astype('str')

    return numpy.core.defchararray.add(this, that)


def switch(conditions, value_by_condition):
    '''
    Reproduces a switch statement: given an array of conditions, return an array of the same size replacing each
    condition item by the corresponding given value.

    Examples:
        >>> conditions = numpy.array([1, 1, 1, 2])
        >>> value_by_condition = {1: 80, 2: 90}
        >>> switch(conditions, value_by_condition)
        array([80, 80, 80, 90])

    '''

    assert len(value_by_condition) > 0, \
        "switch must be called with at least one value"
    condlist = [
        conditions == condition
        for condition in value_by_condition.keys()
        ]
    return numpy.select(condlist, value_by_condition.values())