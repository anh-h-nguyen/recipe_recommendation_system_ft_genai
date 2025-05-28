# Import libraries
import ast
import streamlit as st
import openai
import os

# Set OpenAI API key from Streamlit secrets
os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']

# Initialize OpenAI client using the API key from environment variables
client = openai.OpenAI(api_key=os.environ['OPENAI_API_KEY'])

# Function to format recipe output properly
def format_recipe(response_text):
    # Ensure key sections are on separate lines
    response_text = response_text.replace("Recipe ID:", "\nRecipe ID:")
    response_text = response_text.replace("Ingredients:", "\nIngredients:")
    response_text = response_text.replace("Cooking Time:", "\nCooking Time:")
    response_text = response_text.replace("Steps:", "\nSteps:\n")

    # Remove duplicate cooking time
    lines = response_text.split("\n")
    cleaned_lines = []
    seen_cooking_time = False
    for line in lines:
        if "Cooking Time:" in line:
            if seen_cooking_time:
                continue 
            seen_cooking_time = True
        cleaned_lines.append(line)
    
    response_text = "\n".join(cleaned_lines)

    # Format ingredients as a bullet-point list
    if "Ingredients:" in response_text:
        parts = response_text.split("Ingredients:")
        ingredients_section = parts[1].strip()
        ingredients_list = ingredients_section.split("; ") 
        bullet_ingredients = "\n- " + "\n- ".join(ingredients_list) 
        response_text = parts[0] + "Ingredients:" + bullet_ingredients

    # Fix steps formatting if enclosed in brackets
    if "Steps:\n[" in response_text:
        try:
            raw_steps = eval(response_text.split("Steps:\n")[1].strip()) 
            formatted_steps = "\n".join([f"{idx+1}. {step.strip()}" for idx, step in enumerate(raw_steps)])
            response_text = response_text.replace(str(raw_steps), formatted_steps)
        except Exception as e:
            print("Error formatting steps:", e)
    
    return response_text

# Function to retrieve recipe from OpenAI API
def get_recipe(ingredients, dietary_restriction, max_time):
    prompt = f"Suggest a recipe using {ingredients}. "
    if dietary_restriction:
        prompt += f"The recipe should be {dietary_restriction}. "
    if max_time:
        prompt += f"It should take no more than {max_time} minutes to prepare."

    response = client.chat.completions.create(
        model="ft:gpt-3.5-turbo-0125:personal::BViYBdjc",
        messages=[
            {"role": "system", "content": 
             "You are a recipe assistant. ALWAYS return responses in this format:\n\n"
             "Recipe Title: [Title]\n"
             "Recipe ID: [ID]\n"
             "Ingredients: [List of Ingredients]\n"
             "Cooking Time: [Minutes]\n"
             "Steps:\n"
             "1. [Step 1]\n"
             "2. [Step 2]\n"
             "3. [Step 3]\n"
             "4. [Step 4]"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=400
    )

    recipe_text = response.choices[0].message.content

    return format_recipe(recipe_text)  # Ensure properly formatted output

# Streamlit UI setup
st.title("ChefGPT 🍽️")
st.write("Tell me what ingredients you have, any dietary preferences, and how much time you have!")

# User inputs
ingredients = st.text_input("Enter ingredients (e.g., chicken, rice, spinach):")
dietary_restriction = st.selectbox("Select dietary preference (optional)", ["None", "Vegan", "Vegetarian", "Gluten-free", "Nut-free", "Keto", "Paleo"])
max_time = st.number_input("Max cooking time (in minutes, optional)", min_value=5, max_value=120, step=5)

# Generate recipe only when user clicks the button
if st.button("Get Recipe"):
    if ingredients:
        recipe = get_recipe(ingredients, dietary_restriction if dietary_restriction != "None" else "", max_time if max_time > 0 else None)

        # Apply formatting before displaying
        recipe = format_recipe(recipe)

        # Display structured response
        st.write("### 🍽️ Recommended Recipe:")
        st.markdown(recipe, unsafe_allow_html=True)
    else:
        st.write("❗ Please enter ingredients before generating a recipe.")
