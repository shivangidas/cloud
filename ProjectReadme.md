Side note : using conda env while doing this
Python 3.7.4

# AWS CLI

1. Get AWS CLI
   <pre>pip3 install awscli --upgrade --user</pre>
2. Add to path
   <pre>export PATH=~/.local/bin:$PATH</pre>
   Check with <pre>aws --version
   aws-cli/1.16.283 Python/3.7.4 Darwin/18.7.0 botocore/1.13.19</pre>
3. aws configure
   open and edit credentials
   <pre>open ~/.aws/credentials</pre>

# Install boto framework

<pre>pip install boto3</pre>

After launching instance
ssh -i ~/Downloads/nonce.pem ubuntu@ec2-107-22-113-225.compute-1.amazonaws.com

elastic ip is nice

IN the VM
sudo apt update
sudo apt-get install python3-pip
transfer file with filezilla

if you get an error saying request expired, update the ~/.aws/credentials file with latest credentials
