# CVAT Labeltool
!!! note
    This is only important for internal developers.

### Build CVAT
The forked repository with our changes is hosted at [github](https://github.com/BerlinUnited/cvat) in the naoth-develop branch.
This branch is always based on the upstream develop branch. Always use rebase instead of merge on the original develop branch to keep our changes
cleanly separated from the cvat commits.

On the internal ball.informatik.hu-berlin.de server, the code is checked out at `/opt/cvat-repo`.

There are three helper scripts for starting/stopping and building cvat:  

**build_cvat.sh**  
```bash
cd  cvat-repo || exit

export CVAT_HOST=ball.informatik.hu-berlin.de
export ACME_EMAIL=schlottb@informatik.hu-berlin.de

docker compose -f docker-compose.yml -f docker-compose.dev.yml -f docker-compose.https.yml -f docker-compose.override.yml -f components/serverless/docker-compose.serverless.yml build
```

**start_cvat.sh**  
```bash
cd cvat-repo || exit

export CVAT_HOST=ball.informatik.hu-berlin.de
export ACME_EMAIL=schlottb@informatik.hu-berlin.de

docker compose -f docker-compose.yml -f docker-compose.dev.yml -f docker-compose.https.yml -f components/serverless/docker-compose.serverless.yml -f docker-compose.override.yml up -d
```

**stop_cvat.sh**  
```bash
cd cvat-repo || exit
docker compose -f docker-compose.yml -f docker-compose.dev.yml -f components/serverless/docker-compose.serverless.yml -f docker-compose.override.yml down --remove-orphans
```


### Setup Docker Network

The server where cvat is hosted is inside the HU network. From the outside it is only accessible via a VPN. However
per default the docker bridge network for cvat can collide with the vpn. When this happens you can't use ssh to log
into the server unless you are already inside the HU network.

The relevant VPN settings are ip: 172.16.0.0 and subnet: 255.240.0.0. So don't use any of those ip addresses for docker. You can
achieve this by adding the following code to `/etc/docker/daemon.json`

```
{
    "default-address-pools" : [
    {
      "base" : "172.240.0.0/16",
      "size" : 24
    }
    ]
}
```

After this change run `systemctl restart docker`

### Problems with HU VPN
With the OpenVPN provided by the university there might be some name resolution errors because of the nameservers used.
In this case modify the vpn config you use. It worked with the following changes
```
#register-dns  # <-- make sure this line is not active
...
dhcp-option DNS 8.8.8.8  # <-- set the name server of your liking
```

### Setup sshfs mounts
Install sshfs:
```bash
sudo apt install sshfs
```
Create group fuse and add users to it:
```bash
sudo addgroup fuse
sudo adduser $USER fuse
```

### Own changes to the CVAT Code
- in our instance it is possible to create bounding boxes that are (partially) outside the image

## Auto Annotation for developers
!!! note
    Add note about sometimes getting errors in cvat ui about models that cant be loaded. I think cvat nuclio project must be recreated

!!! note
    Describe nuctl setup here and reference the official docs
For a general guide to auto annotation see the official [CVAT Docu](https://openvinotoolkit.github.io/cvat/docs/administration/advanced/installation_automatic_annotation/)

!!! note
    Add more descriptions for cvat models and naoth deep learning
    Move used models to models.naoth.de

The code for our models we use for auto annotation can be found at the [CVAT Models](https://github.com/BerlinUnited/cvat_models) repo.
Currently, the models must be deployed on the same server as the CVAT label tool. All further details can be found inside the repository.

----
### Docker and GPU
TODO this is deprecated

Since inference is unbearable slow on a cpu we need to enable GPU access in docker. On the host run this to install the nvidea-docker-toolkit:
```bash
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker
```
Install the nvidea-container runtime on the host
```bash
sudo apt-get install nvidia-container-runtime
```
modify /etc/docker/daemon.json in order to make the gpu work with compose-files
```bash
{
    "runtimes": {
        "nvidia": {
            "path": "/usr/bin/nvidia-container-runtime",
            "runtimeArgs": []
        }
    }
}
```