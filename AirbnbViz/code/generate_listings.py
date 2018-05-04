def generate_listings():
"""
This model read home listing information then transform it into .js formate
It generates listings.js under html/js
"""
	data1 = pd.read_csv("../../data/listings.csv")
	listing = data1.to_json(orient='records')
	file = open("../../html/js/listings.js", "w")
	file.write( "var listings = " + listing)
