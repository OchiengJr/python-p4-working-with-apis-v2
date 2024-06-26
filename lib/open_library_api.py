import requests
import json


class Search:
    def __init__(self):
        self.base_url = "https://openlibrary.org/search.json"
        self.fields = ["title", "author_name"]
        self.limit = 1

    def get_search_url(self, search_term):
        search_term_formatted = search_term.replace(" ", "+")
        fields_formatted = ",".join(self.fields)
        return f"{self.base_url}?title={search_term_formatted}&fields={fields_formatted}&limit={self.limit}"

    def get_search_results(self, search_term="the lord of the rings"):
        url = self.get_search_url(search_term)
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            response.raise_for_status()

    def get_search_results_json(self, search_term="the lord of the rings"):
        url = self.get_search_url(search_term)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_user_search_results(self, search_term):
        try:
            response_json = self.get_search_results_json(search_term)
            if response_json['docs']:
                result = response_json['docs'][0]
                response_formatted = f"Title: {result['title']}\nAuthor: {result['author_name'][0]}"
                return response_formatted
            else:
                return "No results found."
        except (requests.exceptions.RequestException, IndexError, KeyError) as e:
            return f"An error occurred: {e}"


if __name__ == "__main__":
    search_term = input("Enter a book title: ")
    result = Search().get_user_search_results(search_term)
    print("Search Result:\n")
    print(result)
