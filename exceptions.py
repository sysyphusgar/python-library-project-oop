class LibraryError(Exception):
    pass

class LoanLimitError(LibraryError):
    pass

class InvalidTitleError(LibraryError):
    pass

class NoAvailableBookError(LibraryError):
    pass

class NoAvailableUserError(LibraryError):
    pass