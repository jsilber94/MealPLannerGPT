# MealPlannerGPT

## Prompt Engineering

- Give examples of what I want to see
- Detailed and specific instructions

- Find alternatives to rejected ingredients
- Measurements for ingredients should be easy

### Advanced prompt engineering

- Zero Shot Reasoners
  - step by step predictions for better results
- Chain of Thought Prompting
  - use the previous answers/conversation and build on it for context awareness (works with sufficiently large language models)
- Few Shot Prompting for in-context learning.
  - generate more than 14 meals to improve results
- Generated Knowledge Prompting
  - greek salad ingredients
- Self Guided learning
  - use correct output to train the model

## Product quality

- Generate ingredient list at the same time as each meal.
- Specific prompt for each meal. Generate a meal with the limitations.
- Self-Consistency
  - generate numerous meal plans before
- Provide ingredient needed from the meal data.

## Ideas/Improvements:

- Evaluate ingredients and assign a score.
- Follow up emails.
- Allow family to rate meals and ingredients.
- Classify ingredients as red, yellow, green, or blue (adventurous).
- Health rating of food.
- Types of diets: vegan, keto, paleo.
- Different meals for adults and children.
- Integrate with recipe api.

## Things Of Note:

- Keep rejecting meals, dont add the the rejected ones back as an option?
- Each meal consists of protein, vegetable, and starch.
- 2500 calories per adult.
- 1500 calories per child.
- 70% of meals should be based on existing data.
- 30% of meals should be adventurous.

## Questions/Clarifications

1. Is it the same meal for the whole family or a specific meal for each member which is based on allergies and ingredients?
2. Should I be rejecting an entire meal plan or individual meals?
3. Are ingrdients types of food as in meat, vegetable or specifics like onions or garlic
4. What if the family is too restrictive with ingredients? Should I use rejected ingredients to meet caloric and nutrition needs?
5. Multiple families or single family? POC
6. Initial entry to system email or allergies

## Stack- React/Python

#### Part 1 (React)

- Ask meal plan questions
- Approve or reject meals
- Approve plan (once meals are approved)

#### Part 2 (Logic)

- Determine portions based on family size
- Determine common ingredients
- Determine adventurous ingredients
- Determine old meals
- Generate meal replacement
- Persist meals/ingredients/allergies in db

#### Part 3 (ChatGPT + prompt engineering)

- Generate meal plan
- Generate ingredient list
- Write prompts + restrictions

#### Part 4 (Scheduled task)

- Schedule weekly email
- Email meal plan and ingredients
