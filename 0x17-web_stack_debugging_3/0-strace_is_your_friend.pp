# Puppet manifest that debugs a LAMP stack in an Ubuntu 14.04 LTS environment

exec { 'sed fix phpp to php':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin',
}
service { 'apache2':
  restart => 'service apache2 graceful',
  path    => '/usr/sbin',
}
