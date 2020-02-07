mkdir -p /test
git clone https://github.com/bipulkumar7/raintree-systems_Assignment.git ; cd raintree-systems_Assignment/H--RAINTREE-PARKER94-
cwd=$(pwd); cd ../
# path = '/root/raintree/H--RAINTREE-PARKER94-'
sed -i  "s#'/root/raintree.*#\'${cwd}\'#"  logfileName.py
sed -i "s#'/root/raintree.*#\'${cwd}/{}\'#" ComputerNames.py
sed -i "s#'/root/raintree.*#\'${cwd}/{}\'#" report.py
