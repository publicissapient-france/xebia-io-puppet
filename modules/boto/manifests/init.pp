class boto {
        exec {
                "git clone git://github.com/boto/boto.git" :
                        cwd     => "/tmp",
                        path    => ["/usr/bin", "/usr/sbin"],
                        notify  => Exec["python setup.py install"],
                        refreshonly => true
        }

        exec {
                "python setup.py install" :
                        cwd     => "/tmp",
                        path    => ["/usr/bin", "/usr/sbin"],
                        refreshonly => true,
        }


}

