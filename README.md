# YandexTaxiReviewsDownloader

This Python script downloads reviews for Yandex.Taxi from Google Play, enabling analysis of user feedback. It automates fetching ratings and comments to improve app features based on real user insights. Essential for developers and marketers focused on enhancing user satisfaction and service quality.

## Overview

This document provides a detailed explanation of the configuration file for the script designed to fetch reviews for specific apps from the Google Play Store. The script uses a JSON configuration file to specify which app's reviews to fetch, filtering criteria, and other settings.

## Configuration File Example

```json
{
    "appName": "ru.yandex.taxi",
    "minVersion": "4.175.1",
    "lang": "ru",
    "country": "ru",
    "sort": "NEWEST",
    "maxReviews": 1000,
    "timeoutSeconds": 5,
    "minScore": 1,
    "maxScore": 2
}
```

## Configuration Parameters

### `appName`
- **Description**: The package name of the app for which to fetch reviews.
- **Example**: `"ru.yandex.taxi"`

...

### `timeoutSeconds`
- **Description**: The number of seconds to wait without fetching any new reviews before terminating the script.
- **Example**: `5`

### `minScore`
- **Description**: The minimum rating of reviews to fetch (inclusive). Scale is 1 to 5.
- **Example**: `1`

### `maxScore`
- **Description**: The maximum rating of reviews to fetch (inclusive). Scale is 1 to 5.
- **Example**: `2`

## Enhanced Features

### Filtering by App Version and Review Score

The script has been enhanced to filter reviews based on the version of the app they pertain to, as well as the score of the reviews. This ensures that only relevant feedback is considered, making the analysis more focused and useful.

### Writing Reviews to CSV

Filtered reviews are written to a CSV file, allowing for easy storage and further analysis. The CSV file includes details such as Review ID, UserName, UserImage, Content, Score, Thumbs Up, Review Created Version, and Timestamp.

### Handling Timeouts

The script intelligently handles timeouts to prevent hanging. If no new reviews are fetched within a specified number of seconds (`timeoutSeconds`), the script terminates, ensuring efficient operation.

## Usage

1. Ensure the JSON configuration file is named appropriately and placed in a location accessible by the script.
2. Adjust the configuration parameters according to your requirements.
3. Run the script. It will read the configuration file and fetch reviews based on the specified criteria.

## Note

- The configuration file must be valid JSON. Ensure proper syntax, especially the use of double quotes around keys and string values.
- The script's performance and the completeness of fetched reviews depend on the specified configuration and the limitations imposed by the Google Play Store's APIs and policies.

## Running the Script

To run the script, execute the following command in your terminal:

```bash
python yandex_taxi_reviews_downloader.py
```

Ensure you have installed all necessary dependencies, including `google_play_scraper`, before running the script.
