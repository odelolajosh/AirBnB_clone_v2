# Script that configures Nginx and required folders

# update the package list
exec {'update':
    command => 'sudo apt-get update',
    path    => '/usr/bin',
}

# install nginx
package {'nginx':
    ensure  => 'installed',
    require => Exec['update'],
}

# start nginx
service {'nginx':
    ensure  => 'running',
    require => Package['nginx'],
}

# create the required folders
file {'/data/web_static/releases/':
    ensure    => 'directory',
    mode      => '0755',
    owner     => 'ubuntu',
    group     => 'ubuntu',
    recursive => true,
    require   => Package['nginx'],
}

file {'/data/web_static/shared/':
    ensure    => 'directory',
    mode      => '0755',
    owner     => 'ubuntu',
    group     => 'ubuntu',
    recursive => true,
    require   => Package['nginx'],
}

file {'/data/web_static/releases/test/':
    ensure    => 'directory',
    mode      => '0755',
    owner     => 'ubuntu',
    group     => 'ubuntu',
    recursive => true,
    require   => Package['nginx'],
}

# write into /data/web_static/releases/test/index.html
file {'/data/web_static/releases/test/index.html':
    ensure  => 'file',
    mode    => '0644',
    owner   => 'ubuntu',
    group   => 'ubuntu',
    content => 'Holberton School',
    require => File['/data/web_static/releases/test/'],
}

# make symbolic link
file {'/data/web_static/current':
    ensure  => 'link',
    target  => '/data/web_static/releases/test/',
    require => File['/data/web_static/releases/test/index.html'],
}

# add "location" after line that contains "error_page 404" in nginx.conf
exec {'add_location':
  provider => shell,
  command  => 'sudo sed -i \'38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n\' /etc/nginx/sites-available/default',
  require  => File['/data/web_static/current'],
}

# restart nginx
exec {'restart Nginx':
    provider => shell,
    command  => 'sudo service nginx restart',
    require  => Exec['add_location'],
}