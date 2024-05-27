class BooksListCsvStorage:
    def __init__(self, file_name, field_separator, line_separator):
        self.file_name = file_name
        self.field_separator = field_separator
        self.line_separator = line_separator

    def write(self, books):
        try:
            with open(self.file_name, "w") as output:
                output.write(self._build_header() + self.line_separator)
                for book in books:
                    output.write(self._build_line(book) + self.line_separator)
        except Exception as ex:
            print(f'Error writing file {ex}')
        finally:
            output.close()

    def _build_header(self):
        return self.field_separator.join(['Title', 'Price', 'Rating', 'Availability'])

    def _build_line(self, book):
        return self.field_separator.join([
            self._build_field(book.title),
            self._build_field(book.price),
            self._build_field(book.rating),
            self._build_field(book.availability)
        ])

    def _build_field(self, value):
        return value.replace(self.field_separator, self.field_separator + self.field_separator)