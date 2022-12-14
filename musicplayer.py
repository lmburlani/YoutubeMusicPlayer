import tkinter as tk
from tkinter import ttk
import webbrowser
import os
from googleapiclient.discovery import build

# Sua chave API do YouTube
api_key = "YOUR_API_KEY"
youtube = build('youtube', 'v3', developerKey=api_key)

# Cria o GUI
root = tk.Tk()
root.title("YouTube Music Player")

# Criar um campo de entrada de pesquisa
search_string = tk.StringVar()
search_entry = ttk.Entry(root, width=40, textvariable=search_string)
search_entry.pack()

# Criar um botão de pesquisa
def search():
    query = search_string.get()
    response = youtube.search().list(
        part="id",
        type="video",
        q=query,
        videoDefinition="high",
        maxResults=1
    ).execute()

    # Seleciona o primeiro vídeo dos resultados da pesquisa
    video = response["items"][0]
    video_id = video["id"]["videoId"]
    video_url = f"https://www.youtube.com/watch?v={video_id}"

    # Abra o vídeo no navegador padrão
    webbrowser.open(video_url)

search_button = ttk.Button(root, text="Search", command=search)
search_button.pack()

# Executa GUI
root.mainloop()
