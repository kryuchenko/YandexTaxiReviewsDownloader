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
timeout_seconds = config.get('timeoutSeconds', 60)  # Используем значение по умолчанию 60 секунд, если параметр не задан
min_score = config.get('minScore', 1)  # Минимальная оценка отзывов для фильтрации
max_score = config.get('maxScore', 5)  # Максимальная оценка отзывов для фильтрации

with open('reviews.csv', 'w', newline='', encoding='utf-8') as csvfile:
    review_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    review_writer.writerow(['Review ID', 'UserName', 'UserImage', 'Content', 'Score', 'Thumbs Up', 'Review Created Version', 'At'])
    count = 0
    token = None
    last_review_time = time.time()  # Запоминаем текущее время для отслеживания тайм-аута

    while count < max_reviews:
        count_to_fetch = min(max_reviews - count, 100)
        if count_to_fetch <= 0 or time.time() - last_review_time > timeout_seconds:  # Используем значение тайм-аута из конфига
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
                # Проверяем соответствие версии и оценки установленным критериям
                if version_is_greater_or_equal(review['reviewCreatedVersion'], min_version) and min_score <= review['score'] <= max_score:
                    review_writer.writerow([review['reviewId'], review['userName'], review['userImage'], review['content'], review['score'], review['thumbsUpCount'], review['reviewCreatedVersion'], review['at']])
                    count += 1
                    last_review_time = time.time()  # Обновляем время последнего добавленного отзыва
                    print(f"Review {count}/{max_reviews} exported")
                    if count >= max_reviews:
                        break

        except Exception as e:
            print(f"An error occurred while fetching reviews: {e}")
            break

        if token is None or count >= max_reviews:  # Добавляем проверку для выхода из цикла
            break
