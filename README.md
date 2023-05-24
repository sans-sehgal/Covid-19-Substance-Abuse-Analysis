# Covid-19-Substance-Abuse-and-Resource-Prediction

This repository contains the code and data for the project "Defending Against A Pandemic - The Fight for Survival." The project aims to assess the impact of the COVID-19 pandemic on public health, with a focus on substance abuse and mental health issues. Additionally, it provides a forecasting model to predict hospital bed and staffing deficits, contributing to preparedness for future pandemics. The project aligns with the United Nations Sustainable Development Goal 3, which aims to ensure healthy lives and promote well-being for all.

## Background
The COVID-19 pandemic has had a significant impact on global public health, leading to increased stress, anxiety, and social isolation. This project addresses concerns regarding substance abuse and mental health issues during the pandemic. By analyzing data from Reddit and COVID-19 hospital occupancy, the project quantifies the surge in substance abuse, correlates it with COVID-19 cases, and forecasts hospital bed and staffing deficits.

## Methodologies
The project utilizes various methodologies and frameworks, including sentiment analysis, frequency analysis, and time series analysis. The following frameworks and models are employed:

- Sentiment Analysis:
  - Frameworks: Pyspark, PyTorch
  - Model: XLNet (Transformer)

- Frequency Analysis:
  - Frameworks: PyTorch, NLTK

- Time Series Analysis:
  - Models: ARIMA, 
  - Frameworks: sklearn, stat_models

Understanding the United Nations Sustainable Development Goals, particularly SDG 3 related to healthcare, is crucial to comprehending the significance of the project's methodologies.

## Data
The repository contains two datasets used for analysis:

1. Sentiment Analysis Dataset:
   - Reddit COVID Dataset: Size - 14GB
   - Weekly Prevalence of COVID in the US: Size - 5MB

2. Time Series Analysis Dataset:
   - COVID-19 Reported Patient Impact and Hospital Capacity: Size - 50MB

The datasets provide information on Reddit posts related to mental health and substance abuse, COVID-19 cases, and hospital utilization. Descriptive statistics and labels (where applicable) are included in the datasets.

## Methodology
The project follows three main methodologies:

### 1. Sentiment Analysis
The sentiment analysis involves preprocessing the Reddit data, combining existing datasets, and scraping additional data using Reddit's APIs. The XLNet model is employed for classifying posts into severity score classes. Several other models were evaluated, and AIMH/mental-xlnet-base-cased model was found to be the most accurate.

### 2. Frequency Analysis
The frequency analysis focuses on keywords related to mental health and substance abuse. The project analyzes the frequency of these keywords in subreddits before and during the COVID-19 pandemic.

### 3. Time Series Analysis
The time series analysis utilizes COVID-19 hospital bed occupancy data for forecasting bed availability. The ARIMA model is applied to detect trends and patterns in the data and forecast future bed availability. The model is trained on a portion of the data and tested against the remaining data to evaluate its performance.

## Results
The project presents several key results:

1. Sentiment Analysis Results:
   - Categorized posts into severity classes and plotted their distribution over time.
   - Correlated the number of COVID-19 cases with the frequency of posts in each severity class.

2. Frequency Analysis Results:
   - Plots depicting the usage of keywords related to mental health and substance abuse compared to COVID-19 cases over time.

3. ARIMA Forecast Output:
   - Predictions for inpatient and ICU bed availability from March 2023 to mid-May 2023.
   - Comparison of the forecasted values with the actual values, demonstrating the model's performance.

## Conclusion
The project contributes to improving healthcare outcomes during pandemics by providing insights into substance abuse and mental health issues. The sentiment analysis identifies correlations between COVID-19 cases and post severity, while the time series analysis accurately forecasts hospital bed availability. The project aligns with the United Nations Sustainable Development Goal 3 and aims to prepare for future pandemics and improve mental health outcomes.

## References
1. Impact of COVID on Mental Health: [Link](https://www.covidminds.org/)
2. WHO Data: [Link](https://www.who.int/data/gho)
3. Mental Health During the COVID-19 Pandemic: [Link](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0277562)
4. XLNet Paper: [Link](https://arxiv.org/abs/1906.08237)
5. Reddit COVID Dataset: [Link](https://www.kaggle.com/datasets/pavellexyr/the-reddit-covid-dataset)
6. COVID-19 Reported Patient Impact and Hospital Capacity Dataset
7. COVID Prevalence in the US Dataset
8. ARIMA Model: [Link](https://www.researchgate.net/publication/328633706_Fore)

Please refer to the specific files in this repository for more detailed information on the implementation and analysis of the project.
