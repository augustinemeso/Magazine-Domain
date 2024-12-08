# magazine.py
class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []

    def add_article(self, article):
        from article import Article  # Local import to avoid circular imports

        if not isinstance(article, Article):
            raise Exception("Invalid article")
        self._articles.append(article)

    def articles(self):
        return self._articles  # Return the list of articles

    def contributors(self):
        from author import Author
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return [article.title for article in self._articles]
