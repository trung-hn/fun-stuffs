import json
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from bs4 import BeautifulSoup

base_url = "https://www.dicetower.com/dice-tower-reviews"
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    )
}


def generate_review_links(base_url):
    page_number = 120
    while True:
        all_page_links = []
        for _ in range(5):
            # Construct the URL for the current page
            print(f"Fetching page {page_number}...")
            url = f"{base_url}?page={page_number}"
            response = requests.get(url, headers=headers)

            if response.status_code != 200:
                print("No more pages or error fetching the page!")
                break

            soup = BeautifulSoup(response.content, "html.parser")

            # Find review links
            reviews = soup.find_all(
                "a", href=True
            )  # Replace with specific tag or class for review links
            page_links = [
                review["href"] for review in reviews if "review/" in review["href"]
            ]  # Filter for review links

            if not page_links:
                print(f"No links found on page {page_number}. Skipping.")
                page_number += 1
                continue

            all_page_links.extend(page_links)
            page_number += 1

        # Yield all links from the 5 pages as a list
        if all_page_links:
            yield all_page_links
        else:
            break


def get_reviewers_and_scores(url):
    """
    Fetch a list of reviewers and their scores from the given URL.

    Args:
        url (str): URL of the page to scrape.

    Returns:
        list: A list of dictionaries with reviewer names and their scores.
    """
    reviewers_and_scores = []

    try:
        response = requests.get(f"https://www.dicetower.com{url}")
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            title = soup.find(
                class_="ReviewVideo__title"
            ).text.strip()  # Find the h4 inside the class
            name_elements = soup.find_all(
                class_="DicePeople__name"
            )  # Class for reviewer names
            score_elements = soup.find_all(class_="rating")  # Class for ratings

            for name, score in zip(name_elements, score_elements):
                reviewers_and_scores.append(
                    {"name": name.text.strip(), "score": score.text.strip()}
                )
        else:
            print(f"Failed to fetch {url}, status code: {response.status_code}")
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return {}
    return {title: reviewers_and_scores}


def process_urls_in_parallel(url_list, max_workers=16):
    """
    Process a list of URLs in parallel and fetch reviewers and scores for each.

    Args:
        url_list (list): List of URLs to process.
        max_workers (int): Number of worker threads to use.

    Returns:
        dict: A dictionary containing all results.
    """
    results = {}

    # Create a ThreadPoolExecutor with a fixed number of workers
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit tasks for each URL
        future_to_url = {
            executor.submit(get_reviewers_and_scores, url): url for url in url_list
        }

        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                result = future.result()
                if result:
                    results.update(result)
            except Exception as e:
                print(f"Error processing URL {url}: {e}")

    return results


def load_existing_results(filename="reviews.json"):
    """Load existing results from a file if it exists."""
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return {}  # Return an empty dictionary if the file doesn't exist


def save_results_to_file(results, filename="reviews.json"):
    """Save results to a file in JSON format."""
    with open(filename, "w") as file:
        json.dump(results, file, indent=4)


# Load existing results
results = load_existing_results()
for links in generate_review_links(base_url):
    new_results = process_urls_in_parallel(links)
    print(f"Saving {len(new_results)} new results to file...")
    results.update(new_results)
    save_results_to_file(results)
