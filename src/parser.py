import requests
from bs4 import BeautifulSoup
from src.database import DatabaseRepository


class Parser:
    def __init__(self, db_repository):
        self.db_repository = db_repository
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    def parse_page(self, url: str) -> list:
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        parser_results = []
        posts = soup.find_all('div', class_='post')  

        for post in posts:
            post_id = post.get('data-id')
            name_tag = post.find('h2', class_='name')
            message_tag = post.find('p', class_='message')
            if post_id and name_tag and message_tag:
                name = name_tag.get_text(strip=True)
                message = message_tag.get_text(strip=True)
                parser_results.append({
                    'id': int(post_id),
                    'name': name,
                    'message': message
                })

        return parser_results

    def save_to_db(self, parsed_data: list, repository: DatabaseRepository) -> None:
        for item in parsed_data:
            try:
                repository.add(item['id'], item['name'], item['message'])
            except Exception as e:
                print(f"Error saving item {item['id']}: {e}")