import csv
import json
import time
from google_play_scraper import Sort, reviews

def version_is_greater_or_equal(review_version, min_version):
    if review_version is None:
        return False
    review_version_parts = [int(part) for part in review_version.split('.')]
    min_version_parts = [int(part) for part in min_version.split('.')]
    return review_version_parts >= min_version_parts

# Loading settings from the configuration file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

min_version = config['minVersion']
app_name = config['appName']
lang = config['lang']
country = config['country']
sort = Sort[config['sort']]
max_reviews = config['maxReviews']
timeout_seconds = config.get('timeoutSeconds', 60)  # Use default value of 60 seconds if parameter is not set
min_score = config.get('minScore', 1)  # Minimum review score for filtering
max_score = config.get('maxScore', 5)  # Maximum review score for filtering

with open('reviews.csv', 'w', newline='', encoding='utf-8') as csvfile:
    review_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    review_writer.writerow(['Review ID', 'UserName', 'UserImage', 'Content', 'Score', 'Thumbs Up', 'Review Created Version', 'At'])
    count = 0
    token = None
    last_review_time = time.time()  # Remember the current time to track timeout

    while count < max_reviews:
        count_to_fetch = min(max_reviews - count, 100)
        if count_to_fetch <= 0 or time.time() - last_review_time > timeout_seconds:  # Use timeout value from config
            print("Time out: Specified seconds have passed without new reviews")
            break

        try:
            fetched_reviews, token = reviews(
                app_name,
                continuation_token=token,
                count=count_to_fetch,
                sort=sort,
                lang=lang,
                country=country
            )

            if not fetched_reviews:
                print("No more reviews to fetch.")
                break

            for review in fetched_reviews:
                # Check if version and score meet the set criteria
                if version_is_greater_or_equal(review['reviewCreatedVersion'], min_version) and min_score <= review['score'] <= max_score:
                    review_writer.writerow([review['reviewId'], review['userName'], review['userImage'], review['content'], review['score'], review['thumbsUpCount'], review['reviewCreatedVersion'], review['at']])
                    count += 1
                    last_review_time = time.time()  # Update the time of the last added review
                    print(f"Review {count}/{max_reviews} exported")
                    if count >= max_reviews:
                        break

        except Exception as e:
            print(f"An error occurred while fetching reviews: {e}")
            break

        if token is None or count >= max_reviews:  # Add a check to exit the loop
            break
