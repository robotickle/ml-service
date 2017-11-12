
""" Machine Learning as a service Example by sandeep kandekar."""
from flask import Flask, jsonify
import pymysql.cursors
from score import scoreingFunction

APP = Flask(__name__)
__author__ = 'sandeep kandekar'

@APP.route('/', methods=['GET'])
def root():
    """ root path for the application """
    return 'Welcome - Machine Learning as a service DEMO! - sandeep kandekar'

@APP.route('/test', methods=['GET'])
def inventory():
    someprarameters = "123xyz"
    ipt = "ID~@~"+str(someprarameters)

    z = scoreingFunction(ipt)
    return z

    """ return some vehicles """
    return jsonify({'make': "Ford"})



if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0')
