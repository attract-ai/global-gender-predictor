import json
import gzip
from pkg_resources import resource_filename


def convert_prob_to_byte(gender, prob):
    return ["M", "F", "?"].index(gender) + 3*round(prob*1000)


def convert_byte_to_prob(byte):
    return ["M", "F", "?"][byte%3], (byte//3)/1000


def _parse_file(data_path):
    name_gender_dict = {}
    with gzip.open(data_path, 'rb') as f:
        for line in f:
            name_dict = json.loads(line)
            max_gender = max(name_dict['gender_prob'], key=name_dict['gender_prob'].get)
            max_gender_prob = name_dict['gender_prob'][max_gender]
            byte = convert_prob_to_byte(max_gender, max_gender_prob)
            name_gender_dict[name_dict['name']] = byte
    return name_gender_dict


class GlobalGenderPredictor:
    def __init__(self, data_path=None):
        data_path = data_path or resource_filename("global_gender_predictor", "data/gender_wgnd2.jsonl.gz")
        self.name_gender_dict = _parse_file(data_path)

        self.gender_map = {"F": "Female", "M": "Male", "?": "Unknown"}

    def predict_gender(self, name, threshold=0.6):
        byte = self.name_gender_dict.get(name.lower(), 0)
        gender, weight = convert_byte_to_prob(byte)

        if weight >= threshold:
            return self.gender_map[gender]
        return "Unknown"
