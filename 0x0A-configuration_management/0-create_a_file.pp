# Create a file in /tmp using Puppet

$doc_root ='/tmp/holberton'
file {'doc_root':
  ensure  =>'present',
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  path    => '/tmp/holberton'
}
