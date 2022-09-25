#!/usr/bin/python3.6

import os 

def discover(initial_path):
    
    extensions = [
    # 'exe', 'dll', 'so', 'rpm', 'deb', 'vmlinuz', 'img', # Arquivos do Sistema
    'jpg', 'jpeg', 'tmp', 'gif', 'png', 'svg', 'psd', 'raw', # imagens
    'mp3', 'mp4', 'm4a', 'aac', 'ogg', 'flac', 'wav', 'wma', 'aiff', 'ape', #audios
    'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp', #videos
    'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', #microsoft office
    # OpenOffice, Adobe, Latex, Markdown, etc
    'odt', 'odp', 'ods', 'txt', 'rtf', 'text', 'pdf', 'epub', 'md'
    'yml', 'yaml', 'json', 'xml', 'csv', #dados estruturados e config
    'db', 'sql', 'dbf', 'mdb', 'iso', #banco de dados e imagens de disco
    'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css', #tecnologias web
    'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx', #codigo-fonte c/c++
    'java', 'class', 'jar', #codigo-fonte java
    'ps', 'bat', 'vb', #scripts windows
    'awk', 'sh', 'cgi', 'pl', 'ada', 'swift', #scripts *nix
    'go', 'py', 'pyc', 'bf', 'coffee', #outras linguagens
    'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak', #arquivos compactados

    ]
    
    for dirpath, dirs, files in os.walk(initial_path):
        for _file in files:
            absolute_path = os.path.abspath(os.path.join(dirpath, _file))
            ext = absolute_path.split('.')[-1]
            if ext in extensions:
                yield absolute_path

#só é executado se você excutar o modulo diretamente

if __name__ == '__main__':
    x = discover(os.getcwd())
    for i in x:
        print(i)







    