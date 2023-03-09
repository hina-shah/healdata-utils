* Create a dataset called mydata
clear
input str10 id str10 visit_dt_str byte sex_at_birth byte race byte hispanic_ethnicity byte SU4 byte age
1 "06/05/1988" 1 2 1 15 59
2 "04/07/1989" 2 2 0 4 48
3 .a .a .b .a .a 33
end
* convert the visit_dt_str variable to a date variable
gen visit_dt = date(visit_dt_str, "MDY")
drop visit_dt_str
format %td visit_dt
* Set variable labels
label variable id "Unique identifier for participant"
label variable visit_dt "Date of the interview"
label variable sex_at_birth "The self-reported sex of the participant/subject at birth"
label variable race "Self-reported race"
label variable hispanic_ethnicity "Are you of Hispanic, Latino, or Spanish origin?"
label variable SU4 "Heroin Days Used in days"
label variable age "Age of participant in year"

* Set value labels for sex_at_birth
label define sex_at_birth_lbl 1 "Male" 2 "Female" 3 "Intersex" 4 "None of these describe me" .a "Not reported" .b "Prefer not to answer"
label values sex_at_birth sex_at_birth_lbl

* Set value labels for race
label define race_lbl 1 "White" 2 "Black or African American" 3 "American Indian or Alaska Native" ///
                          4 "Native" 5 "Hawaiian or Other Pacific Islander" 6 "Asian" ///
                          7 "Some other race" 8 "Multiracial" .a "Not reported" .b "Prefer not to answer"
label values race race_lbl

* Set value labels for ethnicity
label define hispanic_lbl 1 "Yes" 0 "No" .a "Not reported" .b "Prefer not to answer"
label values hispanic_ethnicity hispanic_lbl

* Display the dataset
browse

save "example.dta",replace