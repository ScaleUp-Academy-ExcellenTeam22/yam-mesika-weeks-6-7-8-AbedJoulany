import string
from typing import Tuple, Union, Literal

_FILE_TYPE = Union['Directory', 'TextualFile', 'BinaryFile']
_TYPES = Literal["binary", "txt", "directory"]


class User:
    """ User class. includes a user name and password.
    :ivar str username: user name
    :ivar str password: password.
    :param username: passed username.
    :param password: passed password.
    """
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self) -> str:
        return self.username

    def create_file(self, filename: str = '', content: str = '', filetype: _TYPES = 'txt') -> _FILE_TYPE:
        """
        :param str filename: the file name
        :param str content: file content
        :param str filetype: file type
        :return File : created file
        """
        if filetype == "directory":
            return Directory(filename)
        elif filetype == "binary":
            return BinaryFile(filename, content, self)
        elif filetype == "txt":
            return TextualFile(filename, content, self)


class SystemAdmin (User):
    """
        system admin class inheriting from user
    """
    def __init__(self, username: str, password: str):
        super ().__init__ (username, password)


class RegularUser (User):
    """
       regular user class inheriting from user
    """
    def __init__(self, username: str, password: str):
        super ().__init__ (username, password)


class File:
    """ a class that represents a file
    :ivar str filename: filename
    :param str filename: passed filename
    """
    def __init__(self, filename: str):
        self.filename = filename

    def rename(self, name: str = "") -> None:
        """ Rename the file.
        :param name: The new name.
        :return: None.
        """
        self.filename = name

    def __str__(self) -> str:
        return self.filename


class Directory (File):
    """ a class that represents a directory inherit2ing from user
        :ivar list file_list: list that include files
        :param list filename: passed filename
    """
    def __init__(self, filename: str):
        super ().__init__ (filename)
        self.file_list = []

    def add_file(self, file: _FILE_TYPE) -> None:
        try:
            if file in self.file_list:
                raise RuntimeError (f"file: {file} is already in directory.")
            else:
                self.file_list.append (file)
        except RuntimeError as error:
            print (error)

    def remove_file(self, file):
        try:
            self.file_list.remove (file)
        except ValueError as error:
            print (error)


class ReadAbleFile (File):
    """ a class that represents a directory inherit2ing from user
        :ivar str content: file content
        :ivar float size: the weight of the file
        :ivar User user: the creator user
        :param list filename: passed filename
        :param str content: passed content
        :param User user: passed User
    """

    def __init__(self, filename: str, content: str, user: User):
        super ().__init__ (filename)
        self.content = content
        self.size = len (self.content.encode ('utf-8'))
        self.user = user

    def read(self, user: User) -> Union[str, None]:
        """
        :param User user: user that wants to reach file content
        :return: file content or None
        """
        return self.content if isinstance (user, SystemAdmin) or user.username == user.username else None


class TextualFile (ReadAbleFile):
    """ textual file class inherits from ReadAbleFile"""
    def __init__(self, filename, content, user):
        super ().__init__ (filename, content, user)

    def count(self, my_string: str) -> int:
        """
        function to count a string within the file content
        :param str my_string: the search string
        :return int: count of appearances
        """
        return self.content.lower ().count (my_string.lower ())


class BinaryFile (ReadAbleFile):
    """ binary file class inherits from ReadAbleFile"""
    def __init__(self, filename, content, user):
        super ().__init__ (filename, content, user)

    def get_dimensions(self) -> Tuple[float, float]:
        """
        function that return the picture dimensions.
        :return tuple: Width and height.
        """
        pass


if __name__ == '__main__':
    admin = SystemAdmin ('admin', 'admin')
    print('admin created')
    regular_user = RegularUser ('user1', 'user1')
    print('regular user created')
    home_dir = admin.create_file(filename="Home", filetype="directory")
    print('home directory created')
    file1 = regular_user.create_file('hello','hello world1, hello world2','txt')
    print('file1 created by regular_user')
    home_dir.add_file(file1,)
    print('file1 added to home dir')
    print('count hello in file1', file1.count('hello'))
