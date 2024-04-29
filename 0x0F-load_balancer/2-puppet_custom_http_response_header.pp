# Puppet manifest to add a custom HTTP header to Nginx

# Define the package resource to install Nginx
package { 'nginx':
  ensure => 'installed',
}

# Define the file resource to add custom HTTP header to Nginx configuration
file { '/etc/nginx/sites-available/custom_header':
  ensure  => 'file',
  content => "server {
    listen 80;
    server_name _;

    location / {
      add_header X-Served-By $::hostname;
    }
  }",
  require => Package['nginx'], # Ensure Nginx package is installed before configuring
}

# Define the symbolic link resource to enable the custom configuration
file { '/etc/nginx/sites-enabled/custom_header':
  ensure => 'link',
  target => '/etc/nginx/sites-available/custom_header',
  require => File['/etc/nginx/sites-available/custom_header'],
  notify => Service['nginx'], # Notify Nginx service to reload configuration
}

# Define the service resource for Nginx
service { 'nginx':
  ensure => 'running',
  enable => true,
}
