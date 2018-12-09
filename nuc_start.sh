#!/bin/bash -v

HOSTNAME=`hostname`
NODE_1=miura-nuc-1
NODE_2=sensor2
NODE_3=miura-nuc-3
DEFAULT_FREQ=1

DEFAULT_DST=10.10.0.11
CLOUD_NODE_DIR="/home/miura/p/sample_app/app_eval"
SENSOR_NODE_DIR="/home/miura/p/sample_app/app_eval"
#DEFAULT_DST=192.168.3.33
#SENSOR_NODE_DIR="/home/miura/p/sample_app"
#CLOUD_NODE_DIR="/home/pi/p/sample_app"

add_cloud_network_info()
{
	sudo ip route add 192.168.1.0/24 dev eno1
	# smart-router-1 enp2s0
	sudo arp -s 192.168.1.1 80:ee:73:e0:0c:9a
	
	sudo ip route add 10.10.0.0/24 dev eno1
	# smart-router-1 enp3s0
	sudo arp -s 10.10.0.1 80:ee:73:e0:0c:9b
	# nuc1
	sudo arp -s 10.10.0.11 f4:4d:30:68:bf:e2
}

add_node_network_info()
{
  	### =========== smart-router-3
  	# smart-router-3: enp2s0
  	sudo arp -s 192.168.1.3 80:ee:73:e0:0b:26

  	sudo ip route add 192.168.3.0/24 dev eno1
  	# smart-router-3: enp3s0
  	sudo arp -s 192.168.3.3 80:ee:73:e0:0b:27
    # nuc-3
  	sudo arp -s 192.168.3.33 f4:4d:30:67:f5:9e


  	### =========== smart-router-2
  	# smart-router-2: enp2s0
  	sudo arp -s 192.168.1.2 80:ee:73:e0:0b:56

  	sudo ip route add 192.168.2.0/24 dev eno1
  	# smart-router-2: enp3s0
  	sudo arp -s 192.168.2.2 80:ee:73:e0:0b:57
    #nuc-2?
  	sudo arp -s 192.168.2.22 b8:27:eb:55:a3:5f
}


if [ $# -eq 1 ]; then
	DEFAULT_DST=$1
fi

case ${HOSTNAME} in
	${NODE_1})
    		add_node_network_info
    		cd $CLOUD_NODE_DIR
    		python soc_server.py ${DEFAULT_DST} 8080 1;;
		    #cd $SENSOR_NODE_DIR
		    #python soc_cli.py ${DEFAULT_DST} 8080 2 10000 0.0001;;
	${NODE_2})
		    add_cloud_network_info
		    cd $SENSOR_NODE_DIR
		    python soc_cli.py ${DEFAULT_DST} 8080 2 10000 ${DEFAULT_FREQ};;
	${NODE_3})
		    add_cloud_network_info	
		    #cd $SENSOR_NODE_DIR
		    #python soc_cli.py ${DEFAULT_DST} 8080 3 1000 1;;
    	  cd $CLOUD_NODE_DIR
		    python soc_cli.py ${DEFAULT_DST} 8080 3 10000 ${DEFAULT_FREQ};;
	*)
		echo "Unknown hostname"
esac

