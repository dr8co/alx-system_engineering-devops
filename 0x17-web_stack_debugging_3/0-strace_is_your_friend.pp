# A puppet scripts that fixes incorrect 'phpp' extensions to 'php'

exec { 'fix-phpp':
  command => 'sed -i s/phpp/php/g /var/www/wp-settings.php',
  path    => '/bin:/usr/bin'
}
