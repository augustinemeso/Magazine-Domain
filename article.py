# article.py
class Article:
    def __init__(self, author, magazine, title):
        from author import Author
        from magazine import Magazine

        if not isinstance(author, Author) or not isinstance(magazine, Magazine):
            raise Exception("Invalid author or magazine")
        self.author = author
        self.magazine = magazine
        self.set_title(title)

    def set_title(self, title):
        if len(title) < 5:  # Title must be at least 5 characters
            raise Exception("Title must be at least 5 characters long.")
        if len(title) > 50:  # Title must be no longer than 50 characters
            raise Exception("Title must be no longer than 50 characters.")
        self._title = title  # Use internal variable to store the title

    @property
    def title(self):
        return self._title  # Return the internal title value

    @title.setter
    def title(self, value):
        self.set_title(value)  # Use the set_title method to validate the title
