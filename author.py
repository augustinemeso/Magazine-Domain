# author.py
class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []  # List to store articles written by the author

    def add_article(self, magazine, title):
        from article import Article
        article = Article(self, magazine, title)
        magazine.add_article(article)
        self._articles.append(article)  # Add article to the author's list
        return article

    def articles(self):
        return self._articles  # Return the list of articles

    def topic_areas(self):
        return list(set(article.magazine.category for article in self._articles))  # Unique list of topics
