ChefMate: Restaurant Clustering & AI Cooking Guide

An end-to-end Machine Learning application that combines Restaurant Recommendation, Unsupervised Clustering, AWS Cloud Services, and an AI-powered Cooking Assistant.

# Project Overview

**ChefMate** is an AI-powered restaurant recommendation and cooking assistant that combines **Machine Learning**, **Cloud Computing**, and **Conversational AI** to provide a personalized dining experience.

The application analyzes restaurant data from the **Zomato Dataset**, clusters restaurants using **unsupervised machine learning**, recommends restaurants based on user preferences, and provides an intelligent cooking assistant capable of guiding users through recipes step by step.

The complete solution is deployed as a **Streamlit web application** on **AWS Cloud**.

---

# Objectives

- Recommend restaurants based on user preferences
- Cluster restaurants using Machine Learning
- Provide restaurant insights with ratings and maps
- Integrate an AI-powered cooking assistant
- Deploy an end-to-end cloud application using AWS

---

# Tech Stack

| Category  | Technologies |
| Language  | Python |
| Framework | Streamlit |
| ML Library | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Database | AWS RDS (MySQL/PostgreSQL) |
| Cloud Storage | AWS S3 |
| Deployment | AWS EC2 |
| ORM | SQLAlchemy |
| Visualization | Plotly, Matplotlib |
| Version Control | Git & GitHub |

---

#  AWS Architecture

             Raw JSON Dataset
                     │
                     ▼
               AWS S3 Storage
                     │
                     ▼
         Data Cleaning & Preprocessing
                     │
                     ▼
             AWS RDS Database
                     │
                     ▼
           Feature Engineering
                     │
                     ▼
        Restaurant Clustering Model
                     │
                     ▼
       Recommendation Engine
                     │
                     ▼
      Streamlit Application (AWS EC2)
          │                     │
          ▼                     ▼
Restaurant Recommendation   AI Cooking Assistant

---

# Dataset

The project utilizes the **Zomato Restaurant Dataset** in JSON format.

### Features

- Restaurant ID
- Restaurant Name
- City
- Location
- Cuisine
- Cost for Two
- Price Range
- Customer Ratings
- Online Delivery
- Table Booking
- Latitude
- Longitude

---

# Project Workflow

## Data Collection

- Uploaded raw restaurant dataset to AWS S3
- Retrieved data for processing

---

## Data Preprocessing

- Removed duplicate records
- Handled missing values
- Converted JSON to structured format
- Standardized categorical variables
- Prepared features for Machine Learning

Processed data is stored in **AWS RDS**.

---

## Restaurant Clustering

Implemented **Unsupervised Machine Learning** to group similar restaurants based on:

- Cuisine
- Ratings
- Cost
- Location
- Restaurant Features
  
---

## Recommendation Engine

The recommendation engine suggests restaurants using:

- Cuisine
- Location
- Budget
- Ratings
- Dish Preferences

Each recommendation includes:

- Restaurant Details
- Ratings
- Pricing
- Interactive Maps

---

## AI Cooking Assistant

An intelligent chatbot capable of:

- Step-by-step cooking guidance
- Recipe suggestions
- Ingredient recommendations
- Cooking tips
- Conversational assistance

---

## Streamlit Dashboard

Interactive application features:

- Restaurant Search
- Cuisine Recommendations
- Restaurant Ratings
- Budget Filtering
- Interactive Maps
- AI Cooking Assistant
- Restaurant Analytics

---

## Deployment

Application deployed on **AWS EC2** with:

- Cloud-hosted Streamlit App
- Machine Learning Model
- SQL Database Integration
- Scalable Architecture


# Key Features

- AI-powered Restaurant Recommendation
- Machine Learning Clustering
- Cloud Deployment on AWS
- Interactive Streamlit Dashboard
- SQL Database Integration
- Restaurant Maps
- Conversational Cooking Assistant
- Modular Project Architecture


# Repository Structure

ChefMate-Restaurant-Clustering/
├── data/
├── notebooks/
├── models/
├── chatbot/
├── src/
│   ├── preprocessing.py
│   ├── clustering.py
│   ├── recommendation.py
│   └── database.py
│
├── streamlit_app/
│   └── app.py
│
├── screenshots/
├── requirements.txt
├── README.md
└── LICENSE

# Machine Learning Pipeline

Dataset
   >
Data Cleaning
   >
Feature Engineering
   >
Restaurant Clustering
   >
Recommendation Engine
   >
Prediction & Visualization


# Business Impact

ChefMate enables:

- Personalized restaurant discovery
- Better customer engagement
- Intelligent cooking assistance
- Data-driven restaurant insights
- Scalable cloud deployment
- Enhanced user experience


# Learning Outcomes

This project helped me gain practical experience in:

- Streamlit Application Development
- Machine Learning
- Unsupervised Clustering
- Recommendation Systems
- Data Cleaning
- Feature Engineering
- AWS Cloud (S3, RDS, EC2)
- SQL Integration
- Data Visualization
- Cloud Deployment


# Future Enhancements

- LLM-powered Recipe Assistant
- Personalized Recommendations
- Collaborative Filtering
- Voice-based Cooking Assistant
- Food Delivery API Integration
- Docker & Kubernetes Deployment
- User Authentication
- Multilingual Chatbot


# Application Screenshots

Add screenshots inside the **screenshots/** folder.

screenshots
├── home.png
├── recommendation.png
├── chatbot.png
├── dashboard.png

Example:

```markdown
## Home Page

![Home](screenshots/home.png)

## Recommendation Page

![Recommendation](screenshots/recommendation.png)
```

---

# Installation

```bash
git clone https://github.com/yourusername/ChefMate-Restaurant-Clustering.git

cd ChefMate-Restaurant-Clustering

pip install -r requirements.txt

streamlit run streamlit_app/app.py



# Keywords

Machine Learning • Restaurant Recommendation • Clustering • Streamlit • AWS • S3 • RDS • EC2 • Python • SQL • Scikit-learn • Data Visualization • Recommendation Engine • Conversational AI


# Project Highlights

✔ End-to-End Machine Learning Project

✔ Restaurant Recommendation Engine

✔ AI-powered Cooking Assistant

✔ AWS Cloud Deployment

✔ Streamlit Interactive Dashboard

✔ SQL Database Integration

✔ Scalable Cloud Architecture

✔ Portfolio-ready Data Science Project


## Author

**Shabaresh M**

Senior Technical Recruiter | Data Science Enthusiast | Machine Learning Learner
