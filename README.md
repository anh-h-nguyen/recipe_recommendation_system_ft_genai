# 🥘 Recipe Recommendation System ft. GenAI

## Technologies Used  
- Programming Language: Python  
- Framework: Streamlit  
- AI Model: GPT-3.5 (fine-tuned for structured recipe recommendations)  
- API: OpenAI API  

## Project Overview  
Finding the right recipe can be frustrating, especially when time is limited or specific ingredients are available. This project leverages fine-tuned AI to generate personalized recipe recommendations based on user-selected ingredients, dietary needs, and cooking time constraints.  

This system makes meal planning simpler and more efficient, ensuring users receive tailored suggestions that fit their preferences without endless searching.  

## Table of Contents  
1. Introduction  
2. Features  
3. How It Works  
4. Interactive User Input  
5. Challenges & Solutions  
6. Future Improvements  

## Introduction  
This AI-powered tool creates customized recipes based on what users have available, making meal planning seamless. Instead of browsing through countless recipes online, users receive instant recommendations that match their ingredients, dietary restrictions, and time availability.  

## Features  
- Ingredient-Based Suggestions → Users enter ingredients they have, and the model generates relevant recipes.  
- Dietary Customization → Supports vegan, vegetarian, gluten-free, keto, and more dietary preferences.  
- Time-Conscious Cooking → Users specify a maximum cooking time to receive practical meal ideas.  
- Refined Prompt Engineering → Ensures AI-generated recipes align closely with user inputs for accuracy.  
- Recipe Link Extraction → Where possible, the system provides external links to full recipe instructions.  

## How It Works  
1. Users input their available ingredients.  
2. They select dietary preferences, if any.  
3. They define a maximum cooking time.  
4. The AI model processes the inputs and generates a structured recipe suggestion.  
5. The output includes step-by-step instructions and potential external recipe links.  

## Interactive User Input  
Users can:  
- Enter multiple ingredients to receive relevant recipes.  
- Select dietary preferences to filter suggestions.  
- Define a cooking time limit to ensure practical meal options.  
- Receive recipe links when available for full cooking details.  

## Challenges & Solutions  
- Slow Response Times → Optimized API calls, reduced token usage, and implemented caching for efficiency.  
- Generic AI Suggestions → Enhanced model prompts to produce more relevant recommendations.  
- Extracting Recipe Links → Developed filtering mechanisms to provide users with verified sources for cooking instructions.  

## Future Improvements  
- Recipe Personalization → Allow users to save favorites and refine future suggestions.  
- Expanded Dietary Support → Introduce additional dietary filters for inclusivity.  
- Improved Recipe Links → Ensure all generated recipes provide a direct verified source.  
- Deployment as a Public Web App → Make the tool accessible online for seamless use.  
