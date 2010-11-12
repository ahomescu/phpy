<?php

function foo($x, &$z) {
  $y = $x + 2;
}

$z = 2;
foo($z, $z);
foo(foo(5, $z), $z);
echo $z;

?>
