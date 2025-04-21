# VPC-peering-demo
AWS EC2 -> Confluent -> Atlas Stream Processing -> Atlas Cluster

# AWS setup:

![01-AWS-vpc](images/01-AWS-vpc.png)
![02-AWS-subnet.png](images/02-AWS-subnet.png)
![03-AWS-RT.png](images/03-AWS-RT.png)
![04-AWS-IGW.png](images/04-AWS-IGW.png)
![05-AWS-EIP.png](images/05-AWS-EIP.png)
![06-AWS-PC.png](images/06-AWS-PC.png)
![07-AWS-PC.png](images/07-AWS-PC.png)
![08-AWS-EC2.png](images/08-AWS-EC2.png)

# Confluent setup:

![09-CFLT-NW1.png](images/09-CFLT-NW1.png)
![10-CFLT-NW2.png](images/10-CFLT-NW2.png)

# Proxy setup to use the Confluent web UI on a VPC cluster:

![11-CFLT-proxy1.png](images/11-CFLT-proxy1.png)
![12-CFLT-proxy2.png](images/12-CFLT-proxy2.png)

# Atlas setup:

![13-Atlas-NW1.png](images/13-Atlas-NW1.png)
![14-Atlas-SP1.png](images/14-Atlas-SP1.png)

# Create a peering connection between Confluent and Atlas Stream Processing:

![15-Atlas-SP-VPC.png](images/15-Atlas-SP-VPC.png)

# Create and start the stream process worker:

![16-Atlas-SP2.png](images/16-Atlas-SP2.png)
![17-Atlas-SP3.png](images/17-Atlas-SP3.png)

# Run the python code in EC2:

![18-EC2-python1.png](images/18-EC2-python1.png)
![19-EC2-python2.png](images/19-EC2-python2.png)

# Verify that it all works:

![20-CFLT-topic.png](images/20-CFLT-topic.png)
![21-Atlas-db.png](images/21-Atlas-db.png)
![22-CFLT-flow.png](images/22-CFLT-flow.png)

