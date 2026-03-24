# croissant-topping-reviews
Analysis of 450+ Dutch croissant topping reviews using NLP, time-of-day trend analysis, and statistical testing of topping mixture complexity.

## Overview

This project analyzes more than 450 croissant topping suggestions collected from a public promotional event hosted on a company website. The dataset was anonymized before publication to protect reviewer privacy.

The goal of the project is to extract customer preference patterns that may help cafés or food businesses understand taste segments, topping trends, and variation in review complexity.

## Data

The original dataset contained reviewer names, timestamps, and comments. In the published version, names were removed and replaced with anonymized reviewer IDs.

An additional column, `inferred_gender`, was created during preprocessing using Python's `gender.detector` library. This is a derived variable rather than a confirmed demographic label, so it includes an `unknown` category and may contain classification error.

## Main analyses

This notebook includes three main parts:

1. Time-of-day trends in sweet and savory topping preferences.
2. Gender-based differences in sweet and savory topping mentions.
3. NLP-based feature engineering for review complexity, including hypothesis testing of complexity differences between male and female reviews.

## Methods

- Text preprocessing and exploratory analysis in Python.
- NLP extraction of nouns, adjectives, and verbs.
- Topping grouping into categories such as sweet, savory, and protein-related items.
- Construction of complexity-related features from review content.
- Statistical testing using Welch’s t-test and Mann-Whitney U test.

## Key findings

- Cheese was one of the most frequently mentioned toppings in the dataset.
- Sweet and savory topping mentions showed different patterns across the hours of the day.
- Savory toppings appeared similarly common across gender groups, while sweet toppings were mentioned more often in female reviews.
- Female reviews showed significantly higher average topping-combination complexity than male reviews.

## Notes

The published dataset contains anonymized data only. The original private name column was used only during preprocessing and is not included in this repository.

The extracted nouns, adjectives, and verbs, along with their frequencies, are available in the analysis outputs. NLP processing was performed with spaCy using the `en_core_web_sm` model.
