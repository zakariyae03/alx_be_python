class Book:
    def __init__(self, title, author, year):
        """
        Constructor to initialize a Book instance.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor to print a message when the object is deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String representation of the Book instance.
        """
        return f"{self.title
