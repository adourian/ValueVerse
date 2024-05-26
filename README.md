# ValueVerse

#### Description:
This is a web app that allows the user to select a standard stock-valuation model, and get a stock value by entering some data about the company and calculating the value based on the models.

To use, simply:

- Download the repository to your local files
- open an IDE
- navigate to the downloaded folder in a terminal
- make sure flask is installed (pip install flask)
- run the following:
    - set FLASK_APP=app.py
    - flask run --port=5001
- ctrl+click the link


The web app has a navigation bar with a directory, which links to all the pages of the web app. The navigation bar is at the top of all of the webpages, but stays visible when the user scrolls down. This is done by writing a JavaScript code that changes the class of the nav bar when the user scrolls down, and setting appropriate CSS styling for when the user is at the top or when he has scrolled down, using the window.onscroll function of javaScript.

There are 4 main pages accessible from the nav bar: the home page, a models page, a contact page, and a support page. The models page contains a list and descriptions of the three available models. The contact page contains bogus contact information.

In the home page, the user is welcomed to the website, and instructed to select a model, either the DCF model, the DDM, or a simple Warren Buffett-inspired formula. He is given a short description of each model. When he clicks on a model, he is then taken to the specific model page.

On the specific model page, he is given a decription of the model, instructions of when it is appropriate to use it, and what are the shortcomings and risks of using such a model.

Under this, there is a calculator widget, that lets the user input float numbers only (positive, negative or zero, by setting input type="number" and step="0.00001", thus preventing user from inputting any wrong values). Below the calculator, the user is given a couple of definitions and recommendations to guide him when entering the required data. When the user clicks the "Calculate" button, the value of the stock appears in bold right below the button. This is done by running the web app on flask. The calculator is a <form>, which the user fills in. When he clicks the button, the form is submitted to the server (method="POST") and processed by flask. The necessary parameters are extracted in python using request.form.get(id). The stock value is then calculated in the back-end in python, then converted to json, and sent back to the front-end, client-side page.

The client-side website then has a javascript code that includes eventListeners, and when the data is sent from the back-end, the front-end processes this data, uses some Ajax code in addition to js to update the correct tag and send it a .text response. The stock value is then displayed in bold below the calculate button.

That way, the page is not refreshed when the user submits data, and he can conduct some sensitivity analysis by changing the parameters and assumptions and see how it affects the stock result in an interactive way.
