INSERT INTO users
( f_name, l_name, email, password, dob, sex, weight, height )
VALUES
( $1, $2, $3, $4, $5, $6, $7, $8 )
RETURNING *;