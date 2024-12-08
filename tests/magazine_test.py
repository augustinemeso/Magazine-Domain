import pytest
from article import Article
from author import Author
from magazine import Magazine

def test_magazine_creation():
    magazine = Magazine("Fashion Monthly", "Fashion")
    
    # Assertions to verify Magazine creation
    assert magazine.name == "Fashion Monthly"
    assert magazine.category == "Fashion"

def test_add_article_to_magazine():
    author = Author("Emma Stone")
    magazine = Magazine("Tech Today", "Technology")
    
    # Create an article and add it to the magazine
    article = Article(author, magazine, "Tech Innovations")
    
    magazine.add_article(article)
    
    # Assertions
    assert len(magazine.articles()) == 1
    assert article in magazine.articles()

def test_magazine_contributors():
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")
    magazine = Magazine("Tech Weekly", "Technology")
    
    # Add articles by authors
    author1.add_article(magazine, "Tech Trends")
    author2.add_article(magazine, "Gadget Reviews")
    
    # Check unique contributors
    contributors = magazine.contributors()
    assert len(contributors) == 2
    assert author1 in contributors
    assert author2 in contributors

def test_magazine_article_titles():
    author = Author("Mark Twain")
    magazine = Magazine("Science Digest", "Science")
    
    # Add articles
    author.add_article(magazine, "Quantum Physics")
    author.add_article(magazine, "Astrophysics Breakthroughs")
    
    titles = magazine.article_titles()
    assert "Quantum Physics" in titles
    assert "Astrophysics Breakthroughs" in titles
    assert len(titles) == 2
