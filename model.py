import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

data = pd.read_csv('data/dolar_cop.csv')
data.columns = ['DATE', 'PRICE']


def fix_date(data):
    data['YEAR'] = data['DATE'].str[:4]
    data['MONTH'] = data['DATE'].str[5:7]
    data['DAY'] = data['DATE'].str[8:10]
    
    data['DATE'] = data['YEAR']+'-'+data['MONTH']+'-'+data['DAY']
    data['DATE'] = pd.to_datetime(data['DATE'])
    return data

def prepare_data(data):
    X = data.drop(['DATE', 'PRICE'], axis=1)
    y = data['PRICE']
    return X, y

def model_training(x, y):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.40, random_state=42)
    model.fit(x_train, y_train)
    
    return x_test, y_test, model

def model_evaluation(model, x, y):
    prediction = model.predict(x)
    
    df = pd.DataFrame({
        'True Value': y,
        'Prediction': prediction
    })
    
    mse = mean_squared_error(y, prediction)
    r2 = r2_score(y, prediction)
    
    print(f'Mean Squared Error: {mse:.4f}')
    print(f'R2 Score: {r2:.4f}')
    
    print(df)
    return mse, r2
    
if __name__ == '__main__':
    data = fix_date(data)
    x,y = prepare_data(data)
    x_test,y_test,model = model_training(x,y)
    mse, r2 = model_evaluation(model, x_test, y_test)
    
    # joblib.dump(model, 'app/model/cop_predictor.pkl')
    

