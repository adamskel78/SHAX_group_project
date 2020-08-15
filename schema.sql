CREATE TABLE cardio_table (
  id INTEGER,
  age varchar,
  gender INTEGER,
  height INTEGER,
  weight_patient varchar,
  ap_hi INTEGER,
  ap_lo INTEGER,
  cholesterol INTEGER,
  gluc INTEGER,
  smoke INTEGER,
  alco INTEGER,
  active INTEGER,
  cardio INTEGER
);

Select * From cardio_table;
drop table cardio_table;

copy cardio_table
From '/Users/adamskel78/Desktop/Data_Analyst/SHAX_group_project/Resources/cardio_train.csv'
DELIMITER ';' CSV HEADER; 