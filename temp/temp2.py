from langchain_community.document_loaders import WebBaseLoader
import bs4  # BeautifulSoup for parsing HTML
from langchain_community.document_loaders.text import TextLoader

loader = WebBaseLoader(
    web_paths=("https://lt.wikipedia.org/wiki/Vilnius",),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer()
    ),
)
wiki = loader.load()






MEMORY_FILE = "Vilnius.txt"


text_loader = TextLoader(MEMORY_FILE, encoding="utf-8")
content = text_loader.load()





loader = WebBaseLoader(
    web_paths=("https://faktograma.lt/faktu-rinkinys-6-faktai-apie-vilniu/",),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer()
    ),
)
faktograma = loader.load()

# all_info = wiki + content + faktograma

all_info = wiki + content + faktograma

print(f"Type of wiki: {type(wiki)}")
print(f"Type of content: {type(content)}")
print(f"Type of faktograma: {type(faktograma)}")