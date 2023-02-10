import pymagnitude 
from pymagnitude import * 
from pymagnitude import MagnitudeUtils 
import pandas as pd 
import forager 
import difflib as dl
import keyword 

vectors = Magnitude(MagnitudeUtils.download_model('word2vec/medium/GoogleNews-vectors-negative300'))

print("clownfish" in vectors)