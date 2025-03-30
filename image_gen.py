import requests
from dotenv import load_dotenv
import os

def gen_image():
    load_dotenv()

    key = os.getenv("HIVE_API_KEY")

    print(key)


    #prompt generation

    import google.generativeai as genai #google-generativeai>=0.7.2 this is the version of gemini being used
    from google.api_core import retry

    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    model = genai.GenerativeModel('gemini-2.0-flash')

    # For convenience, a simple wrapper to let the SDK handle error retries
    def generate(model, prompt):
        return model.generate_content(prompt)



    import json

    # Load the JSON file
    with open("test.json", "r") as file:
        data = json.load(file)

    # Access the first (and only) section in the processed_region
    section = data["processed_region"]["audio"]["music"]["sections"][0]

    def number_to_word(num):
        if num >= 0 and num <= 0.2:
            word = "weakly/unlikely"
        elif num >= 0.2 and num <= 0.5:
            word = "moderately"
        else:
            word = "strongly/likely"
        return word

    # Retrieve the desired attributes
    loudness = section["loudness"]
    loudness_word = ""
    if loudness >= -9 and loudness <= 0:
        loudness_word = "loud"
    elif loudness >= -15 and loudness < -9:
        loudness_word = "medium volume"
    elif loudness < -15:
        loudness_word = "soft"
    bpm = section["bpm"]
    bpm_word = ""
    if bpm < 40:
        bpm_word =  "Grave"
    elif bpm < 60:
        bpm_word = "Largo"
    elif bpm < 66:
        bpm_word = "Larghetto"
    elif bpm < 76:
        bpm_word = "Adagio"
    elif bpm < 108:
        bpm_word = "Andante"
    elif bpm < 120:
        bpm_word = "Moderato"
    elif bpm < 168:
        bpm_word = "Allegro"
    else:
        bpm_word = "Presto"
    keym = section["key"]
    key_word = number_to_word(keym[0][1]) + " "+ keym[0][0]
    genre = section["genre"]
    genre_word = ""
    for i in genre:
        genre_word += i[0] + " " + number_to_word(i[1]) + ","
    genre_word = "."
    # era = section["era"]
    # era_word = number_to_word(era[0][1]) + " " + era[0][0]
    instrument = section["instrument"]
    instrument_word = ""
    for i in instrument:
        instrument_word += i[0] + " " + number_to_word(i[1]) + ","

    # Print the values
    print("Loudness:", loudness)
    print("BPM:", bpm)
    print("Key:", key)
    print("Genre:", genre)
    #print("Era:", era)
    print("Instrument:", instrument)



    persona = '''\
    You are a prompt engineer for a creative image AI. You are tasked with generating an image reflective of a music and audio input.'''

    guidelines = '''\
    You want to make your art appreciated by the audience, especially the people who provided the music and audio input. You also love to be descriptive.'''

    music_info = f'''\
    {persona} {guidelines}

    The music provided to you is a {loudness_word}, {bpm_word} piece in the key of {key_word}. The genre is {genre_word}, and its instruments used are {instrument_word}. Don't make the prompt longer than 4 sentences, and don't make them needlessly complicated.'''

    prompt = generate(model, music_info).text


    headers = {
        'authorization': 'Bearer ' + key,
        'Content-Type': 'application/json',
    }

    json_data = {
        'input': {
            'prompt': prompt,
            'negative_prompt': 'blurry',
            'image_size': { 'width': 1024, 'height': 1024},
            'num_inference_steps': 15,
            'guidance_scale': 3.5,
            'num_images': 1,
            'seed': 67,
            'output_format': 'png'
        }
    }
        
    response = requests.post('https://api.thehive.ai/api/v3/hive/sdxl-enhanced', headers=headers, json=json_data)
    json_response = response.json()
    image_urls = [entry["url"] for entry in json_response.get("output", [])]
    print(image_urls)
    return image_urls[0]

# print("abel")