def generate_neighbourhoods():
    """
    This function read raw data then transform it to neighbourhoods 
    data used in neighbourhood_view.html
    It generated 4 files under path : html/js
    1. ranked_rating.js
    2. ranked_price.js
    3. neighbourhoods.json
    4. neighbourhoods.js
    """
    data1 = pd.read_csv("../../data/listings.csv")
    data2 = pd.read_csv("../../data/listings2.csv")
    neighbourhood = data1['neighbourhood'].tolist()
    price = data1['price'].tolist()
    rating = data2['review_scores_rating'].tolist()

    # neighourhood name list
    name_list = []
    n = len(neighbourhood)
    for i in range(0, n):
        if neighbourhood[i] not in name_list:
            name_list.append(neighbourhood[i])

    # avg price, avg rating by neighbourhood
    price_list = data1.groupby(data1.neighbourhood).mean()['price']
    rating_list = data2.groupby(data1.neighbourhood).mean()['review_scores_rating']

    avg_price = []
    avg_rating = []

    d = len(name_list)
    for i in range(0, d):
        price_target = price_list[name_list[i]]
        rating_target = rating_list[name_list[i]]
        avg_price.append(price_target)
        avg_rating.append(rating_target)

    # generate ranked rating by neighbourhood
    ranked_rating_list = rating_list.sort_values(ascending = False)
    ranked_rating_index = ranked_rating_list.index.tolist()
    ranked_rating_value = ranked_rating_list.tolist()

    file = open("../../html/js/ranked_rating.js", "w")
    file.write( "var ranked_rating_index = " + str(ranked_rating_index) + "\n"
            + "var ranked_rating_value = " + str(ranked_rating_value));
    file.close()

    # generate ranked price by neighbourhood
    ranked_price_list = price_list.sort_values(ascending = False)
    ranked_price_index = ranked_price_list.index.tolist()
    ranked_price_value = ranked_price_list.tolist()

    file = open("../../html/js/ranked_price.js", "w")
    file.write( "var ranked_price_index = " + str(ranked_price_index) + "\n"
            + "var ranked_price_value = " + str(ranked_price_value));
    file.close()

    with open('../../data/neighbourhoods.geojson') as f:
        data = json.load(f)
    n = len(data["features"])
    for i in range(0,n):
        name = data["features"][i]["properties"]["neighbourhood"]
        if name in ranked_price_index:
            idx = ranked_price_index.index(name)
            a_dict = {'price':ranked_price_value[idx]}
            data["features"][i]["properties"].update(a_dict)
        else:
            a_dict = {'price': 'No data'}
            data["features"][i]["properties"].update(a_dict)
        if name in ranked_rating_index:
            idx = ranked_rating_index.index(name)
            a_dict = {'rating':ranked_rating_value[idx]}
            data["features"][i]["properties"].update(a_dict)
        else:
            a_dict = {'rating': 'No data'}
            data["features"][i]["properties"].update(a_dict)

    with open('../../html/js/neighbourhoods.json', 'w') as f:
        json.dump(data, f)
    file = open('../../html/js/neighbourhoods.json')
    data = json.load(file)

    with open('../../html/js/neighbourhoods.js', 'w') as f:
        f.write( "var neighbourhoods = " + str(data));
        f.close()
