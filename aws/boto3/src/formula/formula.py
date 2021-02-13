#!/usr/bin/python3
import boto3
import os

def run(access_key, secret_access_key, region, vpc_cidr, vpc_name):

    # client = boto3.client(
    #     'dynamodb',
    #     endpoint_url='http://localhost:8000',
    #     region_name=region,
    #     aws_access_key_id=access_key,
    #     aws_secret_access_key=secret_access_key
    # )

    session = boto3.session.Session(
        region_name=region,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_access_key
    )

    s3 = session.resource('s3')
    print("\n1️⃣  Listing buckets for the \033[94m{}\033[0m region".format(region))
    for bucket in s3.buckets.all():
        print("\n\033[1mBucket:\033[0m {}".format(bucket.name))
        print("\033[1mCreation Date:\033[0m {}".format(bucket.creation_date))

    print("\n2️⃣  Creating VPC on the \033[94m{}\033[0m region".format(region))
    ec2 = session.resource('ec2')
    vpc = ec2.create_vpc(CidrBlock=vpc_cidr)

    print("\n3️⃣  Assigning \033[94m{}\033[0m name to VPC".format(vpc_name))
    vpc.create_tags(Tags=[{"Key": "Name", "Value": vpc_name}])
    vpc.wait_until_available()

    print("\n4️⃣  Enabling Public DNS hostname for VPC ID : \033[94m{}\033[0m".format(vpc.id))
    ec2_client = session.client('ec2')
    ec2_client.modify_vpc_attribute( VpcId = vpc.id , EnableDnsSupport = { 'Value': True } )
    ec2_client.modify_vpc_attribute( VpcId = vpc.id , EnableDnsHostnames = { 'Value': True } )

    print("\n5️⃣  Creating an Internet Gateway (attaching it to VPC)")
    internetgateway = ec2.create_internet_gateway()
    vpc.attach_internet_gateway(InternetGatewayId=internetgateway.id)

    print("\n6️⃣  Creating Route Table and Public Route")
    routetable = vpc.create_route_table()
    route = routetable.create_route(DestinationCidrBlock='0.0.0.0/0', GatewayId=internetgateway.id)

    print("\n7️⃣  Creating Subnet and associating it to Route Table")
    subnet = ec2.create_subnet(CidrBlock='10.0.1.0/24', VpcId=vpc.id)
    routetable.associate_with_subnet(SubnetId=subnet.id)

    print("\n8️⃣  Creating Security Group (allowing SSH inbound rule through the VPC)")
    securitygroup = ec2.create_security_group(GroupName='SSH-ONLY', Description='only allow SSH traffic', VpcId=vpc.id)
    securitygroup.authorize_ingress(CidrIp='0.0.0.0/0', IpProtocol='tcp', FromPort=22, ToPort=22)

    print("\n9️⃣  Configuring Instance")
    key_name ='ec2-keypair-' + vpc_name
    outfile = open(key_name + '.pem','w')
    key_pair = ec2.create_key_pair(KeyName=key_name)
    key_pair_out = str(key_pair.key_material)
    print(key_pair_out)
    outfile.write(key_pair_out)

    print("\n🔟  Creating Linux Instance in the Subnet")
    instances = ec2.create_instances(
        ImageId='ami-08f7f9fcedda2e070',
        InstanceType='t2.micro',
        MaxCount=1,
        MinCount=1,
        NetworkInterfaces=[{
            'SubnetId': subnet.id,
            'DeviceIndex': 0,
            'AssociatePublicIpAddress': True,
            'Groups': [securitygroup.group_id]
        }],
        KeyName=key_name
    )

    os.system('chmod 400 ' + key_name + '.pem')

    print("\n✅  VPC successfully configured with Boto3!")
