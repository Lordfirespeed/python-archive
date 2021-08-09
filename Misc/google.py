import webbrowser


def search(query):
    url = "https://www.google.com.tr/search?q={}".format(query)
    webbrowser.open_new_tab(url)

