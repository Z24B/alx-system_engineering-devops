# practice configuring your server with Puppet

# Define the package resource to install Nginx
package { 'nginx':
  ensure => 'installed',
}

# Define the service resource to ensure Nginx is running and enabled
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

# Define the file resource to create the custom Nginx configuration file for redirection
file { '/etc/nginx/sites-available/redirect':
  ensure  => 'file',
  content => "
    server {
        listen 80;
        server_name _;

        location /redirect_me {
            return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }
    }
  ",
  require => Package['nginx'],
}

# Define the symbolic link resource to enable the custom configuration
file { '/etc/nginx/sites-enabled/redirect':
  ensure => 'link',
  target => '/etc/nginx/sites-available/redirect',
  notify => Service['nginx'],
  require => File['/etc/nginx/sites-available/redirect'],
}

# Define the file resource to create the index.html file with "Hello World!" content
file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
  notify  => Service['nginx'],
  require => Package['nginx'],
}
