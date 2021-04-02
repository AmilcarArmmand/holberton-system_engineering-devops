#Puppet  manifest that kills a process named killmenow

exec { 'pkill killmenow':
  command  => 'pkill -SIGKILL -f killmenow',
  path     => '/usr/bin:/usr/sbin:/bin',
  provider => shell,
}
