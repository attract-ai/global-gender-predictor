# Global Gender Predictor
Predict gender using first name using data from World Gender Name Dictionary 2.0. 
The dataset contains 4,148,966 unique names. The predictor is case-insensitive and predicts ``Male``, ``Female``, or ``Unknown`` (i.e. unisex or not found in data)

Install using pip:
```bash
pip install global_gender_predictor
```
## Usage
```python
from global_gender_predictor import GlobalGenderPredictor

predictor = GlobalGenderPredictor()

predictor.predict_gender('John')
'Male'
predictor.predict_gender('Jane')
'Female'
predictor.predict_gender('attract.ai')
'Unknown'
```
The dataset contains probabilities for each name:
`{'name': 'taylor', 'gender_prob': {'F': 0.699, 'M': 0.301}}`.
Change the probability threshold for unisex names:
```python
predictor.predict_gender('taylor',threshold=0.5)
'Female'
predictor.predict_gender('taylor',threshold=0.8)
'Unknown'
```

## Citation
World Gender Name Dictionary (WGND 2.0)
```bibtex
@data{DVN/MSEGSJ_2021,
author = {Raffo, Julio},
publisher = {Harvard Dataverse},
title = {{WGND 2.0}},
UNF = {UNF:6:5rI3h1mXzd6zkVhHurelLw==},
year = {2021},
version = {DRAFT VERSION},
doi = {10.7910/DVN/MSEGSJ},
url = {https://doi.org/10.7910/DVN/MSEGSJ}
}
```

## deployment 
```
rm dist/*
python3 -m build
twine upload dist/*
```