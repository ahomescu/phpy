<?php

$v = -1;

function next_pos_key() {
  global $v;
  $v++;
  echo 'key: ' . $v . "\n";
  return $v;
}

function next_pos_value() {
  global $v;
  $v++;
  echo 'value: ' . $v . "\n";
  return $v;
}

$a = array("x", "y", "z");
$b = array();
$c = array();
$d = array();
$e = array();
$i = 0;

foreach($a as $b[$i++] => $b[$i++]) {
  echo implode(', ', $b) . "\n";
}

foreach($a as $c[] => $c[]) {
  echo implode(', ', $c) . "\n";
}

foreach($a as $d[] => &$d[]) {
  echo implode(', ', $d) . "\n";
}

foreach($a as $e[next_pos_key()] => $e[next_pos_value()]) {
  echo implode(', ', $e) . "\n";
}

foreach($a as $x => $x) {
  echo $x . "\n";
}

?>
