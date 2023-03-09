proc format;
   value sexformat 1='Male' 2='Female' 3='Intersex' 4='None of these describe me' .A='Not reported' .B='Prefer not to answer';
   value raceformat 1='White' 2='Black or African American' 3='American Indian or Alaska Native' 4='Native' 5='Hawaiian or Other Pacific Islander' 6='Asian' 7='Some other race' 8='Multiracial' .A='Not reported' .B='Prefer not to answer';
   value booleanformat 1='Yes' 0='No' .A='Not reported' .B='Prefer not to answer';
   value missing .A='Not reported' .B='Prefer not to answer';
run;

data example;
   infile datalines dlm=',' truncover;
   missing A B;
   input id visit_dt : mmddyy10. sex_at_birth race hispanic_ethnicity SU4 age;
   format visit_dt date9. sex_at_birth sexformat. race raceformat. hispanic_ethnicity booleanformat. SU4 missing. age missing.;
   informat visit_dt mmddyy10.;
   label id='Unique identifier for participant'
         visit_dt='Date of the interview'
         sex_at_birth='The self-reported sex of the participant/subject at birth'
         race='Self-reported race'
         hispanic_ethnicity='Are you of Hispanic, Latino, or Spanish origin?'
         SU4='Heroin Days Used in days'
         age='Age of participant in year';
   datalines;
1,06/05/1988,1,2,1,15,59
2,04/07/1989,2,2,0,4,48
3,04/06/2000,.A,.B,.A,.A,33
;
run;

LIBNAME out "";

PROC COPY in=work out=out;
SELECT example;
RUN;