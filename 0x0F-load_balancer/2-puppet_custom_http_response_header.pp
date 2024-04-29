# Puppet manifest to add a custom HTTP header to Nginx

# Define the package resource to install Nginx
exec { 'update server':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell',
}

# install nginx web server on server
package { 'nginx':
  ensure   => present,
  provider => 'apt'
}

# Define the file resource to add custom HTTP header to Nginx configuration
file_line { 'add HTTP header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;'
}

# start service
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx']
}
