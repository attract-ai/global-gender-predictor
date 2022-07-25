import json
import gzip
import hashlib
from pkg_resources import resource_filename


def convert_prob_to_byte(gender, prob):
    return ["M", "F", "?"].index(gender) + 3*round(prob*1000)


def convert_byte_to_prob(byte):
    return ["M", "F", "?"][byte%3], (byte//3)/1000


class GlobalGenderPredictor:
    def __init__(self):
        self.name_gender_dict = {}
        self.gender_map = {"F": "Female", "M": "Male", "?": "Unknown"}

    def predict_gender(self, name, threshold=0.6):
        if name not in self.name_gender_dict:
            self._load_file(name)
        byte = self.name_gender_dict.get(name.lower(), 0)
        gender, weight = convert_byte_to_prob(byte)

        if weight >= threshold:
            return self.gender_map[gender]
        return "Unknown"

    def _load_file(self, name):
        name_hash = hashlib.md5(name.encode("utf-8")).hexdigest()[0]
        data_path = resource_filename("global_gender_predictor", f"data/gender_wgnd2.{name_hash}.jsonl.gz")

        with gzip.open(data_path, 'rb') as f:
            for line in f:
                name_dict = json.loads(line)
                max_gender = max(name_dict['gender_prob'], key=name_dict['gender_prob'].get)
                max_gender_prob = name_dict['gender_prob'][max_gender]
                byte = convert_prob_to_byte(max_gender, max_gender_prob)
                self.name_gender_dict[name_dict['name']] = byte
