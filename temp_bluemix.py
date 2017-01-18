import os
import pandas as pd
import numpy as np
from flask import Flask
from flask import request
app = Flask(__name__)
def json_retval(latval,lonval):
    ret_str = '{ "Latitude":' +  '"' + str(latval) + '",' + \
               '"Longitude":' + '"' + str(lonval) + '"}';
    return ret_str;

@app.route('/')
def api():
    latval=float(request.args.get('lat'))
    lonval=float(request.args.get('lon'))
#    varargs = varargs.split("?")
#    num_sensor=len(varargs)-1 #last argument includes the customer key  or the table name in DashDB
#    lon_list=np.array([])
#    lat_list=np.array([])
#    
#    if(num_sensor==1):
#        lat_list=np.append(lat_list,varargs[0])
#        lon_list=np.append(lat_list,varargs[1])
#    else:
#       for i in xrange(0,num_sensor-1,2):
#         lat_list=np.append(lat_list,varargs[i])
#         lon_list=np.append(lon_list,varargs[i+1])
#    Coordinate_dataframe=pd.DataFrame({'Latitude':pd.Series(lat_list),'Longitude':pd.Series(lon_list)})
    return(json_retval(latval,lonval))

if __name__ == "__main__":
    #app.debug = True
    #app.run(host='0.0.0.0', port=int(port))
    PORT=int(os.getenv('VCAP_APP_PORT','5000'))
    HOST = str(os.getenv('VCAP_APP_HOST', '0.0.0.0'))
    app.run(host=HOST, port=PORT)    