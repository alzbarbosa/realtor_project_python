 echo "BUILD START"
 python3.11 -m pip install -r requirements.txt
 python3.11 manage.py collectstatic
 echo "BUILD END"