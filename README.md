![alt text](https://github.com/wangbeiqi199159/AirbnbViz/blob/master/Docs/Project_logo.png)

# AirbnbViz

# "Analysis and Visualization of Airbnb in Seattle"

Airbnb is a web-based marketplace for people to list, discover, and book unique accommodations around the world. Airbnb users include hosts and travelers: hosts list and rent out their unused spaces, and travelers search for and book accommodations in more than 34,000 cities and 190 countries.

The AirbnbViz team aims to provide more information and insights to guests of Airbnb in Seattle to help them have a deeper understanding of what factors influence the listing price most, which neighborhood has higher/lower listing price and which neighborhood has higher and lower guests' rating via our different interactive visualizations. On the other hand, As hosts of Airbnb, they will have more idaes that how other hosts priced around them relative to dimensions such as amenities and location and what is the average listing prices of different neighborhoods in Seattle.


## Author

#### Beiqi Wang



## Data

- [Source 1: Seattle’s Airbnb listing data from Inside Airbnb](http://insideairbnb.com)

- [Source 2: NOAA Weather](http://www.noaa.gov)

- Source 3: Seattle Neighborhoods GeoJSON Data


## Software dependencies and license information
#### Programming language: 

- Python version 3.0 and above 
- JavaScript
- HTML

#### Python packages needed:

- pandas
- NumPy
- sklearn

#### License Information:
The MIT License is a permissive free software license originating at the Massachusetts Institute of Technology (MIT). As a permissive license, it puts only very limited restriction on reuse and has therefore an excellent license compatibility. For detailed description of the contents of license please refer to the file [License](https://github.com/wangbeiqi199159/analyze-of-seattle-airbnb-hosts/blob/master/LICENSE).


## Directory Structure

The package is organized as follows:
```
AirbnbViz (master)
|     .gitignore
|     License
|     README.md
|     setup.py
|     start.py
|
|----- Docs
|     |      Design Specification.md
|     |      Functional Specification.md
|     |      Logo.png
|     |      Final Presentation.pdf
|----- AirbnbViz
|     |   __init__.py
|     |  
|     |----- data
|     |      |   listings.csv
|     |      |   listings2.csv
|     |      |   listings_combined.csv
|     |      |   neighbourhoods.geojson
|     |      | 
|     |----- examples 
|     |      |    Price VS. Comments and Reviews.ipynb
|     |      |    Rating VS Comment's length.ipynb
|     |      |    create avg.js.ipynb
|     |      |    generate ranked price by neighbour group.ipynb
|     |      |    neighborhood data.ipynb
|     |      |    price predict model.ipynb
|     |      | 
|     |----- code
|     |      |    generate_listings.py
|     |      |    generate_neighbourhoods.py   
|     |      |    generate_ranked_data.py   
|     |      |    price.py    
|     |      |    probability.py   
|     |      |            
|     |----- tests
|     |      |    test_generate_listings.py
|     |      |    test_generate_neighbourhoods.py
|     |      |    test_generate_ranked_data.py
|     |      |
|     |----- home page
|     |      |    index.html
|     |      |
|     |----- html
|     |      |    home_view.html
|     |      |    price.html
|     |      |    rating.html
|     |      |    prediction.html
|     |      |
|     |      |----- js  
|     |      |        |   ranked_price_data_by_group.js  
|     |      |        |   ranked_rating_data_by_group.js
|     |      |        |   listings.js
|     |      |        |   neighbourhoods.js
|     |      |        |   neighbourhoods.json
|     |      |        |   predict_source.js
|     |      |        |   ranked_price.js
|     |      |        |   ranked_rating.js





