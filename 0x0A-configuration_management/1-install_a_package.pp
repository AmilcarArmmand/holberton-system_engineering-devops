# Puppet script that installs puppet-lint package

$package ='puppet-lint'

package { $package:
  ensure   =>'2.1.1',
  provider => 'gem'
}
