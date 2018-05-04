def prob_model():
"""
This function is to generate model in csv format.
It first cleaned the data, and then do three features 
selecting to selesct features. 

Then use Logistic regression CV to find the optimal 
alpha and then use logstic regression to fit the modekl.

It finally generate coefficients with CSV file.
"""
	host=pd.read_csv('host_data.csv') #load data 
	df_host=host[['available','host_response_time','host_response_rate', 'host_acceptance_rate', 
              'host_is_superhost','host_total_listings_count','host_has_profile_pic',
              'host_identity_verified', 'neighbourhood_group_cleansed','property_type', 'room_type',
              'accommodates', 'bathrooms', 'bedrooms', 'beds', 'bed_type', 'price_y',
              'minimum_nights', 'maximum_nights','number_of_reviews', 'review_scores_rating', 
              'review_scores_cleanliness', 'review_scores_checkin','review_scores_value', 
              'requires_license', 'cancellation_policy',
              'require_guest_profile_picture', 'require_guest_phone_verification',
              'calculated_host_listings_count', 'reviews_per_month', 'PRCP']]

    print((len(df_host)-df_host.count())/len(df_host)) #check the percentage of Na for each variable 
    df_host_1=df_host.dropna(axis=0)# drop Na row 
    print((len(df_host)-len(df_host_1))/len(df_host))
    
    #change the type $100 to 100 
    pd.options.mode.chained_assignment=None 
    df_host_1['host_response_rate']=df_host_1['host_response_rate'].astype(str)
    df_host_1['host_acceptance_rate']=df_host_1['host_acceptance_rate'].astype(str)
    df_host_1['price_y']=df_host_1['price_y'].astype(str)
    df_host_1['host_acceptance_rate']=df_host_1['host_acceptance_rate'].str.replace("%","").astype("float")
    df_host_1['host_response_rate']=df_host_1['host_response_rate'].str.replace("%","").astype("float")
    df_host_1['price_y']=df_host_1['price_y'].str.replace("$","").astype("float")

    #change to dummy 
    df_host_1['host_is_superhost'].replace('f',0,inplace=True)
    df_host_1['host_is_superhost'].replace('t',1,inplace=True)
    df_host_1['host_has_profile_pic'].replace('f',0,inplace=True)
    df_host_1['host_has_profile_pic'].replace('t',1,inplace=True)
    df_host_1['host_identity_verified'].replace('f',0,inplace=True)
    df_host_1['host_identity_verified'].replace('t',1,inplace=True)
    df_host_1['require_guest_phone_verification'].replace('f',0,inplace=True)
    df_host_1['require_guest_phone_verification'].replace('t',1,inplace=True)
    df_host_1['requires_license'].replace('f',0,inplace=True)
    df_host_1['requires_license'].replace('t',1,inplace=True)
    df_host_1['require_guest_profile_picture'].replace('f',0,inplace=True)
    df_host_1['require_guest_profile_picture'].replace('t',1,inplace=True)
    df_host_1['require_guest_phone_verification'].replace('f',0,inplace=True)
    df_host_1['require_guest_phone_verification'].replace('t',1,inplace=True)

    df_host_1.select_dtypes(include=['object']).columns
    df_host_category=df_host_1[['host_response_time', 'neighbourhood_group_cleansed', 'property_type', 'room_type'
                            ,'bed_type', 'cancellation_policy']]
    dummy_host=pd.get_dummies(df_host_category)

    del df_host_1['host_response_time']
    del df_host_1['neighbourhood_group_cleansed']
    del df_host_1['property_type']
    del df_host_1['room_type']
    del df_host_1['bed_type']
    del df_host_1['cancellation_policy']

    df_host_2=pd.merge(df_host_1,dummy_host,left_index=True,right_index=True)
    y_host=df_host_2['available'] 
    x_host=df_host_2.drop('available',axis=1)

    
    test_uni=SelectKBest(score_func=chi2,k=4) 
    fit=test_uni.fit(x_host,y_host)
    np.set_printoptions(precision=3)
    print(fit.scores_)
    feature=fit.transform(x_host)
    print(feature[0:20,:])

    # Rescursive Feature Elimination
    
    x_train_host, x_valid_host, y_train_host, y_valid_host= cross_validation.train_test_split(x_host, y_host, random_state=0)

    model_rfe=LogisticRegression()
    rfe=RFE(model_rfe,20)
    fit_rfe=rfe.fit(x_valid_host,y_valid_host)

    print("Num Features: %d" %fit_rfe.n_features_)
    print('Selected Features: %s' %fit_rfe.get_support(indices=True))
    print('Featur Raking: %s'%fit_rfe.ranking_ )

    # Randomized Logistic Regression 
    

    clf= RandomizedLogisticRegression()
    clf.fit(x_valid_host,y_valid_host)
    print (clf.get_support(indices=True))

    for i in fit_rfe.get_support(indices=True):
    print(x_host.columns[i])

    select_varaible=[]
    for i in fit_rfe.get_support(indices=True):
    	select_varaible.append(x_host.columns[i])
    select_varaible.append(x_host.columns[10])
    x_host_select=df_host_2[select_varaible]


    #fit model with selecting featurs
   
    x_train_host, x_valid_host, y_train_host, y_valid_host= cross_validation.train_test_split(x_host_select, y_host, random_state=0)
    #use cv to find optimal labmda
    lr_cv=sklearn.linear_model.LogisticRegressionCV(penalty='l2',fit_intercept=True,tol=10e-8,max_iter=1000)
    lr_cv.fit(x_train_host,y_train_host)

    optimal_lambda=lr_cv.C_[0]
    print('Optimal=',optimal_lambda)

    lr=sklearn.linear_model.LogisticRegression(penalty='l2',C=optimal_lambda,fit_intercept=True,tol=10e-8,max_iter=1000)
    lr.fit(x_train_host,y_train_host)

    y_pred=lr.predict_proba(x_valid_host)

    a=np.reshape(lr.coef_,(21,))
    a=np.append(a,[lr.intercept_])
    columns=np.append(x_host_select.columns,['intercept'])
    df_log=pd.Series(a,index=columns)
    #generate CSV
    df_log.to_csv('Log_Model.csv',index=True)
