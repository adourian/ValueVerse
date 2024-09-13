import json
from flask import Flask, render_template, request, redirect, Response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/models')
def models():
    return render_template('models.html')

@app.route('/dcf', methods=['POST', 'GET'])
def calculate_dcf():
    """
    Calculate the Discounted Cash Flow (DCF) and return the enterprise value based on user input.

    This function calculates the enterprise value of a company using the Discounted Cash Flow (DCF) model. 
    It takes the following inputs from a POST request:
    - free cash flow (FCF) for the current year
    - discount rate
    - terminal growth rate
    - terminal multiple

    The calculation involves:
    1. Projecting the free cash flow for 5 years and discounting it to its present value.
    2. Estimating the terminal value at the end of the projection period using the terminal multiple.
    3. Discounting the terminal value to its present value.
    4. Summing the discounted projected cash flows and the discounted terminal value to compute the total enterprise value.

    Returns:
        JSON response containing the calculated enterprise value.
        
    Methods:
        - POST: Processes user input and returns the DCF enterprise value in JSON format.
        - GET: Renders the DCF input form template.
    """
    if request.method == "POST":

        current_fcf = float(request.form['free-cash-flow'])
        discount_rate = float(request.form['discount-rate']) / 100
        terminal_growth_rate = float(request.form['terminal-growth-rate']) / 100
        terminal_multiple = float(request.form['terminal-multiple'])

        years = 5  # Number of years for projection

        # Calculate projected FCF for each year and their present value
        present_value_cash_flows = sum(
            current_fcf * pow(1 + terminal_growth_rate, year) / pow(1 + discount_rate, year)
            for year in range(1, years + 1)
        )
        
        # Calculate Terminal Value using the Terminal Multiple Approach
        terminal_value = terminal_multiple * (current_fcf * pow(1 + terminal_growth_rate, years))
        
        # Discount the Terminal Value to the present
        present_value_terminal_value = terminal_value / pow(1 + discount_rate, years)
        
        # Total Enterprise Value
        enterprise_value = present_value_cash_flows + present_value_terminal_value

        # Round Enterprise Value
        enterprise_value = round(enterprise_value, 2)
        
        print(json.dumps({'enterprise_value': enterprise_value}))
        return Response(json.dumps({'enterprise_value': enterprise_value}), mimetype='application/json')
    else:
        return render_template("dcf.html")


@app.route('/ddm', methods=['POST', 'GET'])
def calculate_ddm():
    """
    Calculate the Dividend Discount Model (DDM) enterprise value based on user input.

    This function calculates the enterprise value of a company using the Dividend Discount Model (DDM), specifically
    the Gordon Growth Model. It takes the following inputs from a POST request:
    - Dividend per share
    - Risk-free rate
    - Beta
    - Market return rate
    - Dividend growth rate

    The calculation involves:
    1. Computing the Cost of Equity using the Capital Asset Pricing Model (CAPM), which combines the risk-free rate,
       beta, and market return.
    2. Estimating the enterprise value using the Gordon Growth Model, which accounts for the expected growth in dividends.

    Returns:
        JSON response containing the calculated enterprise value rounded to 2 decimal places.

    Methods:
        - POST: Processes user input and returns the DDM enterprise value in JSON format.
        - GET: Renders the DDM input form template.
    """
    
    if request.method == "POST":

        # Inputs from form
        dividend = float(request.form['dividend'])
        risk_free_rate = float(request.form['risk-free-rate']) / 100
        beta = float(request.form['beta'])
        market_return = float(request.form['market-return']) / 100
        dividend_growth = float(request.form['dividend-growth-rate']) / 100
        
        # Calculate Cost of Equity using CAPM
        cost_of_equity = risk_free_rate + beta * (market_return - risk_free_rate)
        
        # Calculate Enterprise Value using Gordon Growth Model
        enterprise_value = dividend * (1 + dividend_growth) / (cost_of_equity - dividend_growth)
        
        # Round to 2 decimal places
        enterprise_value = round(enterprise_value, 2)
        return Response(json.dumps({'enterprise_value': enterprise_value}), mimetype='application/json')
    else:
        return render_template("ddm.html")

@app.route('/buffett', methods=['POST', 'GET'])
def calculate_buffett():
    if request.method == "POST":

        # Inputs from form
        earnings = float(request.form['trailing-eps'])
        growth_rate = float(request.form['expected-eps-growth']) / 100  # Convert percentage to decimal
        risk_free_rate = float(request.form['treasury-rate']) / 100  # Convert percentage to decimal
        market_return = float(request.form['expected-market-return']) / 100  # Convert percentage to decimal
        beta = float(request.form['beta'])  # Beta is already in decimal form
        
        # Calculate Discount Rate using CAPM
        discount_rate = risk_free_rate + beta * (market_return - risk_free_rate)
        
        # Calculate Fair Value using the Warren Buffett Formula
        fair_value = (earnings * (8.5 + 2 * growth_rate)) / discount_rate
        
        # Round to 2 decimal places
        enterprise_value = round(fair_value, 2)
        
        print(json.dumps({'enterprise_value': enterprise_value}))
        return Response(json.dumps({'enterprise_value': enterprise_value}), mimetype='application/json')
    else:
        return render_template("buffett.html")

