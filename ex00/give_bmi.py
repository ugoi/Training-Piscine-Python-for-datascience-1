def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    if len(height) != len(weight):
        raise ValueError("The two lists must have the same length.")
    
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise ValueError("All elements in the lists should be of type int or float.")
    
    bmi_list = [w / h ** 2 for h, w in zip(height, weight)]
    return bmi_list

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    for b in bmi:
        if not isinstance(b, (int, float)):
            raise ValueError("All elements in the BMI list should be of type int or float.")
    if not isinstance(limit, int):
        raise ValueError("Limit should be of type int.")
    
    bmi_limits = [i > limit for i in bmi]
    return bmi_limits
