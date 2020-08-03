#Using Puppet, create a manifest that kills a process named killmenow

exec { 'pkill -p killmenow':
  path    => '/usr/bin',
}
