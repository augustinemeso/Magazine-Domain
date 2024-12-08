# debug.py
import logging
from article import Article
from author import Author
from magazine import Magazine

# Set up logging for debug output
logging.basicConfig(level=logging.DEBUG)

def debug_article_creation():
    logging.debug("Creating an article and inspecting it...")
    
    # Create an Author and Magazine
    author = Author("Jane Doe")
    magazine = Magazine("Tech Today", "Technology")
    
    # Create an Article
    article = Article(author, magazine, "The Future of AI")
    
    # Debugging output
    logging.debug(f"Article title: {article.title}")
    logging.debug(f"Article author: {article.author.name}")
    logging.debug(f"Article magazine: {article.magazine.title}")
    
    # Inspect the article object itself
    logging.debug(f"Article object: {vars(article)}")
    
    # Checking article state
    article.publish()
    logging.debug(f"Article published: {article.published}")
    
    # Add contributor and log it
    new_author = Author("John Smith")
    article.add_contributor(new_author)
    logging.debug(f"Article contributors: {[author.name for author in article.contributors]}")

def debug():
    # Running all the debugging functions
    logging.debug("Starting Debugging Script...")
    
    # Debugging article creation
    debug_article_creation()

# This ensures the script can be run independently and also be imported
if __name__ == "__main__":
    debug()
