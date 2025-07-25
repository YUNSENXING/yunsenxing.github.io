with open('index.html', 'r+') as f:
    html = f.read()
    if '<link rel="icon"' not in html:
        html = html.replace('<head>', '<head>\n<link rel="icon" href="photos/icon.png">')
    f.seek(0)
    f.write(html)
    f.truncate()
