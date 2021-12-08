# CVAT Labeltool
!!! note
    This is only important for internal developers.

### Build CVAT
The forekd repository with our changes is hosted at [github](https://github.com/BerlinUnited/cvat).
The code is checked out at `/opt/cvat-repo`.

There are three helper scripts for starting/stopping and building cvat:  

**build_cvat.sh**  
```bash
cd  cvat-repo || exit

export CVAT_HOST=ball.informatik.hu-berlin.de
export ACME_EMAIL=schlottb@informatik.hu-berlin.de

docker-compose -f docker-compose.yml -f docker-compose.dev.yml -f docker-compose.https.yml -f docker-compose.override.yml -f components/serverless/docker-compose.serverless.yml build
```

**start_cvat.sh**  
```bash
cd cvat-repo || exit

export CVAT_HOST=ball.informatik.hu-berlin.de
export ACME_EMAIL=schlottb@informatik.hu-berlin.de

docker-compose -f docker-compose.yml -f docker-compose.dev.yml -f docker-compose.https.yml -f components/serverless/docker-compose.serverless.yml -f docker-compose.override.yml up -d
```

**stop_cvat.sh**  
```bash
cd cvat-repo || exit
docker-compose -f docker-compose.yml -f docker-compose.dev.yml -f components/serverless/docker-compose.serverless.yml -f docker-compose.override.yml down --remove-orphans
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


### Own changes to the CVAT Code
- in our instance it is possible to create bounding boxes that are (partially) outside the image

## Auto Annotation for developers
For a general guide to auto annotation see the official [CVAT Docu](https://openvinotoolkit.github.io/cvat/docs/administration/advanced/installation_automatic_annotation/)

The code for our models we use for auto annotation can be found at the [CVAT Models](https://github.com/BerlinUnited/cvat_models) repo.
Currently the models must be deployed on the same server as the CVAT label tool. All further details can be found inside the repository.
