from core.xml_mod import CustomElement


class BookModel(CustomElement):
    def __init__(self, tag, attrs=None, value=None):
        super().__init__(tag, attrs, value)


class MainModel(CustomElement):
    def __init__(self, tag, books, title, attrs=None, value=None):
        super().__init__(tag, attrs, value)
        self.books = books
        self.title = title
