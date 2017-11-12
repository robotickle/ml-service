from sklearn.externals import joblib
import datetime as datetime
import time
import os as os
#from pyspark import SparkFiles


def scoreingFunction(input):

    observation = input
    start = time.time()
    # load the model and make a prediction    
    model = joblib.load('random_forest_regressor_export.pkl')
    #model = joblib.load(model.read())
    end = time.time()

    #print "\nLoading and Execution took %s seconds" % (end-start)

    # date
    current_date = datetime.datetime.now()
    pred = model.predict([observation])
    remove_pred = current_date + datetime.timedelta(days = int(pred))

    return_val = "id : {cid}, prediction : {pr}".format(cid = pred_id,pr = baeysian_pred)
    #print(return_val)
    return return_val