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

### `minVersion`
- **Description**: Minimum version of the app for which reviews are to be fetched. Reviews for versions older than this will be ignored.
- **Example**: `"4.175.1"`

### `lang`
- **Description**: The ISO 639-1 code of the language in which reviews should be fetched.
- **Example**: `"ru"`

### `country`
- **Description**: The ISO 3166-1 Alpha-2 code of the country from which reviews should be fetched.
- **Example**: `"ru"`

### `sort`
- **Description**: Determines the order in which reviews are fetched. Options include:
  - `"NEWEST"`: Fetches the most recent reviews first.
  - `"RATING"`: Sorts reviews by their rating, from highest to lowest.
  - `"MOST_RELEVANT"`: Sorts reviews to prioritize relevance to the current app version, based on a combination of factors.
- **Example**: `"NEWEST"`

### `maxReviews`
- **Description**: The maximum number of reviews to fetch.
- **Example**: `1000`

### `timeoutSeconds`
- **Description**: The number of seconds to wait without fetching any new reviews before terminating the script.
- **Example**: `5`

### `minScore`
- **Description**: The minimum rating of reviews to fetch (inclusive). Scale is 1 to 5.
- **Example**: `1`

### `maxScore`
- **Description**: The maximum rating of reviews to fetch (inclusive). Scale is 1 to 5.
- **Example**: `2`

## Usage

1. Ensure the JSON configuration file is named appropriately and placed in a location accessible by the script.
2. Adjust the configuration parameters according to your requirements.
3. Run the script. It will read the configuration file and fetch reviews based on the specified criteria.

## Note

- The configuration file must be valid JSON. Ensure proper syntax, especially the use of double quotes around keys and string values.
- The script's performance and the completeness of fetched reviews depend on the specified configuration and the limitations imposed by the Google Play Store's APIs and policies.
```
