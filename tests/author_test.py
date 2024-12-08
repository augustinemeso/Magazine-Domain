import pytest
from article import Article
from author import Author
from magazine import Magazine

def test_author_creation():
    author = Author("John Doe")
    
    # Assertions to verify Author creation
    assert author.name == "John Doe"

def test_add_article_to_author():
    author = Author("Jane Smith")
    magazine = Magazine("Tech Monthly", "Technology")
    
    # Create an article and add it to the author
    article = author.add_article(magazine, "AI Advances")
    
    assert len(author.articles()) == 1
    assert article in author.articles()
    assert article.title == "AI Advances"
    assert article.author == author
    assert article.magazine == magazine

def test_author_topic_areas():
    author = Author("Mark Lee")
    magazine1 = Magazine("Science World", "Science")
    magazine2 = Magazine("Tech Today", "Technology")
    
    author.add_article(magazine1, "Space Exploration")
    author.add_article(magazine2, "AI Breakthroughs")
    
    # Test for unique categories
    assert "Science" in author.topic_areas()
    assert "Technology" in author.topic_areas()
    assert len(author.topic_areas()) == 2
