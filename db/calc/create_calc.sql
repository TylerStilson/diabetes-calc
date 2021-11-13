INSERT INTO users
( health_id, correction_factor, correction_variable, icr_ration, long_lasting_one, long_lasting_two, bs_high, bs_low, bs_target, precision, iob, duration )
VALUES
( $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12 )
RETURNING *;
