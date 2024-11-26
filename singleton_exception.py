# CPSC 8700
# Fall 2024
# Robert Taylor, Emily Port, Daniel Scarnavack
# Final Project
class SingletonException(Exception):
    """Singleton Exception"""
    def __init__(self, message):
        # Call the base class constructor
             # with the parameters it needs
        super().__init__(message)
