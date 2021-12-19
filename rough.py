import webbrowser
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(r"C:\Program Files (x86)\Google\Update\Download\{8A69D345-D564-463C-AFF1-A69D9E530F96}\95.0.4638.69\chrome.exe"))
k=webbrowser.get('chrome')
k.open(f"https://www.google.co.in/search?q=facebook")