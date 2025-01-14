healcsvschema = {
    "description": "Variable level metadata individual fields integrated into "
    "the variable level\n"
    "metadata object within the HEAL platform metadata service.\n"
    "\n"
    "> Note, only `name` and `description` are required.\n"
    ">  Listed at the end of the description are suggested "
    '"priority" levels in brackets (e.g., [<priority>]):\n'
    "  1. [Required]: Needs to be filled out to be valid.\n"
    "  2. [Highly recommended]: Greatly help using the data "
    "dictionary but not required. \n"
    "  3. [Optional, if applicable]: May only be applicable to "
    "certain fields.\n"
    "  4. [Autopopulated, if not filled]: These fields are "
    "intended to be autopopulated from other fields but can be "
    "filled out if desired.\n"
    "  5. [Experimental]: These fields are not currently used but "
    "are in development.\n",
    "title": "HEAL Variable Level Metadata Fields",
    "fields": [
        {
            "name": "module",
            "description": "The section, form, survey instrument, set of "
            "measures  or other broad category used \n"
            "to group variables.\n",
            "title": "Module",
            "examples": [
                "Demographics",
                "PROMIS",
                "Substance use",
                "Medical History",
                "Sleep questions",
                "Physical activity",
            ],
            "type": "string",
        },
        {
            "name": "name",
            "description": "The name of a variable (i.e., field) as it "
            "appears in the data. \n"
            "\n"
            "[Required]\n",
            "title": "Variable Name",
            "type": "string",
            "constraints": {"required": True},
        },
        {
            "name": "title",
            "description": "The human-readable title or label of the "
            "variable. \n"
            "\n"
            "[Highly recommended]\n",
            "title": "Variable Label (ie Title)",
            "examples": ["My Variable (for name of my_variable)"],
            "type": "string",
        },
        {
            "name": "description",
            "description": "An extended description of the variable. This "
            "could be the definition of a variable or the \n"
            "question text (e.g., if a survey). \n"
            "\n"
            "[Required]\n",
            "title": "Variable Description",
            "examples": ["Definition", "Question text (if a survey)"],
            "type": "string",
            "constraints": {"required": True},
        },
        {
            "name": "type",
            "description": "A classification or category of a particular "
            "data element or property expected or allowed "
            "in the dataset.\n"
            "\n"
            "-  `number` (A numeric value with optional "
            "decimal places. (e.g., 3.14))\n"
            "-  `integer` (A whole number without decimal "
            "places. (e.g., 42))\n"
            "-  `string` (A sequence of characters. (e.g., "
            '\\"test\\"))\n'
            "-  `any` (Any type of data is allowed. (e.g., "
            "true))\n"
            "-  `boolean` (A binary value representing true "
            "or false. (e.g., true))\n"
            "-  `date` (A specific calendar date. (e.g., "
            '\\"2023-05-25\\"))\n'
            "-  `datetime` (A specific date and time, "
            "including timezone information. (e.g., "
            '\\"2023-05-25T10:30:00Z\\"))\n'
            "-  `time` (A specific time of day. (e.g., "
            '\\"10:30:00\\"))\n'
            "-  `year` (A specific year. (e.g., 2023)\n"
            "-  `yearmonth` (A specific year and month. "
            '(e.g., \\"2023-05\\"))\n'
            "-  `duration` (A length of time. (e.g., "
            '\\"PT1H\\")\n'
            "-  `geopoint` (A pair of latitude and "
            "longitude coordinates. (e.g., [51.5074, "
            "-0.1278]))\n",
            "title": "Variable Type",
            "type": "string",
            "constraints": {
                "enum": [
                    "integer",
                    "geopoint",
                    "string",
                    "yearmonth",
                    "number",
                    "date",
                    "boolean",
                    "any",
                    "year",
                    "duration",
                    "time",
                    "datetime",
                ]
            },
        },
        {
            "name": "format",
            "description": "A format taken from one of the [frictionless "
            "specification](https://specs.frictionlessdata.io/) "
            "schemas.\n"
            "For example, for tabular data, there is the "
            "[Table Schema "
            "specification](https://specs.frictionlessdata.io/table-schema)\n"
            "\n"
            "Each format is dependent on the `type` "
            "specified. For example:\n"
            'If `type` is "string", then see the String '
            "formats. \n"
            "If `type` is one of the date-like formats, "
            "then see Date formats.\n",
            "title": "Frictionless Formats",
            "type": "any",
        },
        {
            "name": "constraints.maxLength",
            "description": "Indicates the maximum length of an iterable "
            "(e.g., array, string, or\n"
            "object). For example, if 'Hello World' is the "
            "longest value of a\n"
            "categorical variable, this would be a "
            "maxLength of 11.\n"
            "\n"
            "[Optional,if applicable]\n",
            "title": "Maximum Length",
            "type": "integer",
        },
        {
            "name": "constraints.enum",
            "description": "Constrains possible values to a set of "
            "values.\n"
            "\n"
            "[Optional,if applicable]\n",
            "title": "Variable Possible Values",
            "type": "string",
            "constraints": {"pattern": "^(?:[^|]+\\||[^|]*)(?:[^|]*\\|)*[^|]*$"},
        },
        {
            "name": "constraints.pattern",
            "description": "A regular expression pattern the data MUST "
            "conform to.\n"
            "\n"
            "[Optional,if applicable]\n",
            "title": "Regular Expression Pattern",
            "type": "string",
        },
        {
            "name": "constraints.maximum",
            "description": "Specifies the maximum value of a field (e.g., "
            "maximum -- or most\n"
            "recent -- date, maximum integer etc). Note, "
            "this is different then\n"
            "maxLength property.\n"
            "\n"
            "[Optional,if applicable]\n",
            "title": "Maximum Value",
            "type": "integer",
        },
        {
            "name": "constraints.minimum",
            "description": "Specifies the minimum value of a field.\n"
            "\n"
            "[Optional,if applicable]\n",
            "title": "Minimum Value",
            "type": "integer",
        },
        {
            "name": "encodings",
            "description": "Variable value encodings provide a way to "
            "further annotate any value within a any "
            "variable type,\n"
            "making values easier to understand. \n"
            "\n"
            "\n"
            "Many analytic software programs (e.g., "
            "SPSS,Stata, and SAS) use numerical encodings "
            "and some algorithms\n"
            "only support numerical values. Encodings (and "
            "mappings) allow categorical values to be "
            "stored as\n"
            "numerical values.\n"
            "\n"
            "Additionally, as another use case, this field "
            "provides a way to\n"
            'store categoricals that are stored as  "short" '
            "labels (such as\n"
            "abbreviations).\n"
            "\n"
            "[Optional,if applicable]\n",
            "title": "Variable Value Encodings (i.e., mappings; value " "labels)",
            "examples": ["0=No|1=Yes", "HW=Hello world|GBW=Good bye world|HM=Hi,Mike"],
            "type": "string",
            "constraints": {"pattern": "^(?:.*?=.*?(?:\\||$))+$"},
        },
        {
            "name": "ordered",
            "description": "Indicates whether a categorical variable is "
            "ordered. This variable  is\n"
            "relevant for variables that have an ordered "
            "relationship but not\n"
            "necessarily  a numerical relationship (e.g., "
            "Strongly disagree < Disagree\n"
            "< Neutral < Agree).\n"
            "\n"
            "[Optional,if applicable]\n",
            "title": "An ordered variable",
            "type": "boolean",
        },
        {
            "name": "missingValues",
            "description": "A list of missing values specific to a "
            "variable.\n"
            "\n"
            "[Optional, if applicable]\n",
            "title": "Missing Values",
            "type": "string",
            "constraints": {"pattern": "^(?:[^|]+\\||[^|]*)(?:[^|]*\\|)*[^|]*$"},
        },
        {
            "name": "trueValues",
            "description": "For boolean (true) variable (as defined in "
            "type field), this field allows\n"
            "a physical string representation to be cast as "
            "true (increasing\n"
            "readability of the field). It can include one "
            "or more values.\n"
            "\n"
            "[Optional, if applicable]\n",
            "examples": [
                "Required|REQUIRED",
                "required|Yes|Y|Checked",
                "Checked",
                "Required",
            ],
            "type": "string",
            "constraints": {"pattern": "^(?:[^|]+\\||[^|]*)(?:[^|]*\\|)*[^|]*$"},
        },
        {
            "name": "falseValues",
            "description": "For boolean (false) variable (as defined in "
            "type field), this field allows\n"
            "a physical string representation to be cast as "
            "false (increasing\n"
            "readability of the field) that is not a "
            "standard false value. It can include one or "
            "more values.\n",
            "title": "Boolean False Value Labels",
            "type": "string",
            "constraints": {"pattern": "^(?:[^|]+\\||[^|]*)(?:[^|]*\\|)*[^|]*$"},
        },
        {
            "name": "repo_link",
            "description": "A link to the variable as it exists on the "
            "home repository, if applicable\n",
            "title": "Variable Repository Link",
            "type": "string",
        },
        {
            "name": "standardsMappings.type",
            "description": "The **type** of mapping linked to a published "
            "set of standard variables such as the NIH "
            "Common Data Elements program.\n"
            "[Autopopulated, if not filled]\n",
            "title": "Standards Mapping - Title",
            "examples": ["cde", "ontology", "reference_list"],
            "type": "string",
        },
        {
            "name": "standardsMappings.label",
            "description": "A free text **label** of a mapping indicating "
            "a mapping(s) to a published set of standard "
            "variables such as the NIH Common Data Elements "
            "program.\n"
            "\n"
            "[Autopopulated, if not filled]\n",
            "title": "Standards Mapping - Label",
            "examples": ["substance use", "chemical compound", "promis"],
            "type": "string",
        },
        {
            "name": "standardsMappings.url",
            "description": "The url that links out to the published, "
            "standardized mapping.\n"
            "\n"
            "[Autopopulated, if not filled]\n",
            "title": "Standards Mapping - Url",
            "examples": ["https://cde.nlm.nih.gov/deView?tinyId=XyuSGdTTI"],
            "type": "string",
        },
        {
            "name": "standardsMappings.source",
            "description": "The source of the standardized variable.\n",
            "title": "Standard Mapping - Source",
            "examples": ["TBD (will have controlled vocabulary)"],
            "type": "string",
        },
        {
            "name": "standardsMappings.id",
            "description": "The id locating the individual mapping within "
            "the given source.\n",
            "title": "Standard Mapping - Id",
            "type": "string",
        },
        {
            "name": "relatedConcepts.type",
            "description": "The **type** of mapping to a published set of "
            "concepts related to the given field such as \n"
            "ontological information (eg., NCI thesaurus, "
            "bioportal etc)\n"
            "\n"
            "[Autopopulated, if not filled]\n",
            "title": "Related concepts - Type",
            "type": "string",
        },
        {
            "name": "relatedConcepts.label",
            "description": "A free text **label** of mapping to a "
            "published set of concepts related to the given "
            "field such as \n"
            "ontological information (eg., NCI thesaurus, "
            "bioportal etc)\n"
            "\n"
            "[Autopopulated, if not filled]\n",
            "title": "Related Concepts - Label",
            "type": "string",
        },
        {
            "name": "relatedConcepts.url",
            "description": "The url that links out to the published, "
            "standardized concept.\n"
            "\n"
            "[Autopopulated, if not filled]\n",
            "title": "Related Concepts - Url",
            "examples": ["https://cde.nlm.nih.gov/deView?tinyId=XyuSGdTTI"],
            "type": "string",
        },
        {
            "name": "relatedConcepts.source",
            "description": "The source of the related concept.\n"
            "\n"
            "[Autopopulated, if not filled]\n",
            "title": "Related Concepts - Source",
            "examples": ["TBD (will have controlled vocabulary)"],
            "type": "string",
        },
        {
            "name": "relatedConcepts.id",
            "description": "The id locating the individual mapping within "
            "the given source.\n"
            "\n"
            "[Autopopulated, if not filled]\n",
            "title": "Related Concepts - Id",
            "type": "string",
        },
        {"name": "univarStats.median", "type": "number"},
        {"name": "univarStats.mean", "type": "number"},
        {"name": "univarStats.std", "type": "number"},
        {"name": "univarStats.min", "type": "number"},
        {"name": "univarStats.max", "type": "number"},
        {"name": "univarStats.mode", "type": "number"},
        {"name": "univarStats.count", "type": "integer"},
        {"name": "univarStats.twentyFifthPercentile", "type": "number"},
        {"name": "univarStats.seventyFifthPercentile", "type": "number"},
        {"name": "univarStats.categoricalMarginals.name", "type": "string"},
        {"name": "univarStats.categoricalMarginals.count", "type": "integer"},
    ],
    "missingValues": [""],
}
