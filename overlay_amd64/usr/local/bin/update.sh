emaint sync -a
emerge --ask --verbose --update --deep --newuse @world
emerge --ask --depclean
eclean-dist --deep
eclean-pkg --deep