def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculate BMI for each pair of height and weight values from two lists.

    Parameters:
    - height (list[int | float]): List of heights.
    - weight (list[int | float]): List of weights.

    Returns:
    - list[int | float]: List of BMI values calculated for each height-weight
      pair.

    Raises:
    - ValueError: If the two input lists do not have the same length.
    - ValueError: If any element in the input lists is not of type int
    or float.
    """

    if len(height) != len(weight):
        raise ValueError("The two lists must have the"
                         " same length.")

    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise ValueError("All elements in the lists should be"
                             " of type int or float.")

    bmi_list = [w / h ** 2 for h, w in zip(height, weight)]
    return bmi_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Check if each BMI value in the list exceeds a given limit.

    Parameters:
    - bmi (list[int | float]): List of BMI values.
    - limit (int): The limit value against which BMI values are checked.

    Returns:
    - list[bool]: List indicating if each BMI value exceeds the limit.

    Raises:
    - ValueError: If any element in the BMI list is not of type int or float.
    - ValueError: If the limit is not of type int.
    """

    for b in bmi:
        if not isinstance(b, (int, float)):
            raise ValueError("All elements in the BMI list should be"
                             " of type int or float.")
    if not isinstance(limit, int):
        raise ValueError("Limit should be of type int.")

    bmi_limits = [i > limit for i in bmi]
    return bmi_limits
