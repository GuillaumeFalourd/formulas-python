#!/usr/bin/python3
import wikipedia

def run(keywords, language):
    wikipedia.set_lang(language)
    
    kw = wikipedia.page(keywords)
    
    print("Title:", kw.title)
    print("Url:", kw.url)
    print("Content:", kw.content)