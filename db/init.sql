CREATE TABLE user (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50)  NOT NULL,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(2500) NOT NULL,
    dob VARCHAR(50) NOT NULL,
    sex VARCHAR(50) NOT NULL,
    weight INT(10) NOT NULL,
    height INT(10) NOT NULL
)

CREATE TABLE calc (
    health_id REFERENCES user(user_id)
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