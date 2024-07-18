# selenium-testing
This is a practice training repository to continue working with Selenium and write test automation scripts in Python for Selenium (previously my selenium script writing was done all in C#).

Project: To create test automation script(s) that will incorporate lots of testing scenarios/interactions across numerous web based objects that could be encountered. Several websites will be used to include: 
- https://www.selenium.dev/selenium/web/
- https://formy-project.herokuapp.com/
- https://jqueryui.com/draggable/

As I work through the various pages and objects, I will tackle performing various actions just like I was a SDET working for the company that designed the site (like as if there were real test requirements associated with the test automation).

Most scripts are organized by the main web element that is being presented in the page.

Some scripts have more logic than others based on the overall functionality that the page provides.
For instance the "webForm.py" contains more logic than most pages. Since it is a web form page with multiple objects, the script was turned into a Data Driven Test, with multiple rows of data in a tuple to process through and also contains a python function.