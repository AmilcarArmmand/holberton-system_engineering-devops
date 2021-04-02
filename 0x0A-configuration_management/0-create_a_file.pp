# Script that creates a file in /tmp using Puppet

$doc_root ='/tmp/holberton'

file {'doc_root':
  ensure  =>'present',
  path    => '/tmp/holberton',
  mode    => '0744',
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
}
