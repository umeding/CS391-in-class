# --- Function WITH Docstring ---

def calculate_rectangle_area(length, width):
    """Calculates the area of a rectangle.

    Provides a warning and returns None if dimensions are non-positive.

    Args:
        length (int | float): The length of the rectangle. Must be numeric.
        width (int | float): The width of the rectangle. Must be numeric.

    Returns:
        float | int | None: The calculated area (length * width) if inputs
        are positive numeric values. Returns None if either length or
        width is zero or negative.

    Raises:
        TypeError: If either length or width is not an integer or float.
    """
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Both length and width must be numeric.")
    if length <= 0 or width <= 0:
        # Using print isn't ideal for libraries, but okay for simple example
        print("Warning: Dimensions must be positive for a valid area.")
        return None
    return length * width
