import json
import pickle
import numpy as np
__location=None
__model=None
__data_columns=None

def estimated_price(location,sqft , bhk , bath):
    try:
      location_index=__data_columns.index(location.lower())
    except:
        location_index=-1

    xi=np.zeros(len(__data_columns))
    xi[0]=sqft
    xi[1]=bath
    xi[2]=bhk
    if location_index>=0:
        xi[location_index]=1
    return  round(__model.predict([xi])[0],2)


def get_location_names():
    return __location

def load_saved_artifacts():
    print("loading saved artifacts")
    global __location
    global __data_columns
    global __model

    try:
        with open("./artifacts/columns.json",'r') as f:
            __data_columns = json.load(f)['data_columns']
            __location = __data_columns[3:]
        with open("./artifacts/bengaluru_house_price.pickle",'rb') as f:
            __model = pickle.load(f)
        print("loaded saved artifacts successfully")
    except Exception as e:
        print("Error loading artifacts:", e)



if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(estimated_price('1st block jayanagar' ,1000 , 3 , 3))
    print(estimated_price('Kalhalli' , 1000 , 3 ,3))