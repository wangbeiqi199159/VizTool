def price_model():
"""
This function is to generate Machiene learning model. 
It will generate file in cvs format.
It will generate Lasso and Ridge regression Coe. 
"""
	
	listing=pd.read_csv('all.csv')
	df=listing[['host_response_rate','host_response_time','host_acceptance_rate',
            'host_is_superhost','neighbourhood_group_cleansed','property_type','room_type',
            'accommodates','bathrooms','bedrooms','beds','price','minimum_nights',
            'maximum_nights','number_of_reviews','review_scores_rating',
            'review_scores_value','cancellation_policy',
            'require_guest_profile_picture','instant_bookable',
            'require_guest_phone_verification','reviews_per_month']]
    print((len(df)-df.count())/len(df)) #see the percentage of NA of each Varaible 

    df2=df.dropna(axis=0) #drop the Na
    #change format $100 to 100 
    pd.options.mode.chained_assignment=None
    df2['host_acceptance_rate']=df2['host_acceptance_rate'].astype(str)
    df2['host_response_rate']=df2['host_response_rate'].astype(str)
    df2['price']=df2['price'].astype(str)

    #data cleanning 
    df2['host_acceptance_rate']=df2['host_acceptance_rate'].str.replace("%","").astype("float")
    df2['host_response_rate']=df2['host_response_rate'].str.replace("%","").astype("float")
    df2['price']=df2['price'].str.replace("$","").astype("float")

    #transfer to dummy 
    df2['host_is_superhost'].replace('f',0,inplace=True)
    df2['host_is_superhost'].replace('t',1,inplace=True)
    df2['instant_bookable'].replace('f',0,inplace=True)
    df2['instant_bookable'].replace('t',1,inplace=True)
    df2['require_guest_profile_picture'].replace('f',0,inplace=True)
    df2['require_guest_profile_picture'].replace('t',1,inplace=True)
    df2['require_guest_phone_verification'].replace('f',0,inplace=True)
    df2['require_guest_phone_verification'].replace('t',1,inplace=True)
    df2['cancellation_policy'].replace('f',0,inplace=True)
    df2['cancellation_policy'].replace('t',1,inplace=True)

    # transfer to factor 
    df_cate=df2[['host_response_time','neighbourhood_group_cleansed','property_type','room_type','cancellation_policy']]
    dummy=pd.get_dummies(df_cate)
    del df2['host_response_time']
    del df2['neighbourhood_group_cleansed']
    del df2['property_type']
    del df2['room_type']
    del df2['cancellation_policy']

    df3=pd.merge(df2,dummy,left_index=True,right_index=True)
    #define x and y
    y=df3['price']
    X=df3.drop('price',axis=1)
    #split data in training and valid set 
    
    X_train, X_valid, y_train, y_valid = cross_validation.train_test_split(X, y, random_state=0)
    #standardlize the x
    scaler=sklearn.preprocessing.StandardScaler()
    scaler.fit(X_train)
    X_train=scaler.transform(X_train)
    X_valid=scaler.transform(X_valid)

    #Fit the CV model to find best alppha
    ridgecv=RidgeCV(alphas=alphas,fit_intercept=True,scoring='mean_squared_error',normalize=True)
    ridgecv.fit(X_train,y_train)
    print('optimal alpha is %f:' %ridgecv.alpha_)

    #fit the model with optimal alpha 
    optimal_al_redige=ridgecv.alpha_
    ridge_optimal= Ridge(alpha=optimal_al_redige,fit_intercept=True,normalize=True)
    ridge_optimal.fit(X_train,y_train)

    #add intercept 
    b=ridge_optimal.coef_
    b=np.append(b,[ridge_optimal.intercept_])
    columns1=np.append(X.columns,['intercept'])

    #generate pd 
    df_ridge=pd.Series(b,index=columns1)
    print(df_ridge)

    #find optimal aplpha by cv 
    lassocv=LassoCV(alphas=None,fit_intercept=True,cv=10,max_iter=10000,normalize=True)
    lassocv.fit(X_train,y_train)
    print(lassocv.alpha_)

    #append intercept


    #gengerate df 
    optimal_al_lasso=lassocv.alpha_
    lasso=Lasso(alpha=optimal_al_lasso,fit_intercept=True,normalize=True)
    lasso.fit(X_train,y_train)
    df_lasso=pd.Series(a,index=columns)
    # append intercept
    a = lasso.coef_
    a = np.append(a, [lasso.intercept_])
    columns = np.append(X.columns, ['intercept'])

    #convert to csv
    df_lasso.to_csv('Lasso_Model.csv',index=True)
    df_ridge.to_csv('Ridge_Model.csv',index=True)