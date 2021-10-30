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
$headers[] = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0';
$headers[] = 'Content-Type: application/x-www-form-urlencoded';
$gas = curl('API', 'loginFail=0&userid='.$username.'&password='.$password.'', $headers);
