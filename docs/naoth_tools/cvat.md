# CVAT Labeltool
!!! note
    This is only important for internal developers.

### Build CVAT
The forked repository with our changes is hosted at [github](https://github.com/BerlinUnited/cvat) in the naoth-develop branch.
This branch is always based on the upstream develop branch. Always use rebase instead of merge on the original develop branch to keep our changes
cleanly separated from the cvat commits.

On the internal ball.informatil.hu-berlin.de server, the code is checked out at `/opt/cvat-repo`.

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
### Problems with Nuclio Dashboard
When you use the auto annotation feature in cvat a request gets made to `http:nuclio:8070`. The nuclio dashboard acts
as a proxy to the container that actually holds the annotation function. In a normal docker environment this would be
`172.17.0.1:<port_number>`. Where port number is the port specified during deployment of the nuclio function. But because
the nuclio developers are insanely stupid they hardcoded the default docker gateway. You have to rebuild the
nuclio dasboard image and use that.

!!! Note
    You can download the modified nuclio dashboard image by running `docker pull stellacbc/nuclio_dashboard:hu_berlin`
    or instead building it yourself as described below.

```bash
# get the correct nuclio version as specified in https://github.com/openvinotoolkit/cvat/blob/develop/components/serverless/docker-compose.serverless.yml
wget https://github.com/nuclio/nuclio/archive/refs/tags/1.5.16.zip
unzip 1.5.16.zip
cd nuclio-1.5.16

# replace all occurrence of 172.17.0.1 with 172.240.0.1 in  pkg/platform/local/platform.go

# NOTE: it will fail at some point but it should build the nuclio dashboard
make build

# tag the image with a name that is later used in cvat
docker tag quay.io/nuclio/dashboard modified_nuclio_dashboard
# save the newly build image to a tar file
docker save modified_nuclio_dashboard > nuclio_dashboard.tar

# after moving the container to the server where nuclio and cvat run extract the image from the tar file
docker load < nuclio_dashboard.tar

# you should now have image with the name modified_nuclio_dashboard
```
You now need to modify the docker-compose.serverless.yml inside the cvat repo. Set the image to the name of the 
downloaded or built image. For example:
```bash
image: stellacbc/nuclio_dashboard:hu_berlin
```
After this change run the build and start script again



### Own changes to the CVAT Code
- in our instance it is possible to create bounding boxes that are (partially) outside the image
- fixed api address to the ball server so that swagger works correctly

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
Currently the models must be deployed on the same server as the CVAT label tool. All further details can be found inside the repository.
