open-falcon plugins
===================

中文版文档请点[这里](README.cn.md)。

### Prerequisite

Falcon agent is downloaded and deployed.
If not, download the latest release from
[here](https://github.com/open-falcon/falcon-plus/releases).
Decompress it.

The binaries inside are runnable on Linux and you do _not_ need Golang.

### Install agents

Note: skip this section if you _already_ have agents running on your servers.

A similar content has been already covered in
[this article](http://book.open-falcon.org/zh_0_2/distributed_install/agent.html).
English version is also available on the same site.

An agent should be deployed to every server you wish to monitor.
You still need to download and decompress the whole Falcon+ package.
Its config file is stored as `$OPEN_FALCON_HOME/agent/config/cfg.json`.

* The `addrs` field of "transfer" is the most important part of all configurations
that determines to which transfer service this agent sends its data.
By default it is the port 8433 of Falcon master API service.
* Change `heartbeat` to point to heartbeat service on the master,
similar to the previous step.
* Enable "plugin" and it will be useful later.
* (Optional but strongly encouraged) enable "http" so that the agent accepts custom data push.

Now it is good to start the agent
```
cd $OPEN_FALCON_HOME
./open-falcon start agent
```

### Install this repo

If `plugin` is not enabled in `$OPEN_FALCON_HOME/agent/config/cfg.json` yet,
do it.

Replace "git" to "https://github.com/btccom/open-falcon-plugins".

For each plugin to work, you will need a config JSON file in 
`$OPEN_FALCON_HOME/agent/config` which has the _same_ name as the plugin.
For example in order for `proc/60_pid.py` to work,
a file named `60_pid.json` needs to be present.
Read the comments of individual plugins for more details on the format and content of config files.

### Run

Run the command below:
```
curl http://127.0.0.1:1988/plugin/update
```
It will pull the git repo and start scheduling your plugins.

If necessary, restart the agent.
```
cd $OPEN_FALCON_HOME
./open-falcon restart agent
```

### Debug

See all the logs of agents.
```
tail -f agent/logs/agent.log
```