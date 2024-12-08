import pytest
from article import Article
from author import Author
from magazine import Magazine

def test_article_creation():
    # Create an Author and a Magazine for testing
    author = Author("John Doe")
    magazine = Magazine("Tech Magazine", "Technology")
    
    # Create an article
    article = Article(author, magazine, "How to Code")
    
    # Assertions to verify Article creation
    assert article.title == "How to Code"
    assert article.author == author
    assert article.magazine == magazine

def test_article_title():
    author = Author("Jane Smith")
    magazine = Magazine("Health Weekly", "Health")
    article = Article(author, magazine, "Health Tips")
    
    # Test title constraints
    with pytest.raises(Exception):
        article.title = "Hi"  # Too short

    with pytest.raises(Exception):
        article.title = "T" * 51  # Too long

    # Correct title
    article.title = "Healthy Living"
    assert article.title == "Healthy Living"
