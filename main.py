<?php
error_reporting(0);
echo "Username : ";
$username = trim(fgets(STDIN));
echo "Password : ";
$password = trim(fgets(STDIN));
echo "List Voucher : ";
$xyz = trim(fgets(STDIN));
echo "\n";
echo "\n";
foreach (explode("\n", str_replace("\r", "", file_get_contents($xyz))) as $key => $akun) {
    $pecah = explode("|", trim($akun));
    $voucher = trim($pecah[0]);
$headers = array();
