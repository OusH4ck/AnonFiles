#!/usr/bin/env python3

import os, sys, requests, argparse
from colorama import Fore, Back, Style

API_ENDPOINT = 'https://api.anonfiles.com/upload'

def upload_file(file_path):
    files = {'file': open(file_path, 'rb')}
    response = requests.post(API_ENDPOINT, files=files)
    return response.json()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script for uploading files to AnonFiles')
    parser.add_argument('-f', '--file', help='Path of the file to upload', required=True)
    args = parser.parse_args()

    file_path = args.file
    response = upload_file(file_path)

    if response['status']:
        file_url = response['data']['file']['url']['full']
        print(Fore.GREEN+Style.BRIGHT+'\nFile uploaded successfully!\n\n'+Fore.WHITE+Style.NORMAL+'URL: {}\n'.format(file_url))
    else:
        error_message = response['error']['message']
        print('Error uploading the file:', error_message)
