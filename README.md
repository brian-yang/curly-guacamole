# curly-guacamole

### TODO IN DESIGN.PDF:
* Fix arrow pointing to browse in sitemap
* Add overview/project description to DESIGN.pdf
* Remove browse.html
* Change from Nutritionix API to USDA APi
* Add gender to user_diagnostics table

### Extra Modules
time - Used to get the date with the strftime() function
unirest - Used to communicate with the BMI API and retrieve information
from the API (the API would not allow requests made by urllib2)

###Setting up and running the website
1. To run the website, you must first install flask and unirest.
To install these two modules, do `pip install flask` and `pip install unirest` in your virtual environment.
2. Put the API key text file in the root of the project directory and name it `keys.txt`.
3. Run `python app.py`.

###How to use the website