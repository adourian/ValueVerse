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
    if request.method == "POST":

        dividend = float(request.form['dividend'])
        risk_free_rate = float(request.form['risk-free-rate']) / 100
        beta = float(request.form['beta']) / 100
        market_return = float(request.form['market-return'])
        dividend_growth = float(request.form['dividend-growth-rate']) / 100

        cost_of_cap_capm = risk_free_rate + beta * (market_return - risk_free_rate)

        enterprise_value = dividend / (cost_of_cap_capm - dividend_growth)

        enterprise_value = round(enterprise_value, 2)
        print(json.dumps({'enterprise_value': enterprise_value}))
        return Response(json.dumps({'enterprise_value': enterprise_value}), mimetype='application/json')
    else:
        return render_template("ddm.html")

@app.route('/buffett', methods=['POST', 'GET'])
def calculate_buffett():
    if request.method == "POST":

        earnings = float(request.form['trailing-eps'])
        growth_rate = float(request.form['expected-eps-growth']) / 100
        risk_free_rate = float(request.form['treasury-rate']) / 100
        market_return = float(request.form['expected-market-return']) / 100
        beta = float(request.form['beta']) / 100

        discount_rate = risk_free_rate + beta * (market_return - risk_free_rate)

        fair_value = (earnings * (8.5 + 2 * growth_rate)) / discount_rate

        enterprise_value = round(fair_value, 2)
        print(json.dumps({'enterprise_value': enterprise_value}))
        return Response(json.dumps({'enterprise_value': enterprise_value}), mimetype='application/json')
    else:
        return render_template("buffett.html")

