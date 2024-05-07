import os

import json
from openai import OpenAI
from dotenv import load_dotenv

from util import read_csv

load_dotenv()

model = "gpt-3.5-turbo"
prompts_name = "prompts.json"
data_name = "meals.csv"


with open(prompts_name, 'r') as json_File:
    config = json.load(json_File)

client = OpenAI(
    # This is the default and can be omitted
    organization="org-CRPjgX2sXjMrNTB00bMNzjN5",
    api_key=os.getenv("OPENAI_KEY")
)


def init_gpt():
    data = read_csv(prompts_name)

    initial_prompt = config["initial_prompt"]
    # print(initial_prompt, "\n")
    content = f"{initial_prompt} The data is: {data}"
    client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": content}],
    )


def send_user_message(message):
    completion = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": message}],
    )
    return completion


def get_plan_prompts():
    food_plan_prompts = config["food_plan_prompts"]
    cleaned_food_plan_prompts = cleanse_prompt(food_plan_prompts)
    return cleaned_food_plan_prompts


def get_ingredient_prompts():
    ingredient_prompts = config["ingredient_prompts"]
    cleaned_ingredient_prompts = cleanse_prompt(ingredient_prompts)
    return cleaned_ingredient_prompts


def cleanse_prompt(prompts):
    prompts = prompts.replace("$adults_amount", str(config["adults_amount"]))
    prompts = prompts.replace(
        "$children_amount", str(config["children_amount"]))
    prompts = prompts.replace("$allergies", config["allergies"])
    prompts = prompts.replace("$disliked_food", config["disliked_food"])
    prompts = prompts.replace("$lunch_amount", str(config["lunch_amount"]))
    prompts = prompts.replace("$dinner_amount", str(config["dinner_amount"]))
    prompts = prompts.replace("$keyword", config["keyword"])
    prompts = prompts.replace("$skipped_meals", config["skipped_meals"])
    prompts = prompts.replace("$wanted_meals", config["wanted_meals"])
    return prompts


def cleanse_response(chat_resonse):
    chat_resonse = chat_resonse.replace(config["allergies"], "")
    chat_resonse = chat_resonse.replace(config["disliked_food"], "")
    return chat_resonse


def generate_plan():
    food_plan_prompts = get_plan_prompts()
    # print(food_plan_prompts, "\n")
    completion = send_user_message(food_plan_prompts)
    chat_resonse = completion.choices[0].message.content
    cleansed_response = cleanse_response(chat_resonse)
    print(cleansed_response, "\n")
    return cleansed_response


def generate_ingredient_list(meals):
    ingredient_prompts = get_ingredient_prompts()
    # print(ingredient_prompts, "\n")
    message = f"{ingredient_prompts} {meals}"
    completion = send_user_message(message)
    chat_resonse = completion.choices[0].message.content
    cleansed_response = cleanse_response(chat_resonse)
    print(cleansed_response, "\n")


def change_meals(chat_response):
    part1 = "Please replace any meal that has chicken with turkey while also following all the previous rules."
    message = f"{part1} Use this meal plan: {chat_response}"
    completion = send_user_message(message)
    chat_resonse_2 = completion.choices[0].message.content
    print(f"{chat_resonse_2}")


def no_input():
    init_gpt()
    chat_response = generate_plan()
    generate_ingredient_list(chat_response)


def some_input():
    init_gpt()
    chat_response = generate_plan()
    meals = change_meals(chat_response)
    print(meals)


no_input()
# some_input()
