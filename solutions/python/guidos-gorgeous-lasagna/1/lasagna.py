"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_time):
    """Calculate the bake time remaining.
    time_remaining = EXPECTED_BAKE_TIME - elapsed_time
    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    time_remaining = EXPECTED_BAKE_TIME - elapsed_time
    return time_remaining

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time for the lasagna.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        
    Returns:
        int: the total preparation time
        
    This function takes one integer representing the number of layers of lasagna to be prepped. It then calculates
    the estimated preparation time.
    """
    total = number_of_layers * PREPARATION_TIME
    return total

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time for the lasagna.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): The time the lasagna has been baking in the oven, in minutes
        
    Returns:
        int: the total elapsed time (in minutes) spent preparing and baking the lasagna.
        
    This function takes two integers representing the number of layers of lasagna to be prepped and the 
    elapsed baking time. It then calculates the total elapsed time spent cooking the lasagna.
    """
    total = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return total