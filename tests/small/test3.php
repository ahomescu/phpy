<?php

function foo($x) {
  $y = $x + 2;
}

$z = 2;
foo($z);
foo(foo(5));

?>
