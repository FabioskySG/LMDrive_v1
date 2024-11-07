#!/usr/bin/env bash

# Download and install CARLA
mkdir carla
cd carla

# CARLA 0.9.10.1
wget https://carla-releases.s3.us-east-005.backblazeb2.com/Linux/CARLA_0.9.10.1.tar.gz
wget https://carla-releases.s3.us-east-005.backblazeb2.com/Linux/AdditionalMaps_0.9.10.1.tar.gz
tar -xf CARLA_0.9.10.1.tar.gz
tar -xf AdditionalMaps_0.9.10.1.tar.gz
rm CARLA_0.9.10.1.tar.gz
rm AdditionalMaps_0.9.10.1.tar.gz

# CARLA 0.9.15
# wget https://carla-releases.s3.us-east-005.backblazeb2.com/Linux/CARLA_0.9.15.tar.gz
# wget https://carla-releases.s3.us-east-005.backblazeb2.com/Linux/AdditionalMaps_0.9.15.tar.gz
# tar -xf CARLA_0.9.15.tar.gz
# tar -xf AdditionalMaps_0.9.15.tar.gz
# rm CARLA_0.9.15.tar.gz
# rm AdditionalMaps_0.9.15.tar.gz
cd ..
