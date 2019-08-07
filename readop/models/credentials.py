"""
Contains class for storing username/password pairs.
"""

from readop.utility import validator


class Credentials:
    """
    Stores credential information.
    """

    def __init__(
            self,
            username: str,
            password: str
    ):
        """
        Initializes the stored values using the provided arguments.
        
        :param username: username
        :param password: password
        """

        self.username = username
        self.password = password

    @property
    def username(self) -> str:
        """
        The username of the credentials.
        
        :getter: Returns the username.
        :setter: Sets the username.
        """

        return self.__username

    @property
    def password(self) -> str:
        """
        The password of the credentials.
        
        :getter: Returns the password.
        :setter: Sets the password.
        """

        return self.__password

    @username.setter
    def username(self, username: str) -> None:
        self.__username = validator.validate_string_not_empty(username)

    @password.setter
    def password(self, password: str) -> None:
        self.__password = validator.validate_string_not_empty(password)
