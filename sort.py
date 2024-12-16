def sort(width, height, length, mass):
    """
    Sort packages into appropriate stacks based on their dimensions and mass.
    
    Args:
        width (float): Width in cm (must be positive)
        height (float): Height in cm (must be positive)
        length (float): Length in cm (must be positive)
        mass (float): Mass in kg (must be positive)
    
    Returns:
        str: "STANDARD", "SPECIAL", or "REJECTED"
    
    Raises:
        ValueError: If any input is negative
    """
    if any(dim < 0 for dim in (width, height, length, mass)):
        raise ValueError("All measurements must be positive")

    volume = width * height * length
    is_bulky = volume >= 1_000_000 or max(width, height, length) >= 150
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    return "STANDARD"
