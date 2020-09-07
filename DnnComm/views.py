from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
import json
import pandas as pd
import numpy as np
from sklearn import preprocessing
from pickle import load
from pathlib import Path
from decouple import config
import requests


# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def predictDiabetes(request):
    try:
        user = request.user
        data = request.data
        data_keys = data.keys()
        needed_Keys = ['pregnancies', 'glucose', 'blood_pressure', 'skin_thickness', 'insulin', 'bmi', 'dpf', 'age']
        for i in needed_Keys:
            if i not in data_keys:
                raise KeyError
        for i in data_keys:
            val = data[i]
            data[i] = [val]
        dataframe = pd.DataFrame(data)
        normalized_data = normalize(dataframe)
        res = predict_request(normalized_data.values)
        if res.status_code == 200:
            res = res.json()
            output = res['outputs']
            output = output[0][0]
            if output <= 0:
                if output < 0.7:
                    res_dict = {
                        "output": 0,
                        "chance": "very likely"
                    }
                else :
                    res_dict = {
                        "output": 0,
                        "chance": "likely"
                    }
            else:
                if output > 0.7:
                    res_dict = {
                        "output": 1,
                        "chance": "very likely"
                    }
                else:
                    res_dict = {
                        "output": 1,
                        "chance": "likely"
                    }
            json_data = json.dumps(res_dict)
            print(json_data)
            return Response(data=json_data, status=200)
        else:
            return Response(data="internal server error", status=500)
    except KeyError as e:
        return Response(data="all of the needed values were not present", status=400)


def predict_request(data: list):
    try:
        url = config("ML_HOST") + config("ML_PREDICT")
        series = pd.Series(data[0])
        data = series.tolist()
        dict_data = {
            "inputs": [data]
        }
        res = requests.post(url, data=json.dumps(dict_data))
        return res
    except ConnectionError as e:
        return Response(data="internal ml server not running" , status=500)



def normalize(data: pd.DataFrame):
    """

    Args:
        data (pandas.DataFrame):
    """
    parent_path = Path(__file__).parent.parent
    scaler_path = parent_path / 'model_info' / 'MinMaxScaler.pkl'
    scaler = load(open(scaler_path, 'rb'))
    data[['pregnancies', 'glucose', 'blood_pressure', 'skin_thickness', 'insulin', 'bmi', 'dpf',
          'age']] = scaler.transform(
        data[['pregnancies', 'glucose', 'blood_pressure', 'skin_thickness', 'insulin', 'bmi', 'dpf', 'age']].to_numpy())
    return data
