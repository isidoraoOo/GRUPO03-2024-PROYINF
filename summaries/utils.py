import requests
from bs4 import BeautifulSoup
from newspaper import Article
from transformers import pipeline

def generar_resumen(url):
    try:
        # Extraer el contenido de la página
        article = Article(url)
        article.download()
        article.parse()

        # Inicializar el modelo de resumen
        summarizer = pipeline("summarization")

        # Generar resumen
        resumen = summarizer(article.text, max_length=150, min_length=30, do_sample=False)
        return resumen[0]['summary_text']
    except Exception as e:
        return f"Error procesando el enlace: {e}"
