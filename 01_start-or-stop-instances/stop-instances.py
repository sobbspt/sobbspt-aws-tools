import sys
from boto import ec2

__author__ = 'sobbspt'

credentialProfile = sys.argv[1]
region = sys.argv[2]
tagName = sys.argv[3]
tagValue = sys.argv[4]


ec2conn = ec2.connect_to_region(region, profile_name=credentialProfile)

reservations = ec2conn.get_all_instances(filters={"tag:"+tagName: tagValue})

instanceID = []
i = 0
for res in reservations:
    for inst in res.instances:
        if inst.state == "stopped":
            ec2conn.stop_instances(inst.id)
            i += 1

print(str(i) +" instance(s) with tag "+ tagName+":"+tagValue +" was stopped")
