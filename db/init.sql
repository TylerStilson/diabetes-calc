CREATE TABLE calc (
    health_id REFERENCES users(id),
    correction_factor INT(10) NOT NULL,
    correction_variable INT(10) NOT NULL,
    icr_ratio INT(10) NOT NULL,
    long_lasting_one INT(10) NOT NULL,
    long_lasting_two INT(10),
    bs_high INT(10) NOT NULL,
    bs_low INT(10) NOT NULL,
    bs_target INT(10) NOT NULL,
    precision INT(10) NOT NULL,
    iob BOOLEAN NOT NULL,
    duration INT(10) NOT NULL
)
