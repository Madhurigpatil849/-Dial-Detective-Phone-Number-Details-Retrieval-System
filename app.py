from flask import Flask, request, jsonify
from flask_cors import CORS
import phonenumbers
from phonenumbers import timezone, geocoder, carrier
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
import numpy as np

app = Flask(__name__)
CORS(app)

# Load the dataset
try:
    df = pd.read_csv('spam_dataset.csv')
    print("Dataset Loaded Successfully!")
except Exception as e:
    print("Error loading dataset:", e)

# Encode labels
encoder = LabelEncoder()
df['label'] = encoder.fit_transform(df['label'])

# Separate "not_spam" numbers for exemption
not_spam_numbers = df[df['label'] == 0]['phone_number'].tolist()  # Assuming 'label' 0 = "not_spam"

# Feature extraction function
def extract_features(number):
    number_str = str(number)
    return [
        sum(int(d) for d in number_str),                     # Sum of Digits
        len(set(number_str)),                                # Unique Digit Count
        number_str.count(number_str[0]) / len(number_str)   # First Digit Frequency
    ]

# Apply feature extraction
df['features'] = df['phone_number'].apply(extract_features)
X = pd.DataFrame(df['features'].tolist())
y = df['label']

# Train KNN Model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)
print("KNN Model Trained Successfully!")

@app.route("/")
def home():
    return "Server is running! API is ready to detect phone numbers."

@app.route('/detect', methods=['POST'])
def detect():
    data = request.get_json()
    number = data.get('number', '').strip().replace(" ", "")
    
    if not number:
        return jsonify({'error': 'No phone number provided'}), 400

    try:
        # Validate country code
        if not number.startswith("+"):
            return jsonify({'error': 'Invalid phone number. Please include country code with +.'}), 400

        # Parse the phone number
        phone_number = phonenumbers.parse(number)

        # Extract phone number details
        response = {
            'country_code': phone_number.country_code,
            'national_number': phone_number.national_number,
            'timezone': timezone.time_zones_for_number(phone_number),
            'location': geocoder.description_for_number(phone_number, "en"),
            'service_provider': carrier.name_for_number(phone_number, "en")
        }

        # Check if the number is in the not_spam list
        if phone_number.national_number in not_spam_numbers:
            response['spam_status'] = "not_spam"
            return jsonify(response), 200

        # Perform spam detection using KNN
        features = np.array(extract_features(phone_number.national_number)).reshape(1, -1)
        prediction = knn.predict(features)[0]
        result = "spam" if prediction == 1 else "not_spam"

        response['spam_status'] = result
        return jsonify(response), 200

    except phonenumbers.NumberParseException as e:
        return jsonify({'error': f'Invalid phone number format: {str(e)}'}), 400
    except Exception as e:
        print("Unexpected Error:", e)
        return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)


