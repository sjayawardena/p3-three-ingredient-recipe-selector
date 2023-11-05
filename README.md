# Three Ingredient Recipe Selector

![Screenshot from ui.dev/ am I responsive?](assets/images/screenshots-etc/project-3-am-I-responsive-screenshot.png)

Welcome! The Tree-Ingredient Recipe Selector is a Command Line Interface application whereby users can retrieve recipes which only require three ingredients. 

It is the third project for my Diploma in Full Stack Software Development, and utilises Pytyhon.

After users enter their choice of sweet or savoury recipes, and in the latter case their choice of meat or no meat, the user is given a randomly selected recipe from a bank of recipes that matches their criteria.

Users are also asked whether they are happy with the choice of recipe offered, and whether they want to go through the process again.

It is targeted at people who want to try new recipes but may require something simpler to start with.

This is a link to the deployed site: https://three-ingredient-recipe-select-e7093ff803a7.herokuapp.com/

## User Experience (UX)

### User Demographic

The site is intended for:

- Users who want to try new recipes.
- Users who perhaps do not cook much and as such want the recipes be easy, and not require many ingredients.
- User who want to be able to search for recipes by whether they are sweet or savoury, and whether they contain meat or not.

### User Stories

As a new user I want to:
- Quickly and easily find new, simple recipes.
- Not be restricted to the first recipe choice I am offered.
- Try to cook in ways I would normally not e.g. dessert recipes, vegetarian recipes.

As an existing user I want to:
- Look for more recipes of this type (with three ingredients only), should previous recipes have worked out well.
- Find a complementary recipe to prepare alongside one retrieved previouly that has gone well e.g. a dessert to a main.
- Check back for any additions of new recipes.

## Design

The Three-Ingredient Recipe Selector uses a template built by Code Institute. It has a Command Line Interface (CLI) for users to type in their choices. This CLI is boxed against a white background. It is responsive across different screen sizes.

## Ideas Chart

As wireframes were not appropriate for the ideas stage of this project, a chart laying out the flow of choices for the user to make was instead made. This informed the development of functions for the project. 

![Screenshot of ideas chart](assets/images/screenshots-etc/project-3-idea-chart-screenshot.png)

The chart was generally adhered to, but the function to give the user a choice of 30-minute recipes was ommitted and, for simplicity, relevant information is given to the user when their recipe suggestion is presented instead, stating whether it takes 30 minutes or under or not.

## Features

As everything takes place via the Command Line Interface, the various steps and choices of the process for the Three-Ingredient-Recipe Selector can be thought of as the features of it, and these are what are outlined below. 

### Existing Features

#### Introduction/Sweet or Savoury

When the user opens the application, they see the welcome screen, which asks them to enter either "sweet" or "savoury".

![Intro screenshot](assets/images/screenshots-etc/project-3-intro-welcome-screenshot.png)

#### Savoury/Meat or No Meat

If the user chooses savoury, they are asked to enter their choice of meat or no meat.

![Meat or not screenshot](assets/images/screenshots-etc/project-3-savoury-meat-or-not-screenshot.png)

#### Presentation of Recipe

Once the users has entered either sweet or savoury, and in the case of the latter meat or no meat, they are presented with their recipe.

First they see the name of their recipe, the 3 ingredients, and whether it takes under 30 minutes or not. 

![Recipe presented screenshot 1](assets/images/screenshots-etc/project-3-recipe-presented-screenshot-1.png)

There is a delay in executing the next part of the function that presents the recipes, so that the above information can be registered first by the user. Then, the user is presented with the steps for their recipe. 

![Recipe presented screenshot 2](assets/images/screenshots-etc/project-3-recipe-presented-screenshot-2.png)

If the user scrolls up from the steps, they will see the recipe name, ingredients and 30 minutes of under information again.

#### Happy or Not 

Once the user has been presented with a recipe that meets their criteria, they are asked whether they are happy with it.

If they input 'yes', a goodbye greeting is presented expressing pleasure at this outcome, and no more choices are presented either, which makes clear the session is over.

![Happy or not 'yes' screenshot](assets/images/screenshots-etc/project-3-happy-or-not-yes-screenshot.png)

#### Try Again or Not

If the user selects 'no' when asked if they are happy with their recipe, they are offered the chance to try the process again.

![Happy or not 'no' screenshot](assets/images/screenshots-etc/project-3-happy-or-not-no-screenshot.png)

If they select 'no', a goodbye greeting is presented expressing regret at this outcome, and no more choices are presented either, which makes clear the session is over.

![Try again 'no' screenshot](assets/images/screenshots-etc/project-3-try-again-no-screenshot.png)

If the user selects 'yes' the process starts again, bringing the user back to the 'sweet' or 'savoury' choice.

![Try again 'yes' screenshot](assets/images/screenshots-etc/project-3-try-again-yes-screenshot.png)

#### Exception/Error Handling

Throughout the whole process, exception/error handling is in place, so that if the user does not enter either of the choices they are prompted to enter at the various steps ('sweet' or 'savoury'; 'meat' or 'no meat'; 'yes' or 'no'), they are told that what they have entered is invalid, and asked to try again. 

It should be noted that the relevant functions all utilise the .lower() method for the user inputs, so that they can enter their choices in lower, upper, or mixed case and it won't matter. 

The screenshots below are a couple of examples of the error messages generated.

![Error screenshot 1](assets/images/screenshots-etc/project-3-error-screenshot-1.png)

![Error screenshot 2](assets/images/screenshots-etc/project-3-error-screenshot-2.png)

### Features Left To Implement

#### 30 Minutes or Under Choice

If it would be of value to add a choice at the relevant part of the process for the user to select whether they want recipes that take under 30 minutes or not, then this could be added. But there is the risk that this would add too many choices to the process, when the whole idea is that it is quick and easy.

#### Popularity Tracking

Data could be appended to the relevant column of the linked Google Sheet that contains the recipe bank, recording for each recipe whether users said they were happy with it or not. This data could then be sorted in order to obtain the most popular recipes in order. Which could in turn allow for new features, such as offering the user the chance to see the most popular recipe.


### 30 Minutes or Under Choice

## Deployment

### GitHub and Gitpod

### Google Cloud Platform

### Heroku

## Technologies Used

## Testing

### Validator Testing

## Unfixed Bugs

## Credits

### Content

