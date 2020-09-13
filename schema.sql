CREATE TABLE physical_traits_table (
  id INTEGER,
  age BIGINT,
  gender INTEGER,
  height INTEGER,
  weight DECIMAL,
  PRIMARY KEY (id)
);

CREATE TABLE medical_traits_table (
  id INTEGER,
  ap_hi INTEGER,
  ap_lo INTEGER,
  cholesterol INTEGER,
  gluc INTEGER,
  smoke INTEGER,
  alco INTEGER,
  active INTEGER,
  cardio INTEGER,
  FOREIGN KEY (id) REFERENCES physical_traits_table (id)
);

SELECT pt.id, pt.age,
    pt.gender, pt.height,
    pt.weight, mt.ap_hi,
    mt.ap_lo, mt.cholesterol,
    mt.gluc, mt.smoke,
    mt.alco, mt.active,
    mt.cardio
INTO cardio_table
FROM physical_traits_table AS pt
LEFT JOIN medical_traits_table as mt 
ON (pt.id = mt.id);

CREATE TABLE cardio_table (
  id INTEGER,
  age BIGINT,
  gender INTEGER,
  height INTEGER,
  weight DECIMAL,
  ap_hi INTEGER,
  ap_lo INTEGER,
  cholesterol INTEGER,
  gluc INTEGER,
  smoke INTEGER,
  alco INTEGER,
  active INTEGER,
  cardio INTEGER,
  PRIMARY KEY (id)
);

UPDATE cardio_table SET age = age / 365 ;

CREATE TABLE cardio_prob (
    id INTEGER,
    prob DECIMAL
    FOREIGN KEY (id) REFERENCES cardio_table (id)
);

SELECT ct.id, ct.age,
    ct.gender, ct.height,
    ct.weight, ct.ap_hi,
    ct.ap_lo, ct.cholesterol,
    ct.gluc, ct.smoke,
    ct.alco, ct.active,
    ct.cardio, cp.prob
INTO cardio
FROM cardio_table AS ct
LEFT JOIN cardio_prob as cp 
ON (ct.id = cp.id);

