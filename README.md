# nutrition-finder

The nutrition-finder project is a website designed to provide users with nutritional information about the foods they eat, provided by the USDA APIs. If they so wish, they can sign up to keep track of the foods they eat. Our website will keep track of the total amount of calories a user has eaten for a certain day depending on the meals they have eaten that day. Then our BMI API can help calculate a user's BMI using user's basic medical information such as height and weight, which is required when users sign up, and our website will inform users of any health risks they may have depending on their BMI, courtesy of the BMI API.

## Team
* Brian Yang
* Jason Chua
* Shaeq Ahmed
* Amy Xu

## Instructions
### Getting the required API Keys (free)
1. Get the nutritionix API key [here](https://developer.nutritionix.com/).
2. Get the BMI Calculator API key [here](https://market.mashape.com/nviror/bmi-calculator).
3. Put the nutritionix API key on the first line of keys.txt. Put the BMI Calculator API key on the second line of keys.txt. keys.txt should be placed in the root directory of the project (in the same folder as app.py).
### Running
1. To run the website, you must first install flask and unirest. The time module does not need to be installed.
To install these two modules, do `pip install flask` and `pip install unirest` in your virtual environment.
2. Put the API key text file in the root of the project directory and name it `keys.txt`.
3. Run `python app.py`.

## How to use the website
1. To see the nutritional information for a certain food/meal, enter in search keywords in the search bar at top of the page. Then you will be taken to a page with a list of results best matching what you entered and the nutritional information for each food result. Using the search bar does NOT require you to be logged in.
2. If you want to sign up, click the login button on the navbar. You will be taken to the login/registration page, where you can then register.
3. When you register, you must enter in all the fields, which are the username, password, age, height, weight, and gender. The age and height (inches) need to be from 1 to 100. The weight should be from 1 to 1000. There should be a green message saying that registration was successful.
4. After you login, you will be brought to your profile page. On the profile page, it will show your basic medical information as well as the BMI. In the calories tab, the calories you've consumed and the meals you've eaten for each day will be displayed.
5. To enter in meals you've eaten today, use the search bar again while LOGGED IN. When you search for a food using the search bar, you will now see buttons that say "Add" in each search result. Click an Add button for a search result if you ate that meal today. The meal that you added will be stored in the website's database as a food you've eaten for that day, and the number of calories that the meal contains will contribute to the calorie count displayed in the calories page for that day.
6. To logout, simply click the logout button on the navbar.
