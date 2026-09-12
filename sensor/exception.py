import sys

"""
Custom exception handling for the LiveSensor project.

This module provides a custom exception class, `SensorException`,
which captures useful debugging information such as:

    - The file where the exception occurred
    - The line number where the exception occurred
    - The original error message

Example:
    try:
        result = 10 / 0

    except Exception as e:
        raise SensorException(e, sys)
"""



class SensorException(Exception):
    """
    Custom exception class for the LiveSensor project.

    This exception extends Python's built-in `Exception` class and
    provides additional information about where an error occurred.

    Attributes:
        error_message (str): Detailed error message containing the
            file name, line number, and original exception message.

    Example:
        >>> try:
        ...     x = 10 / 0
        ... except Exception as e:
        ...     raise SensorException(e, sys)
    """

    def __init__(
        self,
        error_message: Exception,
        error_detail: sys
    ):
        """
        Initialize the SensorException.

        Args:
            error_message (Exception):
                The original exception that was raised.

            error_detail (sys):
                The `sys` module used to retrieve exception
                traceback information.
        """

        # Initialize the parent Exception class with the original
        # exception message.
        super().__init__(error_message)

        # Generate a detailed error message containing the
        # file name and line number where the error occurred.
        self.error_message = self.get_detailed_error_message(
            error_message=error_message,
            error_detail=error_detail
        )

    @staticmethod
    def get_detailed_error_message(
        error_message: Exception,
        error_detail: sys
    ) -> str:
        """
        Generate a detailed error message.

        The traceback information is extracted from the `sys` module
        to identify the file and line number where the exception
        occurred.

        Args:
            error_message (Exception):
                The original exception.

            error_detail (sys):
                The `sys` module used to retrieve traceback details.

        Returns:
            str:
                A formatted error message containing the file name,
                line number, and original error message.
        """

        # Get the current exception traceback.
        _, _, exc_tb = error_detail.exc_info()

        # Get the name of the Python file where the exception occurred.
        file_name = exc_tb.tb_frame.f_code.co_filename

        # Get the line number where the exception occurred.
        line_number = exc_tb.tb_lineno

        # Construct a detailed error message.
        detailed_error_message = (
            f"Error occurred in script: [{file_name}] "
            f"at line number: [{line_number}] "
            f"with error message: [{error_message}]"
        )

        return detailed_error_message

    def __str__(self) -> str:
        """
        Return the detailed error message as a string.

        Returns:
            str:
                The detailed error message containing the file name,
                line number, and original exception message.
        """

        return self.error_message