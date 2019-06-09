# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 15:56:20 2019

@author: ercan
"""

import urllib
import json
import numpy as np

#mqtt_api_key = '3GZ0LWRKWFKEUIPS' # for those students who want to complete the task using MQTT
channel_no = 644166 # this is the channel no that we will get data from
number_of_results = 200
number_of_feats = 5
field_no = 1 # if you are going to get data from each of the fileds separately, you may need to increase this number within a loop upto number_of_feats

feature_matrix = np.zeros([number_of_results, number_of_feats])
# replace the zero entries of feature_matrix with the data you read from thingspeak

# first generate the URL for getting data from thingspeak
# call this URL using the appropriate function of urllib library
# convert what you get from URL call into a python dictionary using json library
# iterate over the contents of the library and write the data into feature_matrix

