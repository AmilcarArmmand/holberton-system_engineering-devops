# Puppet script requirements
# Nginx should be listening on port 80
# GET request using curl, must return a page that contains 'Holberton School'
# The redirection must be a “301 Moved Permanently”

exec { 'apt-get update':
  command  => 'sudo apt-get update',
  path     => '/usr/bin',
  provider => shell
}

package { 'nginx':
  ensure => present,
}

file { 'index':
  ensure  => present,
  path    => '/var/www/html/index.html',
  content => "Holberton School\n",
}

file { '404':
  ensure  => present,
  path    => '/var/www/html/404.html',
  content => "Ceci n'est pas une page\n",
}

file { 'nginx-config':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  content => "server {\n\tlisten 80 default_server;\n\tlisten [::]:80 default_server;\n\troot /var/www/html;\n\tindex index.html index.htm index.nginx-debian.html;\n\tserver_name _;\nrewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;\n\t}\n\\terror_page 404 /404.html;\n\tlocation = /404.html {\n\t\troot /var/www/html;\n\t\tinternal;\n\t}"
}

exec { 'restart nginx':
  command => '/usr/sbin/service nginx restart',
}
