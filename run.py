__author__ = 'michaelokuboyejo'
# Run a test server at localhost:8080
from app import application
application.run(host='0.0.0.0', port=8080, debug=True)
