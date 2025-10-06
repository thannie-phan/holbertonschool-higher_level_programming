#!/usr/bin/python3
"""This module fetch and print or save post"""


import csv
import json
import requests


response = requests.get("https://jsonplaceholder.typicode.com/posts")


def fetch_and_print_posts():
    """fetch and print post from json placeholder"""
    print(f'Status code: {response.status_code}')
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
    else:
            print('Failed to fetch post')

def fetch_and_save_posts():
    """fetch and save post from json placeholder"""
    if response.status_code == 200:
        posts = response.json()
        posts_data = []

        for post in posts:
            one_post = {
                'id': post['id'],
                'body': post['body'],
                'title': post['title']
            }
            posts_data.append(one_post)

            with open("posts.csv", 'w') as file:
                writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
                writer.writeheader()
                writer.writerows(posts_data)

        print("Data has been writen to posts.csv")
    
    else:
        print("Failed to fetch posts")

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()


        


