<!DOCTYPE html>
<html>
<body>

<!-- PHP files can embed HTML -->
<h1>My first PHP page</h1>

<?php
// This is a single-line comment
# This is also a single-line comment
/*
This is a multiple-lines comment block
that spans over multiple
lines
*/

# Strings can be single or double quote
echo "Hello World!";
ECHO 'Equivalent function';
$variable = "value1"
$VARIABLE = "value2"
$txt = "Hello World!";
echo "Text: $txt";
echo "Text: " . $txt;
# Integers can be negative or positive
$x = 5;
$y = -4;
echo $x + $y;
# Floats can be decimal or exponential
$x = 4 * 2.5; # Stored as float
$y = 7.64E+5 # Exponential
$z = 5.56E-5
var_dump($x); # Returns data type and data
# Booleans
$x = true;
$y = false;
# Unassigned variables are of type null
$x = null;
?>

<?php
// Cast float to int
$x = 23465.768;
$int_cast = (int)$x;
echo $int_cast;
// Cast string to int
$x = "23465.768";
$int_cast = (int)$x;
echo $int_cast;
?> 
</body>
</html> 