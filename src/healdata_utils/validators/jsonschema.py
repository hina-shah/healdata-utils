""" 
validation of json records against a jsonschema specification 
and conversion of one schema spec to jsonschema specification 
eg frictionless --> jsonschema

""" 

import jsonschema


def __validate_property(self,instance,property_in_schema):
    try:
        jsonschema.validate(instance,schema=property_in_schema)
        return "VALID"
    except jsonschema.exceptions.ValidationError as e:
        return "ERROR"+e.message
        
def _validate_record(self,record):
    #TODO: allow for nested records
    report = {}
    self.is_valid = True
    for propname,prop in self.schema.get("properties",{}).items():
        is_required = propname in schema.get("required",False)
        instance = record.get(propname,{})

        if instance:
            error_message = __validate_property(instance,prop)
        elif not instance and is_required:
            error_message: "ERROR:required"
        elif not instance and not is_required:
            error_message = "MISSING"

        report[propname] = error_message

        #if a property is missing or valid it is "valid"
        if not error_message in ["VALID","MISSING"]:
            self.is_valid = False
    
    return report


def validate_against_jsonschema(records,schema):
    table_report = []
    is_valid = True
    for record in records:
        is_valid,record_report = _validate_record(record,schema)
        if not is_valid:
            is_valid = False

        table_report.append(record_report)

    return {"valid":is_valid,"errors":table_report}