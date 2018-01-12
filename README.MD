# Sconveer

Simple Program for servers maintain.

Synatx : **sconveer path/to/cfg [-v]**

-v : verbose

Configuration file example ver 0.1:

```

USER:alex
PASS:ask_pass
host:10.1.1.2
user:root
commands{
    --hostname
    --cd /tmp
    --apt install curl
    --curl -L -O https://download.elastic.co/beats/topbeat/topbeat_1.3.1_amd64.deb
    --dpkg -i topbeat_1.3.1_amd64.deb
}
host:10.1.1.5
commands{
    --hostname
    --cd /tmp
    --curl -L -O https://download.elastic.co/beats/topbeat/topbeat-1.3.1-x86_64.rpm
    --sudo rpm -vi topbeat-1.3.1-x86_64.rpm
}

```

Configuration file example ver 0.2(work in progress):

```

#Global use parameters. ask_pass - asking your password or you may write the password
USER:alex
PASS:ask_pass

#hosts:10.1.1.2,10.1.1.3,10.1.1.4 or path to file with hosts addresses or FQDN
host:10.1.1.2
user:root
  commands{
      hostname
      update
      reboot
      pkg list
      # or pure shell commands
  }
  install {
      # in a string with comma or with new line
      7zip, htop, vim
      git
  }

```
