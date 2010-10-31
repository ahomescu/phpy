<?php

$primes = array(2);
$i = 3;
while ($i <= 500) {
    $j = 0;
    while ($j < count($primes)) {
        if (($i % $primes[$j]) == 0)
            break;
        $j++;
    }
    if ($j == count($primes)) {
        $primes[] = $i;
    }
    $i++;
}


?>
