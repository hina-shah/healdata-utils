import visions as v
import pandas.api.types as pdt
from functools import partial
# for declarative API example used as reference see:
# https://github.com/dylan-profiler/visions/blob/develop/examples/declarative_typeset.py

# for Categorical vision type reference, see ydata-profiling:
# https://github.com/ydataai/ydata-profiling/blob/develop/src/ydata_profiling/model/typeset.py
def is_category(series):
    return pdt.is_categorical_dtype(series)

def is_boolean(series):
    return pdt.is_bool_dtype(series)

def is_integer(series):
    return pdt.is_integer_dtype(series)

def is_float(series): 
    return pdt.is_float_dtype(series)

def is_number(series):
    return pdt.is_number(series)
class contains:
    def is_category(series,state):
        return is_category(series)

    def is_integer_category(series,state):

        is_valid = False 
        if is_category(series):
            if is_integer(series.categories):
                is_valid = True

        return is_valid

    def is_string_category(series,state):

        is_valid = False
        if is_category(series):
            if is_string(series.categories):
                is_valid = True

        return is_valid


    def is_float_category(series,state):

        is_valid = False
        if is_category(series):
            if is_float(series.categories):
                is_valid = True 

        return is_valid

class _transformers:
    def to_category(series,state):
        return pd.Categorical(series)

class _relationships:
    def type_is_category(series,k,threshold):
        nunique = series.nunique()
        few_enough_cats = nunique<=k
        low_enough_thresh = (nunique/series.size)<threshold
        is_not_boolean = not is_boolean(series)
        return few_enough_cats and low_enough_thresh and is_not_boolean

class inference_relations:

    def type_to_category(
        related_types=[v.Integer,v.Float,v.String],
        k=5,threshold=.2):

        relationships = []
        for vision_type in related_types:
            relation = dict(
                related_type=vision_type,
                relationship=lambda series,state: partial(_relationships.type_is_category,k=k,threshold=threshold)(series),
                transformer=_transformers.to_category)
            relationships.append(relation)
        return relationships    
    # def integer_to_category(
    #     k=5,
    #     threshold=.2):
    #     relation = dict(
    #         related_type=v.Integer,
    #         relationship=lambda series,state: partial(_relationships.type_is_category,k=k,threshold=threshold)(series),
    #         transformer=_transformers.to_category)
        
    #     return relation

    # def string_to_category(
    #     k=5,
    #     threshold=.2):
    #     relation = dict(
    #         related_type=v.String,
    #         relationship=lambda series,state: partial(_relationships.type_is_category,k=k,threshold=threshold)(series),
    #         transformer=_transformers.to_category)
        
    #     return relation
                
    # def float_to_category(
    #     k=5,
    #     threshold=.2):
    #     relation = dict(
    #         related_type=v.Float,
    #         relationship=lambda series,state: partial(_relationships.type_is_category,k=k,threshold=threshold)(series),
    #         transformer=_transformers.to_category)
        
    #     return relation
# types in the CompleteSet but not in StandardSet
## just manually add additions so additional dependencies
## for unused types not necessary

# {Count,
#  Date,
#  EmailAddress,
#  File,
#  Geometry,
#  IPAddress,
#  Image,
#  Ordinal,
#  Path,
#  Time,
#  URL,
#  UUID}

#TODO: make function to allow specification of params (eg k and threshold). Currently using sensiable default (see typesets_relations.py)
Categorical= v.create_type(
    "Categorical",
    identity=[v.Generic],
    contains=contains.is_category,
    inference=inference_relations.type_to_category()
)

# CategoricalFloat = v.create_type(
#     "CategoricalFloat",
#     identity=[v.Float],
#     contains=contains.is_float_category,
#     inference=inference_relations.float_to_category()
# )

# CategoricalInteger = v.create_type(
#     "CategoricalInteger",
#     identity=v.Generic,
#     contains=contains.is_integer_category,
#     inference=inference_relations.type_to_category([v.Integer])
# )
# CategoricalFloat = v.create_type(
#     "CategoricalFloat",
#     identity=v.Generic,
#     contains=contains.is_float_category,
#     inference=inference_relations.type_to_category([v.Float])
# )
# CategoricalString = v.create_type(
#     "CategoricalString",
#     identity=v.Generic,
#     contains=contains.is_string_category,
#     inference=inference_relations.type_to_category([v.String])
# )

typeset_original = (
    v.StandardSet()
    - v.Categorical
    + v.Date 
    + v.Time
)
typeset_with_categorical = (
    typeset_original
     + Categorical
 )
    # + CategoricalInteger
    # + CategoricalFloat
    # + CategoricalString

def infer_frictionless_schema(df,typeset=typeset_original):
    df_inferred,paths,_ = typset.infer(df)

    fields = []

    for col in list(df):
        field = {"name":col}

        # type mappings (before inferring categoricals)
        coltype = types[col].lower()
        if coltype=="float":
            coltype = "number"
        elif coltype=="generic":
            coltype = "any"
        field["type"] = coltype

        # enums for inferred categoricals
        if [col].lower()=="categorical":
            field["constraints"] = {"enum":list(df[col].categories)}
        
        fields.append(field)

        # TODO: infer formats with extended dtypes (eg url, email etc)
    
    return fields

import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    ,dtype="string"
)
typeset_with_categorical.infer_type(df)