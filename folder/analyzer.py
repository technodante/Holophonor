import joblib

# Replace 'path_to_downloaded' with your actual path
lgbm_model = joblib.load('LGBM_model_last')
scaler = joblib.load('Scaler_last')

# Example: assuming 'input_data' is your raw data as a NumPy array
input_data_scaled = scaler.transform(input_data)

predictions = lgbm_model.predict(input_data_scaled)
print(predictions)

