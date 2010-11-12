<?php

function f(&$a) {
  $a += 2;
}

$i = 1;
f(++$i);
f($i += 3); 
echo $i;

?>
